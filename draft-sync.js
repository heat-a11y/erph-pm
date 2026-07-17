/**
 * DraftSync — Robust offline-first draft synchronization for e-RPH forms
 *
 * Features:
 *  - Auto-saves form state to IndexedDB (with localStorage fallback)
 *  - 800ms debounced writes to avoid thrashing
 *  - State hydration: detects drafts on mount, prompts restore via accessible modal
 *  - Online/offline network status badge (role="status")
 *  - WCAG 2.2 AA: focus trap in modal, aria-live announcements, keyboard dismissible
 *
 * Usage:
 *   const sync = new DraftSync({
 *     key: 'erph-draft',           // storage key
 *     onSave: (state) => {},        // optional callback after save
 *     onRestore: (state) => {},     // callback when user chooses to restore
 *   });
 *   sync.watch(formState);         // Alpine.js $watch or manual call
 *   sync.destroy();                // cleanup
 */

class DraftSync {
  constructor(opts = {}) {
    this.options = {
      key: opts.key || 'erph-draft',
      debounceMs: opts.debounceMs || 800,
      maxRetries: 3,
      onSave: opts.onSave || (() => {}),
      onRestore: opts.onRestore || (() => {}),
    };

    this._pending = null;
    this._timer = null;
    this._badge = null;
    this._toast = null;
    this._modal = null;
    this._online = navigator.onLine;
    this._saving = false;

    this._initBadge();
    this._initListeners();
  }

  // ────────────────────────────────────────────
  //  PUBLIC API
  // ────────────────────────────────────────────

  /** Call this whenever the form state changes (e.g. from Alpine $watch) */
  watch(state) {
    this._pending = this._clone(state);
    this._debouncedSave();
  }

  /** Manually trigger an immediate save */
  saveNow(state) {
    this._pending = this._clone(state);
    this._write();
  }

  /** Check for existing draft and prompt user */
  async checkForDraft() {
    const draft = await this._read();
    if (!draft || !draft._timestamp) return null;

    const age = Date.now() - draft._timestamp;
    const ageMinutes = Math.floor(age / 60000);
    const ageText = ageMinutes < 1 ? 'just now' :
                    ageMinutes < 60 ? `${ageMinutes} minute(s) ago` :
                    `${Math.floor(ageMinutes / 60)} hour(s) ago`;

    this._showRestoreModal(draft, ageText);
    return draft;
  }

  /** Clear saved draft */
  async clearDraft() {
    try {
      const db = await this._db();
      const tx = db.transaction('drafts', 'readwrite');
      tx.objectStore('drafts').delete(this.options.key);
      await this._txComplete(tx);
    } catch {
      localStorage.removeItem(this.options.key);
    }
    this._announce('Draft cleared');
  }

  /** Clean up event listeners and DOM */
  destroy() {
    clearTimeout(this._timer);
    window.removeEventListener('online', this._onlineHandler);
    window.removeEventListener('offline', this._offlineHandler);
    if (this._badge && this._badge.parentNode) this._badge.parentNode.removeChild(this._badge);
    if (this._modal && this._modal.parentNode) this._modal.parentNode.removeChild(this._modal);
  }

  /** Get current online status */
  isOnline() { return this._online; }

  // ────────────────────────────────────────────
  //  INTERNAL
  // ────────────────────────────────────────────

  _debouncedSave() {
    clearTimeout(this._timer);
    this._timer = setTimeout(() => this._write(), this.options.debounceMs);
  }

  async _write() {
    if (!this._pending || this._saving) return;
    this._saving = true;

    const data = { ...this._pending, _timestamp: Date.now(), _version: 2 };

    for (let attempt = 0; attempt < this.options.maxRetries; attempt++) {
      try {
        const db = await this._db();
        const tx = db.transaction('drafts', 'readwrite');
        tx.objectStore('drafts').put(data, this.options.key);
        await this._txComplete(tx);
        this._saving = false;
        this._announce('Draf disimpan');
        this.options.onSave(data);
        return;
      } catch (e) {
        if (attempt === this.options.maxRetries - 1) {
          // Fallback to localStorage
          try {
            localStorage.setItem(this.options.key, JSON.stringify(data));
            this._saving = false;
            this._announce('Draf disimpan (local)');
            this.options.onSave(data);
            return;
          } catch (lsError) {
            console.warn('DraftSync: all storage attempts failed', lsError);
            this._saving = false;
          }
        }
        // Wait before retry (exponential backoff)
        await new Promise(r => setTimeout(r, 200 * Math.pow(2, attempt)));
      }
    }
    this._saving = false;
  }

  async _read() {
    try {
      const db = await this._db();
      const tx = db.transaction('drafts', 'readonly');
      const req = tx.objectStore('drafts').get(this.options.key);
      const result = await this._reqPromise(req);
      if (result) return result;
    } catch { /* fall through */ }
    // Fallback
    try {
      const raw = localStorage.getItem(this.options.key);
      return raw ? JSON.parse(raw) : null;
    } catch { return null; }
  }

  _clone(obj) {
    try { return JSON.parse(JSON.stringify(obj)); }
    catch { return { ...obj }; }
  }

  // ── IndexedDB ──
  _dbPromise = null;
  _db() {
    if (!this._dbPromise) {
      this._dbPromise = new Promise((resolve, reject) => {
        const req = indexedDB.open('DraftSyncDB', 1);
        req.onupgradeneeded = (e) => {
          const db = e.target.result;
          if (!db.objectStoreNames.contains('drafts')) {
            db.createObjectStore('drafts');
          }
        };
        req.onsuccess = (e) => resolve(e.target.result);
        req.onerror = (e) => reject(e.target.error);
      });
    }
    return this._dbPromise;
  }

  _reqPromise(req) {
    return new Promise((resolve, reject) => {
      req.onsuccess = () => resolve(req.result);
      req.onerror = () => reject(req.error);
    });
  }

  _txComplete(tx) {
    return new Promise((resolve, reject) => {
      tx.oncomplete = () => resolve();
      tx.onerror = (e) => reject(e.target.error);
    });
  }

  // ── Network Status Badge ──
  _initBadge() {
    this._badge = document.createElement('div');
    this._badge.setAttribute('role', 'status');
    this._badge.className = 'ds-badge';
    this._badge.innerHTML = this._online
      ? '<span class="ds-dot ds-dot-online"></span> Online'
      : '<span class="ds-dot ds-dot-offline"></span> Offline';
    this._badge.setAttribute('aria-live', 'polite');
    document.body.appendChild(this._badge);
  }

  _initListeners() {
    this._onlineHandler = () => {
      this._online = true;
      this._updateBadge();
      this._announce('Sambungan internet kembali');
    };
    this._offlineHandler = () => {
      this._online = false;
      this._updateBadge();
      this._announce('Sambungan internet terputus. Draf disimpan secara tempatan.');
    };
    window.addEventListener('online', this._onlineHandler);
    window.addEventListener('offline', this._offlineHandler);
  }

  _updateBadge() {
    if (!this._badge) return;
    this._badge.innerHTML = this._online
      ? '<span class="ds-dot ds-dot-online"></span> Online'
      : '<span class="ds-dot ds-dot-offline"></span> Offline';
  }

  // ── Restore Modal (accessible) ──
  _showRestoreModal(draft, ageText) {
    if (this._modal) return;

    this._modal = document.createElement('div');
    this._modal.setAttribute('role', 'dialog');
    this._modal.setAttribute('aria-modal', 'true');
    this._modal.setAttribute('aria-labelledby', 'ds-modal-title');
    this._modal.className = 'ds-overlay';

    // Restore focus to previous element on close
    const prevFocus = document.activeElement;

    this._modal.innerHTML = `
      <div class="ds-modal">
        <h2 id="ds-modal-title" class="ds-modal-title">Draft Ditemui</h2>
        <p class="ds-modal-text">Kami menjumpai draf RPH yang belum selesai, disimpan <strong>${ageText}</strong>.</p>
        <p class="ds-modal-text">Adakah anda ingin menyambung semula kerja yang lepas?</p>
        <div class="ds-modal-actions">
          <button id="ds-restore-btn" class="ds-btn ds-btn-primary">Ya, Sambung Semula</button>
          <button id="ds-discard-btn" class="ds-btn ds-btn-secondary">Buang Draf</button>
        </div>
      </div>
    `;

    document.body.appendChild(this._modal);

    // Focus trap: trap focus inside modal
    const restoreBtn = this._modal.querySelector('#ds-restore-btn');
    const discardBtn = this._modal.querySelector('#ds-discard-btn');

    // Focus first button
    setTimeout(() => restoreBtn.focus(), 100);

    // Trap focus
    this._modal.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        this._closeModal(prevFocus);
        return;
      }
      if (e.key === 'Tab') {
        const focusable = [restoreBtn, discardBtn];
        const first = focusable[0];
        const last = focusable[focusable.length - 1];
        if (e.shiftKey && document.activeElement === first) {
          e.preventDefault();
          last.focus();
        } else if (!e.shiftKey && document.activeElement === last) {
          e.preventDefault();
          first.focus();
        }
      }
    });

    // Click outside to close
    this._modal.addEventListener('click', (e) => {
      if (e.target === this._modal) this._closeModal(prevFocus);
    });

    restoreBtn.addEventListener('click', () => {
      this.options.onRestore(draft);
      this.clearDraft();
      this._closeModal(prevFocus);
    });

    discardBtn.addEventListener('click', () => {
      this.clearDraft();
      this._closeModal(prevFocus);
    });
  }

  _closeModal(prevFocus) {
    if (this._modal) {
      if (this._modal.parentNode) this._modal.parentNode.removeChild(this._modal);
      this._modal = null;
    }
    if (prevFocus && prevFocus.focus) prevFocus.focus();
  }

  // ── Toast notification ──
  _announce(msg) {
    // Use aria-live region (create if needed)
    if (!this._toast) {
      this._toast = document.createElement('div');
      this._toast.setAttribute('aria-live', 'polite');
      this._toast.className = 'ds-toast sr-only';
      document.body.appendChild(this._toast);
    }
    this._toast.textContent = '';
    requestAnimationFrame(() => { this._toast.textContent = msg; });
  }
}

// ────────────────────────────────────────────
//  STYLES
// ────────────────────────────────────────────
(function injectDraftSyncStyles() {
  if (document.getElementById('ds-styles')) return;
  const s = document.createElement('style');
  s.id = 'ds-styles';
  s.textContent = `
    .ds-badge {
      position: fixed; bottom: 1rem; left: 1rem; z-index: 9999;
      display: inline-flex; align-items: center; gap: 0.35rem;
      padding: 0.3rem 0.65rem; border-radius: 9999px;
      font-size: 0.65rem; font-weight: 600;
      background: #1e293b; color: #e2e8f0;
      box-shadow: 0 2px 8px rgba(0,0,0,0.15);
      transition: opacity 0.3s;
    }
    .ds-dot { display: inline-block; width: 7px; height: 7px; border-radius: 50%; }
    .ds-dot-online { background: #22c55e; box-shadow: 0 0 4px #22c55e88; }
    .ds-dot-offline { background: #ef4444; box-shadow: 0 0 4px #ef444488; }
    .ds-overlay {
      position: fixed; inset: 0; z-index: 10000;
      display: flex; align-items: center; justify-content: center;
      background: rgba(0,0,0,0.4); backdrop-filter: blur(2px);
    }
    .ds-modal {
      background: #fff; border-radius: 1rem; padding: 1.5rem 2rem;
      max-width: 400px; width: 90%; box-shadow: 0 20px 60px rgba(0,0,0,0.15);
    }
    .ds-modal-title { font-size: 1.1rem; font-weight: 700; color: #1e293b; margin-bottom: 0.5rem; }
    .ds-modal-text { font-size: 0.85rem; color: #475569; line-height: 1.5; margin-bottom: 0.5rem; }
    .ds-modal-actions { display: flex; gap: 0.5rem; margin-top: 1rem; }
    .ds-btn {
      flex: 1; padding: 0.55rem 1rem; border-radius: 0.5rem;
      font-size: 0.8rem; font-weight: 600; cursor: pointer; border: none;
      transition: background 0.15s, transform 0.1s;
    }
    .ds-btn:focus-visible { outline: 2px solid #6366f1; outline-offset: 2px; }
    .ds-btn-primary { background: #6366f1; color: #fff; }
    .ds-btn-primary:hover { background: #4f46e5; }
    .ds-btn-secondary { background: #f1f5f9; color: #334155; }
    .ds-btn-secondary:hover { background: #e2e8f0; }
    .ds-toast { position: absolute; }
    .sr-only { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border-width: 0; }
    @media (prefers-reduced-motion: reduce) { .ds-modal { transition: none; } }
  `;
  document.head.appendChild(s);
})();

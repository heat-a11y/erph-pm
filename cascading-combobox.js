/**
 * CascadingCombobox — Framework-agnostic, WAI-ARIA compliant cascading combobox
 * for hierarchical DSKP curriculum data: Year → Subject → Unit → Content Std → Learning Std
 *
 * WCAG 2.2 AA • Works with Alpine.js, React, Vue, or vanilla JS
 *
 * Usage:
 *   const cc = new CascadingCombobox(containerElement, {
 *     data: CURRICULUM_DATA,   // your hierarchical JSON
 *     onChange: (path) => { /* path = {year, subject, unit, cs, ls} */ }
 *   });
 */
class CascadingCombobox {
  constructor(container, opts = {}) {
    this.container = container;
    this.data = opts.data || {};
    this.onChange = opts.onChange || (() => {});
    this.path = { year: '', subject: '', unit: '', cs: '', ls: '' };
    this.debounceTimers = {};
    this.combos = {};
    this.liveRegion = null;

    this.LABELS = {
      year:   { bm: 'Tahun', en: 'Year', zh: '年级' },
      subject:{ bm: 'Subjek', en: 'Subject', zh: '科目' },
      unit:   { bm: 'Unit', en: 'Unit', zh: '单元' },
      cs:     { bm: 'Standard Kandungan', en: 'Content Standard', zh: '内容标准' },
      ls:     { bm: 'Standard Pembelajaran', en: 'Learning Standard', zh: '学习标准' },
    };
    this.LANG = opts.lang || 'zh';

    this._build();
    this._announce('Cascading combobox initialized');
  }

  // ── BUILD DOM ──
  _build() {
    this.container.classList.add('cc-container');

    // aria-live region for announcements
    this.liveRegion = document.createElement('div');
    this.liveRegion.setAttribute('aria-live', 'polite');
    this.liveRegion.setAttribute('aria-atomic', 'true');
    this.liveRegion.className = 'sr-only';
    this.container.appendChild(this.liveRegion);

    const levels = ['year', 'subject', 'unit', 'cs', 'ls'];
    levels.forEach((level, idx) => {
      const wrapper = document.createElement('div');
      wrapper.className = 'cc-level';
      wrapper.dataset.level = level;

      const label = document.createElement('label');
      label.className = 'cc-label';
      label.id = `cc-label-${level}`;
      label.textContent = this._lbl(level);

      const combo = document.createElement('div');
      combo.className = 'cc-combobox';
      combo.setAttribute('role', 'combobox');
      combo.setAttribute('aria-expanded', 'false');
      combo.setAttribute('aria-haspopup', 'listbox');
      combo.setAttribute('aria-controls', `cc-list-${level}`);
      combo.setAttribute('aria-labelledby', `cc-label-${level}`);
      combo.dataset.level = level;

      const input = document.createElement('input');
      input.type = 'text';
      input.className = 'cc-input';
      input.id = `cc-input-${level}`;
      input.setAttribute('role', 'searchbox');
      input.setAttribute('aria-autocomplete', 'list');
      input.setAttribute('aria-controls', `cc-list-${level}`);
      input.setAttribute('aria-activedescendant', '');
      input.setAttribute('autocomplete', 'off');
      input.placeholder = `Pilih ${this._lbl(level)}...`;
      input.dataset.level = level;

      const toggle = document.createElement('button');
      toggle.type = 'button';
      toggle.className = 'cc-toggle';
      toggle.setAttribute('tabindex', '-1');
      toggle.setAttribute('aria-label', 'Toggle dropdown');
      toggle.innerHTML = '▾';
      toggle.dataset.level = level;

      const list = document.createElement('ul');
      list.className = 'cc-list';
      list.id = `cc-list-${level}`;
      list.setAttribute('role', 'listbox');
      list.setAttribute('aria-labelledby', `cc-label-${level}`);
      list.hidden = true;
      list.dataset.level = level;

      combo.appendChild(input);
      combo.appendChild(toggle);
      wrapper.appendChild(label);
      wrapper.appendChild(combo);
      wrapper.appendChild(list);
      this.container.appendChild(wrapper);

      this.combos[level] = { wrapper, combo, input, toggle, list, label };
      this._bindEvents(level);
    });
  }

  _lbl(key) {
    return this.LABELS[key]?.[this.LANG] || key;
  }

  // ── EVENTS ──
  _bindEvents(level) {
    const c = this.combos[level];
    if (!c) return;

    // Input: filter on keyup (debounced)
    c.input.addEventListener('input', () => {
      this._debounce(`filter-${level}`, () => this._filter(level), 200);
    });

    // Focus: open list
    c.input.addEventListener('focus', () => this._open(level));

    // Click on toggle
    c.toggle.addEventListener('click', () => {
      if (c.combo.getAttribute('aria-expanded') === 'true') {
        this._close(level);
      } else {
        this._open(level);
      }
    });

    // Keyboard
    c.input.addEventListener('keydown', (e) => this._keydown(level, e));

    // Click outside
    document.addEventListener('click', (e) => {
      if (!c.wrapper.contains(e.target)) this._close(level);
    });

    // Blur: close on delay for click on list item
    c.input.addEventListener('blur', () => {
      setTimeout(() => this._close(level), 200);
    });
  }

  // ── KEYBOARD ──
  _keydown(level, e) {
    const c = this.combos[level];
    const items = c.list.querySelectorAll('[role="option"]');
    const active = c.list.querySelector('[role="option"][aria-selected="true"]');
    let idx = active ? Array.from(items).indexOf(active) : -1;

    switch (e.key) {
      case 'ArrowDown':
        e.preventDefault();
        if (!c.list.hidden) {
          const next = Math.min(idx + 1, items.length - 1);
          this._setActive(level, next);
        } else {
          this._open(level);
        }
        break;
      case 'ArrowUp':
        e.preventDefault();
        if (!c.list.hidden) {
          const prev = Math.max(idx - 1, 0);
          this._setActive(level, prev);
        }
        break;
      case 'Enter':
      case ' ':
        e.preventDefault();
        if (!c.list.hidden && active) {
          this._select(level, active.dataset.value, active.textContent);
          this._close(level);
        }
        break;
      case 'Escape':
        e.preventDefault();
        this._close(level);
        c.input.blur();
        break;
      case 'Home':
        e.preventDefault();
        this._setActive(level, 0);
        break;
      case 'End':
        e.preventDefault();
        this._setActive(level, items.length - 1);
        break;
    }
  }

  // ── OPEN / CLOSE / FILTER ──
  _getOptions(level) {
    try {
      switch (level) {
        case 'year': return Object.keys(this.data).map(y => ({ value: y, label: y }));
        case 'subject': {
          if (!this.path.year) return [];
          const entry = this.data[this.path.year];
          if (!entry) return [];
          const subjCodes = Object.keys(entry);
          const subjNames = window.SUBJECTS || [];
          return subjCodes.map(c => ({ value: c, label: subjNames.find(s => s.c === c)?.n || c }));
        }
        case 'unit': {
          if (!this.path.year || !this.path.subject) return [];
          const units = this.data[this.path.year]?.[this.path.subject]?.units || [];
          return units.map(u => ({ value: u.title, label: u.title }));
        }
        case 'cs': {
          const lang = this.data.LANG?.[this.path.subject] || 'zh';
          const sk = this.data.SK?.[lang] || [];
          return sk.map(s => ({ value: s, label: s }));
        }
        case 'ls': {
          const lang = this.data.LANG?.[this.path.subject] || 'zh';
          const sp = this.data.SP?.[lang] || [];
          return sp.map(s => ({ value: s, label: s }));
        }
        default: return [];
      }
    } catch { return []; }
  }

  _open(level) {
    const c = this.combos[level];
    this._filter(level);
    c.combo.setAttribute('aria-expanded', 'true');
    c.list.hidden = false;
  }

  _close(level) {
    const c = this.combos[level];
    c.combo.setAttribute('aria-expanded', 'false');
    c.list.hidden = true;
    c.input.setAttribute('aria-activedescendant', '');
  }

  _filter(level) {
    const c = this.combos[level];
    const query = c.input.value.toLowerCase();
    const options = this._getOptions(level);
    const filtered = query ? options.filter(o => o.label.toLowerCase().includes(query)) : options;
    this._renderList(level, filtered);
  }

  _renderList(level, options) {
    const c = this.combos[level];
    c.list.innerHTML = '';
    if (!options.length) {
      const li = document.createElement('li');
      li.className = 'cc-empty';
      li.textContent = 'Tiada pilihan';
      li.setAttribute('role', 'option');
      li.setAttribute('aria-disabled', 'true');
      c.list.appendChild(li);
      return;
    }
    options.forEach((opt, i) => {
      const li = document.createElement('li');
      li.className = 'cc-option';
      li.id = `cc-opt-${level}-${i}`;
      li.setAttribute('role', 'option');
      li.setAttribute('aria-selected', 'false');
      li.dataset.value = opt.value;
      li.textContent = opt.label;
      li.addEventListener('click', () => {
        this._select(level, opt.value, opt.label);
        this._close(level);
        c.input.focus();
      });
      li.addEventListener('mouseenter', () => this._setActive(level, i));
      c.list.appendChild(li);
    });
    // auto-highlight first
    if (options.length) this._setActive(level, 0);
  }

  _setActive(level, idx) {
    const c = this.combos[level];
    const items = c.list.querySelectorAll('[role="option"]');
    items.forEach((item, i) => {
      item.setAttribute('aria-selected', i === idx ? 'true' : 'false');
      item.classList.toggle('cc-active', i === idx);
    });
    const active = items[idx];
    if (active) {
      c.input.setAttribute('aria-activedescendant', active.id);
      active.scrollIntoView({ block: 'nearest' });
    }
  }

  _select(level, value, label) {
    const c = this.combos[level];
    c.input.value = label;
    this.path[level] = value;

    // Clear dependent levels
    const levels = ['year', 'subject', 'unit', 'cs', 'ls'];
    const idx = levels.indexOf(level);
    for (let i = idx + 1; i < levels.length; i++) {
      this.path[levels[i]] = '';
      this.combos[levels[i]].input.value = '';
    }

    // Close all lower lists
    for (let i = idx + 1; i < levels.length; i++) {
      this._close(levels[i]);
    }

    this.onChange({ ...this.path });

    // Announce for screen readers
    const nextLevel = idx < levels.length - 1 ? this._lbl(levels[idx + 1]) : null;
    this._announce(
      `Dipilih: ${label}. ${nextLevel ? `Sila pilih ${nextLevel}.` : 'Semua peringkat telah dipilih.'}`
    );
  }

  // ── UTILITY ──
  _debounce(key, fn, ms) {
    clearTimeout(this.debounceTimers[key]);
    this.debounceTimers[key] = setTimeout(fn, ms);
  }

  _announce(msg) {
    if (this.liveRegion) {
      this.liveRegion.textContent = '';
      requestAnimationFrame(() => { this.liveRegion.textContent = msg; });
    }
  }

  // ── PUBLIC API ──
  setData(data) { this.data = data; this._announce('Data dikemas kini'); }
  setLang(lang) { this.LANG = lang; Object.keys(this.combos).forEach(l => { this.combos[l].label.textContent = this._lbl(l); }); }
  getPath() { return { ...this.path }; }
  setPath(path) {
    Object.assign(this.path, path);
    Object.keys(path).forEach(level => {
      if (this.combos[level]) this.combos[level].input.value = path[level] || '';
    });
    this._announce('Laluan dikemas kini');
  }
  destroy() {
    Object.values(this.combos).forEach(c => { c.wrapper.remove(); });
    if (this.liveRegion) this.liveRegion.remove();
  }
}

// ── STYLES (inject once) ──
(function injectStyles() {
  if (document.getElementById('cc-styles')) return;
  const style = document.createElement('style');
  style.id = 'cc-styles';
  style.textContent = `
    .cc-container { display: flex; flex-direction: column; gap: 0.5rem; width: 100%; }
    .cc-level { display: flex; flex-direction: column; gap: 0.15rem; position: relative; }
    .cc-label { font-size: 0.7rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; color: #64748b; }
    .cc-combobox { display: flex; align-items: center; border: 1px solid #cbd5e1; border-radius: 0.5rem; background: #fff; transition: border-color 0.15s; }
    .cc-combobox:focus-within { border-color: #6366f1; box-shadow: 0 0 0 2px rgba(99,102,241,0.2); }
    .cc-input { flex: 1; border: none; background: transparent; padding: 0.45rem 0.5rem; font-size: 0.8rem; outline: none; min-width: 0; color: #1e293b; }
    .cc-input::placeholder { color: #94a3b8; }
    .cc-toggle { padding: 0.25rem 0.5rem; background: transparent; border: none; cursor: pointer; color: #64748b; font-size: 0.7rem; line-height: 1; }
    .cc-toggle:hover { color: #334155; }
    .cc-list { position: absolute; top: 100%; left: 0; right: 0; z-index: 50; max-height: 180px; overflow-y: auto; background: #fff; border: 1px solid #e2e8f0; border-radius: 0.5rem; margin-top: 2px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); list-style: none; padding: 0.25rem 0; }
    .cc-list:not([hidden]) { display: block; }
    .cc-option { padding: 0.35rem 0.75rem; font-size: 0.75rem; cursor: pointer; color: #334155; transition: background 0.1s; }
    .cc-option:hover, .cc-option.cc-active { background: #eef2ff; color: #4338ca; }
    .cc-option[aria-selected="true"] { background: #eef2ff; color: #4338ca; font-weight: 500; }
    .cc-empty { padding: 0.5rem 0.75rem; font-size: 0.7rem; color: #94a3b8; text-align: center; }
    .sr-only { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border-width: 0; }
    @media (prefers-reduced-motion: reduce) { .cc-list { transition: none; } }
    /* Focus ring */
    .cc-input:focus-visible { outline: 2px solid #6366f1; outline-offset: 1px; border-radius: 0.25rem; }
    .cc-toggle:focus-visible { outline: 2px solid #6366f1; outline-offset: 1px; border-radius: 0.25rem; }
  `;
  document.head.appendChild(style);
})();

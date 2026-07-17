/**
 * TagPicker — Accessible multiselect chip array for EMK/KBAT/PAK-21 tags
 *
 * WCAG 2.2 AA:
 *  - Keyboard: Arrow keys navigate, Space/Enter toggles selection
 *  - aria-pressed on each chip, aria-label on the group
 *  - 4.5:1+ contrast ratios on all states
 *  - Hidden <select> or hidden input for form submission
 *
 * Usage:
 *   const tp = new TagPicker(container, {
 *     tags: ['EMK: Bahasa', 'EMK: TMK', 'KBAT: Menganalisis', ...],
 *     selected: ['EMK: Bahasa'],
 *     onChange: (selected) => { /* array of values */ },
 *     columns: 3,           // grid columns
 *     label: 'EMK & KBAT',  // group label
 *   });
 */
class TagPicker {
  constructor(container, opts = {}) {
    this.container = container;
    this._tags = opts.tags || [];
    this._selected = new Set(opts.selected || []);
    this._onChange = opts.onChange || (() => {});
    this._columns = opts.columns || 3;
    this._label = opts.label || 'Pilih tag';
    this._id = opts.id || 'tp-' + Math.random().toString(36).slice(2, 8);
    this._focusIdx = -1;

    this.container.classList.add('tp-container');
    this._build();
  }

  // ── TAG GROUPS ──
  static EMK = [
    'Bahasa', 'Sains dan Teknologi', 'TMK', 'Nilai Murni',
    'Kreativiti dan Inovasi', 'Keusahawanan', 'Kelestarian Alam',
  ];
  static KBAT = [
    'Menganalisis', 'Menilai', 'Mencipta', 'Mengaplikasi',
    'Memahami', 'Mengingat', 'Menyelesaikan Masalah',
  ];
  static PAK21 = [
    'Think-Pair-Share', 'Gallery Walk', 'Round Table', 'Hot Seat',
    'Role Play', 'Jigsaw', 'Brainstorming', 'Stations',
    '3 Stray 1 Stay', 'Bus Stop', 'Quiz Quiz Trade', 'Fan-N-Pick',
  ];

  // ── BUILD ──
  _build() {
    this.container.innerHTML = '';

    // Hidden input for form submission
    this._hidden = document.createElement('input');
    this._hidden.type = 'hidden';
    this._hidden.name = this._id;
    this._hidden.value = [...this._selected].join(',');
    this.container.appendChild(this._hidden);

    // Label
    const label = document.createElement('div');
    label.id = `${this._id}-label`;
    label.className = 'tp-label';
    label.textContent = this._label;
    this.container.appendChild(label);

    // Grid
    const grid = document.createElement('div');
    grid.className = 'tp-grid';
    grid.setAttribute('role', 'group');
    grid.setAttribute('aria-labelledby', `${this._id}-label`);
    grid.style.gridTemplateColumns = `repeat(${this._columns}, 1fr)`;
    grid.tabIndex = -1;

    this._tags.forEach((tag, i) => {
      const chip = document.createElement('button');
      chip.type = 'button';
      chip.className = 'tp-chip';
      chip.id = `${this._id}-chip-${i}`;
      chip.setAttribute('role', 'button');
      chip.setAttribute('aria-pressed', this._selected.has(tag) ? 'true' : 'false');
      chip.dataset.value = tag;
      chip.dataset.index = i;
      chip.textContent = tag;

      // Visual state
      if (this._selected.has(tag)) chip.classList.add('tp-selected');

      // Click
      chip.addEventListener('click', () => this._toggle(tag));

      grid.appendChild(chip);
    });

    this.container.appendChild(grid);
    this._grid = grid;

    // Keyboard on container (delegated)
    this.container.addEventListener('keydown', (e) => this._keydown(e));
    this._chips = grid.querySelectorAll('.tp-chip');
  }

  // ── TOGGLE ──
  _toggle(tag) {
    if (this._selected.has(tag)) {
      this._selected.delete(tag);
    } else {
      this._selected.add(tag);
    }
    this._syncUI();
    this._onChange([...this._selected]);
  }

  _syncUI() {
    this._chips.forEach(chip => {
      const tag = chip.dataset.value;
      const isSel = this._selected.has(tag);
      chip.setAttribute('aria-pressed', isSel ? 'true' : 'false');
      chip.classList.toggle('tp-selected', isSel);
    });
    this._hidden.value = [...this._selected].join(',');
  }

  // ── KEYBOARD ──
  _keydown(e) {
    const chips = this._chips;
    if (!chips.length) return;

    switch (e.key) {
      case 'ArrowRight':
      case 'ArrowDown':
        e.preventDefault();
        this._focusIdx = Math.min(this._focusIdx + 1, chips.length - 1);
        this._focusIdx = Math.max(this._focusIdx, 0);
        chips[this._focusIdx].focus();
        break;

      case 'ArrowLeft':
      case 'ArrowUp':
        e.preventDefault();
        this._focusIdx = Math.max(this._focusIdx - 1, 0);
        chips[this._focusIdx].focus();
        break;

      case ' ':
      case 'Enter':
        e.preventDefault();
        if (document.activeElement?.dataset?.value) {
          this._toggle(document.activeElement.dataset.value);
        }
        break;

      case 'Home':
        e.preventDefault();
        this._focusIdx = 0;
        chips[0]?.focus();
        break;

      case 'End':
        e.preventDefault();
        this._focusIdx = chips.length - 1;
        chips[chips.length - 1]?.focus();
        break;
    }
  }

  // ── PUBLIC API ──
  getSelected() { return [...this._selected]; }
  setSelected(arr) {
    this._selected = new Set(arr);
    this._syncUI();
  }
  addTag(tag) {
    if (!this._tags.includes(tag)) {
      this._tags.push(tag);
      this._build();
    }
  }
  destroy() { this.container.innerHTML = ''; }
}

// ── STYLES ──
(function injectTPStyles() {
  if (document.getElementById('tp-styles')) return;
  const s = document.createElement('style');
  s.id = 'tp-styles';
  s.textContent = `
    .tp-container { display: flex; flex-direction: column; gap: 0.5rem; width: 100%; }
    .tp-label { font-size: 0.7rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; color: #475569; }
    .tp-grid { display: grid; gap: 0.35rem; }
    .tp-chip {
      display: inline-flex; align-items: center; justify-content: center;
      padding: 0.4rem 0.6rem; border-radius: 9999px;
      font-size: 0.7rem; font-weight: 500; line-height: 1.3;
      border: 1.5px solid #cbd5e1; background: #fff; color: #334155;
      cursor: pointer; transition: all 0.12s ease;
      min-height: 32px;
      user-select: none;
      -webkit-tap-highlight-color: transparent;
    }
    .tp-chip:hover { border-color: #818cf8; background: #eef2ff; }
    .tp-chip:focus-visible {
      outline: 2px solid #6366f1; outline-offset: 2px;
      box-shadow: 0 0 0 3px rgba(99,102,241,0.2);
    }
    /* Selected: deep indigo bg + white text = 6.5:1 contrast */
    .tp-chip.tp-selected {
      background: #4338ca; color: #fff; border-color: #4338ca;
    }
    .tp-chip.tp-selected:hover {
      background: #3730a3; border-color: #3730a3;
    }
    /* Remove button style for non-selected */
    .tp-chip:not(.tp-selected) { background: #f8fafc; }
    @media (prefers-reduced-motion: reduce) { .tp-chip { transition: none; } }
  `;
  document.head.appendChild(s);
})();

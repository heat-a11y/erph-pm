/**
 * ReflectionGenerator — Interactive mastery-based reflection composer
 *
 * Features:
 *  - Present / Total Students numeric inputs (range sliders + number inputs)
 *  - Auto-generates reflection text based on mastery %
 *  - Editable <textarea> for teacher customization
 *  - WCAG 2.2 AA: labelled inputs, aria-valuenow/min/max on sliders
 *  - Framework-agnostic; emits events for Alpine.js integration
 *
 * Usage:
 *   const rg = new ReflectionGenerator(containerElement, {
 *     present: 12, total: 18,
 *     onChange: (text) => { /* textarea value */ }
 *   });
 *   rg.setValues(15, 20);
 */
class ReflectionGenerator {
  constructor(container, opts = {}) {
    this.container = container;
    this._present = opts.present || 0;
    this._total = opts.total || 0;
    this._onChange = opts.onChange || (() => {});
    this._lang = opts.lang || 'zh';
    this._text = '';

    this.container.classList.add('rg-container');
    this._build();
    this._update();
  }

  // ── LANG-ADAPTED TEMPLATES ──
  _templates() {
    const L = this._lang;
    return {
      presentLabel:   L === 'bm' ? 'Hadir' : L === 'en' ? 'Present' : '出席人数',
      totalLabel:     L === 'bm' ? 'Jumlah' : L === 'en' ? 'Total' : '学生总数',
      masteryLabel:   L === 'bm' ? 'Penguasaan' : L === 'en' ? 'Mastery' : '掌握率',
      generateBtn:    L === 'bm' ? 'Jana Refleksi' : L === 'en' ? 'Generate Reflection' : '生成反思',
      highText:  (p, t) => L === 'bm' ? `${p}/${t} murid berjaya menguasai standard pembelajaran dan boleh menyelesaikan aktiviti pentaksiran secara berdikari.`
                   : L === 'en' ? `${p}/${t} pupils successfully mastered the learning standards and could independently complete the assessment activities.`
                   : `${p}/${t} 的学生成功掌握了今日的学习标准，并能独立完成课堂评估活动。`,
      midText:   (p, t) => L === 'bm' ? `${p}/${t} murid menguasai standard pembelajaran. Murid selebihnya akan diberi bimbingan tambahan semasa waktu pemulihan.`
                   : L === 'en' ? `${p}/${t} pupils mastered the learning standards. The remaining pupils will receive targeted guidance during remedial sessions.`
                   : `${p}/${t} 的学生掌握了今日的学习标准，其余学生将在辅导时间获得针对性辅导。`,
      lowText:       L === 'bm' ? 'Majoriti murid belum mencapai tahap penguasaan. Guru akan mengadakan aktiviti pengukuhan dan ulang kaji pada sesi akan datang.'
                   : L === 'en' ? 'Majority of pupils have not achieved mastery. The teacher will conduct reinforcement and review activities in the next session.'
                   : '多数学生未达标，教师将在下一堂课针对此学习标准进行重温与巩固练习。',
      placeholder:   L === 'bm' ? 'Tambahkan refleksi peribadi...' : L === 'en' ? 'Add personal reflection...' : '添加个人反思...',
    };
  }

  // ── BUILD DOM ──
  _build() {
    this.container.innerHTML = '';
    const T = this._templates();

    // Inputs row
    const row = document.createElement('div');
    row.className = 'rg-row';

    // Present
    const presGroup = this._makeSliderInput('present', T.presentLabel, 0, 60, 1);
    row.appendChild(presGroup.wrapper);

    // Total
    const totalGroup = this._makeSliderInput('total', T.totalLabel, 0, 60, 1);
    row.appendChild(totalGroup.wrapper);

    this.container.appendChild(row);

    // Mastery bar
    const barWrap = document.createElement('div');
    barWrap.className = 'rg-bar-wrap';
    barWrap.innerHTML = `
      <div class="rg-bar-label">
        <span id="rg-mastery-label">${T.masteryLabel}</span>
        <span id="rg-pct" class="rg-pct">0%</span>
      </div>
      <div class="rg-bar-track" role="presentation">
        <div id="rg-bar-fill" class="rg-bar-fill" style="width:0%"></div>
      </div>
    `;
    this.container.appendChild(barWrap);

    // Generate button
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'rg-btn';
    btn.textContent = T.generateBtn;
    btn.addEventListener('click', () => this._generate());
    this.container.appendChild(btn);

    // Textarea
    const ta = document.createElement('textarea');
    ta.id = 'reflection';
    ta.className = 'rg-textarea';
    ta.placeholder = T.placeholder;
    ta.rows = 3;
    ta.addEventListener('input', () => {
      this._text = ta.value;
      this._onChange(ta.value);
    });
    this.container.appendChild(ta);

    // Store refs
    this._els = {
      presentSlider: presGroup.slider,
      presentNumber: presGroup.number,
      totalSlider: totalGroup.slider,
      totalNumber: totalGroup.number,
      pct: barWrap.querySelector('#rg-pct'),
      barFill: barWrap.querySelector('#rg-bar-fill'),
      btn,
      textarea: ta,
    };

    // Sync sliders <-> number inputs
    presGroup.slider.addEventListener('input', () => {
      presGroup.number.value = presGroup.slider.value;
      this._present = parseInt(presGroup.slider.value, 10);
      this._update();
    });
    presGroup.number.addEventListener('input', () => {
      presGroup.slider.value = presGroup.number.value;
      this._present = parseInt(presGroup.number.value, 10) || 0;
      this._update();
    });

    totalGroup.slider.addEventListener('input', () => {
      totalGroup.number.value = totalGroup.slider.value;
      this._total = parseInt(totalGroup.slider.value, 10);
      this._update();
    });
    totalGroup.number.addEventListener('input', () => {
      totalGroup.slider.value = totalGroup.number.value;
      this._total = parseInt(totalGroup.number.value, 10) || 0;
      this._update();
    });
  }

  _makeSliderInput(name, labelText, min, max, step) {
    const wrapper = document.createElement('div');
    wrapper.className = 'rg-field';

    const label = document.createElement('label');
    label.htmlFor = `rg-${name}`;
    label.className = 'rg-field-label';
    label.textContent = labelText;

    const slider = document.createElement('input');
    slider.type = 'range';
    slider.id = `rg-${name}`;
    slider.min = min;
    slider.max = max;
    slider.step = step;
    slider.value = 0;
    slider.setAttribute('aria-valuenow', '0');
    slider.setAttribute('aria-valuemin', min);
    slider.setAttribute('aria-valuemax', max);
    slider.setAttribute('aria-labelledby', label.id || label.htmlFor);
    slider.className = 'rg-slider';

    const number = document.createElement('input');
    number.type = 'number';
    number.className = 'rg-number';
    number.min = min;
    number.max = max;
    number.value = 0;
    number.setAttribute('aria-label', `${labelText} (angka)`);

    wrapper.appendChild(label);
    wrapper.appendChild(slider);
    wrapper.appendChild(number);

    return { wrapper, slider, number };
  }

  // ── UPDATE ──
  _update() {
    const pct = this._total > 0 ? Math.round((this._present / this._total) * 100) : 0;
    if (this._els) {
      this._els.pct.textContent = pct + '%';
      this._els.barFill.style.width = pct + '%';
      // Color the bar
      this._els.barFill.className = 'rg-bar-fill' + (pct >= 80 ? ' rg-bar-high' : pct >= 50 ? ' rg-bar-mid' : ' rg-bar-low');
      // Update aria-valuenow
      this._els.presentSlider.setAttribute('aria-valuenow', this._present);
      this._els.totalSlider.setAttribute('aria-valuenow', this._total);
    }
  }

  // ── GENERATE REFLECTION ──
  _generate() {
    const p = this._present, t = this._total;
    const pct = t > 0 ? (p / t) * 100 : 0;
    const T = this._templates();

    let text;
    if (pct >= 80) {
      text = T.highText(p, t);
    } else if (pct >= 50) {
      text = T.midText(p, t);
    } else {
      text = T.lowText;
    }

    // Append existing text if any
    const existing = this._els.textarea.value.trim();
    this._text = existing ? existing + '\n' + text : text;
    this._els.textarea.value = this._text;
    // Auto-grow
    this._els.textarea.style.height = 'auto';
    this._els.textarea.style.height = this._els.textarea.scrollHeight + 'px';
    this._onChange(this._text);
  }

  // ── PUBLIC API ──
  setValues(present, total) {
    this._present = Math.max(0, Math.min(present, 60));
    this._total = Math.max(0, Math.min(total, 60));
    if (this._els) {
      this._els.presentSlider.value = this._present;
      this._els.presentNumber.value = this._present;
      this._els.totalSlider.value = this._total;
      this._els.totalNumber.value = this._total;
    }
    this._update();
  }

  getValues() { return { present: this._present, total: this._total }; }
  getText() { return this._text || this._els?.textarea?.value || ''; }
  setText(text) { if (this._els) { this._els.textarea.value = text; this._text = text; } }

  setLang(lang) { this._lang = lang; this._rebuild(); }
  _rebuild() { this._build(); this.setValues(this._present, this._total); }

  destroy() {
    if (this.container) this.container.innerHTML = '';
  }
}

// ── STYLES ──
(function injectRGStyles() {
  if (document.getElementById('rg-styles')) return;
  const s = document.createElement('style');
  s.id = 'rg-styles';
  s.textContent = `
    .rg-container { display: flex; flex-direction: column; gap: 0.65rem; }
    .rg-row { display: flex; gap: 1rem; flex-wrap: wrap; }
    .rg-field { flex: 1; min-width: 140px; display: flex; flex-direction: column; gap: 0.2rem; }
    .rg-field-label { font-size: 0.7rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; color: #64748b; }
    .rg-slider { width: 100%; height: 6px; cursor: pointer; accent-color: #6366f1; }
    .rg-slider:focus-visible { outline: 2px solid #6366f1; outline-offset: 2px; border-radius: 4px; }
    .rg-number { width: 4rem; padding: 0.25rem; border: 1px solid #cbd5e1; border-radius: 0.35rem; font-size: 0.8rem; text-align: center; }
    .rg-number:focus-visible { outline: 2px solid #6366f1; outline-offset: 1px; }
    .rg-bar-wrap { display: flex; flex-direction: column; gap: 0.2rem; }
    .rg-bar-label { display: flex; justify-content: space-between; font-size: 0.7rem; color: #64748b; }
    .rg-pct { font-weight: 700; font-size: 0.85rem; }
    .rg-bar-track { height: 8px; background: #e2e8f0; border-radius: 999px; overflow: hidden; }
    .rg-bar-fill { height: 100%; border-radius: 999px; transition: width 0.3s ease, background 0.3s; }
    .rg-bar-high { background: #22c55e; }
    .rg-bar-mid { background: #eab308; }
    .rg-bar-low { background: #ef4444; }
    .rg-btn {
      align-self: flex-start; padding: 0.4rem 1rem; border-radius: 0.5rem;
      font-size: 0.75rem; font-weight: 600; cursor: pointer; border: none;
      background: #6366f1; color: #fff; transition: background 0.15s;
    }
    .rg-btn:hover { background: #4f46e5; }
    .rg-btn:focus-visible { outline: 2px solid #6366f1; outline-offset: 2px; }
    .rg-textarea { width: 100%; padding: 0.65rem; border: 2px solid #fde68a; border-radius: 0.5rem; font-size: 0.8rem; line-height: 1.6; resize: vertical; background: #fffbeb; color: #78350f; }
    .rg-textarea:focus-visible { outline: 2px solid #f59e0b; outline-offset: 1px; }
    @media (prefers-reduced-motion: reduce) { .rg-bar-fill { transition: none; } }
  `;
  document.head.appendChild(s);
})();

/**
 * The Cheat Code — Interactive Step-Through Engine
 * Vanilla JS, zero dependencies. Progressive enhancement.
 *
 * Supports two rendering modes:
 *   - Legacy mode (no contextMode): uses expand panel with data-expand-* attributes
 *   - Context mode (contextMode: 'lightweight' | 'detailed'): uses richer context panel
 *     driven by data-context JSON attribute on diagram elements
 */

(function () {
  'use strict';

  /* ========================================================
     StepEngine — drives the step-through walkthrough
     ======================================================== */
  class StepEngine {
    /**
     * @param {Object} config
     * @param {string} config.container      - CSS selector for diagram canvas
     * @param {Array}  config.steps          - [{id, title, description, highlight: [selector], arrowHighlight: [selector]}]
     * @param {string} [config.contextMode]  - 'lightweight' | 'detailed' — enables context panel
     */
    constructor(config) {
      this.steps = config.steps || [];
      this.container = document.querySelector(config.container);
      this.contextMode = config.contextMode || null; // null = legacy behaviour
      this.currentStep = -1; // -1 = overview
      this.visited = new Set();

      // Track last-clicked element for keyboard 'i' shortcut
      this._lastContextEl = null;

      // Track trigger element for focus restoration on panel close
      this._contextTrigger = null;

      this._buildUI();
      this._bindKeys();
      this._bindClicks();

      if (this.contextMode) {
        this._buildContextPanel();
      } else {
        this._buildExpandPanel();
      }
    }

    /* -------------------------------------------------------
       UI Construction
       ------------------------------------------------------- */

    _buildUI() {
      // Narrative panel
      this.narrativePanel = document.createElement('div');
      this.narrativePanel.className = 'narrative-panel';
      this.narrativePanel.innerHTML = `
        <div class="narrative-step-label"></div>
        <div class="narrative-title"></div>
        <p class="narrative-text"></p>
      `;
      document.body.appendChild(this.narrativePanel);

      // Step bar
      this.stepBar = document.createElement('div');
      this.stepBar.className = 'step-bar';
      this.stepBar.innerHTML = `
        <button class="btn-prev" aria-label="Previous step">\u2190 Prev</button>
        <div class="step-dots">${this.steps.map((_, i) =>
          `<div class="step-dot" data-dot="${i}" title="Step ${i + 1}"></div>`
        ).join('')}</div>
        <div class="step-counter">Overview</div>
        <button class="btn-next btn-primary" aria-label="Next step">Next \u2192</button>
        <button class="btn-reset" aria-label="Reset to overview">\u27f2 Reset</button>
      `;
      document.body.appendChild(this.stepBar);

      // Cache button refs
      this.btnPrev = this.stepBar.querySelector('.btn-prev');
      this.btnNext = this.stepBar.querySelector('.btn-next');
      this.btnReset = this.stepBar.querySelector('.btn-reset');
      this.counter = this.stepBar.querySelector('.step-counter');
      this.dots = Array.from(this.stepBar.querySelectorAll('.step-dot'));

      // Wire buttons
      this.btnPrev.addEventListener('click', () => this.prev());
      this.btnNext.addEventListener('click', () => this.next());
      this.btnReset.addEventListener('click', () => this.reset());
      this.dots.forEach((dot, i) => {
        dot.addEventListener('click', () => this.goTo(i));
      });

      this._updateButtons();
    }

    /* Legacy expand panel — only built when contextMode is NOT set */
    _buildExpandPanel() {
      this.expandOverlay = document.createElement('div');
      this.expandOverlay.className = 'expand-overlay';
      document.body.appendChild(this.expandOverlay);

      this.expandPanel = document.createElement('div');
      this.expandPanel.className = 'expand-panel';
      this.expandPanel.innerHTML = `
        <button class="expand-close" aria-label="Close panel">&times;</button>
        <div class="expand-title"></div>
        <div class="expand-desc"></div>
        <div class="expand-details"></div>
      `;
      document.body.appendChild(this.expandPanel);

      this.expandOverlay.addEventListener('click', () => this._closeExpand());
      this.expandPanel.querySelector('.expand-close').addEventListener('click', () => this._closeExpand());
    }

    /* Context panel — built when contextMode is 'lightweight' or 'detailed' */
    _buildContextPanel() {
      this.contextPanel = document.createElement('div');
      this.contextPanel.className = `context-panel mode-${this.contextMode}`;
      this.contextPanel.setAttribute('aria-label', 'Component context');
      this.contextPanel.setAttribute('role', 'complementary');
      this.contextPanel.innerHTML = `
        <button class="context-close" aria-label="Close panel">&times;</button>
        <div class="context-header">
          <div class="context-title"></div>
        </div>
        <div class="context-content"></div>
      `;
      document.body.appendChild(this.contextPanel);

      this.contextPanel.querySelector('.context-close').addEventListener('click', () => this._closeContext());
    }

    /* -------------------------------------------------------
       Navigation
       ------------------------------------------------------- */

    next() {
      if (this.currentStep < this.steps.length - 1) {
        this.goTo(this.currentStep + 1);
      }
    }

    prev() {
      if (this.currentStep > 0) {
        this.goTo(this.currentStep - 1);
      } else if (this.currentStep === 0) {
        this.reset();
      }
    }

    goTo(stepIndex) {
      if (stepIndex < 0 || stepIndex >= this.steps.length) return;

      this.currentStep = stepIndex;
      this.visited.add(stepIndex);
      const step = this.steps[stepIndex];

      // Activate step mode on container
      this.container.classList.add('step-active');

      // Clear all highlights
      this.container.querySelectorAll('.step-highlight').forEach(el => {
        el.classList.remove('step-highlight');
      });
      this.container.querySelectorAll('.arrow-highlight').forEach(el => {
        el.classList.remove('arrow-highlight');
      });

      // Highlight step elements
      if (step.highlight) {
        step.highlight.forEach(sel => {
          const el = this.container.querySelector(sel);
          if (el) el.classList.add('step-highlight');
        });
      }

      // Highlight arrows
      if (step.arrowHighlight) {
        step.arrowHighlight.forEach(sel => {
          const el = this.container.querySelector(sel);
          if (el) el.classList.add('arrow-highlight');
        });
      }

      // Update narrative
      const panel = this.narrativePanel;
      panel.querySelector('.narrative-step-label').textContent = `Step ${stepIndex + 1} of ${this.steps.length}`;
      panel.querySelector('.narrative-title').textContent = step.title;
      panel.querySelector('.narrative-text').textContent = step.description;
      panel.classList.add('visible');

      // Scroll highlighted element into view
      const firstHighlight = this.container.querySelector('.step-highlight');
      if (firstHighlight) {
        firstHighlight.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }

      this._updateButtons();
    }

    reset() {
      this.currentStep = -1;
      this.container.classList.remove('step-active');

      this.container.querySelectorAll('.step-highlight').forEach(el => {
        el.classList.remove('step-highlight');
      });
      this.container.querySelectorAll('.arrow-highlight').forEach(el => {
        el.classList.remove('arrow-highlight');
      });

      this.narrativePanel.classList.remove('visible');
      this._updateButtons();
    }

    _updateButtons() {
      const atStart = this.currentStep === -1;
      const atEnd = this.currentStep === this.steps.length - 1;

      this.btnPrev.disabled = atStart;
      this.btnNext.disabled = atEnd;
      this.btnNext.textContent = atStart ? 'Start \u2192' : (atEnd ? 'Done' : 'Next \u2192');

      if (atStart) {
        this.counter.textContent = 'Overview';
      } else {
        this.counter.textContent = `Step ${this.currentStep + 1} of ${this.steps.length}`;
      }

      // Update dots
      this.dots.forEach((dot, i) => {
        dot.classList.toggle('active', i === this.currentStep);
        dot.classList.toggle('visited', this.visited.has(i) && i !== this.currentStep);
      });
    }

    /* -------------------------------------------------------
       Keyboard
       ------------------------------------------------------- */

    _bindKeys() {
      document.addEventListener('keydown', (e) => {
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

        switch (e.key) {
          case 'ArrowRight':
          case 'ArrowDown':
            e.preventDefault();
            this.next();
            break;

          case 'ArrowLeft':
          case 'ArrowUp':
            e.preventDefault();
            this.prev();
            break;

          case 'Escape':
            e.preventDefault();
            if (this.contextMode && this.contextPanel && this.contextPanel.classList.contains('visible')) {
              this._closeContext();
            } else if (!this.contextMode && this.expandOverlay && this.expandOverlay.classList.contains('visible')) {
              this._closeExpand();
            } else {
              this.reset();
            }
            break;

          case 'Home':
            e.preventDefault();
            this.reset();
            break;

          // 'i' toggles the context panel for the last-selected element
          case 'i':
          case 'I':
            if (this.contextMode) {
              e.preventDefault();
              if (this.contextPanel && this.contextPanel.classList.contains('visible')) {
                this._closeContext();
              } else if (this._lastContextEl) {
                this._openContext(this._lastContextEl);
              }
            }
            break;
        }
      });
    }

    /* -------------------------------------------------------
       Click Handling — routes to context panel or legacy expand
       ------------------------------------------------------- */

    _bindClicks() {
      this.container.addEventListener('click', (e) => {
        // Look for an element with data-context (context mode click target)
        const contextEl = e.target.closest('[data-context]');
        if (contextEl && this.contextMode) {
          this._lastContextEl = contextEl;
          this._openContext(contextEl);
          return;
        }

        // Fall back to legacy expand panel for data-expand-title elements
        const stepEl = e.target.closest('[data-expand-title]');
        if (!stepEl) return;

        if (this.contextMode) {
          // contextMode is set but element has no data-context — fall back to legacy
          const title = stepEl.dataset.expandTitle || '';
          const desc = stepEl.dataset.expandDesc || '';
          const details = stepEl.dataset.expandDetails || '';
          // Build a temporary legacy panel on demand if it hasn't been built yet
          if (!this.expandPanel) {
            this._buildExpandPanel();
          }
          this._openExpand(title, desc, details);
        } else {
          const title = stepEl.dataset.expandTitle || '';
          const desc = stepEl.dataset.expandDesc || '';
          const details = stepEl.dataset.expandDetails || '';
          this._openExpand(title, desc, details);
        }
      });
    }

    /* -------------------------------------------------------
       Context Panel — open / close / render
       ------------------------------------------------------- */

    _openContext(element) {
      this._contextTrigger = document.activeElement || element;
      let ctx = {};

      try {
        ctx = JSON.parse(element.dataset.context || '{}');
      } catch {
        // Malformed JSON — render what we can
      }

      const title = element.dataset.expandTitle || element.dataset.contextTitle || ctx.title || '';

      // Set title
      this.contextPanel.querySelector('.context-title').textContent = title;

      // Build content
      const content = this.contextPanel.querySelector('.context-content');
      content.innerHTML = '';

      // -- What it is (both modes)
      if (ctx.what) {
        content.appendChild(this._contextSection(
          'What it is',
          `<div class="context-body">${_escHtml(ctx.what)}</div>`
        ));
      }

      // -- What you need / requires (both modes)
      if (Array.isArray(ctx.requires) && ctx.requires.length > 0) {
        const pills = ctx.requires
          .map(r => `<span class="context-pill">${_escHtml(r)}</span>`)
          .join('');
        content.appendChild(this._contextSection(
          'What you need',
          `<div class="context-pills">${pills}</div>`
        ));
      }

      // -- Specifications (detailed only)
      if (this.contextMode === 'detailed' && Array.isArray(ctx.specs) && ctx.specs.length > 0) {
        const rows = ctx.specs.map(s =>
          `<div class="context-row">
             <div class="context-key">${_escHtml(s.key)}</div>
             <div class="context-val">${_escHtml(s.value)}</div>
           </div>`
        ).join('');
        content.appendChild(this._contextSection(
          'Specifications',
          `<div class="context-table">${rows}</div>`
        ));
      }

      // -- Prerequisites (both modes — rendered as checklist)
      if (Array.isArray(ctx.prerequisites) && ctx.prerequisites.length > 0) {
        const items = ctx.prerequisites
          .map(p => `<li><span class="prereq-check">&#10003;</span> ${_escHtml(p)}</li>`)
          .join('');
        content.appendChild(this._contextSection(
          'Prerequisites',
          `<ul class="context-prereqs">${items}</ul>`
        ));
      }

      // -- Get started / links (both modes)
      if (Array.isArray(ctx.links) && ctx.links.length > 0) {
        const anchors = ctx.links.map(l =>
          `<a class="context-link" href="${_escAttr(l.url)}" target="_blank" rel="noopener noreferrer">${_escHtml(l.label)}</a>`
        ).join('');
        content.appendChild(this._contextSection(
          'Get started',
          `<div class="context-links">${anchors}</div>`
        ));
      }

      // -- Code block (both modes)
      if (ctx.code) {
        const escaped = _escHtml(ctx.code);
        content.appendChild(this._contextSection(
          'Code',
          `<div class="context-code">
             <div class="terminal-bar">
               <span class="terminal-dot dot-red"></span>
               <span class="terminal-dot dot-yellow"></span>
               <span class="terminal-dot dot-green"></span>
             </div>
             <pre>${escaped}</pre>
           </div>`
        ));
      }

      this.contextPanel.classList.add('visible');

      // Focus close button for keyboard accessibility
      const closeBtn = this.contextPanel.querySelector('.context-close');
      if (closeBtn) closeBtn.focus();
    }

    _closeContext() {
      if (this.contextPanel) {
        this.contextPanel.classList.remove('visible');
        if (this._contextTrigger) {
          this._contextTrigger.focus();
          this._contextTrigger = null;
        }
      }
    }

    /**
     * Helper — creates a labelled context section element.
     * @param {string} label
     * @param {string} innerHTML
     * @returns {HTMLElement}
     */
    _contextSection(label, innerHTML) {
      const section = document.createElement('div');
      section.className = 'context-section';
      section.innerHTML = `<div class="context-label">${_escHtml(label)}</div>${innerHTML}`;
      return section;
    }

    /* -------------------------------------------------------
       Legacy Expand Panel — open / close / render
       ------------------------------------------------------- */

    _openExpand(title, desc, detailsJSON) {
      this.expandPanel.querySelector('.expand-title').textContent = title;
      this.expandPanel.querySelector('.expand-desc').textContent = desc;

      const detailsEl = this.expandPanel.querySelector('.expand-details');
      detailsEl.innerHTML = '';

      try {
        const sections = JSON.parse(detailsJSON);
        sections.forEach(section => {
          const h3 = document.createElement('h3');
          h3.textContent = section.heading;
          detailsEl.appendChild(h3);
          const ul = document.createElement('ul');
          section.items.forEach(item => {
            const li = document.createElement('li');
            li.textContent = item;
            ul.appendChild(li);
          });
          detailsEl.appendChild(ul);
        });
      } catch {
        // If details aren't valid JSON, show as text
        if (detailsJSON) {
          detailsEl.innerHTML = `<p style="font-size:14px;color:#6B6B8D;">${detailsJSON}</p>`;
        }
      }

      this.expandOverlay.classList.add('visible');
      this.expandPanel.classList.add('visible');
    }

    _closeExpand() {
      if (this.expandOverlay) this.expandOverlay.classList.remove('visible');
      if (this.expandPanel) this.expandPanel.classList.remove('visible');
    }
  }

  /* ========================================================
     HTML escaping utilities (module-private)
     ======================================================== */
  function _escHtml(str) {
    if (str == null) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function _escAttr(str) {
    if (str == null) return '#';
    // Allow safe URL schemes; strip javascript: etc.
    const s = String(str).trim();
    if (/^javascript:/i.test(s)) return '#';
    return s.replace(/"/g, '&quot;');
  }

  /* ========================================================
     Entrance Animations
     ======================================================== */
  function triggerEntranceAnimations() {
    const elements = document.querySelectorAll('[data-step]');
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('animate-in');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.2 });

    elements.forEach(el => {
      el.style.opacity = '0';
      observer.observe(el);
    });
  }

  /* ========================================================
     Konami Code Easter Egg
     ======================================================== */
  function initKonami() {
    const code = [38, 38, 40, 40, 37, 39, 37, 39, 66, 65]; // ↑↑↓↓←→←→BA
    let pos = 0;

    const flash = document.createElement('div');
    flash.className = 'konami-flash';
    flash.textContent = '\uD83C\uDFAE \u2191\u2191\u2193\u2193\u2190\u2192\u2190\u2192 B A START';
    document.body.appendChild(flash);

    document.addEventListener('keydown', (e) => {
      if (e.keyCode === code[pos]) {
        pos++;
        if (pos === code.length) {
          flash.classList.add('active');
          setTimeout(() => flash.classList.remove('active'), 1600);
          pos = 0;
        }
      } else {
        pos = 0;
      }
    });
  }

  /* ========================================================
     Global Navigation
     ======================================================== */
  const NAV_ISSUES = [
    { num: '001', short: '#001', title: 'Code-First Agent Delivery',      path: '../issue-001/', type: 'practical' },
    { num: '002', short: '#002', title: 'Scoped Multi-Source Search',     path: '../issue-002/', type: 'conceptual' },
    { num: '003', short: '#003', title: 'Prompt-Chained Triage',          path: '../issue-003/', type: 'practical' },
    { num: '004', short: '#004', title: 'Secure In-Boundary Processing',  path: '../issue-004/', type: 'conceptual' },
  ];

  function buildGlobalNav() {
    // Detect current issue from URL
    const match = window.location.pathname.match(/issue-(\d{3})/);
    const currentIssue = match ? match[1] : null;

    const nav = document.createElement('nav');
    nav.className = 'global-nav';
    nav.setAttribute('aria-label', 'Issue navigation');

    // Brand
    const brand = document.createElement('a');
    brand.className = 'nav-brand';
    brand.href = '../../';
    brand.textContent = 'The Cheat Code';

    const divider = document.createElement('div');
    divider.className = 'nav-divider';

    // Issue links
    const issueContainer = document.createElement('div');
    issueContainer.className = 'nav-issues';

    NAV_ISSUES.forEach(issue => {
      const a = document.createElement('a');
      a.className = 'nav-issue-link';
      a.href = issue.path;
      a.title = `Issue ${issue.short}: ${issue.title}`;
      if (issue.num === currentIssue) {
        a.classList.add('active');
        a.setAttribute('aria-current', 'page');
      }

      // Issue short label + title text
      const labelSpan = document.createElement('span');
      labelSpan.className = 'issue-label';
      labelSpan.textContent = `${issue.short} ${issue.title}`;

      // Type badge
      const badge = document.createElement('span');
      badge.className = `issue-type type-${issue.type}`;
      badge.textContent = issue.type.toUpperCase();

      a.appendChild(labelSpan);
      a.appendChild(badge);
      issueContainer.appendChild(a);
    });

    nav.appendChild(brand);
    nav.appendChild(divider);
    nav.appendChild(issueContainer);

    document.body.insertBefore(nav, document.body.firstChild);
  }

  /* ========================================================
     Theme Toggle (Light / Dark)
     ======================================================== */
  function buildThemeToggle() {
    const saved = localStorage.getItem('tcc-theme');
    const theme = saved || 'dark';

    if (theme === 'light') {
      document.documentElement.setAttribute('data-theme', 'light');
    }

    const btn = document.createElement('button');
    btn.className = 'theme-toggle';
    btn.setAttribute('aria-label', 'Toggle light/dark mode');
    btn.textContent = theme === 'light' ? '\u263E' : '\u2600';

    btn.addEventListener('click', () => {
      const isLight = document.documentElement.getAttribute('data-theme') === 'light';
      if (isLight) {
        document.documentElement.removeAttribute('data-theme');
        localStorage.setItem('tcc-theme', 'dark');
        btn.textContent = '\u2600';
      } else {
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('tcc-theme', 'light');
        btn.textContent = '\u263E';
      }
    });

    document.body.appendChild(btn);
  }

  /* ========================================================
     Init
     ======================================================== */
  function init() {
    // Global nav — always render
    buildGlobalNav();

    // Theme toggle — always render
    buildThemeToggle();

    // Only init step engine if config is defined by the page
    if (typeof window.interactiveConfig === 'undefined') return;

    const config = window.interactiveConfig;
    const engine = new StepEngine(config);

    // Make engine available for debugging
    window.stepEngine = engine;

    // Entrance animations
    triggerEntranceAnimations();

    // Konami
    initKonami();
  }

  // Wait for DOM
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

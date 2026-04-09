/**
 * The Cheat Code — Interactive Step-Through Engine
 * Vanilla JS, zero dependencies. Progressive enhancement.
 */

(function () {
  'use strict';

  /* ========================================================
     StepEngine — drives the step-through walkthrough
     ======================================================== */
  class StepEngine {
    /**
     * @param {Object} config
     * @param {string} config.container - CSS selector for diagram canvas
     * @param {Array}  config.steps - [{id, title, description, highlight: [selector], arrowHighlight: [selector]}]
     */
    constructor(config) {
      this.steps = config.steps || [];
      this.container = document.querySelector(config.container);
      this.currentStep = -1; // -1 = overview
      this.visited = new Set();

      this._buildUI();
      this._bindKeys();
      this._bindClicks();
      this._buildExpandPanel();
    }

    /* --- UI Construction --- */

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
        <button class="btn-prev" aria-label="Previous step">← Prev</button>
        <div class="step-dots">${this.steps.map((_, i) =>
          `<div class="step-dot" data-dot="${i}" title="Step ${i + 1}"></div>`
        ).join('')}</div>
        <div class="step-counter">Overview</div>
        <button class="btn-next btn-primary" aria-label="Next step">Next →</button>
        <button class="btn-reset" aria-label="Reset to overview">⟲ Reset</button>
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

    /* --- Navigation --- */

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
      this.btnNext.textContent = atStart ? 'Start →' : (atEnd ? 'Done' : 'Next →');

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

    /* --- Keyboard --- */

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
            this._closeExpand();
            this.reset();
            break;
          case 'Home':
            e.preventDefault();
            this.reset();
            break;
        }
      });
    }

    /* --- Click-to-Expand --- */

    _bindClicks() {
      this.container.addEventListener('click', (e) => {
        const stepEl = e.target.closest('[data-expand-title]');
        if (!stepEl) return;

        const title = stepEl.dataset.expandTitle || '';
        const desc = stepEl.dataset.expandDesc || '';
        const details = stepEl.dataset.expandDetails || '';

        this._openExpand(title, desc, details);
      });
    }

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
      this.expandOverlay.classList.remove('visible');
      this.expandPanel.classList.remove('visible');
    }
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
    flash.textContent = '🎮 ↑↑↓↓←→←→ B A START';
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
    { num: '001', short: '#001', title: 'Code-First Agent Delivery', path: '../issue-001/index.html' },
    { num: '002', short: '#002', title: 'Scoped Multi-Source Search', path: '../issue-002/index.html' },
    { num: '003', short: '#003', title: 'Prompt-Chained Triage', path: '../issue-003/index.html' },
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
    brand.href = '../../index.html';
    brand.innerHTML = 'The Cheat Code';

    const divider = document.createElement('div');
    divider.className = 'nav-divider';

    // Issue links
    const issueContainer = document.createElement('div');
    issueContainer.className = 'nav-issues';

    NAV_ISSUES.forEach(issue => {
      const a = document.createElement('a');
      a.className = 'nav-issue-link';
      a.href = issue.path;
      a.textContent = `${issue.short} ${issue.title}`;
      a.title = `Issue ${issue.short}: ${issue.title}`;
      if (issue.num === currentIssue) {
        a.classList.add('active');
        a.setAttribute('aria-current', 'page');
      }
      issueContainer.appendChild(a);
    });

    // Archive link
    nav.appendChild(brand);
    nav.appendChild(divider);
    nav.appendChild(issueContainer);

    document.body.insertBefore(nav, document.body.firstChild);
  }

  /* ========================================================
     Init
     ======================================================== */
  function init() {
    // Global nav — always render
    buildGlobalNav();

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

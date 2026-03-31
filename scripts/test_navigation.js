const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const BASE = 'http://localhost:8787';
  let pass = 0, fail = 0;

  function log(status, msg) {
    const icon = status === 'PASS' ? '✅' : '❌';
    if (status === 'PASS') pass++; else fail++;
    console.log(icon + ' ' + msg);
  }

  try {
    // 1. Load index.html
    await page.goto(BASE + '/index.html', { waitUntil: 'domcontentloaded' });
    const title = await page.title();
    log(title.includes('Ch(e)at Code') ? 'PASS' : 'FAIL', 'index.html loads: ' + title);

    // 2. Global nav on index
    const navBrand = await page.$('.global-nav .nav-brand');
    log(navBrand ? 'PASS' : 'FAIL', 'Global nav present on index.html');

    // 3. Collect internal links
    const links = await page.$$eval('a[href]', els => els.map(a => ({
      href: a.getAttribute('href'),
      text: a.textContent.trim().substring(0, 50)
    })));
    const internalLinks = links.filter(l =>
      l.href && !l.href.startsWith('http') && !l.href.startsWith('mailto') && !l.href.startsWith('#')
    );
    log(internalLinks.length > 0 ? 'PASS' : 'FAIL', 'Found ' + internalLinks.length + ' internal links on index.html');

    console.log('\n📋 Internal links:');
    internalLinks.forEach(l => console.log('   → ' + l.href));

    // 4. Test each internal link resolves
    console.log('\n🔗 Testing each link...');
    const tested = new Set();
    for (const link of internalLinks) {
      if (tested.has(link.href)) continue;
      tested.add(link.href);
      const url = new URL(link.href, BASE + '/index.html').href;
      try {
        const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 10000 });
        const pageTitle = await page.title();
        log(resp.ok() ? 'PASS' : 'FAIL', link.href + ' → ' + resp.status() + ' (' + pageTitle.substring(0, 45) + ')');
      } catch (e) {
        log('FAIL', link.href + ' → NETWORK ERROR: ' + e.message.substring(0, 60));
      }
    }

    // 5. Interactive pages: global nav + step bar
    console.log('\n🧭 Checking interactive page features...');
    for (const issue of ['001', '002']) {
      const iUrl = BASE + '/interactive/issue-' + issue + '/';
      await page.goto(iUrl, { waitUntil: 'domcontentloaded' });

      await page.waitForSelector('.global-nav', { timeout: 5000 }).catch(() => null);
      const hasNav = await page.$('.global-nav');
      log(hasNav ? 'PASS' : 'FAIL', 'issue-' + issue + ' has global nav');

      await page.waitForSelector('.step-bar', { timeout: 5000 }).catch(() => null);
      const hasStepBar = await page.$('.step-bar');
      log(hasStepBar ? 'PASS' : 'FAIL', 'issue-' + issue + ' has step-through bar');

      const archiveHref = await page.$eval('.global-nav .nav-archive', el => el.getAttribute('href')).catch(() => null);
      log(archiveHref ? 'PASS' : 'FAIL', 'issue-' + issue + ' nav archive link: ' + archiveHref);
    }

    // 6. Cross-navigation between interactive pages
    console.log('\n↔️  Cross-navigation from issue-001...');
    await page.goto(BASE + '/interactive/issue-001/', { waitUntil: 'domcontentloaded' });
    await page.waitForSelector('.global-nav', { timeout: 5000 });

    const navLinks = await page.$$eval('.global-nav .nav-issue-link', els => els.map(a => ({
      href: a.getAttribute('href'),
      text: a.textContent.trim()
    })));

    for (const nl of navLinks) {
      const url = new URL(nl.href, BASE + '/interactive/issue-001/').href;
      try {
        const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 10000 });
        log(resp.ok() ? 'PASS' : 'FAIL', 'Nav: ' + nl.text + ' → ' + resp.status());
      } catch (e) {
        log('FAIL', 'Nav: ' + nl.text + ' → ERROR');
      }
    }

    // 7. Back links from interactive → newsletter
    console.log('\n📰 Back-links to newsletters...');
    for (const issue of ['001', '002']) {
      await page.goto(BASE + '/interactive/issue-' + issue + '/', { waitUntil: 'domcontentloaded' });
      const backHref = await page.$eval('.back-link', el => el.getAttribute('href')).catch(() => null);
      if (backHref) {
        const url = new URL(backHref, BASE + '/interactive/issue-' + issue + '/').href;
        try {
          const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 10000 });
          log(resp.ok() ? 'PASS' : 'FAIL', 'Back link #' + issue + ' → ' + backHref + ' (' + resp.status() + ')');
        } catch (e) {
          log('FAIL', 'Back link #' + issue + ' → ' + backHref + ' ERROR');
        }
      } else {
        log('FAIL', 'No back-link on issue-' + issue);
      }
    }

    // 8. Newsletter CTA links → interactive
    console.log('\n🔬 Newsletter CTA → interactive...');
    for (const issue of ['001', '002']) {
      await page.goto(BASE + '/issues/the_cheat_code_issue_' + issue + '.html', { waitUntil: 'domcontentloaded' });
      const ctaHref = await page.$eval('a[href*="interactive"]', el => el.getAttribute('href')).catch(() => null);
      if (ctaHref) {
        const url = new URL(ctaHref, BASE + '/issues/the_cheat_code_issue_' + issue + '.html').href;
        try {
          const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 10000 });
          log(resp.ok() ? 'PASS' : 'FAIL', 'Newsletter #' + issue + ' CTA → ' + ctaHref + ' (' + resp.status() + ')');
        } catch (e) {
          log('FAIL', 'Newsletter #' + issue + ' CTA → ERROR');
        }
      } else {
        log('FAIL', 'No interactive CTA in newsletter #' + issue);
      }
    }

  } catch (err) {
    console.error('\n💥 Test error:', err.message);
  }

  console.log('\n' + '═'.repeat(50));
  console.log('Results: ' + pass + ' passed, ' + fail + ' failed, ' + (pass + fail) + ' total');
  console.log('═'.repeat(50));

  await browser.close();
  process.exit(fail > 0 ? 1 : 0);
})();

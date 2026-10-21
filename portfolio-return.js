(() => {
  'use strict';
  const KEY = 'portfolio.reading.return.v1';
  const query = new URLSearchParams(location.search);
  const navigation = performance.getEntriesByType('navigation')[0];
  let saved = null;
  try {
    const value = JSON.parse(sessionStorage.getItem(KEY));
    if (value?.version === 1 && typeof value.workId === 'string' && Number.isFinite(value.scrollY)) saved = value;
  } catch {}
  const resuming = query.get('resume') === '1' || navigation?.type === 'back_forward';
  const initialWorkId = (resuming && saved?.workId) || query.get('work') || null;
  let getWorkId = () => initialWorkId;
  let focusKey = 'm-open';
  let restoring = false;
  function capture() {
    if (restoring) return;
    const state = {
      version: 1, workId: getWorkId(), scrollY: window.scrollY,
      openKinds: [...document.querySelectorAll('.kind.open')].map(el => el.dataset.kindName),
      focusKey
    };
    try { sessionStorage.setItem(KEY, JSON.stringify(state)); } catch {}
  }
  // 같은 사이트 안의 작품 페이지(작품 모음 자신은 제외)로 갈 때만 돌아올 위치를 남긴다
  function isWorkPage(url) {
    const home = new URL('./', location.href).pathname;
    return url.origin === location.origin && url.pathname !== home && url.pathname !== home + 'index.html';
  }
  function destination(value) {
    const url = new URL(value, location.href);
    if (isWorkPage(url)) url.searchParams.set('from', 'portfolio');
    return url.href;
  }
  function restoreState(state) {
    if (!state) return;
    restoring = true;
    document.querySelectorAll('.kind').forEach(el => {
      const open = Array.isArray(state.openKinds) && state.openKinds.includes(el.dataset.kindName);
      el.classList.toggle('open', open); el.setAttribute('aria-expanded', String(open));
    });
    let cancelled = false;
    const cancel = () => { cancelled = true; };
    addEventListener('wheel', cancel, { once: true, passive: true });
    addEventListener('pointerdown', cancel, { once: true, passive: true });
    const ready = document.fonts?.ready || Promise.resolve();
    Promise.race([ready, new Promise(resolve => setTimeout(resolve, 500))]).then(() => {
      requestAnimationFrame(() => requestAnimationFrame(() => {
        if (!cancelled) {
          window.scrollTo({ top: Math.max(0, state.scrollY), behavior: 'instant' });
          const focus = [...document.querySelectorAll('[data-return-key]')].find(el => el.dataset.returnKey === state.focusKey);
          focus?.focus({ preventScroll: true });
        }
        removeEventListener('wheel', cancel); removeEventListener('pointerdown', cancel);
        restoring = false; document.documentElement.dataset.returnRestored = 'true';
      }));
    });
  }
  window.PortfolioReturn = {
    initialWorkId, capture, destination,
    init(options) {
      getWorkId = options.getWorkId;
      document.addEventListener('click', event => {
        const anchor = event.target.closest('a');
        if (!anchor) return;
        const url = new URL(anchor.href, location.href);
        if (!isWorkPage(url)) return;
        focusKey = anchor.dataset.returnKey || 'm-open'; capture(); anchor.href = destination(anchor.href);
      }, { capture: true });
      addEventListener('pagehide', capture);
      addEventListener('pageshow', event => {
        if (event.persisted) {
          try { restoreState(JSON.parse(sessionStorage.getItem(KEY))); } catch {}
        }
      });
      if (resuming) restoreState(saved);
    }
  };
})();

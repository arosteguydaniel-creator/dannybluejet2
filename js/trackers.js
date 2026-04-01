/**
 * trackers.js — Centralised analytics & pixel loader
 *
 * Strategy: load all third-party scripts without blocking render.
 * Initialisation is deferred with requestIdleCallback (+ setTimeout fallback)
 * so it starts only when the browser is idle, or on the first user interaction,
 * whichever comes first.
 *
 * IDs — edit only this section when IDs change:
 */
var TRACKER_CONFIG = {
  metaPixelId:  '3627643840689292',
  tiktokPixelId: 'D6KT7G3C77U3SAC89O0G',
  umamiScriptUrl: 'https://cloud.umami.is/script.js',
  umamiWebsiteId: '16ceb526-7cf0-4b63-b670-a13e9eb20822'
};

/* ─── helpers ─────────────────────────────────────────────────────────────── */

function loadScript(src, attrs) {
  return new Promise(function (resolve, reject) {
    try {
      var s = document.createElement('script');
      s.src = src;
      s.async = true;
      if (attrs) {
        Object.keys(attrs).forEach(function (k) { s.setAttribute(k, attrs[k]); });
      }
      s.onload  = resolve;
      s.onerror = reject;
      document.head.appendChild(s);
    } catch (e) {
      reject(e);
    }
  });
}

/* ─── Meta Pixel ──────────────────────────────────────────────────────────── */

function initMetaPixel() {
  try {
    /* Minimal Meta Pixel bootstrap (avoids loading fbevents.js before idle) */
    if (!window.fbq) {
      var n = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments); };
      if (!window._fbq) window._fbq = n;
      n.push    = n;
      n.loaded  = true;
      n.version = '2.0';
      n.queue   = [];
      window.fbq = n;
    }

    fbq('init', TRACKER_CONFIG.metaPixelId);
    fbq('track', 'PageView');

    loadScript('https://connect.facebook.net/en_US/fbevents.js').catch(function (e) {
      console.warn('[trackers] Meta Pixel script failed to load:', e);
    });
  } catch (e) {
    console.warn('[trackers] Meta Pixel init error:', e);
  }
}

/* ─── TikTok Pixel ────────────────────────────────────────────────────────── */

function initTikTokPixel() {
  try {
    /* Minimal TikTok Pixel bootstrap */
    if (!window.ttq) {
      var ttq = { _i: [], load: function (e) {
        var t = document.createElement('script');
        t.type = 'text/javascript';
        t.async = true;
        t.src   = 'https://analytics.tiktok.com/i18n/pixel/events.js?sdkid=' + e + '&lib=ttq';
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(t, s);
      }, page: function () {
        try { window.ttq && window.ttq.instance && window.ttq.instance(TRACKER_CONFIG.tiktokPixelId).page(); } catch (e) { /* noop */ }
      } };
      window.ttq = ttq;
    }

    window.ttq.load(TRACKER_CONFIG.tiktokPixelId);
    window.ttq.page();
    window.ttq.track('PageView');
  } catch (e) {
    console.warn('[trackers] TikTok Pixel init error:', e);
  }
}

function trackTikTokEvent(eventName, params) {
  try {
    if (window.ttq && typeof window.ttq.track === 'function') {
      window.ttq.track(eventName, params || {});
    } else {
      console.warn('[trackers] TikTok ttq not ready for event:', eventName);
    }
  } catch (e) {
    console.warn('[trackers] TikTok track error:', e);
  }
}

/* ─── Umami ───────────────────────────────────────────────────────────────── */

function initUmami() {
  loadScript(TRACKER_CONFIG.umamiScriptUrl, {
    'data-website-id': TRACKER_CONFIG.umamiWebsiteId,
    'defer': ''
  }).catch(function (e) {
    console.warn('[trackers] Umami script failed to load:', e);
  });
}

/* ─── Orchestrator ────────────────────────────────────────────────────────── */

function initAllTrackers() {
  initMetaPixel();
  initTikTokPixel();
  initUmami();
}

/* Start on idle, falling back to a 3-second timeout, or on first user input */
var trackersFired = false;
function fireOnce() {
  if (trackersFired) return;
  trackersFired = true;
  removeEarlyListeners();
  initAllTrackers();
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', fireOnce);
} else {
  fireOnce();
}

var earlyEvents = ['mousedown', 'keydown', 'touchstart', 'scroll', 'click'];
function removeEarlyListeners() {
  earlyEvents.forEach(function (ev) {
    document.removeEventListener(ev, fireOnce, { passive: true, capture: true });
  });
}

/* Register early-interaction listeners */
earlyEvents.forEach(function (ev) {
  document.addEventListener(ev, fireOnce, { passive: true, capture: true });
});

/* Also fire on idle / timeout (max 3 s after load) */
if (typeof requestIdleCallback === 'function') {
  requestIdleCallback(fireOnce, { timeout: 3000 });
} else {
  setTimeout(fireOnce, 3000);
}

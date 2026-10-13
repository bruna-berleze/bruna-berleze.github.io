// Fade sections in as they scroll into view.
(function () {
  var items = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window)) {
    items.forEach(function (el) { el.classList.add('in'); });
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { threshold: 0.12 });
  items.forEach(function (el) { io.observe(el); });
})();

// Language switch: remember the visitor's choice and keep the current section.
(function () {
  var KEY = 'bb-lang';
  var pageLang = document.documentElement.lang.indexOf('pt') === 0 ? 'pt' : 'en';
  function save(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }
  function load() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }

  document.querySelectorAll('.lang a').forEach(function (a) {
    a.addEventListener('click', function () {
      save(a.getAttribute('data-lang'));
      if (location.hash) a.href = a.getAttribute('href') + location.hash;
    });
  });

  // Visitor chose a language before and arrived from outside the site: send them to it.
  var saved = load();
  var fromSite = document.referrer && document.referrer.indexOf(location.origin) === 0;
  if (saved && saved !== pageLang && !fromSite) {
    var target = document.querySelector('.lang a[data-lang="' + saved + '"]');
    if (target) location.replace(target.getAttribute('href') + location.hash);
  }
})();

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

// Project filter by tool.
(function () {
  var chips = document.querySelectorAll('.chip[data-filter]');
  if (!chips.length) return;
  var cards = document.querySelectorAll('.card[data-tools]');
  function apply(f) {
    chips.forEach(function (c) { c.setAttribute('aria-pressed', String(c.getAttribute('data-filter') === f)); });
    cards.forEach(function (card) {
      var show = f === 'all' || card.getAttribute('data-tools').split(' ').indexOf(f) >= 0;
      card.hidden = !show;
      if (show) { card.classList.remove('pop'); void card.offsetWidth; card.classList.add('pop'); }
    });
  }
  chips.forEach(function (c) {
    c.addEventListener('click', function () {
      var f = c.getAttribute('data-filter');
      apply(f);
      history.replaceState(null, '', f === 'all' ? location.pathname : '#' + f);
    });
  });
  var initial = location.hash.slice(1);
  if (['bi', 'apps', 'flow'].indexOf(initial) >= 0) apply(initial);
})();

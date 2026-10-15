"""Builds the static site in English (root) and Portuguese (/pt/).

Edit text in T, PROJECTS or SERVICES, then run: python3 build.py
"""
from pathlib import Path

ROOT = Path(__file__).parent
SITE_URL = "https://bruna-berleze.github.io"
PAGES = ["index.html", "projects.html"]

T = {
    "en": {
        "html_lang": "en", "lang_label": "Language",
        "nav_services": "Services", "nav_projects": "Projects",
        "site_title": "Bruna Berleze · Power Platform Developer",
        "home_desc": "Power BI, Power Apps and Power Automate solutions from an Electrical Engineer with real manufacturing experience.",
        "h1": ("I ran the", "operations", "before I built the", "solutions"),
        "pill": ("I'm a", "Power Platform developer", "with real factory experience"),
        "story": ["I spent years on the shop floor of the automotive industry,",
                  "in maintenance, stamping and an emissions lab.",
                  "Now I turn that experience into Power BI dashboards,",
                  "Power Apps and Power Automate flows",
                  "that people actually use."],
        "stats": [("3", "tools: Power BI, Power Apps and Power Automate"), ("5", "portfolio projects"),
                  ("2", "postgraduate specializations"), ("C1", "English, working with global clients")],
        "what": "What I do",
        "sel": ("Selected", "projects"), "all_projects": "All projects ↗",
        "shot": "Screenshot coming soon", "soon": "Case study coming soon",
        "footer": "Power Platform &amp; Process Improvement",
        "proj_title": "Projects",
        "proj_desc": "Power BI dashboards, Power Apps and Power Automate projects built from real operational problems.",
        "proj_h1": ("All", "projects"),
        "proj_sub": "Dashboards, apps and flows built from real operational problems",
        "filter_label": "Filter by tool", "all": "All",
        "nf_title": "Page not found", "nf_h1": ("This page", "doesn't exist"), "nf_btn": "Back to home ↗",
    },
    "pt": {
        "html_lang": "pt-BR", "lang_label": "Idioma",
        "nav_services": "Serviços", "nav_projects": "Projetos",
        "site_title": "Bruna Berleze · Desenvolvedora Power Platform",
        "home_desc": "Soluções em Power BI, Power Apps e Power Automate de uma engenheira eletricista com experiência real na indústria.",
        "h1": ("Eu vivi a", "operação", "antes de criar as", "soluções"),
        "pill": ("Sou", "desenvolvedora Power Platform", "com experiência real de fábrica"),
        "story": ["Passei anos no chão de fábrica da indústria automotiva,",
                  "na manutenção, na estamparia e num laboratório de emissões.",
                  "Hoje transformo essa experiência em dashboards no Power BI,",
                  "apps no Power Apps e fluxos no Power Automate",
                  "que as pessoas realmente usam."],
        "stats": [("3", "ferramentas: Power BI, Power Apps e Power Automate"), ("5", "projetos no portfólio"),
                  ("2", "pós-graduações"), ("C1", "inglês, atendendo clientes do mundo todo")],
        "what": "O que eu faço",
        "sel": ("Projetos em", "destaque"), "all_projects": "Todos os projetos ↗",
        "shot": "Imagem em breve", "soon": "Estudo de caso em breve",
        "footer": "Power Platform &amp; Melhoria de Processos",
        "proj_title": "Projetos",
        "proj_desc": "Projetos em Power BI, Power Apps e Power Automate criados a partir de problemas reais da operação.",
        "proj_h1": ("Todos os", "projetos"),
        "proj_sub": "Dashboards, apps e fluxos criados a partir de problemas reais da operação",
        "filter_label": "Filtrar por ferramenta", "all": "Todos",
        "nf_title": "Página não encontrada", "nf_h1": ("Esta página", "não existe"), "nf_btn": "Voltar ao início ↗",
    },
}

TOOLS = {"bi": "Power BI", "apps": "Power Apps", "flow": "Power Automate"}

# thumb: gradient class + text tone. featured: shown on the home page.
PROJECTS = [
    {"id": "oee", "tools": ["bi"], "thumb": "g1 t-dark", "featured": True,
     "area": {"en": "Manufacturing", "pt": "Manufatura"},
     "title": {"en": "OEE Production Dashboard", "pt": "Dashboard de OEE da Produção"},
     "desc": {"en": "Availability, performance and quality in one view, so production teams see where capacity is lost.",
              "pt": "Disponibilidade, desempenho e qualidade numa só visão, para a produção ver onde perde capacidade."}},
    {"id": "lup", "tools": ["apps"], "thumb": "g2 t-light", "featured": True,
     "area": {"en": "Training", "pt": "Treinamento"},
     "title": {"en": "LUP One-Point Lesson App", "pt": "App de LUP (Lição de Um Ponto)"},
     "desc": {"en": "A simple app to create, find and share one-point lessons on the shop floor instead of printed sheets.",
              "pt": "Um app simples para criar, encontrar e compartilhar lições de um ponto no chão de fábrica, sem folhas impressas."}},
    {"id": "dca", "tools": ["apps"], "thumb": "g3 t-light", "featured": False,
     "area": {"en": "Quality", "pt": "Qualidade"},
     "title": {"en": "DCA Digital Form", "pt": "Formulário Digital DCA"},
     "desc": {"en": "A paper-based process turned into a digital form, with records that can be searched and analysed.",
              "pt": "Um processo em papel transformado em formulário digital, com registros fáceis de buscar e analisar."}},
    {"id": "shift", "tools": ["apps", "flow"], "thumb": "g4 t-dark", "featured": False,
     "area": {"en": "Operations", "pt": "Operações"},
     "title": {"en": "Shift Handover Digitalization", "pt": "Digitalização da Passagem de Turno"},
     "desc": {"en": "Shift handover information captured digitally, so the next shift starts with the full picture.",
              "pt": "Informações da passagem de turno registradas digitalmente, para o próximo turno começar com o quadro completo."}},
    {"id": "retail", "tools": ["bi"], "thumb": "g5 t-dark", "featured": True,
     "area": {"en": "Retail", "pt": "Varejo"},
     "title": {"en": "Retail Sales Performance", "pt": "Desempenho de Vendas no Varejo"},
     "desc": {"en": "Sales, margin and store performance with filters and drill-down for fast business decisions.",
              "pt": "Vendas, margem e desempenho por loja, com filtros e detalhamento para decisões rápidas."}},
]

SVG = {
    "bi": '<svg aria-hidden="true" width="150" height="110" viewBox="0 0 150 110" fill="none"><rect x="6" y="6" width="138" height="92" rx="8" stroke="#8B6CFF" stroke-width="2"/><rect x="20" y="60" width="14" height="26" rx="3" fill="#8B6CFF"/><rect x="42" y="44" width="14" height="42" rx="3" fill="#8B6CFF" opacity=".7"/><rect x="64" y="52" width="14" height="34" rx="3" fill="#8B6CFF" opacity=".5"/><path d="M92 72 L104 54 L116 62 L132 30" stroke="#E6C9E8" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/><circle cx="132" cy="30" r="4" fill="#E6C9E8"/><rect x="20" y="18" width="40" height="8" rx="3" fill="#fff" opacity=".5"/></svg>',
    "apps": '<svg aria-hidden="true" width="150" height="110" viewBox="0 0 150 110" fill="none"><rect x="50" y="4" width="52" height="100" rx="10" stroke="#15122B" stroke-width="2"/><rect x="60" y="20" width="32" height="8" rx="3" fill="#6A4CF0"/><rect x="60" y="36" width="32" height="6" rx="3" fill="#B9B3DA"/><rect x="60" y="48" width="32" height="6" rx="3" fill="#B9B3DA"/><rect x="60" y="72" width="32" height="12" rx="6" fill="#6A4CF0"/><path d="M18 40 h22 M18 54 h16 M112 34 h20 M112 48 h14" stroke="#B9B3DA" stroke-width="2" stroke-linecap="round"/></svg>',
    "flow": '<svg aria-hidden="true" width="150" height="110" viewBox="0 0 150 110" fill="none"><rect x="8" y="40" width="34" height="30" rx="8" stroke="#15122B" stroke-width="2"/><rect x="58" y="12" width="34" height="30" rx="8" fill="#6A4CF0"/><rect x="58" y="68" width="34" height="30" rx="8" stroke="#15122B" stroke-width="2"/><rect x="108" y="40" width="34" height="30" rx="8" stroke="#15122B" stroke-width="2"/><path d="M42 50 L58 30 M42 60 L58 80 M92 27 L108 50 M92 83 L108 60" stroke="#6A4CF0" stroke-width="2" stroke-linecap="round"/></svg>',
    "lean": '<svg aria-hidden="true" width="150" height="110" viewBox="0 0 150 110" fill="none"><circle cx="24" cy="55" r="14" stroke="#fff" stroke-width="2"/><circle cx="75" cy="55" r="14" stroke="#fff" stroke-width="2"/><circle cx="126" cy="55" r="14" fill="#fff"/><path d="M38 55 h23 M89 55 h23" stroke="#fff" stroke-width="2" stroke-linecap="round"/><path d="M75 69 C75 96 126 96 126 69" stroke="#E6C9E8" stroke-width="2" stroke-dasharray="4 4"/><path d="M120 55 l4 4 l8 -8" stroke="#6A4CF0" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
}

SERVICES = [
    ("dark", "bi", {"en": ("Data &amp; KPI dashboards", "Power BI reports with clean data models and DAX, built around the decisions your team makes."),
                    "pt": ("Dashboards e indicadores", "Relatórios em Power BI com modelo de dados limpo e DAX, pensados nas decisões da sua equipe.")}),
    ("gray", "apps", {"en": ("Power Apps for the shop floor", "Simple apps that replace paper forms and scattered spreadsheets."),
                      "pt": ("Power Apps para o chão de fábrica", "Apps simples que substituem formulários em papel e planilhas espalhadas.")}),
    ("lilac", "flow", {"en": ("Power Automate workflows", "Approvals, alerts and data moving on their own, without copy and paste."),
                       "pt": ("Fluxos no Power Automate", "Aprovações, alertas e dados andando sozinhos, sem copiar e colar.")}),
    ("violet", "lean", {"en": ("Process mapping &amp; Lean", "I map how work really flows first, so the tool fixes the right problem."),
                        "pt": ("Mapeamento de processos &amp; Lean", "Primeiro eu mapeio como o trabalho acontece, para a ferramenta resolver o problema certo.")}),
]


def url_for(lang, file):
    base = "/" if lang == "en" else "/pt/"
    return base if file == "index.html" else base + file


def layout(lang, file, title, description, body):
    t = T[lang]
    cur = 'aria-current="page"'
    full_title = t["site_title"] if file == "index.html" else f"{title} · Bruna Berleze"
    en_url, pt_url = url_for("en", file), url_for("pt", file)
    alt = "" if file == "404.html" else f"""<link rel="alternate" hreflang="en" href="{SITE_URL}{en_url}">
<link rel="alternate" hreflang="pt-BR" href="{SITE_URL}{pt_url}">
<link rel="alternate" hreflang="x-default" href="{SITE_URL}{en_url}">
<link rel="canonical" href="{SITE_URL}{url_for(lang, file)}">"""
    services_href = "#services" if file == "index.html" else url_for(lang, "index.html") + "#services"
    return f"""<!doctype html>
<html lang="{t['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:image" content="{SITE_URL}/assets/favicon.png">
{alt}
<meta name="theme-color" content="#D9D5F2">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
<link rel="icon" type="image/png" sizes="64x64" href="/assets/favicon-64.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
</head>
<body>
<div class="page">
<div class="sheet">
<header class="top">
<a class="brand" href="{url_for(lang, 'index.html')}"><span class="mark">B<span>.</span></span>Bruna Berleze</a>
<nav class="nav" aria-label="Main">
<a href="{services_href}">{t['nav_services']}</a>
<a href="{url_for(lang, 'projects.html')}" {cur if file == 'projects.html' else ''}>{t['nav_projects']}</a>
<div class="lang" role="group" aria-label="{t['lang_label']}">
<a href="{en_url}" hreflang="en" lang="en" data-lang="en" {cur if lang == 'en' else ''}>EN</a>
<a href="{pt_url}" hreflang="pt-BR" lang="pt-BR" data-lang="pt" {cur if lang == 'pt' else ''}>PT</a>
</div>
</nav>
</header>
<main>
{body}
</main>
<footer class="foot"><span>© 2026 Bruna Berleze</span><span>{t['footer']}</span></footer>
</div>
</div>
<script src="/assets/main.js"></script>
</body>
</html>
"""


def card(lang, p, cls="rise"):
    t = T[lang]
    tags = "".join(f'<span class="tag {k}">{TOOLS[k]}</span>' for k in p["tools"])
    return f"""<a class="card {cls}" href="{url_for(lang, 'projects.html')}#{p['id']}" data-tools="{' '.join(p['tools'])}" id="{p['id']}">
<div class="thumb {p['thumb']}">{t['shot']}</div>
<div class="card-body">
<div class="tags">{tags}<span class="tag area">{p['area'][lang]}</span></div>
<h3>{p['title'][lang]}</h3>
<p>{p['desc'][lang]}</p>
<div class="card-foot"><span>{t['soon']}</span><span class="go" aria-hidden="true">↗</span></div>
</div>
</a>"""


def home(lang):
    t = T[lang]
    a, b, c, d = t["h1"]
    pa, pb, pc = t["pill"]
    story = "\n".join(f'<span class="lit">{s}</span>' for s in t["story"])
    stats = "".join(f'<div class="stat"><div class="n">{n}</div><div class="l">{l}</div></div>' for n, l in t["stats"])
    run = "".join(f'<span>{t["what"]}</span><span class="arrow">→</span>' for _ in range(3))
    services = "".join(
        f"""<article class="svc {cls} rise"><span class="num">( 0{i + 1} )</span>{SVG[icon]}<h3>{txt[lang][0]}</h3><p>{txt[lang][1]}</p></article>"""
        for i, (cls, icon, txt) in enumerate(SERVICES))
    featured = "".join(card(lang, p) for p in PROJECTS if p["featured"])
    sa, sb = t["sel"]
    body = f"""<section class="hero">
<h1 class="display">{a} <span class="accent">{b}</span><br>{c} <span class="accent">{d}</span>
<span class="aside"><span class="paren" aria-hidden="true">(</span>
<span class="avatars" aria-hidden="true"><span class="av-bi">BI</span><span class="av-apps">Ap</span><span class="av-flow">Au</span></span>
<span class="note">{pa} <b>{pb}</b> {pc}</span><span class="paren" aria-hidden="true">)</span></span>
</h1>
</section>

<section class="story-wrap">
<div class="story">
<p>{story}</p>
<div class="stats">{stats}</div>
</div>
</section>

<section id="services" class="marquee-wrap">
<h2 class="sr-only">{t['what']}</h2>
<div class="marquee" aria-hidden="true"><div>{run}</div><div>{run}</div></div>
</section>
<div class="services">{services}</div>

<section class="section">
<div class="section-head">
<h2>{sa} <span class="accent">{sb}</span></h2>
<a href="{url_for(lang, 'projects.html')}">{t['all_projects']}</a>
</div>
<div class="cards">{featured}</div>
</section>"""
    return layout(lang, "index.html", t["nav_projects"], t["home_desc"], body)


def projects(lang):
    t = T[lang]
    a, b = t["proj_h1"]

    def count(k):
        return len(PROJECTS) if k == "all" else sum(k in p["tools"] for p in PROJECTS)

    chips = "".join(
        f'<button type="button" class="chip" data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">'
        f'<span class="dot {k}" aria-hidden="true"></span>{t["all"] if k == "all" else TOOLS[k]}'
        f'<span class="count">{count(k)}</span></button>'
        for k in ["all", "bi", "apps", "flow"])
    cards = "".join(card(lang, p, "pop") for p in PROJECTS)
    body = f"""<section class="hero">
<h1 class="display">{a} <span class="accent">{b}</span>
<span class="aside"><span class="paren" aria-hidden="true">(</span><span class="note">{t['proj_sub']}</span><span class="paren" aria-hidden="true">)</span></span>
</h1>
</section>
<div class="filters" role="group" aria-label="{t['filter_label']}">{chips}</div>
<section class="projects-grid" aria-live="polite">
<div class="cards">{cards}</div>
</section>"""
    return layout(lang, "projects.html", t["proj_title"], t["proj_desc"], body)


def not_found(lang):
    t = T[lang]
    a, b = t["nf_h1"]
    body = f"""<section class="hero" style="padding-bottom:120px">
<h1 class="display">{a} <span class="accent">{b}</span></h1>
<p style="margin-top:32px"><a href="{url_for(lang, 'index.html')}" style="font-weight:600;text-decoration:none">{t['nf_btn']}</a></p>
</section>"""
    return layout(lang, "404.html", t["nf_title"], t["nf_title"], body)


for lang in ("en", "pt"):
    out = ROOT if lang == "en" else ROOT / "pt"
    out.mkdir(exist_ok=True)
    (out / "index.html").write_text(home(lang), encoding="utf-8")
    (out / "projects.html").write_text(projects(lang), encoding="utf-8")
(ROOT / "404.html").write_text(not_found("en"), encoding="utf-8")
print("built en + pt")

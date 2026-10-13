"""Builds the static site in English (root) and Portuguese (/pt/) from one layout.

Edit text in the T dictionary or PROJECTS list, then run: python3 build.py
"""
from pathlib import Path

ROOT = Path(__file__).parent
SITE_URL = "https://bruna-berleze.github.io"
# Fill in your profile links here, then run the script again.
FIVERR_URL = "#contact"
UPWORK_URL = "#contact"

PAGES = ["index.html", "projects.html", "demos.html", "about.html"]

T = {
    "en": {
        "html_lang": "en",
        "nav": {"index.html": "Home", "projects.html": "Projects", "demos.html": "Live Demos", "about.html": "About & Contact"},
        "lang_label": "Language",
        "site_title": "Bruna Berleze · Power Platform Developer",
        "footer": "© 2026 Bruna Berleze · Power Platform &amp; Process Improvement",
        "cta_title": "Let's work together",
        "cta_text": "Message me on the platform you found me on.",
        "cta_fiverr": "Hire me on Fiverr",
        "cta_upwork": "Hire me on Upwork",
        "pill": "Power Platform Developer · Electrical Engineer",
        "h1": "I ran the operations before I built the solutions.",
        "lead": "Power BI dashboards, Power Apps and Power Automate workflows that digitalize operations and improve decisions in maintenance, production and business.",
        "btn_projects": "View projects",
        "btn_demos": "See live demos",
        "deliver": "HOW I DELIVER",
        "step_apps": ("Capture · Power Apps", "Replace paper forms and spreadsheets with simple apps."),
        "step_flow": ("Automate · Power Automate", "Approvals, alerts and data flowing on their own."),
        "step_bi": ("Decide · Power BI", "KPIs and dashboards people actually use."),
        "work_eyebrow": "Selected work",
        "work_h2": "Real problems, digital solutions",
        "work_p": "Solutions built from hands-on experience in automotive manufacturing: maintenance, production, quality and operations.",
        "preview_soon": "Preview coming soon",
        "read_more": "Read more →",
        "see_all": "See all projects",
        "home_desc": "Power BI, Power Apps and Power Automate solutions from an Electrical Engineer with real manufacturing experience.",
        "proj_title": "Projects",
        "proj_eyebrow": "Portfolio projects",
        "proj_p": "Each project shows the problem, what I built and what changed. Data shown is fictional or anonymized.",
        "proj_desc": "Power BI dashboards, Power Apps and Power Automate projects with problem, solution and result.",
        "shot_soon": "Screenshot coming soon",
        "problem": "Problem", "solution": "Solution", "result": "Result",
        "case_soon": "Case study coming soon",
        "demos_title": "Live Demos",
        "demos_eyebrow": "Live demos",
        "demos_h1": "See it working",
        "demos_p": "Interactive dashboards you can explore, and short videos of apps and flows in action. All data is fictional or anonymized.",
        "demos_desc": "Interactive Power BI dashboards and video demos of Power Apps and Power Automate solutions.",
        "bi_tag": "Power BI · interactive",
        "bi_hint": "Filter, click and drill down",
        "bi_soon": "Interactive dashboard coming soon",
        "bi_sub": "Power BI report embedded here",
        "apps_tag": "Power Apps · video",
        "flow_tag": "Power Automate · video",
        "lup_demo": "LUP App walkthrough",
        "flow_demo": "Approval flow demo",
        "video_soon": "Video coming soon",
        "about_title": "About & Contact",
        "about_eyebrow": "About &amp; contact",
        "about_h1": "Hi, I'm Bruna",
        "about_desc": "Bruna Berleze, Electrical Engineer and Power Platform developer with manufacturing experience at Renault Group.",
        "about_p": "Electrical Engineer (UTFPR) with hands-on experience in industrial maintenance and process improvement at Renault Group's stamping department and HORSE Powertrain's emissions lab. I map the process first, then pick the right tool: an app, a flow, a dashboard, or all three.",
        "services": "SERVICES",
        "svc": ["Data &amp; KPI Dashboards", "Workflow Digitalization", "Process Mapping &amp; Improvement"],
        "tools": "TOOLS",
        "credentials": "CREDENTIALS",
        "creds": ["BSc Electrical Engineering · UTFPR", "Postgraduate · Maintenance Engineering",
                  "Postgraduate · Business Intelligence, Big Data &amp; AI",
                  "Google Project Management Professional Certificate", "English · C1 Advanced"],
        "nf_title": "Page not found", "nf_h1": "This page doesn't exist.", "nf_btn": "Back to home",
    },
    "pt": {
        "html_lang": "pt-BR",
        "nav": {"index.html": "Início", "projects.html": "Projetos", "demos.html": "Demonstrações", "about.html": "Sobre & Contato"},
        "lang_label": "Idioma",
        "site_title": "Bruna Berleze · Desenvolvedora Power Platform",
        "footer": "© 2026 Bruna Berleze · Power Platform &amp; Melhoria de Processos",
        "cta_title": "Vamos trabalhar juntos",
        "cta_text": "Fale comigo pela plataforma onde você me encontrou.",
        "cta_fiverr": "Contrate pelo Fiverr",
        "cta_upwork": "Contrate pela Upwork",
        "pill": "Desenvolvedora Power Platform · Engenheira Eletricista",
        "h1": "Eu vivi a operação antes de criar as soluções.",
        "lead": "Dashboards em Power BI, apps em Power Apps e fluxos em Power Automate que digitalizam operações e melhoram decisões na manutenção, na produção e no negócio.",
        "btn_projects": "Ver projetos",
        "btn_demos": "Ver demonstrações",
        "deliver": "COMO EU ENTREGO",
        "step_apps": ("Capturar · Power Apps", "Troque formulários em papel e planilhas por apps simples."),
        "step_flow": ("Automatizar · Power Automate", "Aprovações, alertas e dados fluindo sozinhos."),
        "step_bi": ("Decidir · Power BI", "Indicadores e dashboards que as pessoas realmente usam."),
        "work_eyebrow": "Trabalhos em destaque",
        "work_h2": "Problemas reais, soluções digitais",
        "work_p": "Soluções criadas a partir da experiência prática na indústria automotiva: manutenção, produção, qualidade e operações.",
        "preview_soon": "Prévia em breve",
        "read_more": "Saiba mais →",
        "see_all": "Ver todos os projetos",
        "home_desc": "Soluções em Power BI, Power Apps e Power Automate de uma engenheira eletricista com experiência real na indústria.",
        "proj_title": "Projetos",
        "proj_eyebrow": "Projetos do portfólio",
        "proj_p": "Cada projeto mostra o problema, o que eu construí e o que mudou. Os dados exibidos são fictícios ou anonimizados.",
        "proj_desc": "Projetos em Power BI, Power Apps e Power Automate com problema, solução e resultado.",
        "shot_soon": "Imagem em breve",
        "problem": "Problema", "solution": "Solução", "result": "Resultado",
        "case_soon": "Estudo de caso em breve",
        "demos_title": "Demonstrações",
        "demos_eyebrow": "Demonstrações",
        "demos_h1": "Veja funcionando",
        "demos_p": "Dashboards interativos para explorar e vídeos curtos de apps e fluxos em ação. Todos os dados são fictícios ou anonimizados.",
        "demos_desc": "Dashboards interativos em Power BI e vídeos de soluções em Power Apps e Power Automate.",
        "bi_tag": "Power BI · interativo",
        "bi_hint": "Filtre, clique e aprofunde",
        "bi_soon": "Dashboard interativo em breve",
        "bi_sub": "Relatório do Power BI incorporado aqui",
        "apps_tag": "Power Apps · vídeo",
        "flow_tag": "Power Automate · vídeo",
        "lup_demo": "Demonstração do app LUP",
        "flow_demo": "Demonstração de fluxo de aprovação",
        "video_soon": "Vídeo em breve",
        "about_title": "Sobre & Contato",
        "about_eyebrow": "Sobre &amp; contato",
        "about_h1": "Olá, eu sou a Bruna",
        "about_desc": "Bruna Berleze, engenheira eletricista e desenvolvedora Power Platform com experiência industrial no Grupo Renault.",
        "about_p": "Engenheira eletricista (UTFPR) com experiência prática em manutenção industrial e melhoria de processos na estamparia do Grupo Renault e no laboratório de emissões da HORSE Powertrain. Primeiro eu mapeio o processo, depois escolho a ferramenta certa: um app, um fluxo, um dashboard ou os três.",
        "services": "SERVIÇOS",
        "svc": ["Dashboards e Indicadores", "Digitalização de Processos", "Mapeamento e Melhoria de Processos"],
        "tools": "FERRAMENTAS",
        "credentials": "FORMAÇÃO",
        "creds": ["Engenharia Elétrica · UTFPR", "Pós-graduação · Engenharia de Manutenção",
                  "Pós-graduação · Business Intelligence, Big Data &amp; IA",
                  "Certificado Google de Gestão de Projetos", "Inglês · C1 Avançado"],
        "nf_title": "Página não encontrada", "nf_h1": "Esta página não existe.", "nf_btn": "Voltar ao início",
    },
}

# (id, title, tags, thumb class, description) per language
PROJECTS = [
    ("oee", {"en": "OEE Production Dashboard", "pt": "Dashboard de OEE da Produção"},
     {"en": [("Power BI", "bi"), ("Manufacturing", "")], "pt": [("Power BI", "bi"), ("Manufatura", "")]}, "g1",
     {"en": "Availability, performance and quality in one view, so production teams see where capacity is lost.",
      "pt": "Disponibilidade, desempenho e qualidade numa só visão, para a produção ver onde perde capacidade."}),
    ("lup", {"en": "LUP One-Point Lesson App", "pt": "App de LUP (Lição de Um Ponto)"},
     {"en": [("Power Apps", "apps"), ("Training", "")], "pt": [("Power Apps", "apps"), ("Treinamento", "")]}, "g2",
     {"en": "A simple app to create, find and share one-point lessons on the shop floor instead of printed sheets.",
      "pt": "Um app simples para criar, encontrar e compartilhar lições de um ponto no chão de fábrica, sem folhas impressas."}),
    ("dca", {"en": "DCA Digital Form", "pt": "Formulário Digital DCA"},
     {"en": [("Power Apps", "apps"), ("Quality", "")], "pt": [("Power Apps", "apps"), ("Qualidade", "")]}, "g3",
     {"en": "A paper-based process turned into a digital form, with records that can be searched and analysed.",
      "pt": "Um processo em papel transformado em formulário digital, com registros fáceis de buscar e analisar."}),
    ("shift", {"en": "Shift Handover Digitalization", "pt": "Digitalização da Passagem de Turno"},
     {"en": [("Power Platform", "flow"), ("Operations", "")], "pt": [("Power Platform", "flow"), ("Operações", "")]}, "g1",
     {"en": "Shift handover information captured digitally, so the next shift starts with the full picture.",
      "pt": "Informações da passagem de turno registradas digitalmente, para o próximo turno começar com o quadro completo."}),
    ("retail", {"en": "Retail Sales Performance", "pt": "Desempenho de Vendas no Varejo"},
     {"en": [("Power BI", "bi"), ("Retail", "")], "pt": [("Power BI", "bi"), ("Varejo", "")]}, "g2",
     {"en": "Sales, margin and store performance with filters and drill-down for fast business decisions.",
      "pt": "Vendas, margem e desempenho por loja, com filtros e detalhamento para decisões rápidas."}),
]

TOOLS = ["Power BI", "DAX", "Power Query", "Power Apps", "Power Automate", "SharePoint", "Excel", "Lean"]

ICON_APP = '<svg aria-hidden="true" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="2" width="12" height="20" rx="2"/><path d="M10 18h4"/></svg>'
ICON_FLOW = '<svg aria-hidden="true" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L4 14h7l-1 8 9-12h-7z"/></svg>'
ICON_BI = '<svg aria-hidden="true" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 5-6"/></svg>'


def url_for(lang, file):
    """Absolute site path of a page in a language."""
    base = "/" if lang == "en" else "/pt/"
    return base if file == "index.html" else base + file


def layout(lang, file, title, description, body):
    t = T[lang]
    cur = 'aria-current="page"'
    nav = "\n".join(
        f'<a href="{url_for(lang, f)}" {cur if f == file else ""}>{t["nav"][f]}</a>' for f in PAGES)
    full_title = t["site_title"] if file == "index.html" else f"{title} · Bruna Berleze"
    en_url, pt_url = url_for("en", file), url_for("pt", file)
    alt = "" if file == "404.html" else f"""<link rel="alternate" hreflang="en" href="{SITE_URL}{en_url}">
<link rel="alternate" hreflang="pt-BR" href="{SITE_URL}{pt_url}">
<link rel="alternate" hreflang="x-default" href="{SITE_URL}{en_url}">
<link rel="canonical" href="{SITE_URL}{url_for(lang, file)}">"""
    en_cur = cur if lang == "en" else ""
    pt_cur = cur if lang == "pt" else ""
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
<meta name="theme-color" content="#0B0D1F">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
<link rel="icon" type="image/png" sizes="64x64" href="/assets/favicon-64.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
</head>
<body>
<div class="glow v" aria-hidden="true"></div>
<div class="glow c" aria-hidden="true"></div>
<div class="glow p" aria-hidden="true"></div>
<header>
<div class="wrap nav">
<a class="brand" href="{url_for(lang, 'index.html')}">Bruna Berleze<span>.</span></a>
<div class="nav-right">
<nav class="menu" aria-label="Main">
{nav}
</nav>
<div class="lang" role="group" aria-label="{t['lang_label']}">
<a href="{en_url}" hreflang="en" lang="en" data-lang="en" {en_cur}>EN</a>
<a href="{pt_url}" hreflang="pt-BR" lang="pt-BR" data-lang="pt" {pt_cur}>PT</a>
</div>
</div>
</div>
</header>
<main class="wrap">
{body}
</main>
<footer>
<div class="wrap">{t['footer']}</div>
</footer>
<script src="/assets/main.js"></script>
</body>
</html>
"""


def cta(lang):
    t = T[lang]
    return f"""<section id="contact" class="reveal">
<div class="cta">
<div>
<h2>{t['cta_title']}</h2>
<p>{t['cta_text']}</p>
</div>
<div class="btns">
<a class="btn primary" href="{FIVERR_URL}">{t['cta_fiverr']}</a>
<a class="btn ghost" href="{UPWORK_URL}">{t['cta_upwork']}</a>
</div>
</div>
</section>"""


def tags_html(tags):
    return '<div class="tags">' + "".join(f'<span class="tag {c}">{x}</span>' for x, c in tags) + "</div>"


def home(lang):
    t = T[lang]
    featured = "".join(
        f"""<article class="card glass">
<div class="thumb {thumb}">{t['preview_soon']}</div>
<div class="body">
{tags_html(tags[lang])}
<h3>{title[lang]}</h3>
<p>{desc[lang]}</p>
<a class="more" href="{url_for(lang, 'projects.html')}#{pid}">{t['read_more']}</a>
</div>
</article>""" for pid, title, tags, thumb, desc in PROJECTS[:3])
    body = f"""<section class="hero">
<div class="stack">
<span class="pill">{t['pill']}</span>
<h1>{t['h1']}</h1>
<p class="lead">{t['lead']}</p>
<div class="btns">
<a class="btn primary" href="{url_for(lang, 'projects.html')}">{t['btn_projects']}</a>
<a class="btn ghost" href="{url_for(lang, 'demos.html')}">{t['btn_demos']}</a>
</div>
<div class="tags">
<span class="tag bi">Power BI</span><span class="tag apps">Power Apps</span><span class="tag flow">Power Automate</span><span class="tag">SharePoint</span><span class="tag">Lean</span>
</div>
</div>
<div class="steps glass">
<span class="label">{t['deliver']}</span>
<div class="step apps"><div class="icon">{ICON_APP}</div><div><h3>{t['step_apps'][0]}</h3><p>{t['step_apps'][1]}</p></div></div>
<div class="step flow"><div class="icon">{ICON_FLOW}</div><div><h3>{t['step_flow'][0]}</h3><p>{t['step_flow'][1]}</p></div></div>
<div class="step bi"><div class="icon">{ICON_BI}</div><div><h3>{t['step_bi'][0]}</h3><p>{t['step_bi'][1]}</p></div></div>
</div>
</section>

<section class="reveal">
<div class="head">
<span class="eyebrow">{t['work_eyebrow']}</span>
<h2>{t['work_h2']}</h2>
<p>{t['work_p']}</p>
</div>
<div class="grid">
{featured}
</div>
<div class="btns" style="margin-top:28px"><a class="btn ghost" href="{url_for(lang, 'projects.html')}">{t['see_all']}</a></div>
</section>

{cta(lang)}"""
    return layout(lang, "index.html", t["nav"]["index.html"], t["home_desc"], body)


def projects(lang):
    t = T[lang]
    cases = "".join(
        f"""<article id="{pid}" class="case glass reveal">
<div class="thumb {thumb}">{t['shot_soon']}</div>
<div class="body">
{tags_html(tags[lang])}
<h2>{title[lang]}</h2>
<p style="color:var(--muted)">{desc[lang]}</p>
<div class="psr">
<div><b>{t['problem']} · </b><span class="soon">{t['case_soon']}</span></div>
<div><b>{t['solution']} · </b><span class="soon">{t['case_soon']}</span></div>
<div><b>{t['result']} · </b><span class="soon">{t['case_soon']}</span></div>
</div>
</div>
</article>""" for pid, title, tags, thumb, desc in PROJECTS)
    body = f"""<section>
<div class="head">
<span class="eyebrow">{t['proj_eyebrow']}</span>
<h1>{t['proj_title']}</h1>
<p>{t['proj_p']}</p>
</div>
{cases}
</section>
{cta(lang)}"""
    return layout(lang, "projects.html", t["proj_title"], t["proj_desc"], body)


def demos(lang):
    t = T[lang]
    body = f"""<section>
<div class="head">
<span class="eyebrow">{t['demos_eyebrow']}</span>
<h1>{t['demos_h1']}</h1>
<p>{t['demos_p']}</p>
</div>

<div class="demo glass reveal">
<div class="top"><div class="tags"><span class="tag bi">{t['bi_tag']}</span></div><span class="hint">{t['bi_hint']}</span></div>
<h3>{PROJECTS[4][1][lang]}</h3>
<div class="frame report">
<!-- Paste the Power BI "Publish to web" iframe src below and remove the .empty div:
<iframe title="Retail Sales Performance" src="PASTE_POWER_BI_LINK_HERE" allowfullscreen loading="lazy"></iframe> -->
<div class="empty"><strong>{t['bi_soon']}</strong><span>{t['bi_sub']}</span></div>
</div>
</div>

<div class="grid">
<div class="demo glass reveal">
<div class="tags"><span class="tag apps">{t['apps_tag']}</span></div>
<h3>{t['lup_demo']}</h3>
<div class="frame video">
<!-- <iframe title="LUP App" src="https://www.youtube-nocookie.com/embed/VIDEO_ID" allowfullscreen loading="lazy"></iframe> -->
<div class="empty"><strong>{t['video_soon']}</strong></div>
</div>
</div>
<div class="demo glass reveal">
<div class="tags"><span class="tag flow">{t['flow_tag']}</span></div>
<h3>{t['flow_demo']}</h3>
<div class="frame video">
<!-- <iframe title="Approval flow" src="https://www.youtube-nocookie.com/embed/VIDEO_ID" allowfullscreen loading="lazy"></iframe> -->
<div class="empty"><strong>{t['video_soon']}</strong></div>
</div>
</div>
</div>
</section>
{cta(lang)}"""
    return layout(lang, "demos.html", t["demos_title"], t["demos_desc"], body)


def about(lang):
    t = T[lang]
    svc_cls = ["bi", "apps", "flow"]
    svc = "".join(f'<span class="tag {c}">{s}</span>' for s, c in zip(t["svc"], svc_cls))
    tools = "".join(f'<span class="tag">{x}</span>' for x in TOOLS)
    creds = "".join(f"<div>{c}</div>" for c in t["creds"])
    body = f"""<section>
<div class="head">
<span class="eyebrow">{t['about_eyebrow']}</span>
<h1>{t['about_h1']}</h1>
</div>
<div class="grid">
<div class="panel glass reveal">
<p style="color:var(--muted)">{t['about_p']}</p>
<span class="label">{t['services']}</span>
<div class="tags">{svc}</div>
<span class="label">{t['tools']}</span>
<div class="tags">{tools}</div>
</div>
<div class="panel glass reveal">
<span class="label">{t['credentials']}</span>
<div class="list">{creds}</div>
</div>
</div>
</section>
{cta(lang)}"""
    return layout(lang, "about.html", t["about_title"], t["about_desc"], body)


def not_found(lang):
    t = T[lang]
    body = f"""<section class="hero"><div class="stack">
<span class="pill">404</span><h1>{t['nf_h1']}</h1>
<div class="btns"><a class="btn primary" href="{url_for(lang, 'index.html')}">{t['nf_btn']}</a></div></div></section>"""
    return layout(lang, "404.html", t["nf_title"], t["nf_title"], body)


for lang in ("en", "pt"):
    out = ROOT if lang == "en" else ROOT / "pt"
    out.mkdir(exist_ok=True)
    for name, fn in [("index.html", home), ("projects.html", projects), ("demos.html", demos), ("about.html", about)]:
        (out / name).write_text(fn(lang), encoding="utf-8")
(ROOT / "404.html").write_text(not_found("en"), encoding="utf-8")
print("built en + pt")

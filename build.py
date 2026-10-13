"""Builds the static pages from one shared layout. Run: python3 build.py"""
from pathlib import Path

ROOT = Path(__file__).parent
SITE_URL = "https://bruna-berleze.github.io"
# Fill in your profile links here, then run the script again.
FIVERR_URL = "#contact"
UPWORK_URL = "#contact"

PAGES = [
    ("index.html", "Home"),
    ("projects.html", "Projects"),
    ("demos.html", "Live Demos"),
    ("about.html", "About & Contact"),
]

ICON_APP = '<svg aria-hidden="true" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="2" width="12" height="20" rx="2"/><path d="M10 18h4"/></svg>'
ICON_FLOW = '<svg aria-hidden="true" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L4 14h7l-1 8 9-12h-7z"/></svg>'
ICON_BI = '<svg aria-hidden="true" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 5-6"/></svg>'


def layout(file, title, description, body):
    nav = "\n".join(
        f'<a href="{f}"{" aria-current=\"page\"" if f == file else ""}>{name}</a>' for f, name in PAGES
    )
    full_title = "Bruna Berleze · Power Platform Developer" if file == "index.html" else f"{title} · Bruna Berleze"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE_URL}/{'' if file == 'index.html' else file}">
<meta name="theme-color" content="#0B0D1F">
<link rel="icon" type="image/png" href="assets/favicon-64.png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<div class="glow v" aria-hidden="true"></div>
<div class="glow c" aria-hidden="true"></div>
<div class="glow p" aria-hidden="true"></div>
<header>
<div class="wrap nav">
<a class="brand" href="index.html">Bruna Berleze<span>.</span></a>
<nav class="menu" aria-label="Main">
{nav}
</nav>
</div>
</header>
<main class="wrap">
{body}
</main>
<footer>
<div class="wrap">© 2026 Bruna Berleze · Power Platform &amp; Process Improvement</div>
</footer>
<script src="assets/main.js"></script>
</body>
</html>
"""


def cta():
    return f"""<section id="contact" class="reveal">
<div class="cta">
<div>
<h2>Let's work together</h2>
<p>Message me on the platform you found me on.</p>
</div>
<div class="btns">
<a class="btn primary" href="{FIVERR_URL}">Hire me on Fiverr</a>
<a class="btn ghost" href="{UPWORK_URL}">Hire me on Upwork</a>
</div>
</div>
</section>"""


PROJECTS = [
    # (id, title, tags, thumb class, short description)
    ("oee", "OEE Production Dashboard", [("Power BI", "bi"), ("Manufacturing", "")], "g1",
     "Availability, performance and quality in one view, so production teams see where capacity is lost."),
    ("lup", "LUP One-Point Lesson App", [("Power Apps", "apps"), ("Training", "")], "g2",
     "A simple app to create, find and share one-point lessons on the shop floor instead of printed sheets."),
    ("dca", "DCA Digital Form", [("Power Apps", "apps"), ("Quality", "")], "g3",
     "A paper-based process turned into a digital form, with records that can be searched and analysed."),
    ("shift", "Shift Handover Digitalization", [("Power Platform", "flow"), ("Operations", "")], "g1",
     "Shift handover information captured digitally, so the next shift starts with the full picture."),
    ("retail", "Retail Sales Performance", [("Power BI", "bi"), ("Retail", "")], "g2",
     "Sales, margin and store performance with filters and drill-down for fast business decisions."),
]


def tags_html(tags):
    return '<div class="tags">' + "".join(
        f'<span class="tag {c}">{t}</span>' for t, c in tags) + "</div>"


def home():
    featured = "".join(
        f"""<article class="card glass">
<div class="thumb {thumb}">Preview coming soon</div>
<div class="body">
{tags_html(tags)}
<h3>{title}</h3>
<p>{desc}</p>
<a class="more" href="projects.html#{pid}">Read more →</a>
</div>
</article>""" for pid, title, tags, thumb, desc in PROJECTS[:3])
    body = f"""<section class="hero">
<div class="stack">
<span class="pill">Power Platform Developer · Electrical Engineer</span>
<h1>I ran the operations before I built the solutions.</h1>
<p class="lead">Power BI dashboards, Power Apps and Power Automate workflows that digitalize operations and improve decisions in maintenance, production and business.</p>
<div class="btns">
<a class="btn primary" href="projects.html">View projects</a>
<a class="btn ghost" href="demos.html">See live demos</a>
</div>
<div class="tags">
<span class="tag bi">Power BI</span><span class="tag apps">Power Apps</span><span class="tag flow">Power Automate</span><span class="tag">SharePoint</span><span class="tag">Lean</span>
</div>
</div>
<div class="steps glass">
<span class="label">HOW I DELIVER</span>
<div class="step apps"><div class="icon">{ICON_APP}</div><div><h3>Capture · Power Apps</h3><p>Replace paper forms and spreadsheets with simple apps.</p></div></div>
<div class="step flow"><div class="icon">{ICON_FLOW}</div><div><h3>Automate · Power Automate</h3><p>Approvals, alerts and data flowing on their own.</p></div></div>
<div class="step bi"><div class="icon">{ICON_BI}</div><div><h3>Decide · Power BI</h3><p>KPIs and dashboards people actually use.</p></div></div>
</div>
</section>

<section class="reveal">
<div class="head">
<span class="eyebrow">Selected work</span>
<h2>Real problems, digital solutions</h2>
<p>Solutions built from hands-on experience in automotive manufacturing: maintenance, production, quality and operations.</p>
</div>
<div class="grid">
{featured}
</div>
<div class="btns" style="margin-top:28px"><a class="btn ghost" href="projects.html">See all projects</a></div>
</section>

{cta()}"""
    return layout("index.html", "Home",
                  "Power BI, Power Apps and Power Automate solutions from an Electrical Engineer with real manufacturing experience.",
                  body)


def projects():
    cases = "".join(
        f"""<article id="{pid}" class="case glass reveal">
<div class="thumb {thumb}">Screenshot coming soon</div>
<div class="body">
{tags_html(tags)}
<h2>{title}</h2>
<p style="color:var(--muted)">{desc}</p>
<div class="psr">
<div><b>Problem · </b><span class="soon">Case study coming soon</span></div>
<div><b>Solution · </b><span class="soon">Case study coming soon</span></div>
<div><b>Result · </b><span class="soon">Case study coming soon</span></div>
</div>
</div>
</article>""" for pid, title, tags, thumb, desc in PROJECTS)
    body = f"""<section>
<div class="head">
<span class="eyebrow">Portfolio projects</span>
<h1>Projects</h1>
<p>Each project shows the problem, what I built and what changed. Data shown is fictional or anonymized.</p>
</div>
{cases}
</section>
{cta()}"""
    return layout("projects.html", "Projects",
                  "Power BI dashboards, Power Apps and Power Automate projects with problem, solution and result.",
                  body)


def demos():
    body = f"""<section>
<div class="head">
<span class="eyebrow">Live demos</span>
<h1>See it working</h1>
<p>Interactive dashboards you can explore, and short videos of apps and flows in action. All data is fictional or anonymized.</p>
</div>

<div class="demo glass reveal">
<div class="top"><div class="tags"><span class="tag bi">Power BI · interactive</span></div><span class="hint">Filter, click and drill down</span></div>
<h3>Retail Sales Performance</h3>
<div class="frame report">
<!-- Paste the Power BI "Publish to web" iframe src below and remove the .empty div:
<iframe title="Retail Sales Performance" src="PASTE_POWER_BI_LINK_HERE" allowfullscreen loading="lazy"></iframe> -->
<div class="empty"><strong>Interactive dashboard coming soon</strong><span>Power BI report embedded here</span></div>
</div>
</div>

<div class="grid">
<div class="demo glass reveal">
<div class="tags"><span class="tag apps">Power Apps · video</span></div>
<h3>LUP App walkthrough</h3>
<div class="frame video">
<!-- <iframe title="LUP App walkthrough" src="https://www.youtube-nocookie.com/embed/VIDEO_ID" allowfullscreen loading="lazy"></iframe> -->
<div class="empty"><strong>Video coming soon</strong></div>
</div>
</div>
<div class="demo glass reveal">
<div class="tags"><span class="tag flow">Power Automate · video</span></div>
<h3>Approval flow demo</h3>
<div class="frame video">
<!-- <iframe title="Approval flow demo" src="https://www.youtube-nocookie.com/embed/VIDEO_ID" allowfullscreen loading="lazy"></iframe> -->
<div class="empty"><strong>Video coming soon</strong></div>
</div>
</div>
</div>
</section>
{cta()}"""
    return layout("demos.html", "Live Demos",
                  "Interactive Power BI dashboards and video demos of Power Apps and Power Automate solutions.",
                  body)


def about():
    body = f"""<section>
<div class="head">
<span class="eyebrow">About &amp; contact</span>
<h1>Hi, I'm Bruna</h1>
</div>
<div class="grid">
<div class="panel glass reveal">
<p style="color:var(--muted)">Electrical Engineer (UTFPR) with hands-on experience in industrial maintenance and process improvement at Renault Group's stamping department and HORSE Powertrain's emissions lab. I map the process first, then pick the right tool: an app, a flow, a dashboard, or all three.</p>
<span class="label">SERVICES</span>
<div class="tags">
<span class="tag bi">Data &amp; KPI Dashboards</span>
<span class="tag apps">Workflow Digitalization</span>
<span class="tag flow">Process Mapping &amp; Improvement</span>
</div>
<span class="label">TOOLS</span>
<div class="tags">
<span class="tag">Power BI</span><span class="tag">DAX</span><span class="tag">Power Query</span><span class="tag">Power Apps</span><span class="tag">Power Automate</span><span class="tag">SharePoint</span><span class="tag">Excel</span><span class="tag">Lean</span>
</div>
</div>
<div class="panel glass reveal">
<span class="label">CREDENTIALS</span>
<div class="list">
<div>BSc Electrical Engineering · UTFPR</div>
<div>Postgraduate · Maintenance Engineering</div>
<div>Postgraduate · Business Intelligence, Big Data &amp; AI</div>
<div>Google Project Management Professional Certificate</div>
<div>English · C1 Advanced</div>
</div>
</div>
</div>
</section>
{cta()}"""
    return layout("about.html", "About & Contact",
                  "Bruna Berleze, Electrical Engineer and Power Platform developer with manufacturing experience at Renault Group.",
                  body)


for name, fn in [("index.html", home), ("projects.html", projects), ("demos.html", demos), ("about.html", about)]:
    (ROOT / name).write_text(fn(), encoding="utf-8")

(ROOT / "404.html").write_text(layout("404.html", "Page not found", "Page not found", """<section class="hero"><div class="stack">
<span class="pill">404</span><h1>This page doesn't exist.</h1>
<div class="btns"><a class="btn primary" href="index.html">Back to home</a></div></div></section>"""), encoding="utf-8")
print("built")

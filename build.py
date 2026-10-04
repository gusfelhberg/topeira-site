#!/usr/bin/env python3
"""build.py: writes the site's pages (English at /, Portuguese at /pt/) from the texts below.
Run it after changing a text: python3 build.py. The output is plain static files; nothing else is needed to host it."""
import pathlib

ROOT = pathlib.Path(__file__).parent
EMAIL = "hello@studiotopeira.com"
STORE = ""          # the App Store address once Iara is live; empty shows "Coming soon"

CSS = """
@font-face { font-family: "Amatic SC"; src: url("%(base)sassets/AmaticSC-Bold.ttf") format("truetype"); font-weight: 700; font-display: swap; }
:root { --bg:#0b1418; --panel:#12212a; --rule:#22343c; --fg:#e9eef0; --muted:#9db0b6; --gold:#ffe3a8; --ember:#f08a3c; }
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { margin:0; background:var(--bg); color:var(--fg); -webkit-text-size-adjust:100%%;
       font:17px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif; }
a { color:var(--gold); }
.wrap { max-width:66rem; margin:0 auto; padding:0 20px; }
header.top { display:flex; align-items:center; justify-content:space-between; padding:18px 0; }
.mark { display:flex; align-items:center; gap:10px; color:var(--gold); text-decoration:none;
        font:700 2rem/1 "Amatic SC",sans-serif; letter-spacing:.04em; }
.mark svg { width:34px; height:34px; }
header.top nav a { color:var(--muted); text-decoration:none; font-size:.9rem; margin-left:18px; }
header.top nav a:hover { color:var(--gold); }
.hero { padding:9vh 0 8vh; text-align:center; }
.hero h1 { font:700 clamp(3.2rem,11vw,6.5rem)/.95 "Amatic SC",sans-serif; color:var(--gold); margin:0 0 .35em; letter-spacing:.03em; }
.hero p { max-width:34rem; margin:0 auto; color:var(--muted); font-size:1.12rem; }
.game { background:var(--panel); border:1px solid var(--rule); border-radius:26px; overflow:hidden;
        display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); }
.game .art { min-height:420px; background:url("%(base)sassets/iara-splash.jpg") center 30%%/cover; }
.game .txt { padding:38px 38px 34px; }
.kicker { text-transform:uppercase; letter-spacing:.16em; font-size:.74rem; color:var(--ember); margin:0 0 10px; }
.title { display:flex; align-items:center; gap:16px; margin:0 0 14px; }
.title img { width:68px; height:68px; border-radius:16px; }
.title h2 { font:700 clamp(2.4rem,6vw,3.4rem)/1 "Amatic SC",sans-serif; color:var(--gold); margin:0; }
.game p { margin:0 0 14px; }
.facts { list-style:none; padding:0; margin:18px 0 24px; display:flex; flex-wrap:wrap; gap:8px; }
.facts li { border:1px solid var(--rule); border-radius:999px; padding:4px 13px; font-size:.86rem; color:var(--muted); }
.cta { display:inline-block; border:1.5px solid var(--gold); color:var(--gold); border-radius:999px; padding:10px 24px;
       font:700 1.5rem/1 "Amatic SC",sans-serif; letter-spacing:.05em; text-decoration:none; }
span.cta { opacity:.75; }
.shots { display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:16px; margin:28px 0 0; }
.shots img { width:100%%; height:auto; border-radius:20px; border:1px solid var(--rule); display:block; }
section.about { padding:9vh 0 2vh; display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:26px; }
section.about h3 { font:700 2rem/1.1 "Amatic SC",sans-serif; color:var(--gold); margin:0 0 8px; letter-spacing:.03em; }
section.about p { margin:0; color:var(--muted); font-size:.98rem; }
footer { border-top:1px solid var(--rule); margin-top:9vh; padding:26px 0 46px; color:var(--muted); font-size:.88rem;
         display:flex; flex-wrap:wrap; gap:8px 22px; justify-content:space-between; }
footer a { color:var(--muted); }
main.doc { max-width:44rem; margin:0 auto; padding:3vh 20px 4vh; }
main.doc h1 { font:700 3rem/1.05 "Amatic SC",sans-serif; color:var(--gold); margin:.4em 0 .3em; }
main.doc h2 { font-size:1.08rem; margin:2.2rem 0 .5rem; color:var(--fg); }
main.doc p, main.doc li { color:#c9d4d8; }
@media (max-width: 760px) {
  .game { grid-template-columns:1fr; }
  .game .art { min-height:300px; }
  .game .txt { padding:26px 22px; }
  .shots { grid-template-columns:repeat(2,minmax(0,1fr)); }
  section.about { grid-template-columns:1fr; }
  header.top nav a:not(.lang) { display:none; }
}
"""

# a molehill with a small light on top: the studio's mark until a drawn one exists
MARK = ('<svg viewBox="0 0 34 34" aria-hidden="true"><path d="M2 27c3-1 5-11 15-11s12 10 15 11z" fill="#ffe3a8"/>'
        '<circle cx="17" cy="9" r="3.2" fill="#f08a3c"/><circle cx="17" cy="9" r="6" fill="#f08a3c" opacity=".25"/></svg>')

T = {
    "en": dict(
        lang="en", base="", other=("pt/", "Português"), home="./",
        title="Studio Topeira", desc="Studio Topeira makes small, carefully made apps and games. First: Iara: River of Lanterns.",
        nav=[("#iara", "Iara"), ("#studio", "The studio"), ("mailto:" + EMAIL, "Contact")],
        h1="Small apps, made with care",
        lead="Studio Topeira is a one-person studio. It makes small apps and games that do one thing well, with no ads and nothing that follows you around.",
        kicker="The first one: a game", name="Iara: River of Lanterns",
        p1="Guide a lantern up five real rivers of the Amazon and bring it home to Iara, the keeper of the waters in Brazilian folklore.",
        p2="One tap pushes the lantern. Frogs, caimans, jaguars and the pink river dolphin are each on the river where they really live, and every river tells you something true about it. In Zen the river is dark, nothing strikes, and your light wakes what lives there.",
        facts=["iPhone", "Free", "25 rivers", "No ads, no purchases", "No account", "English · Português"],
        soon="Coming soon to the App Store", get="Get it on the App Store", shots="Screenshots of Iara: River of Lanterns",
        about=[("Topeira", "It means \"mole\" in Portuguese: a small animal that works out of sight and digs patiently. That is roughly how the studio works."),
               ("How they are made", "One person, in Canada, born in Brazil. Slowly, and checked: every animal, plant and fact in Iara was verified against a source before it went in."),
               ("What they never do", "No advertising, no tracking, no accounts. Iara 1.0 sends nothing from your phone at all.")],
        contact="Contact", privacy="Privacy", support="Support", rights="© 2026 Studio Topeira",
    ),
    "pt": dict(
        lang="pt-BR", base="../", other=("../", "English"), home="./",
        title="Studio Topeira", desc="O Studio Topeira faz apps e jogos pequenos e bem cuidados. O primeiro: Iara: River of Lanterns.",
        nav=[("#iara", "Iara"), ("#studio", "O estúdio"), ("mailto:" + EMAIL, "Contato")],
        h1="Apps pequenos, feitos com cuidado",
        lead="O Studio Topeira é um estúdio de uma pessoa só. Faz apps e jogos pequenos que fazem bem uma coisa só, sem anúncios e sem nada que fique seguindo você.",
        kicker="O primeiro: um jogo", name="Iara: River of Lanterns",
        p1="Leve uma lanterna por cinco rios de verdade da Amazônia até a Iara, a guardiã das águas no folclore brasileiro.",
        p2="Um toque empurra a lanterna. Sapos, jacarés, onças e o boto-cor-de-rosa aparecem cada um no rio onde realmente vivem, e cada rio conta algo verdadeiro sobre ele. No modo Zen o rio está escuro, nada ataca, e a sua luz desperta o que vive ali.",
        facts=["iPhone", "Grátis", "25 rios", "Sem anúncios, sem compras", "Sem conta", "English · Português"],
        soon="Em breve na App Store", get="Baixar na App Store", shots="Telas de Iara: River of Lanterns",
        about=[("Topeira", "É o bicho pequeno que trabalha escondido e cava com paciência. É mais ou menos assim que o estúdio trabalha."),
               ("Como eles são feitos", "Uma pessoa só, no Canadá, nascida no Brasil. Devagar e conferindo: cada animal, planta e fato do Iara foi verificado em uma fonte antes de entrar."),
               ("O que eles nunca fazem", "Nada de anúncios, rastreamento ou contas. O Iara 1.0 não envia nada do seu celular.")],
        contact="Contato", privacy="Privacidade", support="Suporte", rights="© 2026 Studio Topeira",
    ),
}


def head(t, title, base):
    return f"""<!DOCTYPE html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{t['desc']}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{t['desc']}">
<meta property="og:image" content="https://studiotopeira.com/assets/iara-splash.jpg">
<link rel="icon" href="{base}assets/iara-icon.png">
<style>{CSS % dict(base=base)}</style>
</head>
<body>
"""


def top(t, base, nav=True):
    links = "".join(f'<a href="{h}">{n}</a>' for h, n in t["nav"]) if nav else ""
    return (f'<div class="wrap"><header class="top"><a class="mark" href="{base or "./"}">{MARK}Topeira</a>'
            f'<nav>{links}<a class="lang" href="{t["other"][0]}">{t["other"][1]}</a></nav></header></div>\n')


def foot(t, base):
    return (f'<div class="wrap"><footer><span>{t["rights"]}</span><span><a href="mailto:{EMAIL}">{EMAIL}</a> &nbsp;·&nbsp; '
            f'<a href="{base}iara/privacy/">{t["privacy"]}</a> &nbsp;·&nbsp; <a href="{base}iara/support/">{t["support"]}</a></span></footer></div>\n</body>\n</html>\n')


def home(code):
    t = T[code]; base = t["base"]
    cta = f'<a class="cta" href="{STORE}">{t["get"]}</a>' if STORE else f'<span class="cta">{t["soon"]}</span>'
    shots = "".join(f'<img src="{base}assets/iara-{code}-{k}.jpg" alt="{t["shots"]} {k}" loading="lazy" width="507" height="1100">' for k in (1, 2, 3, 4))
    about = "".join(f"<div><h3>{h}</h3><p>{p}</p></div>" for h, p in t["about"])
    facts = "".join(f"<li>{f}</li>" for f in t["facts"])
    return (head(t, t["title"], base) + top(t, base) + f"""<div class="wrap">
<section class="hero"><h1>{t['h1']}</h1><p>{t['lead']}</p></section>
<section id="iara">
  <div class="game">
    <div class="art" role="img" aria-label="Iara"></div>
    <div class="txt">
      <p class="kicker">{t['kicker']}</p>
      <div class="title"><img src="{base}assets/iara-icon.png" alt=""><h2>{t['name']}</h2></div>
      <p>{t['p1']}</p>
      <p>{t['p2']}</p>
      <ul class="facts">{facts}</ul>
      {cta}
    </div>
  </div>
  <div class="shots">{shots}</div>
</section>
<section class="about" id="studio">{about}</section>
</div>
""" + foot(t, base))


PRIVACY = f"""<h1>Privacy Policy: Iara: River of Lanterns</h1>
<p><em>Effective date: 2026-10-05</em></p>
<p>Iara: River of Lanterns ("Iara", "the app") is made by Studio Topeira. This policy says, in plain English, what the app does and does not do with your information.</p>
<h2>What we collect</h2>
<p><strong>Nothing.</strong> Iara has no account and no sign-up, and never asks for your name, email, location, contacts or any other personal information. Version 1.0 on the App Store does not transmit any data: everything the game records about your play stays on your device.</p>
<p>Test versions of the game (TestFlight) can ask whether you want to share anonymous play statistics. If a later App Store version includes that, the app will ask first, nothing is sent unless you say yes, and this policy will be updated before it ships.</p>
<h2>What is stored on your device</h2>
<p>Your progress (rivers passed, stars, best scores), your settings and the curiosities you have already seen are kept inside the app's own storage on your device. Deleting the app deletes all of it.</p>
<h2>Third parties</h2>
<p>Iara contains no third-party SDKs: no advertising, no analytics, no social networks.</p>
<h2>Children's privacy</h2>
<p>Iara is a general-audience game, not directed at children. It does not ask for or collect anyone's personal information, whatever their age, and has no chat or user-generated content.</p>
<h2>Tracking</h2>
<p>None. Iara does not use the advertising identifier (IDFA) and does not track you across other apps or websites.</p>
<h2>Changes to this policy</h2>
<p>If this policy changes, the effective date above is updated and the new version is posted at this address.</p>
<h2>Contact</h2>
<p>Questions about this policy or the app: <a href="mailto:{EMAIL}">{EMAIL}</a></p>"""

SUPPORT = f"""<h1>Support: Iara: River of Lanterns</h1>
<p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> and, if you can, say which iPhone and iOS version you have. Every message is read.</p>
<h2>Does the game need an internet connection?</h2>
<p>No. It works fully offline and version 1.0 makes no network calls at all.</p>
<h2>Is there an account, a subscription or anything to buy?</h2>
<p>No. The game is free, with no ads and no purchases.</p>
<h2>How do I delete my data?</h2>
<p>Delete the app. Everything it remembers is stored on your device, so removing the app removes all of it.</p>
<h2>A river feels impossible</h2>
<p>Zen mode has the same rivers with nothing that strikes. If a spot in Play really cannot be passed, please write and say which river: that is a bug, and it will be fixed.</p>
<h2>How do I change the language?</h2>
<p>In the game's Settings (the gear on the first screen): English or Português.</p>"""


def doc(body, title):
    t = dict(T["en"], base="../../", other=("../../pt/", "Português"))
    return head(t, title, "../../") + top(t, "../../", nav=False) + f'<main class="doc">\n{body}\n</main>\n' + foot(t, "../../")


(ROOT / "index.html").write_text(home("en"))
(ROOT / "pt/index.html").write_text(home("pt"))
(ROOT / "iara/privacy/index.html").write_text(doc(PRIVACY, "Privacy Policy: Iara: River of Lanterns"))
(ROOT / "iara/support/index.html").write_text(doc(SUPPORT, "Support: Iara: River of Lanterns"))
print("written: index.html, pt/index.html, iara/privacy/index.html, iara/support/index.html")

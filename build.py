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
header.top nav { display:flex; align-items:center; }
.switch { display:inline-flex; margin-left:20px; border:1px solid var(--rule); border-radius:999px; padding:3px; }
.switch a, .switch span { margin:0 !important; padding:4px 12px; border-radius:999px; font-size:.8rem; font-weight:600; letter-spacing:.06em; text-decoration:none; color:var(--muted); }
.switch .on { background:var(--gold); color:#0b1418; }
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
#more, #rivers { padding:9vh 0 0; }
h2.more { font:700 clamp(2.6rem,7vw,4rem)/1 "Amatic SC",sans-serif; color:var(--gold); margin:0 0 .3em; letter-spacing:.03em; }
.morelead { max-width:40rem; color:var(--muted); margin:0 0 26px; }
.packs { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:18px; }
.packs.five { grid-template-columns:repeat(5,minmax(0,1fr)); gap:14px; }
.packs.five .pack img { height:260px; }
.packs.five .pack h3 { font-size:1.7rem; }
.pack { position:relative; border-radius:20px; overflow:hidden; border:1px solid var(--rule); background:var(--panel); }
.pack img { display:block; width:100%%; height:320px; object-fit:cover; }
.pack .ptxt { padding:16px 18px 18px; }
.pack h3 { font:700 2.1rem/1.05 "Amatic SC",sans-serif; color:var(--gold); margin:0 0 6px; letter-spacing:.03em; }
.pack p { margin:0; font-size:.95rem; }
.pack .waters { color:var(--muted); font-size:.8rem; margin-top:8px; }
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
@media (max-width: 1040px) { .packs.five { grid-template-columns:repeat(3,minmax(0,1fr)); } }
@media (max-width: 760px) {
  .game { grid-template-columns:1fr; }
  .game .art { min-height:300px; }
  .game .txt { padding:26px 22px; }
  .shots { grid-template-columns:repeat(2,minmax(0,1fr)); }
  section.about { grid-template-columns:1fr; }
  .packs, .packs.five { grid-template-columns:1fr; }
  .pack img { height:240px; }
  header.top nav > a { display:none; }
}
"""

# a molehill with a small light on top: the studio's mark until a drawn one exists
MARK = ('<svg viewBox="0 0 34 34" aria-hidden="true"><path d="M2 27c3-1 5-11 15-11s12 10 15 11z" fill="#ffe3a8"/>'
        '<circle cx="17" cy="9" r="3.2" fill="#f08a3c"/><circle cx="17" cy="9" r="6" fill="#f08a3c" opacity=".25"/></svg>')

T = {
    "en": dict(
        lang="en", base="", en_href="./", br_href="pt/", es_href="es/",
        title="Studio Topeira", desc="Studio Topeira designs and builds apps and games for iPhone. Our first release is Iara: River of Lanterns.",
        nav=[("#iara", "Iara"), ("#rivers", "Rivers"), ("#more", "Coming soon"), ("#studio", "About"), ("mailto:" + EMAIL, "Contact")],
        h1="Studio Topeira",
        lead="We design and build apps and games for iPhone. Our first release is Iara: River of Lanterns.",
        rivers_kicker="In the game now", rivers_title="Five rivers of the Amazon",
        rivers_lead="Twenty-five levels on five real waters, each with its own colour, its own banks and its own animals.",
        more_kicker="Coming soon", more_title="The journey continues",
        more_lead="After the Amazon, the lantern travels on: six journeys of 25 rivers each, across Brazil and South America. Every one a real place, with what really lives there.",
        kicker="Our first release", name="Iara: River of Lanterns",
        p1="Guide a lantern up five real rivers of the Amazon and bring it home to Iara, the keeper of the waters in Brazilian folklore.",
        p2="One tap pushes the lantern. Frogs, caimans, jaguars and the pink river dolphin are each on the river where they really live, and every river tells you something true about it. In Zen the river is dark, nothing strikes, and your light wakes what lives there.",
        facts=["iPhone", "Free", "25 rivers", "No ads, no purchases", "No account", "English · Português"],
        soon="Coming soon to the App Store", get="Get it on the App Store", shots="Screenshots of Iara: River of Lanterns",
        about=[("What we do", "We make apps and games for iPhone, each built around one clear idea. New titles are in development."),
               ("How we work", "We research before we build and test before we release. In Iara, every animal, plant and fact was verified against a source before it went in."),
               ("Privacy", "Our products carry no advertising and no tracking, and need no account. Iara 1.0 sends nothing from your phone.")],
        contact="Contact", privacy="Privacy", support="Support", rights="© 2026 Studio Topeira",
    ),
    "pt": dict(
        lang="pt-BR", base="../", en_href="../", br_href="./", es_href="../es/",
        title="Studio Topeira", desc="O Studio Topeira cria e desenvolve apps e jogos para iPhone. Nosso primeiro lançamento é Iara: River of Lanterns.",
        nav=[("#iara", "Iara"), ("#rivers", "Rios"), ("#more", "Em breve"), ("#studio", "Sobre"), ("mailto:" + EMAIL, "Contato")],
        h1="Studio Topeira",
        lead="Criamos e desenvolvemos apps e jogos para iPhone. Nosso primeiro lançamento é Iara: River of Lanterns.",
        rivers_kicker="No jogo agora", rivers_title="Cinco rios da Amazônia",
        rivers_lead="Vinte e cinco fases em cinco águas de verdade, cada uma com a sua cor, as suas margens e os seus bichos.",
        more_kicker="Em breve", more_title="A viagem continua",
        more_lead="Depois da Amazônia, a lanterna segue viagem: seis jornadas de 25 rios cada, pelo Brasil e pela América do Sul. Cada uma um lugar de verdade, com o que realmente vive ali.",
        kicker="Nosso primeiro lançamento", name="Iara: River of Lanterns",
        p1="Leve uma lanterna por cinco rios de verdade da Amazônia até a Iara, a guardiã das águas no folclore brasileiro.",
        p2="Um toque empurra a lanterna. Sapos, jacarés, onças e o boto-cor-de-rosa aparecem cada um no rio onde realmente vivem, e cada rio conta algo verdadeiro sobre ele. No modo Zen o rio está escuro, nada ataca, e a sua luz desperta o que vive ali.",
        facts=["iPhone", "Grátis", "25 rios", "Sem anúncios, sem compras", "Sem conta", "English · Português"],
        soon="Em breve na App Store", get="Baixar na App Store", shots="Telas de Iara: River of Lanterns",
        about=[("O que fazemos", "Fazemos apps e jogos para iPhone, cada um construído em torno de uma ideia clara. Novos títulos estão em desenvolvimento."),
               ("Como trabalhamos", "Pesquisamos antes de construir e testamos antes de lançar. No Iara, cada animal, planta e fato foi verificado em uma fonte antes de entrar."),
               ("Privacidade", "Nossos produtos não têm anúncios nem rastreamento, e não pedem conta. O Iara 1.0 não envia nada do seu celular.")],
        contact="Contato", privacy="Privacidade", support="Suporte", rights="© 2026 Studio Topeira",
    ),
    # Spanish (owner, 2026-10-04): the site only. Iara 1.0 itself is in English and Portuguese; Spanish comes to the
    # game with the next version, so the page says so and shows the English screenshots.
    "es": dict(
        lang="es", base="../", en_href="../", br_href="../pt/", es_href="./",
        title="Studio Topeira", desc="Studio Topeira diseña y desarrolla apps y juegos para iPhone. Nuestro primer lanzamiento es Iara: River of Lanterns.",
        nav=[("#iara", "Iara"), ("#rivers", "Ríos"), ("#more", "Próximamente"), ("#studio", "Nosotros"), ("mailto:" + EMAIL, "Contacto")],
        h1="Studio Topeira",
        lead="Diseñamos y desarrollamos apps y juegos para iPhone. Nuestro primer lanzamiento es Iara: River of Lanterns.",
        rivers_kicker="En el juego ahora", rivers_title="Cinco ríos de la Amazonía",
        rivers_lead="Veinticinco niveles en cinco aguas reales, cada una con su color, sus orillas y sus animales.",
        more_kicker="Próximamente", more_title="El viaje continúa",
        more_lead="Después de la Amazonía, la linterna sigue su viaje: seis travesías de 25 ríos cada una, por Brasil y Sudamérica. Cada una es un lugar real, con lo que de verdad vive allí.",
        kicker="Nuestro primer lanzamiento", name="Iara: River of Lanterns",
        p1="Guía una linterna por cinco ríos reales de la Amazonía y llévala a casa, hasta Iara, la guardiana de las aguas en el folclore brasileño.",
        p2="Un toque empuja la linterna. Ranas, caimanes, jaguares y el delfín rosado aparecen cada uno en el río donde realmente viven, y cada río te cuenta algo verdadero sobre él. En el modo Zen el río está a oscuras, nada ataca, y tu luz despierta lo que vive allí.",
        facts=["iPhone", "Gratis", "25 ríos", "Sin anuncios, sin compras", "Sin cuenta", "English · Português", "Español: próximamente"],
        soon="Próximamente en el App Store", get="Consíguelo en el App Store", shots="Capturas de Iara: River of Lanterns",
        about=[("Qué hacemos", "Hacemos apps y juegos para iPhone, cada uno construido en torno a una idea clara. Hay nuevos títulos en desarrollo."),
               ("Cómo trabajamos", "Investigamos antes de construir y probamos antes de publicar. En Iara, cada animal, planta y dato se verificó con una fuente antes de entrar."),
               ("Privacidad", "Nuestros productos no llevan publicidad ni rastreo, y no piden cuenta. Iara 1.0 no envía nada desde tu teléfono.")],
        contact="Contacto", privacy="Privacidad", support="Soporte", rights="© 2026 Studio Topeira",
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


def switch(t):
    """EN | BR | ES at the top right: the language showing is filled, the others are links."""
    sides = [("EN", "English", "en", t["en_href"]), ("BR", "Português (Brasil)", "pt-BR", t["br_href"]), ("ES", "Español", "es", t["es_href"])]
    return ('<span class="switch" role="group" aria-label="Language">'
            + "".join(f'<span class="on" aria-current="true" title="{name}">{label}</span>' if code == t["lang"]
                      else f'<a href="{href}" hreflang="{code}" title="{name}">{label}</a>' for label, name, code, href in sides)
            + "</span>")


def top(t, base, nav=True):
    links = "".join(f'<a href="{h}">{n}</a>' for h, n in t["nav"]) if nav else ""
    return (f'<div class="wrap"><header class="top"><a class="mark" href="{base or "./"}">{MARK}Topeira</a>'
            f'<nav>{links}{switch(t)}</nav></header></div>\n')


def foot(t, base):
    return (f'<div class="wrap"><footer><span>{t["rights"]}</span><span><a href="mailto:{EMAIL}">{EMAIL}</a> &nbsp;·&nbsp; '
            f'<a href="{base}iara/privacy/">{t["privacy"]}</a> &nbsp;·&nbsp; <a href="{base}iara/support/">{t["support"]}</a></span></footer></div>\n</body>\n</html>\n')


# The expansion packs, as a tease (owner, 2026-10-04): a painting, a name, a line and the five waters. No dates, no
# prices, no list of animals. (id, English name, Portuguese name, English line, Portuguese line, the five waters);
# PACKS_ES has each one's Spanish name and line, as the game has them.
PACKS = [
    ("amazonia2", "Amazônia II", "Amazônia II", "The lakes, the rapids, the mud and the sea", "Os lagos, as corredeiras, a lama e o mar",
     "Mamirauá · Xingu · Madeira · Marajó · Rio Branco"),
    ("pantanal", "Pantanal", "Pantanal", "The largest wetland on Earth", "A maior planície alagável do mundo",
     "Rio Paraguai · Rio Cuiabá · Rio Miranda · Baías e corixos · Nhecolândia"),
    ("brasil", "Waters of Brazil", "Águas do Brasil", "From the dry backlands to the great falls", "Do sertão às grandes cataratas",
     "São Francisco · Araguaia · Bonito · Jalapão · Iguaçu"),
    ("orinoco", "The Orinoco and the Guianas", "O Orinoco e as Guianas", "Granite, plains, a river of five colours", "Granito, planícies, um rio de cinco cores",
     "Orinoco · Los Llanos · Caño Cristales · Canaima · Kaieteur"),
    ("andes", "The Andes", "Os Andes", "The high lakes, the sacred river, the way down to the forest", "Os lagos do alto, o rio sagrado, a descida até a floresta",
     "Titicaca · Laguna Colorada · Urubamba · Manu · Magdalena"),
    ("sul", "The South", "O Sul", "From the marshes of Iberá to the glaciers", "Dos esteros do Iberá às geleiras",
     "Iberá · Paraná · Uruguay · Valdivia · Patagonia"),
]

# The five rivers the game has today (owner, 2026-10-04: "the existing biomes and then a coming soon section with the
# new ones"): each one's painting, name and line, as the game has them (RiverLore). (id, {lang: name}, {lang: line})
RIVERS = [
    ("varzea", dict(en="Várzea", pt="Várzea", es="Várzea"),
     dict(en="The forest the river floods every year", pt="A floresta que o rio inunda todo ano", es="La selva que el río inunda cada año")),
    ("negro", dict(en="Rio Negro", pt="Rio Negro", es="Río Negro"),
     dict(en="The river the colour of tea", pt="O rio da cor do chá", es="El río del color del té")),
    ("tapajos", dict(en="Tapajós", pt="Tapajós", es="Tapajós"),
     dict(en="Clear water and white sand", pt="Água clara e areia branca", es="Agua clara y arena blanca")),
    ("igapo", dict(en="Igapó", pt="Igapó", es="Igapó"),
     dict(en="Where the trees stand in the river", pt="Onde as árvores ficam dentro do rio", es="Donde los árboles están de pie en el río")),
    ("encontro", dict(en="Encontro das Águas", pt="Encontro das Águas", es="Encuentro de las Aguas"),
     dict(en="Two rivers that won't mix", pt="Dois rios que não se misturam", es="Dos ríos que no se mezclan")),
]

PACKS_ES = {'amazonia2': ('Amazonía II', 'Los lagos, los rápidos, el barro y el mar'),
            'pantanal': ('Pantanal', 'El humedal más grande del mundo'),
            'brasil': ('Aguas de Brasil', 'Del sertón a las grandes cataratas'),
            'orinoco': ('El Orinoco y las Guayanas', 'Granito, llanos, un río de cinco colores'),
            'andes': ('Los Andes', 'Los lagos de altura, el río sagrado, la bajada a la selva'),
            'sul': ('El Sur', 'De los esteros del Iberá a los glaciares')}


def home(code):
    t = T[code]; base = t["base"]
    cta = f'<a class="cta" href="{STORE}">{t["get"]}</a>' if STORE else f'<span class="cta">{t["soon"]}</span>'
    shot = "en" if code == "es" else code          # no Spanish screenshots until the game ships in Spanish
    shots = "".join(f'<img src="{base}assets/iara-{shot}-{k}.jpg" alt="{t["shots"]} {k}" loading="lazy" width="507" height="1100">' for k in (1, 2, 3, 4))
    about = "".join(f"<div><h3>{h}</h3><p>{p}</p></div>" for h, p in t["about"])
    pt = code == "pt"
    packs = "".join(f'<div class="pack"><img src="{base}assets/packs/{pid}.jpg" alt="" loading="lazy" width="514" height="900">'
                    f'<div class="ptxt"><h3>{PACKS_ES[pid][0] if code == "es" else npt if pt else nen}</h3><p>{PACKS_ES[pid][1] if code == "es" else lpt if pt else len_}</p><p class="waters">{waters}</p></div></div>'
                    for pid, nen, npt, len_, lpt, waters in PACKS)
    facts = "".join(f"<li>{f}</li>" for f in t["facts"])
    rivers = "".join(f'<div class="pack"><img src="{base}assets/rivers/{rid}.jpg" alt="" loading="lazy" width="514" height="900">'
                     f'<div class="ptxt"><h3>{names[code]}</h3><p>{lines[code]}</p></div></div>' for rid, names, lines in RIVERS)
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
<section id="rivers">
  <p class="kicker">{t['rivers_kicker']}</p>
  <h2 class="more">{t['rivers_title']}</h2>
  <p class="morelead">{t['rivers_lead']}</p>
  <div class="packs five">{rivers}</div>
</section>
<section id="more">
  <p class="kicker">{t['more_kicker']}</p>
  <h2 class="more">{t['more_title']}</h2>
  <p class="morelead">{t['more_lead']}</p>
  <div class="packs">{packs}</div>
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
<p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> and, if you can, tell us which iPhone and iOS version you have. We read every message.</p>
<h2>Does the game need an internet connection?</h2>
<p>No. It works fully offline and version 1.0 makes no network calls at all.</p>
<h2>Is there an account, a subscription or anything to buy?</h2>
<p>No. The game is free, with no ads and no purchases.</p>
<h2>How do I delete my data?</h2>
<p>Delete the app. Everything it remembers is stored on your device, so removing the app removes all of it.</p>
<h2>A river feels impossible</h2>
<p>Zen mode has the same rivers with nothing that strikes. If a spot in Play really cannot be passed, please write and tell us which river: that is a bug, and we will fix it.</p>
<h2>How do I change the language?</h2>
<p>In the game's Settings (the gear on the first screen): English or Português.</p>"""


def doc(body, title):
    t = dict(T["en"], base="../../", en_href="./", br_href="../../pt/", es_href="../../es/")
    return head(t, title, "../../") + top(t, "../../", nav=False) + f'<main class="doc">\n{body}\n</main>\n' + foot(t, "../../")


(ROOT / "index.html").write_text(home("en"))
(ROOT / "pt/index.html").write_text(home("pt"))
(ROOT / "es").mkdir(exist_ok=True)
(ROOT / "es/index.html").write_text(home("es"))
(ROOT / "iara/privacy/index.html").write_text(doc(PRIVACY, "Privacy Policy: Iara: River of Lanterns"))
(ROOT / "iara/support/index.html").write_text(doc(SUPPORT, "Support: Iara: River of Lanterns"))
print("written: index.html, pt/index.html, iara/privacy/index.html, iara/support/index.html")

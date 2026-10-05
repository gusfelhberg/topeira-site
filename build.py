#!/usr/bin/env python3
"""build.py: writes the site's pages (English at /, Portuguese at /pt/, Spanish at /es/) from the texts below.
Run it after changing a text: python3 build.py. The output is plain static files; nothing else is needed to host it."""
import pathlib

ROOT = pathlib.Path(__file__).parent
EMAIL = "hello@studiotopeira.com"
STORE_IOS = ""      # Iara's App Store address once it is live there; empty shows "Coming soon"
STORE_ANDROID = ""  # Iara's Google Play address once it is live there; empty shows "Coming soon"

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
       font:700 1.5rem/1.15 "Amatic SC",sans-serif; letter-spacing:.05em; text-decoration:none; text-align:center; }
span.cta { opacity:.75; }
.ctas { display:flex; flex-wrap:wrap; gap:10px; }
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
        title="Studio Topeira", desc="Studio Topeira designs and builds apps and games. Our first release is Iara: River of Lanterns.",
        nav=[("#iara", "Iara"), ("#rivers", "Rivers"), ("#more", "More rivers"), ("#studio", "About"), ("mailto:" + EMAIL, "Contact")],
        h1="Studio Topeira",
        lead="We design and build apps and games. Our first release is Iara: River of Lanterns.",
        rivers_kicker="Free: the first 25 rivers", rivers_title="Five rivers of the Amazon",
        rivers_lead="Twenty-five levels on five real waters, each with its own colour, its own banks and its own animals.",
        more_kicker="More rivers, in the game", more_title="The journey continues",
        more_lead="After the Amazon, the lantern travels on: six journeys of 25 rivers each, across Brazil and South America. Every one a real place, with what really lives there. Each is bought once inside the game, and its first river can be tried free.",
        kicker="Our first release", name="Iara: River of Lanterns",
        p1="Guide a lantern up five real rivers of the Amazon and bring it home to Iara, the keeper of the waters in Brazilian folklore.",
        p2="One tap pushes the lantern. Frogs, caimans, jaguars and the pink river dolphin are each on the river where they really live, and every river tells you something true about it. In Zen the river is dark, nothing strikes, and your light wakes what lives there.",
        p3="The first 25 rivers are free. More rivers are bought once inside the game: Into the night (rivers 26 to 60: Igarapé, Serra and the five rivers by night), six journeys of 25 rivers each, or all 185 more at once. The first river of each can be tried free.",
        facts=["iPhone and Android", "Free to start: 25 rivers", "More rivers, bought once", "No ads, no subscription", "No account", "English · Português · Español"],
        soon="Coming soon to the App Store and Google Play", soon_ios="Coming soon to the App Store", soon_android="Coming soon to Google Play",
        get_ios="Get it on the App Store", get_android="Get it on Google Play", shots="Screenshots of Iara: River of Lanterns",
        about=[("What we do", "We make apps and games, each built around one clear idea. New titles are in development."),
               ("How we work", "We research before we build and test before we release. In Iara, every animal, plant and fact was verified against a source before it went in."),
               ("Privacy", "Our products carry no advertising and no tracking, and need no account. Iara sends nothing from your phone to us.")],
        contact="Contact", privacy="Privacy", support="Support", rights="© 2026 Studio Topeira",
    ),
    "pt": dict(
        lang="pt-BR", base="../", en_href="../", br_href="./", es_href="../es/",
        title="Studio Topeira", desc="O Studio Topeira cria apps e jogos. Nosso primeiro lançamento é Iara: River of Lanterns.",
        nav=[("#iara", "Iara"), ("#rivers", "Rios"), ("#more", "Mais rios"), ("#studio", "Sobre"), ("mailto:" + EMAIL, "Contato")],
        h1="Studio Topeira",
        lead="Criamos apps e jogos. Nosso primeiro lançamento é Iara: River of Lanterns.",
        rivers_kicker="Os 25 primeiros rios são grátis", rivers_title="Cinco rios da Amazônia",
        rivers_lead="Vinte e cinco fases em cinco rios que existem de verdade, cada um com sua cor, suas margens e seus bichos.",
        more_kicker="Mais rios dentro do jogo", more_title="A viagem continua",
        more_lead="Depois da Amazônia, a lanterna segue viagem: são seis jornadas de 25 rios cada, pelo Brasil e pela América do Sul. Todos os lugares existem, e os bichos são os que vivem lá de verdade. Você compra cada jornada uma vez só, dentro do jogo, e dá para experimentar o primeiro rio de graça.",
        kicker="Nosso primeiro lançamento", name="Iara: River of Lanterns",
        p1="Guie uma lanterna por cinco rios reais da Amazônia até Iara, a senhora das águas do folclore brasileiro.",
        p2="Com um toque você empurra a lanterna. Sapos, jacarés, onças e o boto-cor-de-rosa só aparecem nos rios onde vivem de verdade, e cada rio traz uma curiosidade real sobre ele. No modo Zen o rio fica escuro, nada ataca, e a sua luz vai acordando o que vive ali.",
        p3="Os 25 primeiros rios são grátis. Os outros você compra uma vez só, dentro do jogo: Noite adentro (rios 26 a 60: Igarapé, Serra e os cinco rios à noite), seis jornadas de 25 rios cada, ou os outros 185 de uma vez. Dá para experimentar de graça o primeiro rio de cada uma.",
        facts=["iPhone e Android", "Comece grátis: 25 rios", "Mais rios: pague uma vez só", "Sem anúncios, sem assinatura", "Sem cadastro", "English · Português · Español"],
        soon="Em breve na App Store e no Google Play", soon_ios="Em breve na App Store", soon_android="Em breve no Google Play",
        get_ios="Baixar na App Store", get_android="Disponível no Google Play", shots="Telas de Iara: River of Lanterns",
        about=[("O que fazemos", "Fazemos apps e jogos, cada um a partir de uma ideia clara. Temos novos títulos a caminho."),
               ("Como trabalhamos", "Pesquisamos antes de criar e testamos antes de lançar. Em Iara, cada animal, cada planta e cada informação foi conferida em uma fonte antes de entrar no jogo."),
               ("Privacidade", "Nossos produtos não têm anúncios nem rastreamento e não pedem cadastro. Iara não envia para nós nada do seu celular.")],
        contact="Contato", privacy="Privacidade", support="Suporte", rights="© 2026 Studio Topeira",
    ),
    # Spanish (owner, 2026-10-04). The game is in English, Portuguese and Spanish (some of its curiosities are not
    # yet in Spanish, so the page claims no more than the three languages' names). Its screenshots are the game's
    # own pictures with Spanish captions (studio-marketing, iara/store/shots/compose.py).
    "es": dict(
        lang="es", base="../", en_href="../", br_href="../pt/", es_href="./",
        title="Studio Topeira", desc="Studio Topeira crea apps y juegos. Nuestro primer lanzamiento es Iara: River of Lanterns.",
        nav=[("#iara", "Iara"), ("#rivers", "Ríos"), ("#more", "Más ríos"), ("#studio", "Nosotros"), ("mailto:" + EMAIL, "Contacto")],
        h1="Studio Topeira",
        lead="Creamos apps y juegos. Nuestro primer lanzamiento es Iara: River of Lanterns.",
        rivers_kicker="Los primeros 25 ríos son gratis", rivers_title="Cinco ríos de la Amazonía",
        rivers_lead="Veinticinco niveles en cinco ríos que existen de verdad, cada uno con su color, sus orillas y sus animales.",
        more_kicker="Más ríos dentro del juego", more_title="El viaje continúa",
        more_lead="Después de la Amazonía, la linterna sigue su viaje: seis travesías de 25 ríos cada una, por Brasil y el resto de Sudamérica. Todos los lugares existen, y los animales son los que de verdad viven allí. Cada travesía se compra una sola vez, dentro del juego, y su primer río se puede probar gratis.",
        kicker="Nuestro primer lanzamiento", name="Iara: River of Lanterns",
        p1="Guía una linterna por cinco ríos reales de la Amazonía hasta Iara, la señora de las aguas del folclore brasileño.",
        p2="Con un toque empujas la linterna. Ranas, caimanes, jaguares y el delfín rosado solo aparecen en los ríos donde viven de verdad, y cada río te cuenta algo cierto sobre él. En el modo Zen el río está a oscuras, nada ataca y tu luz va despertando lo que vive allí.",
        p3="Los primeros 25 ríos son gratis. Los demás se compran una sola vez, dentro del juego: Hacia la noche (ríos 26 a 60: Igarapé, Serra y los cinco ríos de noche), seis travesías de 25 ríos cada una, o los otros 185 de una vez. El primer río de cada una se puede probar gratis.",
        facts=["iPhone y Android", "Empieza gratis: 25 ríos", "Más ríos: un solo pago", "Sin anuncios ni suscripción", "Sin registro", "English · Português · Español"],
        soon="Próximamente en el App Store y Google Play", soon_ios="Próximamente en el App Store", soon_android="Próximamente en Google Play",
        get_ios="Consíguelo en el App Store", get_android="Disponible en Google Play", shots="Capturas de Iara: River of Lanterns",
        about=[("Qué hacemos", "Hacemos apps y juegos, cada uno a partir de una idea clara. Tenemos nuevos títulos en camino."),
               ("Cómo trabajamos", "Investigamos antes de crear y probamos antes de publicar. En Iara, cada animal, cada planta y cada dato se comprobó con una fuente antes de entrar en el juego."),
               ("Privacidad", "Nuestros productos no llevan publicidad ni rastreo y no piden registro. Iara no nos envía nada desde tu teléfono.")],
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


# The expansion packs (in the game at launch, each bought once inside it): a painting, a name, a line and the five
# waters. No dates, no prices, no list of animals. (id, English name, Portuguese name, English line, Portuguese line, the five waters);
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

# The five rivers of the free game (its first 25 rivers), above the packs: each one's painting, name and line, as the game has them (RiverLore). (id, {lang: name}, {lang: line})
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
    if STORE_IOS or STORE_ANDROID:   # a link for each store the game is live on, "coming soon" for the other
        cta = '<div class="ctas">' + "".join(
            f'<a class="cta" href="{url}">{t["get_" + k]}</a>' if url else f'<span class="cta">{t["soon_" + k]}</span>'
            for k, url in (("ios", STORE_IOS), ("android", STORE_ANDROID))) + "</div>"
    else:
        cta = f'<span class="cta">{t["soon"]}</span>'
    shot = code
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
      <p>{t['p3']}</p>
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
<p><strong>Nothing.</strong> Iara has no account and no sign-up, and never asks for your name, email, location, contacts or any other personal information. The game sends no data to us: everything it records about your play stays on your device.</p>
<p>Test versions of the game (TestFlight) can ask whether you want to share anonymous play statistics. If a later version on the App Store or Google Play includes that, the app will ask first, nothing is sent unless you say yes, and this policy will be updated before it ships.</p>
<h2>What is stored on your device</h2>
<p>Your progress (rivers passed, stars, best scores), your settings and the curiosities you have already seen are kept inside the app's own storage on your device. Deleting the app deletes all of it.</p>
<h2>Purchases</h2>
<p>The first 25 rivers are free. More rivers can be bought inside the game. Purchases are made through Apple's App Store or Google Play, which process the payment: we never receive your payment details. The only thing the game learns, from the store, is that a product is owned, and it keeps that on your device.</p>
<h2>Third parties</h2>
<p>Iara contains no advertising, no analytics and no social networks. On Android the game includes Google's billing library, which needs the internet permission for purchases.</p>
<h2>Children's privacy</h2>
<p>Iara is a general-audience game, not directed at children. It does not ask for or collect anyone's personal information, whatever their age, and has no chat or user-generated content.</p>
<h2>Tracking</h2>
<p>None. Iara does not use the advertising identifier (IDFA) and does not track you across other apps or websites.</p>
<h2>Changes to this policy</h2>
<p>If this policy changes, the effective date above is updated and the new version is posted at this address.</p>
<h2>Contact</h2>
<p>Questions about this policy or the app: <a href="mailto:{EMAIL}">{EMAIL}</a></p>"""

SUPPORT = f"""<h1>Support: Iara: River of Lanterns</h1>
<p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> and, if you can, tell us which phone you have and its system version. We read every message.</p>
<h2>Does the game need an internet connection?</h2>
<p>Not to play: it works fully offline. A connection is needed only to buy more rivers or to restore a purchase.</p>
<h2>Is the game free?</h2>
<p>It is free to start: the first 25 rivers are free. There are no ads, no subscription and no account.</p>
<h2>What can I buy?</h2>
<p>More rivers: Into the night (rivers 26 to 60), six journeys of 25 rivers each, or all of them at once. Each is bought once, inside the game, and is yours to keep. You can try the first river of each before buying.</p>
<h2>How do I get my purchases back on a new phone?</h2>
<p>Open the game's Settings and choose "Restore purchases". A purchase belongs to the Apple or Google account it was made with, and does not carry between iPhone and Android.</p>
<h2>Can I get a refund?</h2>
<p>Refunds are handled by Apple or Google, whichever store the purchase was made in. Ask through that store.</p>
<h2>How do I delete my data?</h2>
<p>Delete the app. Everything it remembers is stored on your device, so removing the app removes all of it. Purchases stay with your Apple or Google account and can be restored.</p>
<h2>A river feels impossible</h2>
<p>Zen mode has the same rivers with nothing that strikes. If a spot in Play really cannot be passed, please write and tell us which river: that is a bug, and we will fix it.</p>
<h2>How do I change the language?</h2>
<p>In the game's Settings (the gear on the first screen): English, Português or Español.</p>"""


def doc(body, title):
    t = dict(T["en"], base="../../", en_href="./", br_href="../../pt/", es_href="../../es/")
    return head(t, title, "../../") + top(t, "../../", nav=False) + f'<main class="doc">\n{body}\n</main>\n' + foot(t, "../../")


(ROOT / "index.html").write_text(home("en"))
(ROOT / "pt/index.html").write_text(home("pt"))
(ROOT / "es").mkdir(exist_ok=True)
(ROOT / "es/index.html").write_text(home("es"))
(ROOT / "iara/privacy/index.html").write_text(doc(PRIVACY, "Privacy Policy: Iara: River of Lanterns"))
(ROOT / "iara/support/index.html").write_text(doc(SUPPORT, "Support: Iara: River of Lanterns"))
print("written: index.html, pt/index.html, es/index.html, iara/privacy/index.html, iara/support/index.html")

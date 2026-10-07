#!/usr/bin/env python3
"""Generates the trilingual author site into the repo given as argv[1]."""
import sys, os, html

ROOT = sys.argv[1]
SITE = "https://www.dannybluejet.com"
LANGS = ["es", "en", "ja"]
PREFIX = {"es": "/", "en": "/en/", "ja": "/ja/"}
LANG_LABEL = {"es": "ES", "en": "EN", "ja": "日本語"}
EMAIL = "arosteguy.daniel@gmail.com"

SOCIAL = [
    ("X", "https://x.com/Dannybluejet1"),
    ("Instagram", "https://www.instagram.com/danny_blue_jet"),
    ("TikTok", "https://www.tiktok.com/@danny_blue_jet"),
    ("BoardGameGeek", "https://boardgamegeek.com/boardgamedesigner/176762/daniel-arosteguy"),
]

NAV = {
    "es": [("index.html", "Inicio"), ("sobre-mi.html", "Sobre mí"), ("juegos/", "Juegos"), ("musica.html", "Música"), ("contacto.html", "Contacto")],
    "en": [("index.html", "Home"), ("sobre-mi.html", "About"), ("juegos/", "Games"), ("musica.html", "Music"), ("contacto.html", "Contact")],
    "ja": [("index.html", "ホーム"), ("sobre-mi.html", "プロフィール"), ("juegos/", "ゲーム"), ("musica.html", "音楽"), ("contacto.html", "お問い合わせ")],
}

T = {
    "es": dict(
        tagline="Diseñador de juegos de mesa y músico",
        menu="Menú", privacy="Privacidad", rights="Todos los derechos reservados.",
        see_game="Ver el juego", bgg="Ver en BoardGameGeek", more_games="Todos mis juegos",
        my_games="Mis juegos", other_games="Otros trabajos", listen="Escuchar mi música",
        music="Música", read_bio="Leer mi bio", contact="Contacto", write_me="Escríbeme",
        role="Rol", publisher="Editorial", players="Jugadores", age="Edad", duration="Duración", designer="Diseño", series="Serie",
        credits="Créditos", links="Enlaces", back="← Todos los juegos",
        featured="Destacado", play_video="Reproducir video",
        music_cta="Canciones, videos y shows en vivo.",
    ),
    "en": dict(
        tagline="Board game designer and musician",
        menu="Menu", privacy="Privacy", rights="All rights reserved.",
        see_game="See the game", bgg="View on BoardGameGeek", more_games="All my games",
        my_games="My games", other_games="Other works", listen="Listen to my music",
        music="Music", read_bio="Read my bio", contact="Contact", write_me="Write to me",
        role="Role", publisher="Publisher", players="Players", age="Age", duration="Playing time", designer="Designer", series="Series",
        credits="Credits", links="Links", back="← All games",
        featured="Featured", play_video="Play video",
        music_cta="Songs, videos and live shows.",
    ),
    "ja": dict(
        tagline="ボードゲームデザイナー・ミュージシャン",
        menu="メニュー", privacy="プライバシー", rights="All rights reserved.",
        see_game="作品を見る", bgg="BoardGameGeekで見る", more_games="すべての作品",
        my_games="作品", other_games="その他の作品", listen="音楽を聴く",
        music="音楽", read_bio="プロフィールを読む", contact="お問い合わせ", write_me="メールを送る",
        role="担当", publisher="出版社", players="プレイ人数", age="対象年齢", duration="プレイ時間", designer="デザイン", series="シリーズ",
        credits="クレジット", links="リンク", back="← 作品一覧",
        featured="注目作", play_video="動画を再生",
        music_cta="楽曲、ミュージックビデオ、ライブ。",
    ),
}

BIO_SHORT = {
    "es": "Danny Blue Jet (Daniel Arosteguy) es diseñador de juegos de mesa y músico chileno. Es co-diseñador de <em>My Extreme Skatepark</em> junto a Naotaka Shimamoto, publicado por itten, y fundador de la editorial La Vaca del Tablero.",
    "en": "Danny Blue Jet (Daniel Arosteguy) is a Chilean board game designer and musician. He co-designed <em>My Extreme Skatepark</em> with Naotaka Shimamoto, published by itten, and founded the publisher La Vaca del Tablero.",
    "ja": "Danny Blue Jet（ダニエル・アロステギ）は、チリ出身のボードゲームデザイナー・ミュージシャンです。Naotaka Shimamoto氏との共同デザイン作品『My Extreme Skatepark』（itten）を手がけ、出版レーベル「La Vaca del Tablero」を主宰しています。",
}

BIO_LONG = {
    "es": [
        "Danny Blue Jet es el nombre artístico de Daniel Arosteguy, diseñador de juegos de mesa, músico y docente chileno.",
        "Fundó la editorial independiente La Vaca del Tablero, con la que autopublicó <em>Armaduras Musicales</em>, un juego para aprender teoría musical, y editó <em>Batalla de Coronas</em>. Diseñó <em>De Cero a CEO</em>, un juego creado para la carrera de Ingeniería Comercial de la Universidad de Los Lagos.",
        "En 2026 debuta internacionalmente con <em>My Extreme Skatepark</em>, co-diseñado con el autor japonés Naotaka Shimamoto y publicado por itten, que se presenta en SPIEL Essen 2026.",
        "Trabaja en la ludoteca de un colegio, donde usa el juego como herramienta de aprendizaje, y compone y toca su propia música.",
    ],
    "en": [
        "Danny Blue Jet is the artist name of Daniel Arosteguy, a Chilean board game designer, musician and teacher.",
        "He founded the independent publisher La Vaca del Tablero, through which he self-published <em>Armaduras Musicales</em>, a game for learning music theory, and edited <em>Batalla de Coronas</em>. He designed <em>De Cero a CEO</em>, a game created for the business administration program at Universidad de Los Lagos.",
        "In 2026 he makes his international debut with <em>My Extreme Skatepark</em>, co-designed with Japanese designer Naotaka Shimamoto and published by itten, premiering at SPIEL Essen 2026.",
        "He runs a school game library, where he uses play as a learning tool, and writes and performs his own music.",
    ],
    "ja": [
        "Danny Blue Jet は、チリのボードゲームデザイナー、ミュージシャン、教育者であるダニエル・アロステギのアーティスト名です。",
        "インディー出版レーベル「La Vaca del Tablero」を設立し、音楽理論を学べるゲーム『Armaduras Musicales』を自主出版、『Batalla de Coronas』の編集を担当しました。ロス・ラゴス大学の経営学科向けに『De Cero a CEO』をデザインしています。",
        "2026年、日本のデザイナーNaotaka Shimamoto氏との共同デザイン作品『My Extreme Skatepark』（itten）で国際デビューし、SPIEL Essen 2026 で初披露されます。",
        "学校のボードゲームライブラリーを担当し、遊びを学びの道具として活用するほか、自身の音楽の作曲・演奏も行っています。",
    ],
}

# ---------------------------------------------------------------- games
GAMES = [
    dict(
        slug="my-extreme-skatepark", title="My Extreme Skatepark", bgg=479479, featured=True,
        cover="/images/mes.webp", card_cover="/images/mes-card.webp", cover_class="cover-mes",
        alt_title="マイ エクストリーム スケートパーク", series="itten Funbrick Series",
        role={"es": "Co-diseño con Naotaka Shimamoto", "en": "Co-designed with Naotaka Shimamoto", "ja": "Naotaka Shimamoto氏との共同デザイン"},
        publisher="itten (Japón)", publisher_i18n={"en": "itten (Japan)", "ja": "itten（日本）"},
        teaser={
            "es": "Un juego de mesa sobre el mundo del skate, creado entre Chile y Japón. Debuta en SPIEL Essen 2026.",
            "en": "A board game about the world of skateboarding, created between Chile and Japan. Premiering at SPIEL Essen 2026.",
            "ja": "チリと日本のコラボレーションから生まれた、スケートボードの世界をテーマにしたボードゲーム。SPIEL Essen 2026 でデビュー。",
        },
    ),
    dict(
        slug="armaduras-musicales", title="Armaduras Musicales", bgg=476924,
        cover="/images/armaduras-musicales.webp", cover_class="cover-armaduras",
        role={"es": "Diseño · La Vaca del Tablero", "en": "Design · La Vaca del Tablero", "ja": "デザイン・La Vaca del Tablero"},
        publisher="La Vaca del Tablero",
        teaser={
            "es": "Un juego para aprender teoría musical jugando.",
            "en": "A game for learning music theory through play.",
            "ja": "遊びながら音楽理論を学べるゲーム。",
        },
        body={
            "es": ["<em>Armaduras Musicales</em> es un juego para aprender teoría musical jugando. Lo diseñé y lo autopubliqué con La Vaca del Tablero, uniendo mis dos mundos: la música y los juegos de mesa."],
            "en": ["<em>Armaduras Musicales</em> (“Key Signatures”) is a game for learning music theory through play. I designed it and self-published it with La Vaca del Tablero, bringing together my two worlds: music and board games."],
            "ja": ["『Armaduras Musicales』（調号）は、遊びながら音楽理論を学べるゲームです。音楽とボードゲームという2つの世界をつなぐ作品として、La Vaca del Tablero から自主出版しました。"],
        },
    ),
    dict(
        slug="batalla-de-coronas", title="Batalla de Coronas", bgg=421255,
        cover="/images/batalla-de-coronas.webp", cover_class="cover-batalla", designer="Pedro Guajardo Cordescu",
        role={"es": "Edición · La Vaca del Tablero", "en": "Editing · La Vaca del Tablero", "ja": "編集・La Vaca del Tablero"},
        publisher="La Vaca del Tablero", players="2", age="10+", duration="20–45 min",
        teaser={
            "es": "Enfrentamientos tácticos y partidas rápidas.",
            "en": "Tactical clashes and quick games.",
            "ja": "戦術的な対決が楽しめる、短時間で遊べるゲーム。",
        },
        body={
            "es": ["<em>Batalla de Coronas</em> es un juego de enfrentamientos tácticos y partidas rápidas que combina estrategia, sorpresa y diversión para grupos de amigos y familia. Es un diseño de Pedro Guajardo Cordescu, que edité y publiqué con La Vaca del Tablero."],
            "en": ["<em>Batalla de Coronas</em> (“Battle of Crowns”) is a game of tactical clashes and quick rounds that mixes strategy, surprise and fun for friends and family. It was designed by Pedro Guajardo Cordescu; I edited and published it with La Vaca del Tablero."],
            "ja": ["『Batalla de Coronas』（王冠の戦い）は、戦略とサプライズが詰まった、友人や家族と短時間で楽しめる対戦ゲームです。デザインは Pedro Guajardo Cordescu 氏。La Vaca del Tablero で編集・出版を担当しました。"],
        },
    ),
    dict(
        slug="de-cero-a-ceo", title="De Cero a CEO", bgg=476764,
        cover="/images/de-cero-a-ceo.webp", cover_class="cover-ceo",
        role={"es": "Diseño", "en": "Design", "ja": "デザイン"},
        publisher="La Vaca del Tablero · Universidad de Los Lagos",
        teaser={
            "es": "Un juego para la carrera de Ingeniería Comercial de la Universidad de Los Lagos.",
            "en": "A game for the business administration program at Universidad de Los Lagos.",
            "ja": "ロス・ラゴス大学 経営学科のためのゲーム。",
        },
        body={
            "es": ["<em>De Cero a CEO</em> es un juego que diseñé para la carrera de Ingeniería Comercial de la Universidad de Los Lagos, para aprender gestión de empresas jugando."],
            "en": ["<em>De Cero a CEO</em> (“From Zero to CEO”) is a game I designed for the business administration program at Universidad de Los Lagos, to learn how companies are run through play."],
            "ja": ["『De Cero a CEO』（ゼロからCEOへ）は、ロス・ラゴス大学の経営学科のためにデザインした、遊びながら企業経営を学べるゲームです。"],
        },
    ),
]
GAME = {g["slug"]: g for g in GAMES}

MES_BODY = {
    "es": dict(
        lead="Un juego de mesa sobre el mundo del skate, creado a cuatro manos entre Chile y Japón.",
        about_h="Sobre el juego",
        about=[
            "<em>My Extreme Skatepark</em> es mi primer juego publicado internacionalmente. Lo co-diseñé con Naotaka Shimamoto, diseñador japonés y director de itten, la editorial que lo publica.",
            "Es una colaboración entre dos autores separados por el océano Pacífico, unidos por los juegos de mesa y la cultura del skate.",
        ],
        spiel_h="SPIEL Essen 2026",
        spiel="El juego debuta en SPIEL Essen 2026 (Essen, Alemania), la feria de juegos de mesa más grande del mundo. Búscalo con itten.",
        design="Diseño", press_h="Prensa y contacto",
        press="¿Quieres escribir sobre el juego, entrevistarnos o recibir imágenes? Escríbeme y te envío el material.",
    ),
    "en": dict(
        lead="A board game about the world of skateboarding, created by two designers from Chile and Japan.",
        about_h="About the game",
        about=[
            "<em>My Extreme Skatepark</em> is my first internationally published game. I co-designed it with Naotaka Shimamoto, Japanese game designer and head of itten, the publisher behind it.",
            "It is a collaboration between two designers on opposite sides of the Pacific, brought together by board games and skate culture.",
        ],
        spiel_h="SPIEL Essen 2026",
        spiel="The game premieres at SPIEL Essen 2026 (Essen, Germany), the world's largest board game fair. Look for it with itten.",
        design="Design", press_h="Press and contact",
        press="Want to write about the game, interview us or get images? Write to me and I will send you the materials.",
    ),
    "ja": dict(
        lead="チリと日本、2人のデザイナーが共同で生み出した、スケートボードの世界をテーマにしたボードゲーム。",
        about_h="ゲームについて",
        about=[
            "『My Extreme Skatepark』は、私にとって初めて海外で出版される作品です。日本のゲームデザイナーであり、出版元 itten の代表である Naotaka Shimamoto氏と共同でデザインしました。",
            "太平洋をはさんだ2人のデザイナーが、ボードゲームとスケートカルチャーでつながったコラボレーションです。",
        ],
        spiel_h="SPIEL Essen 2026",
        spiel="本作は世界最大のボードゲーム見本市、SPIEL Essen 2026（ドイツ・エッセン）でデビューします。itten のブースでぜひご覧ください。",
        design="デザイン", press_h="取材・お問い合わせ",
        press="記事掲載、インタビュー、画像素材のご希望はメールでご連絡ください。資料をお送りします。",
    ),
}

PAGE_TITLES = {
    "index.html": {"es": "Danny Blue Jet — Diseñador de juegos de mesa y músico", "en": "Danny Blue Jet — Board game designer and musician", "ja": "Danny Blue Jet — ボードゲームデザイナー・ミュージシャン"},
    "sobre-mi.html": {"es": "Sobre mí", "en": "About", "ja": "プロフィール"},
    "juegos/index.html": {"es": "Mis juegos", "en": "My games", "ja": "作品"},
    "la-vaca-del-tablero.html": {"es": "La Vaca del Tablero", "en": "La Vaca del Tablero", "ja": "La Vaca del Tablero"},
    "musica.html": {"es": "Música", "en": "Music", "ja": "音楽"},
    "contacto.html": {"es": "Contacto", "en": "Contact", "ja": "お問い合わせ"},
}

SPOTIFY = ["7K8FFh7pG2NeeUo51Govqx", "74K276v26BlH9OAl68Unel"]
YOUTUBE = ["3RhNDPlTqJ4", "I0PjK36jQN8"]

# ---------------------------------------------------------------- template
HEAD_TRACKING = """  <script defer src="/js/trackers.js"></script>
  <meta name="google-site-verification" content="32R62jSZCi8ZxbzMsThoZt71xNq80s7BPerJKDpj3x8">
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-SEK1KR9XGS"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-SEK1KR9XGS');
  </script>
  <!-- Meta Pixel (second pixel that was inline before; trackers.js loads 3627643840689292) -->
  <script>
    !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
    n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
    n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
    t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
    document,'script','https://connect.facebook.net/en_US/fbevents.js');
    fbq('init', '951894654288792');
    fbq('track', 'PageView');
  </script>"""


def url(lang, path):
    p = PREFIX[lang] + path
    return p[: -len("index.html")] if p.endswith("index.html") else p


def esc(s):
    return html.escape(s, quote=True)


def page(lang, path, title, description, body, active=None, og_image="/images/danny-og.jpg", langs=LANGS):
    t = T[lang]
    full_title = title if title.startswith("Danny Blue Jet") else f"{title} — Danny Blue Jet"
    alternates = "\n".join(
        f'  <link rel="alternate" hreflang="{l}" href="{SITE}{url(l, path)}">' for l in langs
    )
    if "es" in langs:
        alternates += f'\n  <link rel="alternate" hreflang="x-default" href="{SITE}{url("es", path)}">'
    jp_font = "&family=Noto+Sans+JP:wght@400;700;900" if lang == "ja" else ""
    nav = "\n".join(
        f'        <li><a href="{url(lang, href)}"{" aria-current=\"page\"" if href == active else ""}>{label}</a></li>'
        for href, label in NAV[lang]
    )
    switch = " ".join(
        (f'<a href="{url(l, path)}" lang="{l}" hreflang="{l}"' + (' aria-current="true"' if l == lang else "") + f">{LANG_LABEL[l]}</a>")
        for l in langs
    )
    social = "\n".join(
        f'        <a href="{u}" target="_blank" rel="noopener noreferrer">{n}</a>' for n, u in SOCIAL
    )
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(full_title)}</title>
  <meta name="description" content="{esc(description)}">
  <link rel="canonical" href="{SITE}{url(lang, path)}">
{alternates}
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Danny Blue Jet">
  <meta property="og:title" content="{esc(full_title)}">
  <meta property="og:description" content="{esc(description)}">
  <meta property="og:url" content="{SITE}{url(lang, path)}">
  <meta property="og:image" content="{SITE}{og_image}">
  <meta property="og:locale" content="{ {'es': 'es_CL', 'en': 'en_US', 'ja': 'ja_JP'}[lang] }">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@Dannybluejet1">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🗻</text></svg>">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800{jp_font}&display=swap">
  <link rel="stylesheet" href="/css/site.css">
{HEAD_TRACKING}
</head>
<body>
  <header class="site-header">
    <nav class="nav" aria-label="{t['menu']}">
      <a href="{url(lang, 'index.html')}" class="nav-logo"><span aria-hidden="true">🗻</span> Danny Blue Jet</a>
      <button class="nav-toggle" aria-label="{t['menu']}" aria-expanded="false" aria-controls="nav-links">
        <span></span><span></span><span></span>
      </button>
      <ul class="nav-links" id="nav-links">
{nav}
      </ul>
      <div class="lang-switch">{switch}</div>
    </nav>
  </header>

  <main>
{body}
  </main>

  <footer class="site-footer">
    <div class="wrap footer-inner">
      <div>
        <p class="footer-name"><span aria-hidden="true">🗻</span> Danny Blue Jet</p>
        <p class="footer-tag">{t['tagline']}</p>
        <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
      <div class="footer-social">
{social}
      </div>
    </div>
    <p class="footer-bottom">© 2026 Danny Blue Jet / Daniel Arosteguy. {t['rights']} · <a href="/privacidad.html">{t['privacy']}</a></p>
  </footer>

  <script src="/js/site.js" defer></script>
</body>
</html>
"""


def cover(g, big=False):
    src = g["cover"] if big else g.get("card_cover", g.get("cover"))
    if src:
        return f'<img class="cover-img{" big" if big else ""}" src="{src}" alt="{esc(g["title"])}" loading="lazy">'
    # Placeholder cover until a real image exists in /images/ (see README).
    return f'<div class="cover-art {g["cover_class"]}{" big" if big else ""}" role="img" aria-label="{esc(g["title"])}"><span>{esc(g["title"])}</span></div>'


def game_card(lang, g):
    return f"""        <a class="game-card" href="{url(lang, 'juegos/' + g['slug'] + '.html')}">
          <div class="game-card-cover">{cover(g)}</div>
          <div class="game-card-body">
            <h3>{esc(g['title'])}</h3>
            <p class="game-role">{g['role'][lang]}</p>
            <p>{g['teaser'][lang]}</p>
          </div>
        </a>"""


def mes_feature(lang):
    g, t = GAME["my-extreme-skatepark"], T[lang]
    return f"""    <section class="feature">
      <div class="wrap feature-inner">
        <div class="feature-cover">{cover(g, big=True)}</div>
        <div class="feature-text">
          <p class="eyebrow">{t['featured']} · SPIEL Essen 2026</p>
          <h2>My Extreme Skatepark</h2>
          <p class="feature-credits">{g['role'][lang]} · itten</p>
          <p>{g['teaser'][lang]}</p>
          <div class="btn-row">
            <a class="btn btn-light" href="{url(lang, 'juegos/my-extreme-skatepark.html')}">{t['see_game']}</a>
            <a class="btn btn-ghost" href="https://boardgamegeek.com/boardgame/{g['bgg']}" target="_blank" rel="noopener noreferrer">BoardGameGeek</a>
          </div>
        </div>
      </div>
    </section>"""


def home(lang):
    t = T[lang]
    others = "\n".join(game_card(lang, g) for g in GAMES if not g.get("featured"))
    body = f"""    <section class="hero">
      <div class="wrap hero-inner">
        <div class="hero-text">
          <p class="eyebrow">{t['tagline']}</p>
          <h1>Danny Blue Jet <span aria-hidden="true">🗻</span></h1>
          <p class="hero-bio">{BIO_SHORT[lang]}</p>
          <div class="btn-row">
            <a class="btn" href="{url(lang, 'sobre-mi.html')}">{t['read_bio']}</a>
            <a class="btn btn-outline" href="{url(lang, 'juegos/')}">{t['my_games']}</a>
          </div>
        </div>
        <img class="hero-photo" src="/images/danny.webp" alt="Danny Blue Jet" width="600" height="800">
      </div>
    </section>

{mes_feature(lang)}

    <section class="section">
      <div class="wrap">
        <h2 class="section-title">{t['other_games']}</h2>
        <div class="game-grid">
{others}
        </div>
        <p class="center"><a class="link-arrow" href="{url(lang, 'juegos/')}">{t['more_games']} →</a></p>
      </div>
    </section>

    <section class="music-band">
      <video class="music-band-video" autoplay muted loop playsinline preload="none" aria-hidden="true">
        <source src="/volver_a_marte_clip.mp4" type="video/mp4">
      </video>
      <div class="wrap music-band-inner">
        <h2>{t['music']}</h2>
        <p>{t['music_cta']}</p>
        <a class="btn btn-light" href="{url(lang, 'musica.html')}">{t['listen']}</a>
      </div>
    </section>
"""
    return page(lang, "index.html", PAGE_TITLES["index.html"][lang], strip(BIO_SHORT[lang]), body, active="index.html")


def strip(s):
    import re
    return re.sub(r"<[^>]+>", "", s)


ABOUT_FACETS = {
    "es": [("🎲", "Diseñador y editor", "Juegos propios, colaboraciones internacionales y la editorial La Vaca del Tablero."),
           ("🎸", "Músico", "Compongo y toco mis canciones como Danny Blue Jet."),
           ("🏫", "Docente", "Trabajo en la ludoteca de un colegio, usando el juego para aprender.")],
    "en": [("🎲", "Designer and publisher", "My own games, international collaborations and the publisher La Vaca del Tablero."),
           ("🎸", "Musician", "I write and play my own songs as Danny Blue Jet."),
           ("🏫", "Teacher", "I run a school game library, using play as a way to learn.")],
    "ja": [("🎲", "デザイナー・出版", "オリジナル作品、海外とのコラボレーション、出版レーベル La Vaca del Tablero。"),
           ("🎸", "ミュージシャン", "Danny Blue Jet として作詞作曲・演奏をしています。"),
           ("🏫", "教育者", "学校のボードゲームライブラリーで、遊びを通した学びを実践しています。")],
}


def about(lang):
    t = T[lang]
    paras = "\n".join(f"          <p>{p}</p>" for p in BIO_LONG[lang])
    facets = "\n".join(
        f'        <div class="facet"><span class="facet-icon" aria-hidden="true">{i}</span><h3>{h}</h3><p>{p}</p></div>'
        for i, h, p in ABOUT_FACETS[lang]
    )
    works = "\n".join(
        f'            <li><a href="{url(lang, "juegos/" + g["slug"] + ".html")}">{esc(g["title"])}</a> — {g["role"][lang]}</li>'
        for g in GAMES
    )
    h = {"es": "Sobre mí", "en": "About me", "ja": "プロフィール"}[lang]
    wh = {"es": "Trabajos", "en": "Works", "ja": "作品"}[lang]
    body = f"""    <section class="section">
      <div class="wrap about">
        <img class="about-photo" src="/images/danny.webp" alt="Danny Blue Jet" width="600" height="800">
        <div class="prose">
          <h1>{h}</h1>
{paras}
          <h2>{wh}</h2>
          <ul>
{works}
            <li><a href="{url(lang, 'la-vaca-del-tablero.html')}">La Vaca del Tablero</a></li>
          </ul>
        </div>
      </div>
    </section>
    <section class="section section-alt">
      <div class="wrap facets">
{facets}
      </div>
    </section>
"""
    return page(lang, "sobre-mi.html", PAGE_TITLES["sobre-mi.html"][lang], strip(BIO_LONG[lang][0]), body, active="sobre-mi.html")


def games_index(lang):
    t = T[lang]
    cards = "\n".join(game_card(lang, g) for g in GAMES)
    intro = {
        "es": "Juegos que he diseñado, co-diseñado o editado.",
        "en": "Games I have designed, co-designed or edited.",
        "ja": "デザイン・共同デザイン・編集を手がけた作品です。",
    }[lang]
    body = f"""    <section class="page-head">
      <div class="wrap">
        <h1>{t['my_games']}</h1>
        <p>{intro}</p>
      </div>
    </section>

{mes_feature(lang)}

    <section class="section">
      <div class="wrap">
        <div class="game-grid">
{cards}
        </div>
      </div>
    </section>
"""
    return page(lang, "juegos/index.html", PAGE_TITLES["juegos/index.html"][lang], intro, body, active="juegos/")


def game_page(lang, g):
    t = T[lang]
    facts = [(t["role"], g["role"][lang]), (t["publisher"], g.get("publisher_i18n", {}).get(lang, g["publisher"]))]
    if g.get("designer"):
        facts.insert(0, (t["designer"], g["designer"]))
    if g.get("series"):
        facts.append((t["series"], g["series"]))
    if g.get("players"):
        facts.append((t["players"], g["players"]))
    if g.get("age"):
        facts.append((t["age"], g["age"]))
    if g.get("duration"):
        facts.append((t["duration"], g["duration"]))
    facts_html = "\n".join(f"            <div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in facts)
    links = [(t["bgg"], f"https://boardgamegeek.com/boardgame/{g['bgg']}")]
    if g["slug"] == "my-extreme-skatepark":
        b = MES_BODY[lang]
        links += [("itten", "https://itten-games.com/"), ("Naotaka Shimamoto (X)", "https://x.com/shimamotonao")]
        main = f"""          <p class="lead">{b['lead']}</p>
          <h2>{b['about_h']}</h2>
{chr(10).join(f'          <p>{p}</p>' for p in b['about'])}
          <h2>{b['spiel_h']}</h2>
          <p>{b['spiel']}</p>
          <h2>{t['credits']}</h2>
          <ul>
            <li>{b['design']}: Daniel Arosteguy Pino (Danny Blue Jet), Naotaka Shimamoto</li>
            <li>{t['publisher']}: itten</li>
          </ul>
          <!-- TODO: agregar galería de fotos y video de partida cuando estén disponibles (images/mes-*.jpg) -->
          <h2>{b['press_h']}</h2>
          <p>{b['press']}</p>
          <p><a class="btn" href="mailto:{EMAIL}?subject=My%20Extreme%20Skatepark">{t['write_me']}</a></p>"""
        desc = strip(b["lead"])
    else:
        if g["publisher"] == "La Vaca del Tablero":
            links.append(("La Vaca del Tablero", url(lang, "la-vaca-del-tablero.html")))
        main = "\n".join(f"          <p>{p}</p>" for p in g["body"][lang])
        main += "\n          <!-- TODO: agregar fotos, duración de partida y la historia de cómo nació el juego -->"
        desc = strip(g["teaser"][lang])
    links_html = "\n".join(
        f'            <li><a href="{u}"' + (' target="_blank" rel="noopener noreferrer"' if u.startswith("http") else "") + f">{n}</a></li>"
        for n, u in links
    )
    body = f"""    <section class="game-hero{' game-hero-mes' if g.get('featured') else ''}">
      <div class="wrap game-hero-inner">
        <div class="game-hero-cover">{cover(g, big=True)}</div>
        <div>
          <a class="back" href="{url(lang, 'juegos/')}">{t['back']}</a>
          {"<p class='eyebrow'>SPIEL Essen 2026</p>" if g.get('featured') else ''}
          <h1>{esc(g['title'])}</h1>
          {f'<p class="alt-title" lang="ja">{g["alt_title"]}</p>' if lang == "ja" and g.get("alt_title") else ""}
          <dl class="facts">
{facts_html}
          </dl>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="wrap game-body">
        <div class="prose">
{main}
        </div>
        <aside class="side">
          <h2>{t['links']}</h2>
          <ul>
{links_html}
          </ul>
        </aside>
      </div>
    </section>
"""
    return page(lang, f"juegos/{g['slug']}.html", g["title"], desc, body, active="juegos/")


def vaca(lang):
    text = {
        "es": ("La Vaca del Tablero es la editorial independiente de juegos de mesa que fundé en Chile. Con ella autopubliqué <em>Armaduras Musicales</em> y edité <em>Batalla de Coronas</em>.",
               "¿Eres tienda, distribuidor o quieres proponer un juego? Escríbeme."),
        "en": ("La Vaca del Tablero is the independent board game publisher I founded in Chile. Through it I self-published <em>Armaduras Musicales</em> and edited <em>Batalla de Coronas</em>.",
               "Are you a store or distributor, or want to pitch a game? Write to me."),
        "ja": ("La Vaca del Tablero は、私がチリで設立したインディーのボードゲーム出版レーベルです。『Armaduras Musicales』を自主出版し、『Batalla de Coronas』の編集を担当しました。",
               "販売店・流通関係の方、ゲームの持ち込みをご希望の方はメールでご連絡ください。"),
    }[lang]
    cat = {"es": "Catálogo", "en": "Catalog", "ja": "カタログ"}[lang]
    cards = "\n".join(game_card(lang, GAME[s]) for s in ["armaduras-musicales", "batalla-de-coronas"])
    body = f"""    <section class="page-head">
      <div class="wrap prose">
        <h1>La Vaca del Tablero</h1>
        <p>{text[0]}</p>
      </div>
    </section>
    <section class="section">
      <div class="wrap">
        <h2 class="section-title">{cat}</h2>
        <div class="game-grid">
{cards}
        </div>
        <p class="center">{text[1]} <a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
    </section>
"""
    return page(lang, "la-vaca-del-tablero.html", "La Vaca del Tablero", strip(text[0]), body, active="juegos/")


def music(lang):
    t = T[lang]
    h = {"es": ("Canciones", "Videos"), "en": ("Songs", "Videos"), "ja": ("楽曲", "ミュージックビデオ")}[lang]
    intro = {
        "es": "Compongo y toco mis propias canciones. Aquí puedes escucharlas y ver mis videos.",
        "en": "I write and play my own songs. Listen to them and watch my videos here.",
        "ja": "オリジナル曲の作詞作曲・演奏をしています。楽曲とミュージックビデオはこちら。",
    }[lang]
    tracks = "\n".join(
        f'          <iframe class="spotify" src="https://open.spotify.com/embed/track/{s}?utm_source=generator" height="152" '
        f'allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy" title="Spotify"></iframe>'
        for s in SPOTIFY
    )
    vids = "\n".join(
        f'          <button class="yt" data-id="{v}" aria-label="{t["play_video"]}" style="background-image:url(https://i.ytimg.com/vi/{v}/hqdefault.jpg)"><span class="yt-play" aria-hidden="true"></span></button>'
        for v in YOUTUBE
    )
    body = f"""    <section class="music-band music-hero">
      <video class="music-band-video" autoplay muted loop playsinline aria-hidden="true">
        <source src="/volver_a_marte_clip.mp4" type="video/mp4">
      </video>
      <div class="wrap music-band-inner">
        <h1>{t['music']}</h1>
        <p>{intro}</p>
      </div>
    </section>
    <section class="section">
      <div class="wrap music-grid">
        <div>
          <h2 class="section-title">{h[0]}</h2>
{tracks}
        </div>
        <div>
          <h2 class="section-title">{h[1]}</h2>
          <div class="yt-grid">
{vids}
          </div>
        </div>
      </div>
    </section>
    <!-- Próximos shows: agrega aquí una sección cuando haya fechas. -->
"""
    return page(lang, "musica.html", PAGE_TITLES["musica.html"][lang], intro, body, active="musica.html")


def contact(lang):
    t = T[lang]
    intro = {
        "es": "Para prensa, colaboraciones, editoriales, shows o talleres de juegos, escríbeme.",
        "en": "For press, collaborations, publishers, shows or game workshops, write to me.",
        "ja": "取材、コラボレーション、出版、ライブ、ゲームワークショップのご依頼はメールでどうぞ。",
    }[lang]
    social = "\n".join(
        f'          <a class="social-pill" href="{u}" target="_blank" rel="noopener noreferrer">{n}</a>' for n, u in SOCIAL
    )
    body = f"""    <section class="section">
      <div class="wrap contact">
        <h1>{t['contact']}</h1>
        <p>{intro}</p>
        <p><a class="btn" href="mailto:{EMAIL}">{EMAIL}</a></p>
        <div class="social-row">
{social}
        </div>
      </div>
    </section>
"""
    return page(lang, "contacto.html", PAGE_TITLES["contacto.html"][lang], intro, body, active="contacto.html")


PRIVACY = """    <section class="section">
      <div class="wrap prose">
        <h1>Políticas de Privacidad</h1>
        <p class="muted">Última actualización: 7 de octubre de 2026</p>
        <h2>1. Responsable</h2>
        <p>Este sitio es operado por Daniel Arosteguy (Danny Blue Jet). Para cualquier consulta sobre privacidad escribe a <a href="mailto:arosteguy.daniel@gmail.com">arosteguy.daniel@gmail.com</a>.</p>
        <h2>2. Datos que recopilamos</h2>
        <ul>
          <li><strong>Analítica:</strong> usamos Umami y Google Analytics para medir el tráfico del sitio, y los píxeles de Meta y TikTok para medir el alcance de nuestras publicaciones. Estos servicios pueden usar cookies según sus propias políticas.</li>
          <li><strong>Contacto voluntario:</strong> si nos escribes, usamos los datos que nos envíes solo para responder tu mensaje.</li>
        </ul>
        <h2>3. Contenido de terceros</h2>
        <p>Las páginas de música incluyen reproductores de Spotify. Los videos de YouTube se cargan solo cuando haces clic en ellos. Ambos servicios aplican sus propias políticas de privacidad.</p>
        <h2>4. Tus derechos</h2>
        <p>Puedes pedir acceso, corrección o eliminación de los datos que nos hayas enviado escribiendo al correo indicado. No vendemos ni compartimos tus datos con terceros con fines comerciales.</p>
      </div>
    </section>
"""


def redirect(target):
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="robots" content="noindex">
  <title>Danny Blue Jet</title>
  <link rel="canonical" href="{SITE}{target}">
  <meta http-equiv="refresh" content="0; url={target}">
</head>
<body>
  <p><a href="{target}">Danny Blue Jet</a></p>
</body>
</html>
"""


def write(rel, content):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    for lang in LANGS:
        pre = "" if lang == "es" else lang + "/"
        write(pre + "index.html", home(lang))
        write(pre + "sobre-mi.html", about(lang))
        write(pre + "juegos/index.html", games_index(lang))
        for g in GAMES:
            write(pre + f"juegos/{g['slug']}.html", game_page(lang, g))
        write(pre + "la-vaca-del-tablero.html", vaca(lang))
        write(pre + "musica.html", music(lang))
        write(pre + "contacto.html", contact(lang))
    write("privacidad.html", page("es", "privacidad.html", "Políticas de Privacidad", "Política de privacidad de dannybluejet.com", PRIVACY, langs=["es"]))

    # Old URLs → new pages, so existing links keep working.
    redirects = {"games.html": "/juegos/", "music.html": "/musica.html", "expotaku.html": "/musica.html",
                 "terminos.html": "/", "pago-exitoso.html": "/", "pago-fallido.html": "/"}
    for f in sorted(os.listdir(os.path.join(ROOT, "products"))):
        if f.endswith(".html"):
            redirects["products/" + f] = "/juegos/batalla-de-coronas.html" if f == "batallas.html" else "/juegos/"
    for old, new in redirects.items():
        write(old, redirect(new))

    pages = ["index.html", "sobre-mi.html", "juegos/index.html"] + [f"juegos/{g['slug']}.html" for g in GAMES] + \
            ["la-vaca-del-tablero.html", "musica.html", "contacto.html"]
    entries = []
    for pth in pages:
        for lang in LANGS:
            alts = "\n".join(f'    <xhtml:link rel="alternate" hreflang="{l}" href="{SITE}{url(l, pth)}"/>' for l in LANGS)
            entries.append(f"  <url>\n    <loc>{SITE}{url(lang, pth)}</loc>\n    <lastmod>2026-10-07</lastmod>\n{alts}\n  </url>")
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
          + "\n".join(entries) + "\n</urlset>\n")


main()

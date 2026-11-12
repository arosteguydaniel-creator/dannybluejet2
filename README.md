# 🗻 Danny Blue Jet

Sitio de autor de Danny Blue Jet (Daniel Arosteguy): diseñador de juegos de mesa y músico.
Sitio estático en tres idiomas, publicado con GitHub Pages en www.dannybluejet.com.

## Estructura

| Ruta | Idioma |
| --- | --- |
| `/` | Español (por defecto) |
| `/en/` | Inglés |
| `/ja/` | Japonés |

Cada idioma tiene las mismas páginas, con el mismo nombre de archivo:

```
index.html                       Inicio
sobre-mi.html                    Bio
juegos/index.html                Mis juegos
juegos/my-extreme-skatepark.html ★ destacado
juegos/armaduras-musicales.html
juegos/batalla-de-coronas.html
juegos/de-cero-a-ceo.html
la-vaca-del-tablero.html         Editorial
musica.html                      Música
contacto.html                    Contacto
```

`comprar-batalla-de-coronas.html` (la página de venta) está solo en español: las ventas son solo dentro de Chile.

## Radar de prensa

El blog se sacó del sitio el 12-11-2026; sus URLs (`/blog/`, `/en/blog/`, `/ja/blog/` y la entrada de prensa)
redirigen al inicio y a la página de My Extreme Skatepark. Las listas `PRESS`, `VIDEOS` y `BGG_SNAPSHOT` siguen en
`tools/build.py` como registro del radar, por si el blog vuelve.

## Venta

El bloque `SHOP` en `tools/build.py` controla la página de venta:

- `price_clp`: precio en pesos. Si está en `None`, la página invita a consultar por correo.
- `flow_url`: link de pago creado en el portal de Flow (sección *Link de pago*). Si está vacío,
  el botón abre el correo en vez de la pasarela.
- `shipping`: texto de despacho. `stock`: disponibilidad, se refleja en los datos estructurados.

`privacidad.html` está solo en español. Las URLs antiguas de la tienda (`games.html`, `music.html`,
`products/*.html`, `terminos.html`, `pago-*.html`, `expotaku.html`) son redirecciones a las páginas nuevas.

Estilos en `css/site.css`, JavaScript en `js/site.js` (menú móvil y videos de YouTube que cargan al hacer clic).

## Cómo editar

Las páginas se generan con `tools/build.py`, que tiene todos los textos en los tres idiomas.
Para cambiar un texto o agregar un juego, edita `tools/build.py` y ejecuta:

```
python3 tools/build.py .
```

Si editas un HTML a mano, recuerda hacer el mismo cambio en `/en/` y `/ja/`.

Las portadas de My Extreme Skatepark, Armaduras Musicales y De Cero a CEO son provisorias (dibujadas con CSS).
Para usar una imagen real, súbela a `images/` y pon su ruta en el campo `cover` del juego en `tools/build.py`.

## Vista previa local

```
python3 -m http.server 8000
```

y abre http://localhost:8000 (las rutas empiezan con `/`, así que abrir el archivo directo no carga los estilos).

## Analítica

`js/trackers.js` carga Meta Pixel, TikTok Pixel y Umami. Cada página además incluye Google Analytics
(`G-SEK1KR9XGS`) y un segundo Meta Pixel (`951894654288792`) que antes estaba escrito directo en el HTML.

## Contacto

arosteguy.daniel@gmail.com

---

*Danny Blue Jet © 2026*

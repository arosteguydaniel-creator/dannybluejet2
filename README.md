# 🎲🎵 Danny Blue Jet

Sitio web oficial de **Danny Blue Jet** — una plataforma que combina una tienda online de juegos de mesa y una sección de música con player, eventos y venta de tickets.

## 🌐 Páginas

| Página | Descripción |
|---|---|
| `index.html` | Página principal / landing |
| `games.html` | Tienda online de juegos de mesa |
| `music.html` | Sección de música, eventos y tickets |

## 🎨 Estética
- **Colores**: Azul brillante, rosa/magenta, rojo accent y blanco
- **Tipografía**: Poppins (Google Fonts)
- **Diseño**: Moderno, vibrante y responsivo

## 🛠️ Tecnologías
- HTML5
- CSS3 (variables, flexbox, grid)
- JavaScript Vanilla

## 🚀 Cómo usar
1. Clona el repositorio
2. Abre `index.html` en tu navegador
3. ¡Disfruta el sitio!

## 📁 Estructura
```
dannybluejet2/
├── index.html
├── games.html
├── music.html
├── css/
│   ├── style.css
│   ├── games.css
│   └── music.css
├── js/
│   ├── main.js
│   └── trackers.js
└── README.md
```

## 📊 Trackers y analítica

Todos los pixels de seguimiento y herramientas de analítica se gestionan desde un único archivo: **`js/trackers.js`**.

| Herramienta | ID |
|---|---|
| Meta Pixel | `3627643840689292` |
| TikTok Pixel | `D6KT7G3C77U3SAC89O0G` |
| Umami | `16ceb526-7cf0-4b63-b670-a13e9eb20822` |

### Estrategia de carga
- El archivo se incluye con `defer` en el `<head>` de cada página.
- La inicialización se retrasa hasta que el navegador esté inactivo (`requestIdleCallback`) o hasta 3 segundos tras la carga, o bien en el primer evento de interacción del usuario.
- Si algún tracker falla, el error queda contenido y no afecta al resto del sitio.

### Rutas de inclusión
- Páginas en la raíz: `<script defer src="js/trackers.js"></script>`
- Páginas en `products/`: `<script defer src="../js/trackers.js"></script>`

> ⚠️ **Importante:** No agregar snippets inline de trackers directamente en los HTML.
> Todo se gestiona desde `js/trackers.js`.

## 📬 Contacto
- Email: arosteguy.daniel@gmail.com
- Teléfono: +56 9 7828 6738

---
*Danny Blue Jet © 2026*

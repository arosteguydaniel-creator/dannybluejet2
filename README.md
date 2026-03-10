# 🎲🎵 Danny Blue Jet

The official website for Danny Blue Jet — a platform that combines an online board game store and a music section featuring a player, event info, and ticket sales.

## 🌐 Pages

| Page | Description |
| --- | --- |
| `index.html` | Main Page / Landing |
| `games.html` | Online board game store |
| `music.html` | Music section, events, and ticket sales |

## 🎨 Aesthetics

* **Colors**: Bright blue, pink/magenta, red accent, and white.
* **Typography**: Poppins (Google Fonts).
* **Design**: Modern, vibrant, and responsive.

## 🛒 E-commerce Flow: Direct Purchase
To optimize the user experience and ensure low-friction transactions, the platform utilizes a Direct-to-Checkout architecture:

Product Selection: Users browse the catalog in games.html, which is built using CSS Grid for a fully responsive, mobile-first experience.

Streamlined Interaction: Each product is linked directly to a specific checkout endpoint using “Flow” payment links.


## 🛠️ Technologies

* HTML5
* CSS3 (variables, flexbox, grid)
* Vanilla JavaScript

## 🚀 How to use

1. Clone the repository.
2. Open `index.html` in your browser.
3. Enjoy the site!

## 📁 Structure

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

## 📊 Trackers and Analytics

All tracking pixels and analytics tools are managed from a single file: **`js/trackers.js`**.

| Tool | ID |
| --- | --- |
| Meta Pixel | `3627643840689292` |
| TikTok Pixel | `D6KT7G3C77U3SAC89O0G` |
| Umami | `16ceb526-7cf0-4b63-b670-a13e9eb20822` |

### Loading Strategy

* The file is included with `defer` in the `<head>` of each page.
* Initialization is delayed until the browser is idle (`requestIdleCallback`), up to 3 seconds after page load, or upon the user's first interaction.
* If any tracker fails, the error is contained and does not affect the rest of the site.

### Inclusion Paths

* Pages in the root: `<script defer src="js/trackers.js"></script>`
* Pages in `products/`: `<script defer src="../js/trackers.js"></script>`

> ⚠️ **Important:** Do not add inline tracker snippets directly into the HTML files.
> Everything must be managed through `js/trackers.js`.

## 📬 Contact

* Email: arosteguy.daniel@gmail.com
* Phone: +56 9 7828 6738

---

*Danny Blue Jet © 2026*

// ===================== SMOOTH SCROLL =====================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth' });
    }
  });
});

// ===================== NAVBAR HAMBURGER =====================
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.navbar-links');

if (hamburger && navLinks) {
  hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('open');
    const isOpen = navLinks.classList.contains('open');
    hamburger.setAttribute('aria-expanded', isOpen);
  });

  // Close nav when a link is clicked
  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => navLinks.classList.remove('open'));
  });
}

// ===================== SCROLL ANIMATIONS =====================
const observerOptions = { threshold: 0.15 };

const scrollObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      scrollObserver.unobserve(entry.target);
    }
  });
}, observerOptions);

document.querySelectorAll('.fade-in').forEach(el => scrollObserver.observe(el));

// ===================== CART FUNCTIONALITY (games.html) =====================
let cart = JSON.parse(localStorage.getItem('dbj_cart') || '[]');

function saveCart() {
  localStorage.setItem('dbj_cart', JSON.stringify(cart));
}

function addToCart(name, price, emoji) {
  const existing = cart.find(item => item.name === name);
  if (existing) {
    existing.qty += 1;
  } else {
    cart.push({ name, price, emoji, qty: 1 });
  }
  saveCart();
  updateCartUI();
  // Brief visual feedback
  const cartSidebar = document.getElementById('cartSidebar');
  if (cartSidebar) openCart();
}

function removeFromCart(index) {
  cart.splice(index, 1);
  saveCart();
  updateCartUI();
}

function changeQty(index, delta) {
  cart[index].qty += delta;
  if (cart[index].qty <= 0) {
    removeFromCart(index);
    return;
  }
  saveCart();
  updateCartUI();
}

function updateCartUI() {
  const badge = document.getElementById('cartBadge');
  const itemsContainer = document.getElementById('cartItems');
  const totalEl = document.getElementById('cartTotal');

  const totalQty = cart.reduce((sum, item) => sum + item.qty, 0);
  const totalPrice = cart.reduce((sum, item) => sum + item.qty * item.price, 0);

  if (badge) {
    badge.textContent = totalQty;
    badge.style.display = totalQty > 0 ? 'flex' : 'none';
  }

  if (itemsContainer) {
    if (cart.length === 0) {
      itemsContainer.innerHTML = '<p class="cart-empty">Tu carrito está vacío 🛒</p>';
    } else {
      itemsContainer.innerHTML = cart.map((item, i) => `
        <div class="cart-item">
          <div class="cart-item-emoji">${item.emoji}</div>
          <div class="cart-item-info">
            <div class="cart-item-name">${item.name}</div>
            <div class="cart-item-price">$${(item.price * item.qty).toFixed(2)}</div>
          </div>
          <div class="cart-item-qty">
            <button class="qty-btn" onclick="changeQty(${i}, -1)">−</button>
            <span>${item.qty}</span>
            <button class="qty-btn" onclick="changeQty(${i}, 1)">+</button>
          </div>
          <button class="cart-item-remove" onclick="removeFromCart(${i})" title="Eliminar">✕</button>
        </div>
      `).join('');
    }
  }

  if (totalEl) totalEl.textContent = `$${totalPrice.toFixed(2)}`;
}

function openCart() {
  const sidebar = document.getElementById('cartSidebar');
  const overlay = document.getElementById('cartOverlay');
  if (sidebar) sidebar.classList.add('open');
  if (overlay) overlay.classList.add('open');
}

function closeCart() {
  const sidebar = document.getElementById('cartSidebar');
  const overlay = document.getElementById('cartOverlay');
  if (sidebar) sidebar.classList.remove('open');
  if (overlay) overlay.classList.remove('open');
}

function toggleCart() {
  const sidebar = document.getElementById('cartSidebar');
  if (sidebar) {
    if (sidebar.classList.contains('open')) {
      closeCart();
    } else {
      openCart();
    }
  }
}

// Init cart UI on page load
document.addEventListener('DOMContentLoaded', () => {
  updateCartUI();

  // Cart overlay click to close
  const overlay = document.getElementById('cartOverlay');
  if (overlay) overlay.addEventListener('click', closeCart);

  // Checkout
  const checkoutBtn = document.getElementById('checkoutBtn');
  if (checkoutBtn) {
    checkoutBtn.addEventListener('click', () => {
      if (cart.length === 0) {
        alert('Tu carrito está vacío.');
        return;
      }
      alert(`¡Gracias por tu compra! Total: $${cart.reduce((s, i) => s + i.qty * i.price, 0).toFixed(2)}`);
      cart = [];
      saveCart();
      updateCartUI();
      closeCart();
    });
  }
});

// ===================== CATEGORY FILTER (games.html) =====================
function filterProducts(category) {
  // Update active pill
  document.querySelectorAll('.filter-pill').forEach(pill => {
    pill.classList.toggle('active', pill.dataset.category === category);
  });

  // Show/hide products
  document.querySelectorAll('.product-card').forEach(card => {
    const cat = card.dataset.category;
    if (category === 'todos' || cat === category) {
      card.style.display = 'flex';
    } else {
      card.style.display = 'none';
    }
  });
}

// ===================== MUSIC PLAYER (music.html) =====================
const tracks = [
  { name: 'Blue Vibes', artist: 'Danny Blue Jet', duration: 213 },
  { name: 'Electric Dreams', artist: 'Danny Blue Jet', duration: 187 },
  { name: 'Acoustic Soul', artist: 'Danny Blue Jet', duration: 234 },
];

let currentTrack = 0;
let isPlaying = false;
let currentTime = 0;
let playerInterval = null;

function loadTrack(index) {
  currentTrack = index;
  currentTime = 0;
  const track = tracks[index];
  const nameEl = document.getElementById('trackName');
  const artistEl = document.getElementById('trackArtist');
  const totalEl = document.getElementById('timeTotal');
  if (nameEl) nameEl.textContent = track.name;
  if (artistEl) artistEl.textContent = track.artist;
  if (totalEl) totalEl.textContent = formatTime(track.duration);
  updateProgress();
}

function formatTime(seconds) {
  const m = Math.floor(seconds / 60);
  const s = Math.floor(seconds % 60);
  return `${m}:${s.toString().padStart(2, '0')}`;
}

function updateProgress() {
  const fill = document.getElementById('progressFill');
  const currentEl = document.getElementById('timeCurrent');
  const track = tracks[currentTrack];
  if (fill) fill.style.width = `${(currentTime / track.duration) * 100}%`;
  if (currentEl) currentEl.textContent = formatTime(currentTime);
}

function togglePlay() {
  isPlaying = !isPlaying;
  const btn = document.getElementById('playPauseBtn');
  const cover = document.getElementById('albumCover');

  if (btn) btn.textContent = isPlaying ? '⏸' : '▶';
  if (cover) cover.classList.toggle('spinning', isPlaying);

  if (isPlaying) {
    playerInterval = setInterval(() => {
      currentTime++;
      if (currentTime >= tracks[currentTrack].duration) {
        nextTrack();
        return;
      }
      updateProgress();
    }, 1000);
  } else {
    clearInterval(playerInterval);
  }
}

function nextTrack() {
  clearInterval(playerInterval);
  isPlaying = false;
  loadTrack((currentTrack + 1) % tracks.length);
  const btn = document.getElementById('playPauseBtn');
  const cover = document.getElementById('albumCover');
  if (btn) btn.textContent = '▶';
  if (cover) cover.classList.remove('spinning');
}

function prevTrack() {
  clearInterval(playerInterval);
  isPlaying = false;
  loadTrack((currentTrack - 1 + tracks.length) % tracks.length);
  const btn = document.getElementById('playPauseBtn');
  const cover = document.getElementById('albumCover');
  if (btn) btn.textContent = '▶';
  if (cover) cover.classList.remove('spinning');
}

function seekForward() {
  currentTime = Math.min(currentTime + 10, tracks[currentTrack].duration);
  updateProgress();
}

function seekBackward() {
  currentTime = Math.max(currentTime - 10, 0);
  updateProgress();
}

// Init player
document.addEventListener('DOMContentLoaded', () => {
  if (document.getElementById('trackName')) {
    loadTrack(0);

    // Progress bar click to seek
    const progressBg = document.getElementById('progressBg');
    if (progressBg) {
      progressBg.addEventListener('click', (e) => {
        const rect = progressBg.getBoundingClientRect();
        const ratio = (e.clientX - rect.left) / rect.width;
        currentTime = Math.floor(ratio * tracks[currentTrack].duration);
        updateProgress();
      });
    }

    // Volume slider
    const volSlider = document.getElementById('volumeSlider');
    if (volSlider) {
      volSlider.addEventListener('input', (e) => {
        // Visual only - no real audio
        const vol = e.target.value / 100;
        const icon = document.getElementById('volumeIcon');
        if (icon) icon.textContent = vol === 0 ? '🔇' : vol < 0.5 ? '🔉' : '🔊';
      });
    }
  }

  // Ticket form
  const ticketForm = document.getElementById('ticketForm');
  if (ticketForm) {
    ticketForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = ticketForm.querySelector('[name="tname"]').value;
      const event = ticketForm.querySelector('[name="tevent"]').value;
      const qty = ticketForm.querySelector('[name="tqty"]').value;
      alert(`¡Gracias ${name}! Tu compra de ${qty} ticket(s) para "${event}" ha sido procesada.`);
      ticketForm.reset();
    });
  }
});

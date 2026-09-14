/**
 * Chia Cafe — Scroll Reveal & Page Animations
 * Uses Intersection Observer API (no external library needed)
 */

(function () {
  'use strict';

  /* ─── Smooth scroll-to-top button ─────────────────────── */
  const scrollBtn = document.createElement('button');
  scrollBtn.id = 'scroll-top-btn';
  scrollBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
  scrollBtn.setAttribute('aria-label', 'Back to top');
  document.body.appendChild(scrollBtn);

  window.addEventListener('scroll', function () {
    scrollBtn.classList.toggle('visible', window.scrollY > 400);
  });
  scrollBtn.addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  /* ─── Intersection Observer setup ─────────────────────── */
  var observerOptions = {
    threshold: 0.12,
    rootMargin: '0px 0px -40px 0px'
  };

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('ca-visible');
        // Stagger children if parent has data-stagger
        if (entry.target.dataset.stagger) {
          var children = entry.target.querySelectorAll('[data-child]');
          children.forEach(function (child, i) {
            setTimeout(function () {
              child.classList.add('ca-visible');
            }, i * parseInt(entry.target.dataset.stagger, 10));
          });
        }
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  /* ─── Auto-tag elements with animation classes ─────────── */
  function tagElements() {

    // Section titles → fade up
    document.querySelectorAll('.section-title, .form-title, .abt-text, .story-text, .why-header, .breadcrumb-text').forEach(function (el) {
      if (!el.classList.contains('ca-init')) {
        el.classList.add('ca-init', 'ca-fade-up');
        observer.observe(el);
      }
    });

    // Product / why / contact / menu cards — stagger within rows
    document.querySelectorAll('.row:not(.ca-init)').forEach(function (row) {
      var cards = row.querySelectorAll(
        '.single-product-item, .why-card, .contact-info-card, .menu-grid-section, .menu-card'
      );
      if (cards.length > 0) {
        cards.forEach(function (card, i) {
          if (!card.classList.contains('ca-init')) {
            card.classList.add('ca-init', 'ca-fade-up');
            card.style.transitionDelay = (i * 80) + 'ms';
            observer.observe(card);
          }
        });
      }
    });

    // Story / about images — slide from left
    document.querySelectorAll('.story-image-grid, .abt-bg, .image-column .image').forEach(function (el) {
      if (!el.classList.contains('ca-init')) {
        el.classList.add('ca-init', 'ca-fade-left');
        observer.observe(el);
      }
    });

    // Content columns — slide from right
    document.querySelectorAll('.content-column').forEach(function (el) {
      if (!el.classList.contains('ca-init')) {
        el.classList.add('ca-init', 'ca-fade-right');
        observer.observe(el);
      }
    });

    // Contact form panel — fade up
    document.querySelectorAll('.contact-form-panel').forEach(function (el) {
      if (!el.classList.contains('ca-init')) {
        el.classList.add('ca-init', 'ca-fade-up');
        observer.observe(el);
      }
    });

    // Contact info cards — stagger
    document.querySelectorAll('.contact-info-card').forEach(function (el, i) {
      if (!el.classList.contains('ca-init')) {
        el.classList.add('ca-init', 'ca-fade-left');
        el.style.transitionDelay = (i * 90) + 'ms';
        observer.observe(el);
      }
    });

    // Testimonials
    document.querySelectorAll('.single-testimonial-slider').forEach(function (el) {
      if (!el.classList.contains('ca-init')) {
        el.classList.add('ca-init', 'ca-scale-in');
        observer.observe(el);
      }
    });

    // Celebrations banner children
    document.querySelectorAll('.cart-banner .image, .cart-banner .content-column').forEach(function (el, i) {
      if (!el.classList.contains('ca-init')) {
        el.classList.add('ca-init', i === 0 ? 'ca-fade-left' : 'ca-fade-right');
        observer.observe(el);
      }
    });

    // Gallery items
    document.querySelectorAll('.gallery-item, .single-gallery-item, .gallery-img-wrap').forEach(function (el, i) {
      if (!el.classList.contains('ca-init')) {
        el.classList.add('ca-init', 'ca-scale-in');
        el.style.transitionDelay = (i % 4 * 80) + 'ms';
        observer.observe(el);
      }
    });

    // Logo carousel
    document.querySelectorAll('.logo-carousel-section').forEach(function (el) {
      if (!el.classList.contains('ca-init')) {
        el.classList.add('ca-init', 'ca-fade-up');
        observer.observe(el);
      }
    });

    // find-location bar
    document.querySelectorAll('.find-location').forEach(function (el) {
      if (!el.classList.contains('ca-init')) {
        el.classList.add('ca-init', 'ca-fade-up');
        observer.observe(el);
      }
    });

    // Menu category sections (in All tab)
    document.querySelectorAll('.menu-grid-section').forEach(function (el, i) {
      if (!el.classList.contains('ca-init')) {
        el.classList.add('ca-init', 'ca-fade-up');
        el.style.transitionDelay = (Math.min(i, 4) * 60) + 'ms';
        observer.observe(el);
      }
    });
  }

  /* ─── Run on DOM ready ────────────────────────────────── */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', tagElements);
  } else {
    tagElements();
  }

  /* ─── Re-run after Bootstrap tab switches (menu page) ─── */
  document.addEventListener('shown.bs.tab', tagElements);
  document.addEventListener('shown.bs.collapse', tagElements);

  /* ─── Navbar scroll shrink effect ────────────────────── */
  var header = document.getElementById('sticker');
  if (header) {
    window.addEventListener('scroll', function () {
      header.classList.toggle('nav-scrolled', window.scrollY > 60);
    });
  }

  /* ─── Smooth page fade-in on load ────────────────────── */
  document.documentElement.classList.add('page-loading');
  window.addEventListener('load', function () {
    document.documentElement.classList.remove('page-loading');
    document.documentElement.classList.add('page-loaded');
  });

})();

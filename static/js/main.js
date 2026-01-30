/**
 * Brutal Blog — main.js
 * Animations, smooth scroll, AJAX comments, loading indicators
 */

(function () {
  'use strict';

  // ——— Fade-in on scroll (IntersectionObserver) ———
  const fadeEls = document.querySelectorAll('.fade-in');
  if (fadeEls.length && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
          }
        });
      },
      { rootMargin: '0px 0px -40px 0px', threshold: 0.1 }
    );
    fadeEls.forEach(function (el) {
      observer.observe(el);
    });
  }

  // ——— Smooth scroll for anchor links ———
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      const target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // ——— AJAX comment form ———
  const commentForm = document.getElementById('comment-form');
  if (commentForm) {
    commentForm.addEventListener('submit', function (e) {
      e.preventDefault();
      const form = this;
      const submitBtn = form.querySelector('button[type="submit"]');
      const listEl = document.getElementById('comment-list');
      const originalText = submitBtn.textContent;

      submitBtn.disabled = true;
      submitBtn.innerHTML = '<span class="brutalist-loading"></span> Sending...';

      const formData = new FormData(form);
      formData.append('csrfmiddlewaretoken', document.querySelector('[name=csrfmiddlewaretoken]').value);

      fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
          'X-Requested-With': 'XMLHttpRequest',
          'Accept': 'application/json',
        },
      })
        .then(function (r) {
          return r.json().then(function (data) {
            if (!r.ok) throw new Error(data.error || 'Failed');
            return data;
          });
        })
        .then(function (data) {
          if (data.ok && data.html && listEl) {
            listEl.innerHTML = data.html;
            form.reset();
          } else if (!data.ok) {
            submitBtn.textContent = data.error || 'Error';
            setTimeout(function () { submitBtn.textContent = originalText; }, 2000);
          }
        })
        .catch(function () {
          form.submit();
        })
        .finally(function () {
          submitBtn.disabled = false;
          submitBtn.textContent = originalText;
        });
    });
  }

  // ——— Button/link hover scale (CSS handles most; optional shake) ———
  document.querySelectorAll('.animated-button').forEach(function (btn) {
    btn.addEventListener('mouseenter', function () {
      this.style.transition = 'transform 0.2s ease-in-out';
    });
  });
})();

/* ==========================================================================
   Vytalix — site behaviour. Vanilla JS, no dependencies.
   1. Mobile navigation toggle
   2. Cookie notice (stores a preference in localStorage only; sets no cookies)
   3. Contact form: client-side validation and honest status messages
   4. Footer year
   ========================================================================== */
(function () {
  "use strict";

  /* ---------- 1. Navigation ---------- */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("primary-nav");

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.querySelector(".nav-toggle-label").textContent = open ? "Close" : "Menu";
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && nav.classList.contains("is-open")) {
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.querySelector(".nav-toggle-label").textContent = "Menu";
        toggle.focus();
      }
    });
  }

  /* ---------- 2. Cookie notice ---------- */
  var STORAGE_KEY = "vytalix-cookie-preference"; // values: "essential" | "accepted"
  var banner = document.getElementById("cookie-banner");

  function readPreference() {
    try {
      return window.localStorage.getItem(STORAGE_KEY);
    } catch (err) {
      return null;
    }
  }

  function savePreference(value) {
    try {
      window.localStorage.setItem(STORAGE_KEY, value);
    } catch (err) {
      /* Storage unavailable (private mode, blocked). The banner will show again next visit; nothing else breaks. */
    }
  }

  if (banner) {
    if (!readPreference()) {
      banner.hidden = false;
    }
    banner.addEventListener("click", function (event) {
      var button = event.target.closest("[data-cookie-choice]");
      if (!button) { return; }
      savePreference(button.getAttribute("data-cookie-choice"));
      banner.hidden = true;
    });
  }

  /* Allow the cookie-policy page to reset the stored preference. */
  var resetButton = document.getElementById("cookie-reset");
  if (resetButton) {
    resetButton.addEventListener("click", function () {
      try { window.localStorage.removeItem(STORAGE_KEY); } catch (err) { /* ignore */ }
      var status = document.getElementById("cookie-reset-status");
      if (status) {
        status.hidden = false;
        status.textContent = "Your stored preference has been cleared. The notice will show again on your next page load.";
      }
      if (banner) { banner.hidden = false; }
    });
  }

  /* ---------- 3. Contact form ---------- */
  var form = document.getElementById("contact-form");

  if (form) {
    var status = document.getElementById("form-status");

    function setError(field, message) {
      var error = document.getElementById(field.id + "-error");
      if (message) {
        field.setAttribute("aria-invalid", "true");
        if (error) { error.textContent = message; error.classList.add("is-visible"); }
      } else {
        field.removeAttribute("aria-invalid");
        if (error) { error.textContent = ""; error.classList.remove("is-visible"); }
      }
    }

    function validate() {
      var firstInvalid = null;
      var fields = form.querySelectorAll("[data-validate]");

      Array.prototype.forEach.call(fields, function (field) {
        var value = field.value.trim();
        var message = "";

        if (field.required && !value) {
          message = "Please complete this field.";
        } else if (field.type === "email" && value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) {
          message = "Please enter an email address we can reply to.";
        } else if (field.type === "checkbox" && field.required && !field.checked) {
          message = "Please confirm you have read the privacy notice.";
        }

        setError(field, message);
        if (message && !firstInvalid) { firstInvalid = field; }
      });

      return firstInvalid;
    }

    form.addEventListener("submit", function (event) {
      var firstInvalid = validate();
      if (firstInvalid) {
        event.preventDefault();
        firstInvalid.focus();
        return;
      }

      /* TODO: remove this block once the form action points at a real endpoint (see README "Contact form").
         Until then we stop the submission and tell the visitor plainly what happened. */
      if (form.getAttribute("data-endpoint-configured") !== "true") {
        event.preventDefault();
        if (status) {
          status.hidden = false;
          status.className = "notice";
          status.innerHTML = "<p><strong>Thank you.</strong> The contact form is not yet connected to an inbox. " +
            "Please email us directly at the address shown on this page. Your message has not been sent or stored.</p>";
          status.focus();
        }
      }
    });

    /* Clear an error as soon as the visitor corrects it. */
    form.addEventListener("input", function (event) {
      var field = event.target;
      if (field.hasAttribute("data-validate") && field.getAttribute("aria-invalid") === "true") {
        validate();
      }
    });
  }

  /* ---------- 4. Footer year ---------- */
  var year = document.getElementById("year");
  if (year) { year.textContent = String(new Date().getFullYear()); }
})();

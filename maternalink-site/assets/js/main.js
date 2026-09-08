/* MaternaLink site — navigation, language switch, cookie preference. No dependencies. */
(function(){
  'use strict';
  // Mobile nav
  var toggle=document.querySelector('.nav-toggle'), nav=document.getElementById('site-nav');
  if(toggle&&nav){toggle.addEventListener('click',function(){var open=nav.classList.toggle('open');toggle.setAttribute('aria-expanded',open?'true':'false');});}
  // Cookie preference (localStorage only; no tracking cookies are set)
  var banner=document.getElementById('cookie-banner');
  function pref(){try{return localStorage.getItem('ml-cookie-pref');}catch(e){return null;}}
  if(banner&&!pref()){banner.classList.add('show');}
  banner&&banner.querySelectorAll('[data-cookie]').forEach(function(b){b.addEventListener('click',function(){try{localStorage.setItem('ml-cookie-pref',b.getAttribute('data-cookie'));}catch(e){}banner.classList.remove('show');});});
  // Language switch (EN/FR) — applies to any element with data-i18n; dictionary in i18n.js
  var dict=window.ML_I18N||{};
  function apply(lang){
    document.documentElement.setAttribute('lang',lang==='fr'?'fr':'en-GB');
    document.querySelectorAll('[data-i18n]').forEach(function(el){
      var k=el.getAttribute('data-i18n'); var v=dict[lang]&&dict[lang][k];
      if(v==null) return;
      if(el.hasAttribute('data-i18n-attr')){el.setAttribute(el.getAttribute('data-i18n-attr'),v);} else {el.innerHTML=v;}
    });
    document.querySelectorAll('.lang button').forEach(function(b){b.setAttribute('aria-pressed',b.getAttribute('data-lang')===lang?'true':'false');});
    try{localStorage.setItem('ml-lang',lang);}catch(e){}
  }
  document.querySelectorAll('.lang button').forEach(function(b){b.addEventListener('click',function(){apply(b.getAttribute('data-lang'));});});
  var saved=null; try{saved=localStorage.getItem('ml-lang');}catch(e){}
  if(saved==='fr'&&dict.fr) apply('fr');
  // Contact/pilot form: placeholder handler until an endpoint is wired (see README)
  var form=document.getElementById('pilot-form');
  if(form){form.addEventListener('submit',function(e){if(form.getAttribute('action')==='#'){e.preventDefault();var ok=document.getElementById('form-ok');if(ok){ok.hidden=false;ok.focus();}}});}
})();

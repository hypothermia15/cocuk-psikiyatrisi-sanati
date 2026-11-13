/* Çocuk Psikiyatrisinin Sanatı · Okuma Rehberi — görünümler, vaka soruları, karışık test, kavram kartları,
   zor anlar, tarama hesaplayıcısı, formülasyon çalışma sayfası, atıf penceresi, arama */
(function () {
  "use strict";
  var kok = document.documentElement;
  kok.classList.add("js");

  var ANAHTAR = "cocuk-psikiyatrisi-sanati:v1";
  var durum = oku();
  ["okundu", "test", "kart", "not", "form"].forEach(function (k) { durum[k] = durum[k] || {}; });
  function oku() { try { return JSON.parse(localStorage.getItem(ANAHTAR) || "{}") || {}; } catch (e) { return {}; } }
  function yaz() { try { localStorage.setItem(ANAHTAR, JSON.stringify(durum)); } catch (e) { /* özel pencere */ } }

  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  function kacis(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function parla(el) { el.classList.remove("parla"); void el.offsetWidth; el.classList.add("parla"); }
  function katla(s) { return s.toLocaleLowerCase("tr").replace(/ı/g, "i").normalize("NFD").replace(/[̀-ͯ]/g, ""); }
  function kucukHarf(s) { return s.toLocaleLowerCase("tr"); }
  function karistir(a) {
    for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; }
    return a;
  }

  var gorunumler = $$(".view");
  var bolumler = gorunumler.filter(function (v) { return !!v.querySelector(".okundu"); });
  var etkin = null;
  function baslik(v) { return v.getAttribute("data-baslik") || ""; }
  function adres(v) { return v.dataset.view === "giris" ? "#/" : "#/" + v.dataset.view; }

  /* Önceki / sonraki bağlantıları */
  gorunumler.forEach(function (v, i) {
    var nav = $(".ileri-geri", v);
    if (!nav) return;
    var h = "";
    if (i > 0) h += '<a href="' + adres(gorunumler[i - 1]) + '"><span>← Önceki</span>' + kacis(baslik(gorunumler[i - 1])) + "</a>";
    if (i < gorunumler.length - 1) h += '<a href="' + adres(gorunumler[i + 1]) + '"><span>Sonraki →</span>' + kacis(baslik(gorunumler[i + 1])) + "</a>";
    nav.innerHTML = h;
  });

  /* Görünüm değiştirme */
  function goster(ad, alt, odakla) {
    var v = document.getElementById("v-" + ad) || document.getElementById("v-giris");
    ad = v.dataset.view;
    if (etkin !== v) {
      gorunumler.forEach(function (x) { x.classList.toggle("aktif", x === v); });
      etkin = v;
      $$(".yan a[data-nav]").forEach(function (a) {
        if (a.dataset.nav === ad) a.setAttribute("aria-current", "page"); else a.removeAttribute("aria-current");
      });
      document.title = (ad === "giris" ? "" : baslik(v) + " · ") + "Çocuk Psikiyatrisinin Sanatı · Okuma Rehberi · Doç. Dr. Miraç Barış Usta";
      atifKapat();
      if (ad === "giris") ilerlemeCiz();
      if (ad === "kavramlar") kartBaslat(false);
      if (ad === "tarama") taramaCiz();
    }
    menuKapat();
    var hedef = alt ? document.getElementById(ad + "-" + alt) : null;
    if (hedef) {
      hedef.scrollIntoView({ block: "start" });
    } else {
      window.scrollTo(0, 0);
      if (odakla !== false) { var h = $("h1, h2", v); if (h) h.focus({ preventScroll: true }); }
    }
  }

  function git(v, el) {
    if (location.hash !== adres(v)) history.pushState(null, "", adres(v));
    goster(v.dataset.view, null, false);
    var det = el.closest("details");
    if (det) det.open = true;
    el.scrollIntoView({ block: "center" });
    parla(el);
  }

  var ilk = true;
  function rota() {
    var h = location.hash || "";
    var m = h.match(/^#\/([\w-]*)(?:\/([\w-]+))?$/);
    var odak = !ilk;
    ilk = false;
    if (!h || h === "#" || (m && !m[1])) return goster("giris", null, odak);
    if (m) return goster(m[1], m[2], odak);
    var el = document.getElementById(decodeURIComponent(h.slice(1)));
    var v = el && el.closest(".view");
    if (v) { goster(v.dataset.view, null, false); el.scrollIntoView({ block: "center" }); parla(el); }
  }
  window.addEventListener("hashchange", rota);

  /* Mobil menü */
  var menuD = $(".menu-dugme");
  function menuKapat() {
    document.body.classList.remove("menu-acik");
    if (menuD) menuD.setAttribute("aria-expanded", "false");
  }
  if (menuD) menuD.addEventListener("click", function () {
    var acik = document.body.classList.toggle("menu-acik");
    menuD.setAttribute("aria-expanded", acik ? "true" : "false");
  });

  /* Vaka soruları */
  function etiket(kutu, bildi) {
    if (!kutu) return;
    var et = $(".sonuc-etiket", kutu);
    if (!et) { et = document.createElement("span"); et.className = "sonuc-etiket"; kutu.insertBefore(et, kutu.firstChild); }
    et.textContent = bildi ? "✓ Bildiniz" : "✗ Bu sefer olmadı";
  }
  function testUygula(m, k) {
    var dogru = +m.dataset.dogru, bildi = k === dogru;
    m.classList.add("cevaplandi");
    m.classList.toggle("bildi", bildi);
    m.classList.toggle("bilemedi", !bildi);
    $$("button[data-secenek]", m).forEach(function (b) {
      var s = +b.dataset.secenek;
      b.disabled = true;
      b.classList.toggle("secenek-dogru", s === dogru);
      b.classList.toggle("secenek-yanlis", s === k && !bildi);
      b.setAttribute("aria-pressed", s === k ? "true" : "false");
    });
    etiket($(".test-aciklama", m), bildi);
    return bildi;
  }
  function testTemizle(m) {
    m.classList.remove("cevaplandi", "bildi", "bilemedi");
    $$("button[data-secenek]", m).forEach(function (b) {
      b.disabled = false; b.classList.remove("secenek-dogru", "secenek-yanlis"); b.removeAttribute("aria-pressed");
    });
    var et = $(".sonuc-etiket", m);
    if (et) et.remove();
  }
  function say(vid) {
    var v = document.getElementById("v-" + vid);
    var maddeler = v ? $$(".adim-test .test-madde", v) : [];
    var cev = durum.test[vid] || {}, n = 0, d = 0;
    maddeler.forEach(function (m) {
      var y = cev[m.dataset.no];
      if (y === undefined || y === null) return;
      n++;
      if (String(y) === m.dataset.dogru) d++;
    });
    return { toplam: maddeler.length, n: n, d: d };
  }
  function skorYaz(vid) {
    var s = say(vid);
    var sk = $('[data-test-skor="' + vid + '"]');
    if (sk) sk.textContent = s.n ? (s.d + " / " + s.toplam + " doğru" + (s.n < s.toplam ? " · " + (s.toplam - s.n) + " soru kaldı" : "")) : "";
    var sf = $('[data-test-sifirla="' + vid + '"]');
    if (sf) sf.hidden = !s.n;
    durumGuncelle(vid);
  }
  function durumGuncelle(vid) {
    var t = say(vid), p = [];
    if (durum.okundu[vid]) p.push("✓ Okundu");
    if (t.n) p.push("Sorular " + t.d + "/" + t.toplam);
    var kart = $('[data-durum="' + vid + '"]');
    if (kart) kart.textContent = p.join(" · ");
    var nav = $('[data-durum-nav="' + vid + '"]');
    if (nav) nav.textContent = durum.okundu[vid] ? "✓" : "";
    var ok = bolumler.filter(function (v) { return durum.okundu[v.dataset.view]; }).length;
    var il = $("[data-ilerleme]");
    if (il) il.textContent = ok ? ok + " / " + bolumler.length + " oturum okundu" : "";
  }

  /* Karışık test */
  var kAlan = $(".karisik-alan"), kListe = [], kSira = 0, kDogru = 0;
  function kGoster() {
    var butonlar = $(".karisik-dugmeler");
    if (kSira >= kListe.length) {
      var oran = kDogru / kListe.length;
      kAlan.innerHTML = '<p class="karisik-son">' + kDogru + " / " + kListe.length + " doğru</p><p>" +
        (oran >= 0.85 ? "Çok iyi. Kitabın ilkelerini kliniğe taşımaya hazırsınız."
          : oran >= 0.6 ? "İyi. Kaçırdığınız soruların oturumlarına, özellikle “Tartışmaya açık” kısımlarına dönmek iyi olur."
            : "Oturumların “Ana fikirler” ve “ÇRS’de karşılığı” kısımlarıyla başlamak iyi bir tekrar olur.") + "</p>";
      if (butonlar) butonlar.hidden = false;
      var b = $(".karisik-basla", butonlar);
      if (b) { b.textContent = "Yeniden başlat"; b.focus(); }
      return;
    }
    var asil = kListe[kSira], m = asil.cloneNode(true);
    testTemizle(m);
    m.removeAttribute("data-ara");
    var kaynak = asil.closest(".view");
    kAlan.innerHTML = '<p class="karisik-ilerleme">Soru ' + (kSira + 1) + " / " + kListe.length +
      ' · <a href="' + adres(kaynak) + '/test">' + kacis(baslik(kaynak)) + "</a></p>";
    var ol = document.createElement("ol");
    ol.className = "test sina-tek";
    ol.appendChild(m);
    kAlan.appendChild(ol);
    var ilkB = $("button[data-secenek]", m);
    if (ilkB) ilkB.focus();
  }
  $$(".karisik-basla").forEach(function (b) {
    b.addEventListener("click", function () {
      kListe = karistir($$(".view .adim-test .test-madde"));
      kSira = 0; kDogru = 0;
      var butonlar = $(".karisik-dugmeler");
      if (butonlar) butonlar.hidden = true;
      kGoster();
    });
  });
  function kSonraki(bildi) {
    if (bildi) kDogru++;
    var sn = document.createElement("button");
    sn.type = "button";
    sn.className = "dugme karisik-sonraki";
    sn.textContent = kSira + 1 < kListe.length ? "Sonraki soru →" : "Sonucu gör";
    kAlan.appendChild(sn);
    sn.focus();
  }

  /* Kavram kartları */
  var kartlar = $$(".kavram").map(function (li) {
    return { id: li.dataset.id, on: $(".kavram-terim", li).textContent.trim(),
      arka: '<p class="kavram-tanim">' + $(".kavram-tanim", li).innerHTML + "</p>" + '<p class="kavram-ornek">' +
        $(".kavram-ornek", li).innerHTML + "</p>", ref: $(".ders-ref", li).innerHTML };
  });
  var deste = [], dSira = 0, kSahne = $(".kart-sahne");
  function kartBaslat(karisik) {
    if (!kSahne) return;
    var bilinmeyen = kartlar.filter(function (k) { return !durum.kart[k.id]; });
    var bilinen = kartlar.filter(function (k) { return durum.kart[k.id]; });
    deste = (karisik ? karistir(bilinmeyen) : bilinmeyen).concat(karistir(bilinen));
    dSira = 0;
    kartCiz();
  }
  function kartIlerleme() {
    var bil = kartlar.filter(function (k) { return durum.kart[k.id]; }).length;
    var el = $(".kart-ilerleme");
    if (el) el.textContent = "Bilinen: " + bil + " / " + kartlar.length + (dSira < deste.length ? " · Kart " + (dSira + 1) + " / " + deste.length : "");
  }
  function kartCiz() {
    if (dSira >= deste.length) {
      kSahne.innerHTML = '<div class="bilgi-kart bitti"><p class="kart-on-metin">Deste bitti.</p>' +
        '<p>Bilmediğiniz kartlar bir sonraki turda önce gelir.</p><button type="button" class="dugme kart-yeniden">Yeniden başla</button></div>';
      kartIlerleme();
      return;
    }
    var k = deste[dSira];
    kSahne.innerHTML = '<div class="bilgi-kart" tabindex="0" role="button" aria-pressed="false" aria-label="Kartı çevir: ' + kacis(k.on) + '">' +
      '<div class="kart-yuz kart-on"><span class="kart-oturum">Kavram' + (durum.kart[k.id] ? " · biliniyor" : "") + "</span>" +
      '<p class="kart-on-metin">' + kacis(k.on) + '</p><span class="kart-ipucu">Çevirmek için tıklayın ya da boşluk tuşuna basın</span></div>' +
      '<div class="kart-yuz kart-arka"><span class="kart-oturum">' + kacis(k.on) + "</span>" + k.arka +
      '<p class="ders-ref">' + k.ref + "</p></div></div>" +
      '<div class="kart-dugmeler"><button type="button" class="dugme dugme-ikincil kart-tekrar">↺ Tekrar sor</button>' +
      '<button type="button" class="dugme kart-biliyorum">✓ Biliyorum</button></div>';
    kartIlerleme();
  }
  function kartCevir() {
    var k = $(".bilgi-kart:not(.bitti)", kSahne);
    if (!k) return;
    var c = k.classList.toggle("cevrildi");
    k.setAttribute("aria-pressed", c ? "true" : "false");
  }
  if (kSahne) kSahne.addEventListener("keydown", function (e) {
    if ((e.key === " " || e.key === "Enter") && e.target.classList.contains("bilgi-kart")) { e.preventDefault(); kartCevir(); }
  });

  /* Zor anlar */
  var zaAlan = $(".za-alan"), zaBasla = $(".za-basla"), zaListe = [], zaSira = 0, zaD = 0;
  function zaVeri() {
    return $$(".za-veri > li").map(function (li) {
      return { durum: $(".za-durum", li).innerHTML, sec: $$(".za-secenek", li).map(function (s) { return s.innerHTML; }),
        dogru: +li.dataset.dogru, aciklama: $(".za-aciklama", li).innerHTML, oturum: li.dataset.oturum, otad: li.dataset.otad };
    });
  }
  function zaGoster() {
    if (zaSira >= zaListe.length) {
      var n = zaListe.length, onceki = durum.za || {};
      var en = Math.max(onceki.en || 0, zaD);
      durum.za = { d: zaD, n: n, en: en };
      yaz();
      zaAlan.innerHTML = '<p class="karisik-son">' + zaD + " / " + n + " en uygun yanıt</p><p>En iyi skorunuz: " + en + " / " + n +
        ". Gerçek klinikte tek bir doğru yanıt nadirdir; durumlar ilkeleri tartışmak için sadeleştirildi. Kaçırdığınız durumların " +
        "oturumlarına dönmek iyi bir tekrar olur.</p>";
      zaBasla.hidden = false;
      zaBasla.textContent = "Yeniden oyna";
      zaBasla.focus();
      return;
    }
    var c = zaListe[zaSira];
    var sira = karistir(c.sec.map(function (_, i) { return i; }));
    zaAlan.innerHTML = '<p class="karisik-ilerleme">Durum ' + (zaSira + 1) + " / " + zaListe.length + "</p>" +
      '<div class="za-kart"><p class="za-durum-metin">' + c.durum + '</p><p class="sv-soru">En uygun yanıt hangisi?</p>' +
      '<div class="secenekler" role="group" aria-label="Yanıtlar">' +
      sira.map(function (i, k) {
        return '<button type="button" data-za="' + i + '"><span class="harf" aria-hidden="true">' + "ABCD".charAt(k) + "</span><span>" + c.sec[i] + "</span></button>";
      }).join("") + '</div><div class="za-sonuc" hidden></div></div>';
    var b = $("button[data-za]", zaAlan);
    if (b) b.focus();
  }
  if (zaBasla) zaBasla.addEventListener("click", function () {
    zaListe = karistir(zaVeri());
    zaSira = 0; zaD = 0;
    zaBasla.hidden = true;
    zaGoster();
  });

  /* Formülasyon çalışma sayfası */
  var form = $("#formulasyon"), fDurum = $(".form-durum");
  function formOku() {
    var d = {};
    if (!form) return d;
    $$("[data-form]", form).forEach(function (el) { if (el.value.trim()) d[el.dataset.form] = el.value; });
    $$("[data-form-grup]", form).forEach(function (g) {
      var s = $$("input:checked", g).map(function (x) { return x.value; });
      if (s.length) d[g.dataset.formGrup] = s;
    });
    var dd = $$(".dd-satir", form).map(function (r) { return [$(".dd-ad", r).value.trim(), $(".dd-yuzde", r).value.trim()]; });
    if (dd.some(function (x) { return x[0] || x[1]; })) d.dd = dd;
    var dg = $$(".dongu-halka", form).map(function (x) { return x.value.trim(); });
    if (dg.some(Boolean)) d.dongu = dg;
    return d;
  }
  function formYaz(d) {
    $$("[data-form]", form).forEach(function (el) { el.value = d[el.dataset.form] || ""; });
    $$("[data-form-grup]", form).forEach(function (g) {
      var s = d[g.dataset.formGrup] || [];
      $$("input", g).forEach(function (x) { x.checked = s.indexOf(x.value) >= 0; });
    });
    $$(".dd-satir", form).forEach(function (r, i) {
      var x = (d.dd || [])[i] || ["", ""];
      $(".dd-ad", r).value = x[0] || ""; $(".dd-yuzde", r).value = x[1] || "";
    });
    $$(".dongu-halka", form).forEach(function (x, i) { x.value = (d.dongu || [])[i] || ""; });
    formOzet();
  }
  function formOzet() {
    var top = 0, var_ = false;
    $$(".dd-yuzde", form).forEach(function (x) {
      var v = parseFloat(String(x.value).replace(",", "."));
      if (!isNaN(v)) { top += v; var_ = true; }
    });
    var el = $(".dd-toplam", form), tamam = var_ && Math.abs(top - 100) < 0.05;
    if (el) {
      el.textContent = var_ ? "Toplam: %" + (Math.round(top * 10) / 10).toLocaleString("tr-TR") + (tamam ? " ✓" : " · 100 olmalı") : "Toplam: –";
      el.classList.toggle("tamam", tamam);
      el.classList.toggle("eksik", var_ && !tamam);
    }
    var ks = $(".kaynak-sayi", form);
    if (ks) {
      var n = $$('[data-form-grup="kaynak"] input:checked', form).length;
      ks.textContent = n + " kaynak işaretlendi" + (n < 2 ? " · tanıya güvenmek için en az iki bağımsız kaynak arayın" : "");
    }
  }
  function formBos(d) { return !Object.keys(d).length; }
  var fZam = null;
  function formKaydet() {
    clearTimeout(fZam);
    fZam = setTimeout(function () {
      durum.form = formOku();
      yaz();
      if (fDurum) fDurum.textContent = formBos(durum.form) ? "" : "Taslak bu tarayıcıya kaydedildi.";
    }, 350);
  }
  function formBolumleri() {
    var d = formOku(), out = [];
    $$(".form-bolum", form).forEach(function (fs) {
      var b = $(".fb-ad", fs).textContent.trim(), s = [];
      $$("[data-form]", fs).forEach(function (el) {
        if (!el.value.trim()) return;
        var lab = $('label[for="' + el.id + '"]', fs);
        s.push((lab ? lab.textContent.trim() + ": " : "") + el.value.trim());
      });
      $$("[data-form-grup]", fs).forEach(function (g) { var x = d[g.dataset.formGrup]; if (x) s.push(x.join("; ")); });
      if ($(".dd-satir", fs) && d.dd) d.dd.forEach(function (x) { if (x[0] || x[1]) s.push((x[0] || "–") + ": %" + (x[1] || "?")); });
      if ($(".dongu-halka", fs) && d.dongu) s.push(d.dongu.filter(Boolean).join(" → ") + " → (başa döner)");
      if (s.length) out.push({ b: b, s: s });
    });
    return out;
  }
  function formMetin() {
    var satir = ["Formülasyon çalışma sayfası (taslak)", ""];
    formBolumleri().forEach(function (x) { satir.push(x.b, x.s.join("\n"), ""); });
    satir.push("Çocuk Psikiyatrisinin Sanatı · Okuma Rehberi · miracbarisusta.com/cocuk-psikiyatrisi-sanati/");
    return satir.join("\n");
  }
  function formBaskiHazirla() {
    var h = '<h1>Formülasyon çalışma sayfası</h1><p class="baski-alt">Taslak · ' + new Date().toLocaleDateString("tr-TR") +
      " · Çocuk Psikiyatrisinin Sanatı · Okuma Rehberi</p>";
    var bl = formBolumleri();
    if (!bl.length) h += "<p>Form henüz boş.</p>";
    bl.forEach(function (x) { h += "<h2>" + kacis(x.b) + "</h2>" + x.s.map(function (y) { return "<p>" + kacis(y) + "</p>"; }).join(""); });
    var bas = $(".form-baski");
    if (bas.parentNode !== document.body) document.body.appendChild(bas);
    bas.innerHTML = h;
  }
  var fOnay = { ornek: 0, temizle: 0 };
  if (form) {
    formYaz(durum.form || {});
    if (!formBos(durum.form || {}) && fDurum) fDurum.textContent = "Kayıtlı taslak yüklendi.";
    form.addEventListener("input", function () { formOzet(); formKaydet(); });
    form.addEventListener("change", function () { formOzet(); formKaydet(); });
    form.addEventListener("submit", function (e) { e.preventDefault(); });
    window.addEventListener("afterprint", function () { document.body.classList.remove("baski-form"); });
  }
  function formOrnek(btn) {
    if (!formBos(formOku()) && Date.now() - fOnay.ornek > 4000) {
      fOnay.ornek = Date.now();
      btn.textContent = "Taslağın üzerine yazılacak; yeniden tıklayın";
      return;
    }
    var d = {};
    try { d = JSON.parse(form.dataset.ornek || "{}"); } catch (e) { d = {}; }
    formYaz(d);
    btn.textContent = "Örnek vakayı yükle";
    formKaydet();
    if (fDurum) fDurum.textContent = "Kurgusal örnek vaka yüklendi.";
  }
  function formTemizle(btn) {
    if (Date.now() - fOnay.temizle > 4000) {
      fOnay.temizle = Date.now();
      btn.textContent = "Emin misiniz? Silmek için yeniden tıklayın";
      return;
    }
    formYaz({});
    durum.form = {};
    yaz();
    btn.textContent = "Formu temizle";
    if (fDurum) fDurum.textContent = "Form temizlendi.";
  }
  function formKopyala() {
    var metin = formMetin();
    function bitti(ok) { if (fDurum) fDurum.textContent = ok ? "Metin panoya kopyalandı." : "Kopyalanamadı; metni elle seçip kopyalayın."; }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(metin).then(function () { bitti(true); }, function () { bitti(eskiKopya(metin)); });
    } else bitti(eskiKopya(metin));
  }
  function eskiKopya(metin) {
    var ta = document.createElement("textarea");
    ta.value = metin; ta.setAttribute("readonly", ""); ta.style.position = "fixed"; ta.style.opacity = "0";
    document.body.appendChild(ta); ta.select();
    var ok = false;
    try { ok = document.execCommand("copy"); } catch (e) { ok = false; }
    ta.remove();
    return ok;
  }

  /* Tarama hesaplayıcısı */
  var tr = $("#tarama-hesap"), trIzgara = tr ? $(".tarama-izgara", tr) : null;
  function trSayi(x, b) { return x.toLocaleString("tr-TR", { maximumFractionDigits: b === undefined ? 1 : b }); }
  function trAdet(x) { return x > 0 && x < 10 ? trSayi(x, 1) : trSayi(Math.round(x), 0); }
  function trYuzde(x) { return isFinite(x) ? "%" + trSayi(x * 100, x < 0.1 ? 1 : 0) : "–"; }
  function sinirla(x, a, b) { return isNaN(x) ? a : Math.min(b, Math.max(a, x)); }
  function trDeger(ad) {
    var el = $('[data-tr="' + ad + '"]', tr);
    return parseFloat(String(el.value).replace(",", "."));
  }
  function taramaCiz() {
    if (!tr) return;
    var p = sinirla(trDeger("p"), 0.1, 60) / 100, se = sinirla(trDeger("d"), 50, 99.9) / 100, sp = sinirla(trDeger("o"), 50, 99.9) / 100;
    var N = 1000, hasta = N * p, saglam = N - hasta, gp = hasta * se, yn = hasta - gp, gn = saglam * sp, yp = saglam - gn;
    var ppv = gp / (gp + yp), npv = gn / (gn + yn), lr = se / (1 - sp);
    var h = { gp: gp, yp: yp, yn: yn, gn: gn, poz: gp + yp, neg: yn + gn, hasta: hasta, saglam: saglam };
    Object.keys(h).forEach(function (k) { var el = $('[data-h="' + k + '"]', tr); if (el) el.textContent = trAdet(h[k]); });
    $('[data-c="ppv"]', tr).textContent = trYuzde(ppv);
    $('[data-c="npv"]', tr).textContent = trYuzde(npv);
    $('[data-c="lr"]', tr).textContent = isFinite(lr) ? trSayi(lr, 1) + "×" : "–";
    $(".tarama-cumle", tr).innerHTML = "1000 çocuktan <b>" + trAdet(gp + yp) + "</b> çocuğun sonucu pozitif çıkar; bunlardan " + (ppv < 0.5 ? "yalnızca " : "") + "<b>" +
      trAdet(gp) + "</b> çocukta durum gerçekten vardır (" + trYuzde(ppv) + "). Durumu olan <b>" + trAdet(hasta) + "</b> çocuktan <b>" +
      trAdet(yn) + "</b> çocuk test tarafından kaçırılır.";
    if (trIzgara) {
      var a = [Math.round(gp), Math.round(yn), Math.round(yp)], s = "", i, sinif;
      for (i = 0; i < N; i++) {
        sinif = i < a[0] ? "gp" : i < a[0] + a[1] ? "yn" : i < a[0] + a[1] + a[2] ? "yp" : "gn";
        s += '<span class="nk nk-' + sinif + '"></span>';
      }
      trIzgara.innerHTML = s;
    }
    durum.tarama = { p: trDeger("p"), d: trDeger("d"), o: trDeger("o") };
    yaz();
  }
  function trAyarla(ad, v, kaynak) {
    $$('[data-tr="' + ad + '"], [data-tr-r="' + ad + '"]', tr).forEach(function (el) { if (el !== kaynak) el.value = v; });
  }
  if (tr) {
    if (durum.tarama) ["p", "d", "o"].forEach(function (k) { if (durum.tarama[k] !== undefined && !isNaN(durum.tarama[k])) trAyarla(k, durum.tarama[k]); });
    tr.addEventListener("input", function (e) {
      var el = e.target, ad = el.dataset.tr || el.dataset.trR;
      if (!ad) return;
      trAyarla(ad, el.value, el);
      $$("button[data-tr-ayar]", tr).forEach(function (b) { b.setAttribute("aria-pressed", "false"); });
      taramaCiz();
    });
  }

  /* Mini notlar */
  $$("textarea[data-not]").forEach(function (t) {
    var id = t.dataset.not, zam = null;
    if (durum.not[id]) t.value = durum.not[id];
    t.addEventListener("input", function () {
      clearTimeout(zam);
      zam = setTimeout(function () {
        if (t.value.trim()) durum.not[id] = t.value; else delete durum.not[id];
        yaz();
      }, 400);
    });
  });

  /* İlerleme paneli */
  var silOnay = 0;
  function ilerlemeCiz() {
    var panel = $("#ilerlemem");
    if (!panel) return;
    var ok = bolumler.filter(function (v) { return durum.okundu[v.dataset.view]; }).length;
    var q = { n: 0, d: 0, t: 0 };
    bolumler.forEach(function (v) { var b = say(v.dataset.view); q.n += b.n; q.d += b.d; q.t += b.toplam; });
    var bil = kartlar.filter(function (k) { return durum.kart[k.id]; }).length;
    var za = durum.za, fv = !formBos(durum.form || {});
    var var_ = ok || q.n || bil || za || fv;
    panel.hidden = !var_;
    if (!var_) return;
    function kutu(ad, deger, alt, adr) {
      return '<a class="ilerleme-kutu" href="' + adr + '"><span class="ik-ad">' + ad + '</span><span class="ik-deger">' + deger +
        '</span><span class="ik-alt">' + alt + "</span></a>";
    }
    $(".ilerleme-kutular", panel).innerHTML =
      kutu("Okunan oturum", ok + " / " + bolumler.length, ok ? "devam edin" : "henüz yok", "#/oturum-1") +
      kutu("Vaka soruları", q.d + " / " + q.t, q.n + " soru yanıtlandı", "#/tekrar") +
      kutu("Kavram kartları", bil + " / " + kartlar.length, "biliniyor", "#/kavramlar") +
      kutu("Zor anlar", za ? za.en + " / " + za.n : "–", za ? "en iyi skor" : "henüz oynanmadı", "#/zor-anlar") +
      kutu("Formülasyon", fv ? "Taslak var" : "–", fv ? "bu tarayıcıda kayıtlı" : "henüz başlanmadı", "#/formulasyon");
  }

  /* Atıf penceresi */
  var pop = $("#atif-pop"), aktifAtif = null;
  function atifKapat() {
    if (pop && !pop.hidden) { pop.hidden = true; if (aktifAtif && document.activeElement && pop.contains(document.activeElement)) aktifAtif.focus(); }
    aktifAtif = null;
  }
  function atifAc(a) {
    var li = document.getElementById(a.dataset.k);
    if (!li || !pop) return false;
    if (aktifAtif === a && !pop.hidden) { atifKapat(); return true; }
    var c = li.cloneNode(true), g = $(".kaynak-geri", c);
    if (g) g.remove();
    pop.innerHTML = "<p>" + c.innerHTML + '</p><p class="atif-alt"><a href="#/kaynakca" data-git="' + li.id +
      '">Kaynakçada gör</a><button type="button" class="atif-kapat">Kapat ✕</button></p>';
    pop.hidden = false;
    var r = a.getBoundingClientRect(), w = pop.offsetWidth, h = pop.offsetHeight, sx = window.scrollX, gen = document.documentElement.clientWidth;
    var ust = r.bottom + 8 + h > window.innerHeight && r.top - h - 8 > 64;
    pop.style.left = Math.max(12, Math.min(r.left, gen - w - 12)) + sx + "px";
    pop.style.top = window.scrollY + (ust ? r.top - h - 8 : r.bottom + 8) + "px";
    aktifAtif = a;
    return true;
  }

  /* Tıklamalar */
  document.addEventListener("click", function (e) {
    var t = e.target;
    var at = t.closest("a.atif");
    if (at && !e.ctrlKey && !e.metaKey) { if (atifAc(at)) e.preventDefault(); return; }
    var g = t.closest("[data-git]");
    if (g) {
      e.preventDefault();
      var hedef = document.getElementById(g.dataset.git);
      atifKapat();
      if (hedef) git(hedef.closest(".view"), hedef);
      return;
    }
    if (t.closest(".atif-kapat")) { atifKapat(); return; }
    if (pop && !pop.hidden && !t.closest("#atif-pop")) atifKapat();

    var sc = t.closest(".test-madde button[data-secenek]");
    if (sc && !sc.disabled) {
      var tm = sc.closest(".test-madde"), k = +sc.dataset.secenek, tb = testUygula(tm, k);
      if (tm.closest(".karisik-alan")) { kSonraki(tb); return; }
      var tv = tm.closest(".view").dataset.view;
      (durum.test[tv] = durum.test[tv] || {})[tm.dataset.no] = k;
      yaz();
      skorYaz(tv);
      return;
    }
    if (t.closest(".karisik-sonraki")) { kSira++; kGoster(); return; }
    var sf = t.closest("[data-test-sifirla]");
    if (sf) {
      var id = sf.getAttribute("data-test-sifirla");
      delete durum.test[id];
      yaz();
      $$("#v-" + id + " .adim-test .test-madde").forEach(testTemizle);
      skorYaz(id);
      return;
    }
    var ok = t.closest(".okundu");
    if (ok) {
      var o = ok.dataset.okundu;
      if (durum.okundu[o]) delete durum.okundu[o]; else durum.okundu[o] = true;
      yaz();
      ok.setAttribute("aria-pressed", durum.okundu[o] ? "true" : "false");
      durumGuncelle(o);
      return;
    }
    /* kavram kartları */
    if (t.closest(".bilgi-kart:not(.bitti)") && !t.closest("a")) { kartCevir(); return; }
    if (t.closest(".kart-biliyorum") || t.closest(".kart-tekrar")) {
      var kk = deste[dSira];
      if (t.closest(".kart-biliyorum")) durum.kart[kk.id] = 1;
      else { delete durum.kart[kk.id]; deste.splice(Math.min(deste.length, dSira + 4), 0, kk); }
      yaz();
      dSira++;
      kartCiz();
      var kartEl = $(".bilgi-kart", kSahne);
      if (kartEl) kartEl.focus();
      return;
    }
    if (t.closest(".kart-yeniden") || t.closest(".kart-karistir")) { kartBaslat(true); return; }
    if (t.closest(".kart-sifirla")) { durum.kart = {}; yaz(); kartBaslat(true); return; }
    /* zor anlar */
    var zb = t.closest("button[data-za]");
    if (zb && !zb.disabled) {
      var zc = zaListe[zaSira], zs = +zb.dataset.za, zDogru = zs === zc.dogru;
      if (zDogru) zaD++;
      $$("button[data-za]", zaAlan).forEach(function (b) {
        b.disabled = true;
        b.classList.toggle("secenek-dogru", +b.dataset.za === zc.dogru);
        b.classList.toggle("secenek-yanlis", b === zb && !zDogru);
      });
      var zo = $(".za-sonuc", zaAlan);
      zo.innerHTML = '<p><strong class="' + (zDogru ? "iyi" : "kotu") + '">' + (zDogru ? "✓ En uygun yanıt." : "✗ Daha uygun bir yanıt vardı.") +
        "</strong> " + zc.aciklama + '</p><p class="kucuk">İlgili oturum: <a href="#/oturum-' + zc.oturum + '">' + kacis(zc.otad) + "</a></p>" +
        '<button type="button" class="dugme za-sonraki">' + (zaSira + 1 < zaListe.length ? "Sonraki durum →" : "Sonucu gör") + "</button>";
      zo.hidden = false;
      $(".za-sonraki", zo).focus();
      return;
    }
    if (t.closest(".za-sonraki")) { zaSira++; zaGoster(); return; }
    /* formülasyon */
    var fo = t.closest(".form-ornek");
    if (fo) { formOrnek(fo); return; }
    var ft = t.closest(".form-temizle");
    if (ft) { formTemizle(ft); return; }
    if (t.closest(".form-kopyala")) { formKopyala(); return; }
    if (t.closest(".form-yazdir")) { formBaskiHazirla(); document.body.classList.add("baski-form"); window.print(); return; }
    /* tarama hazır ayarları */
    var ta = t.closest("button[data-tr-ayar]");
    if (ta) {
      trAyarla("p", ta.dataset.p); trAyarla("d", ta.dataset.d); trAyarla("o", ta.dataset.o);
      $$("button[data-tr-ayar]").forEach(function (b) { b.setAttribute("aria-pressed", b === ta ? "true" : "false"); });
      var tac = $(".tarama-aciklama");
      if (tac) tac.textContent = ta.dataset.aciklama;
      taramaCiz();
      return;
    }
    var hs = t.closest(".hepsini-sil");
    if (hs) {
      if (Date.now() - silOnay > 4000) { silOnay = Date.now(); hs.textContent = "Emin misiniz? Silmek için yeniden tıklayın"; return; }
      durum = { okundu: {}, test: {}, kart: {}, not: {}, form: {} };  /* za ve tarama da silinir */
      yaz();
      location.reload();
      return;
    }
    if (document.body.classList.contains("menu-acik") && !t.closest(".yan, .menu-dugme")) menuKapat();
    if (araS && !araS.hidden && !t.closest(".ara")) araS.hidden = true;
  });

  /* Kaynakça süzgeci */
  var ksuz = $("#kaynak-suz");
  if (ksuz) ksuz.addEventListener("input", function () {
    var q = katla(ksuz.value.trim()), n = 0;
    $$(".kaynaklar li").forEach(function (li) {
      var g = !q || katla(li.textContent).indexOf(q) >= 0;
      li.hidden = !g;
      if (g) n++;
    });
    $(".kaynak-sonuc").textContent = q ? n + " kaynak bulundu." : "";
  });

  /* Arama */
  var araK = $("#ara"), araS = $("#ara-sonuc"), dizin = null;
  function dizinKur() {
    dizin = $$("[data-ara]").filter(function (el) { return !el.closest(".karisik-alan") && el.closest(".view"); }).map(function (el) {
      var v = el.closest(".view"), adim = el.closest(".adim, .tema"), yer = baslik(v);
      if (adim) { var h = $("h3", adim); if (h) yer += " › " + h.textContent.trim(); }
      var t = el.textContent.replace(/\s+/g, " ").trim();
      return { el: el, v: v, yer: yer, t: t, k: katla(t) };
    });
  }
  function parcacik(d, terim) {
    var i = d.k.indexOf(terim);
    if (i < 0) i = 0;
    var bas = Math.max(0, i - 50), son = Math.min(d.t.length, i + terim.length + 110);
    return (bas ? "…" : "") + kacis(d.t.slice(bas, i)) + "<mark>" + kacis(d.t.slice(i, i + terim.length)) + "</mark>" +
      kacis(d.t.slice(i + terim.length, son)) + (son < d.t.length ? "…" : "");
  }
  function ara() {
    var q = araK.value.trim();
    if (q.length < 2) { araS.hidden = true; return; }
    if (!dizin) dizinKur();
    var terimler = katla(q).split(/\s+/).filter(Boolean), sonuc = [];
    for (var i = 0; i < dizin.length && sonuc.length < 40; i++) {
      var d = dizin[i];
      if (terimler.every(function (t) { return d.k.indexOf(t) >= 0; })) sonuc.push(i);
    }
    araS.innerHTML = sonuc.length ? sonuc.map(function (i) {
      return '<button type="button" data-i="' + i + '"><span class="yer">' + kacis(dizin[i].yer) + "</span>" + parcacik(dizin[i], terimler[0]) + "</button>";
    }).join("") + (sonuc.length === 40 ? '<p class="bos">İlk 40 sonuç gösteriliyor; aramayı daraltın.</p>' : "")
      : '<p class="bos">“' + kacis(q) + "” için sonuç yok.</p>";
    araS.hidden = false;
  }
  if (araK) {
    var zam = null;
    araK.addEventListener("input", function () { clearTimeout(zam); zam = setTimeout(ara, 120); });
    araK.addEventListener("focus", function () { if (araK.value.trim().length >= 2) ara(); });
    araK.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { araS.hidden = true; araK.blur(); }
      else if (e.key === "ArrowDown" || e.key === "Enter") { var b = $("button", araS); if (b && !araS.hidden) { e.preventDefault(); if (e.key === "Enter") b.click(); else b.focus(); } }
    });
    araS.addEventListener("keydown", function (e) {
      var bs = $$("button", araS), i = bs.indexOf(document.activeElement);
      if (e.key === "ArrowDown" && i < bs.length - 1) { e.preventDefault(); bs[i + 1].focus(); }
      else if (e.key === "ArrowUp") { e.preventDefault(); if (i > 0) bs[i - 1].focus(); else araK.focus(); }
      else if (e.key === "Escape") { araS.hidden = true; araK.focus(); }
    });
    araS.addEventListener("click", function (e) {
      var b = e.target.closest("button[data-i]");
      if (!b) return;
      var d = dizin[+b.dataset.i];
      araS.hidden = true;
      git(d.v, d.el);
    });
  }

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") { atifKapat(); menuKapat(); }
    if (e.key === "/" && !/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName) && araK) { e.preventDefault(); araK.focus(); }
  });

  /* Kayıtlı durumu geri yükle */
  Object.keys(durum.test).forEach(function (vid) {
    var v = document.getElementById("v-" + vid);
    if (!v) return;
    $$(".adim-test .test-madde", v).forEach(function (m) { var y = durum.test[vid][m.dataset.no]; if (y !== undefined && y !== null) testUygula(m, +y); });
  });
  gorunumler.forEach(function (v) {
    var vid = v.dataset.view, b = $(".okundu", v);
    if (b) b.setAttribute("aria-pressed", durum.okundu[vid] ? "true" : "false");
    skorYaz(vid);
  });

  rota();
})();

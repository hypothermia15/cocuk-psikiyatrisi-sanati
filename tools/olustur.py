# -*- coding: utf-8 -*-
"""Çocuk Psikiyatrisinin Sanatı · Okuma Rehberi: index.html üreticisi.

Kullanım:  python3 tools/olustur.py
Girdi:     tools/icerik_oturumlar.py, tools/icerik_araclar.py, tools/kaynaklar.json
Çıktı:     index.html (depo kökünde)
"""
import html
import json
import random
import re
import sys
import zlib
from pathlib import Path

ARACLAR = Path(__file__).resolve().parent
KOK = ARACLAR.parent
sys.path.insert(0, str(ARACLAR))

import icerik_araclar as A  # noqa: E402
import icerik_oturumlar as O  # noqa: E402
import icerik_simulasyon as SIM  # noqa: E402

KAYNAK = json.loads((ARACLAR / "kaynaklar.json").read_text(encoding="utf-8"))
KITAP = "williams2025"
KULLANIM = {}      # anahtar -> [(görünüm id, adım, etiket)]
BILINMEYEN = set()
BAGLAM = {"vid": "", "adim": "", "etiket": ""}
ADRES = "https://miracbarisusta.com/cocuk-psikiyatrisi-sanati/"
AD = "Çocuk Psikiyatrisinin Sanatı · Okuma Rehberi"


def esc(s):
    return html.escape(str(s), quote=True)


def atif(m):
    k = m.group(1)
    r = KAYNAK.get(k)
    if not r:
        BILINMEYEN.add(k)
        return esc(k)
    yer = (BAGLAM["vid"], BAGLAM["adim"], BAGLAM["etiket"])
    if yer[0] and yer not in KULLANIM.setdefault(k, []):
        KULLANIM[k].append(yer)
    return f'<a class="atif" href="#k-{k}" data-k="k-{k}">{esc(r["etiket"])}</a>'


def md(s):
    """Kaçış + **kalın**, *eğik*, [@atıf]."""
    t = esc(s)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    t = re.sub(r"\[@([\w-]+)\]", atif, t)
    return t


def md_html(s):
    """Açıklamalarda bilerek bırakılmış <a href="#/…"> bağlantılarına izin verir; geri kalan her şey kaçışlanır."""
    parcalar = re.split(r'(<a href="#/[\w/-]+">.*?</a>)', s)
    out = []
    for p in parcalar:
        m = re.fullmatch(r'<a href="(#/[\w/-]+)">(.*?)</a>', p)
        out.append(f'<a href="{m.group(1)}">{esc(m.group(2))}</a>' if m else md(p))
    return "".join(out)


def baglam(vid, adim="", etiket=""):
    BAGLAM.update(vid=vid, adim=adim, etiket=etiket)


HARF = "ABCD"


def view(vid, baslik, ust, ic, data_baslik=None, sinif=""):
    return (f'<section class="view {sinif}" id="v-{vid}" data-view="{vid}" data-baslik="{esc(data_baslik or baslik)}" '
            f'aria-label="{esc(data_baslik or baslik)}"><header class="oturum-bas"><p class="ust-baslik">{esc(ust)}</p>'
            f'<h2 tabindex="-1">{esc(baslik)}</h2></header>{ic}'
            f'<div class="oturum-son"><nav class="ileri-geri" aria-label="Oturumlar arasında"></nav></div></section>')


def adim(vid, anahtar, ikon, baslik, govde):
    sid = f"{vid}-{anahtar}"
    return (f'<section class="adim adim-{anahtar}" id="{sid}" aria-labelledby="{sid}-b"><h3 id="{sid}-b">'
            f'<span class="adim-ikon" aria-hidden="true">{ikon}</span> {esc(baslik)}</h3>{govde}</section>')


# Doğru şıkların yeri: bütün sorularda dengeli ve her derlemede aynı (yazım sırasındaki 2. şık eğilimini giderir).
# Tarayıcıda kayıtlı yanıtlar şık konumuyla saklandığı için ilk 42 sorunun yerleri dondurulmuştur (13 Kasım 2026 sürümü);
# sonradan eklenen sorular (yeni oturumlar) ayrı bir karıştırmayla yerleşir. Var olan bir oturuma soru eklemek ya da soruların
# sırasını değiştirmek, kayıtlı yanıtları bozar; yeni sorular yalnızca yeni oturumlara eklenmelidir.
ILK_SORU_SAYISI = 42
_tum_sorular = [q for o in O.OTURUMLAR for q in o["sorular"]]
assert len(_tum_sorular) >= ILK_SORU_SAYISI
_h1 = [0, 1, 2, 3] * (ILK_SORU_SAYISI // 4 + 1)
random.Random(20261113).shuffle(_h1)
_h2 = [0, 1, 2, 3] * ((len(_tum_sorular) - ILK_SORU_SAYISI) // 4 + 1)
random.Random(20261114).shuffle(_h2)
_hedefler = _h1[:ILK_SORU_SAYISI] + _h2
HEDEF = {id(q): _hedefler[i] for i, q in enumerate(_tum_sorular)}


def karistir_soru(q):
    """Doğru şıkkı hedef konuma taşır, diğer şıkların göreli sırasını korur."""
    sec = list(q["secenekler"])
    dogru = sec[q["dogru"]]
    digerleri = [s for i, s in enumerate(sec) if i != q["dogru"]]
    h = min(HEDEF.get(id(q), q["dogru"]), len(sec) - 1)
    yeni = digerleri[:h] + [dogru] + digerleri[h:]
    return yeni, h


def test_listesi(vid, sorular):
    out = [f'<p class="sina-ust"><span class="sina-skor" data-test-skor="{vid}" aria-live="polite"></span>'
           f'<button type="button" class="sina-sifirla" data-test-sifirla="{vid}" hidden>Yanıtları sil</button></p><ol class="test">']
    for i, q in enumerate(sorular):
        assert 0 <= q["dogru"] < len(q["secenekler"]) <= 4, q["soru"]
        sec, dogru = karistir_soru(q)
        btn = "".join(f'<button type="button" data-secenek="{k}"><span class="harf" aria-hidden="true">{HARF[k]}</span>'
                      f'<span>{md(s)}</span></button>' for k, s in enumerate(sec))
        out.append(f'<li class="test-madde" data-dogru="{dogru}" data-no="{i}" data-ara><p class="soru">{md(q["soru"])}</p>'
                   f'<div class="secenekler" role="group" aria-label="Seçenekler">{btn}</div>'
                   f'<div class="test-aciklama"><p><strong>Doğru yanıt: {HARF[dogru]}.</strong> {md_html(q["aciklama"])}</p></div></li>')
    out.append("</ol>")
    return "".join(out)


def crs_li(x):
    if x.startswith("TR "):
        return f'<li class="crs-tr" data-ara><span class="tr-rozet" title="Türkiye notu">TR</span> {md(x[3:])}</li>'
    return f"<li data-ara>{md(x)}</li>"


# ---------------------------------------------------------------- oturumlar
oturum_views = []
for o in O.OTURUMLAR:
    vid = f'oturum-{o["no"]}'
    etiket = f'Oturum {o["no"]}'
    parcalar = []
    baglam(vid, "okurken", etiket)
    parcalar.append(adim(vid, "okurken", "📖", "Kitapta ve okurken",
                         f'<p class="kitapta-bolum"><span>Kitapta</span> <i lang="en">{esc(o["kitapta_bolumler"])}</i></p>'
                         f'<p class="kitapta" data-ara>{md(o["kitapta"])}</p><p class="okurken-baslik">Okurken aklınızda tutun</p>'
                         f'<ol class="okurken">{"".join(f"<li data-ara>{md(q)}</li>" for q in o["okurken"])}</ol>'))
    baglam(vid, "fikirler", etiket)
    parcalar.append(adim(vid, "fikirler", "🧭", "Ana fikirler",
                         '<ol class="fikirler">' + "".join(
                             f'<li data-ara><p><strong>{md(h)}.</strong> {md(t)}</p></li>' for h, t in o["fikirler"]) + "</ol>"))
    baglam(vid, "crs", etiket)
    tr_say = sum(1 for x in o["crs"] if x.startswith("TR "))
    parcalar.append(adim(vid, "crs", "🧸", "ÇRS’de karşılığı",
                         ('<p class="not"><span class="tr-rozet">TR</span> etiketli maddeler Türkiye’deki uygulamaya özgüdür; '
                          'hepsi <a href="#/turkiye">Türkiye notları</a> sayfasında da toplandı.</p>' if tr_say else "")
                         + '<ul class="crs-liste">' + "".join(crs_li(x) for x in o["crs"]) + "</ul>"))
    baglam(vid, "tartisma", etiket)
    parcalar.append(adim(vid, "tartisma", "⚖️", "Tartışmaya açık",
                         '<p class="not">Kitabın önerileri ile güncel kanıt arasındaki farklar ve tartışmalı noktalar. '
                         'Künyeler kaynakçada; makaleler PubMed’den ya da yayıncı kayıtlarından doğrulandı.</p>'
                         '<div class="tartisma-liste">' + "".join(
                             f'<article class="tartisma" data-ara><h4>{md(h)}</h4><p>{md(t)}</p></article>'
                             for h, t in o["tartisma"]) + "</div>"))
    baglam(vid, "test", etiket)
    parcalar.append(adim(vid, "test", "✍️", "Vaka soruları",
                         '<p class="not">Vakalar kurgusaldır; kitabın vakalarından alınmamıştır.</p>' + test_listesi(vid, o["sorular"])))
    baglam(vid, "akilda", etiket)
    parcalar.append(adim(vid, "akilda", "🎯", "Akılda kalsın", f'<ul class="akilda"><li data-ara>{md(o["akilda"])}</li></ul>'))
    parcalar.append(adim(vid, "not", "🗒️", "Kendi notum",
                         f'<div class="vaka-not"><label for="{vid}-not-alan">Bu oturumu okurken aklınıza gelenler, kendi '
                         f'pratiğinizle bağlantılar</label><textarea id="{vid}-not-alan" data-not="{vid}" rows="4" '
                         f'placeholder="Hasta kimlik bilgisi yazmayın."></textarea><p class="kucuk">Yazdıklarınız yalnızca bu '
                         f'tarayıcıda saklanır.</p></div>'))
    adimlar_nav = [("okurken", "📖", "Okurken"), ("fikirler", "🧭", "Ana fikirler"), ("crs", "🧸", "ÇRS’de"),
                   ("tartisma", "⚖️", "Tartışma"), ("test", "✍️", "Sorular"), ("akilda", "🎯", "Akılda kalsın"),
                   ("not", "🗒️", "Notum")]
    nav = ('<nav class="adimlar" aria-label="Bu oturumun kısımları">' + "".join(
        f'<a href="#/{vid}/{k}"><span aria-hidden="true">{i}</span> {esc(s)}</a>' for k, i, s in adimlar_nav) + "</nav>")
    bas = (f'<header class="oturum-bas"><p class="ust-baslik">{esc(O.KESIMLER[o["kesim"]])} · Oturum {o["no"]}</p>'
           f'<h2 tabindex="-1">{esc(o["baslik"])}</h2><p class="slogan">{md(o["slogan"])}</p></header>')
    html_ = (f'<section class="view bolum" id="v-{vid}" data-view="{vid}" data-baslik="Oturum {o["no"]}: {esc(o["kisa"])}" '
             f'aria-label="Oturum {o["no"]}">{bas}{nav}{"".join(parcalar)}'
             f'<div class="oturum-son"><button type="button" class="okundu" data-okundu="{vid}" aria-pressed="false">'
             f'Bu oturumu okudum</button><nav class="ileri-geri" aria-label="Oturumlar arasında"></nav></div></section>')
    oturum_views.append(dict(id=vid, no=o["no"], kesim=o["kesim"], kisa=o["kisa"], baslik=o["baslik"], slogan=o["slogan"],
                             kitapta=o["kitapta_bolumler"], html=html_, n_tart=len(o["tartisma"]), n_soru=len(o["sorular"]),
                             tr=tr_say))
# Görünüm sırası kesim sırasını izler (B, C, D, E, F, R); oturum numaraları ve kayıtlı yanıtlar değişmez.
KESIM_SIRA = list(O.KESIMLER)
oturum_views.sort(key=lambda v: (KESIM_SIRA.index(v["kesim"]), v["no"]))
OTURUM_SIRALI = sorted(O.OTURUMLAR, key=lambda o: (KESIM_SIRA.index(o["kesim"]), o["no"]))
OTAD = {v["no"]: f'Oturum {v["no"]} · {v["kisa"]}' for v in oturum_views}

# ---------------------------------------------------------------- tarama hesaplayıcısı
baglam("tarama", "", "Tarama hesaplayıcısı")
ayar_btn = "".join(
    f'<button type="button" class="filtre" data-tr-ayar="{k}" data-p="{p}" data-d="{d}" data-o="{o}" '
    f'data-aciklama="{esc(ac)}" aria-pressed="{"true" if i == 0 else "false"}">{esc(ad)}</button>'
    for i, (k, ad, p, d, o, ac) in enumerate(A.TARAMA_AYARLAR))
k0 = A.TARAMA_AYARLAR[0]
GIRDI = [("p", "Yaygınlık (ön olasılık)", "0.1", "60", "0.1", k0[2]),
         ("d", "Duyarlılık", "50", "99.9", "0.1", k0[3]),
         ("o", "Özgüllük", "50", "99.9", "0.1", k0[4])]
girdiler = "".join(
    f'<div class="tg"><label for="tr-{k}">{esc(ad)}</label><div class="tg-satir">'
    f'<input type="range" data-tr-r="{k}" min="{mn}" max="{mx}" step="{st}" value="{v}" aria-label="{esc(ad)} kaydırıcı">'
    f'<span class="tg-sayi"><input type="number" id="tr-{k}" data-tr="{k}" min="{mn}" max="{mx}" step="{st}" value="{v}" '
    f'inputmode="decimal"><span aria-hidden="true">%</span></span></div></div>' for k, ad, mn, mx, st, v in GIRDI)
GIRDI2 = [("d2", "İkinci testin duyarlılığı", "50", "99.9", "0.1", 90),
          ("o2", "İkinci testin özgüllüğü", "50", "99.9", "0.1", 90)]
girdiler2 = "".join(
    f'<div class="tg"><label for="tr-{k}">{esc(ad)}</label><div class="tg-satir">'
    f'<input type="range" data-tr-r="{k}" min="{mn}" max="{mx}" step="{st}" value="{v}" aria-label="{esc(ad)} kaydırıcı">'
    f'<span class="tg-sayi"><input type="number" id="tr-{k}" data-tr="{k}" min="{mn}" max="{mx}" step="{st}" value="{v}" '
    f'inputmode="decimal"><span aria-hidden="true">%</span></span></div></div>' for k, ad, mn, mx, st, v in GIRDI2)


def ol_satir(k, ad):
    return (f'<div class="ol-satir"><span class="ol-ad">{esc(ad)}</span><span class="ol-cubuk"><span class="ol-dolu ol-{k}" '
            f'data-ol="{k}"></span></span><span class="ol-deger" data-old="{k}">–</span></div>')


olasilik = ('<div class="olasilik" role="img" aria-label="Test öncesi ve sonrası olasılık"><p class="olasilik-baslik">Olasılık nasıl değişiyor?</p>'
            + ol_satir("once", "Testten önce") + ol_satir("poz", "Test pozitifse") + ol_satir("neg", "Test negatifse")
            + '<div class="ol-olcek" aria-hidden="true"><span>%0</span><span>%25</span><span>%50</span><span>%75</span><span>%100</span></div></div>')
tarama_ic = (f'<p class="giris-metin" data-ara>{md(A.TARAMA_GIRIS)}</p>'
             '<div class="tarama" id="tarama-hesap">'
             f'<div class="tarama-ayarlar" role="group" aria-label="Hazır örnekler">{ayar_btn}</div>'
             f'<p class="tarama-aciklama kucuk" aria-live="polite">{esc(k0[5])}</p>'
             f'<div class="tarama-girdiler">{girdiler}</div>'
             '<div class="tarama-kpi">'
             '<div class="kpi"><span class="kpi-ad">Pozitif öngörü değeri</span><span class="kpi-deger" data-c="ppv">–</span>'
             '<span class="kpi-alt">Pozitiflerin gerçekten hasta olanı</span></div>'
             '<div class="kpi"><span class="kpi-ad">Negatif öngörü değeri</span><span class="kpi-deger" data-c="npv">–</span>'
             '<span class="kpi-alt">Negatiflerin gerçekten sağlıklı olanı</span></div>'
             '<div class="kpi"><span class="kpi-ad">Pozitif olabilirlik oranı</span><span class="kpi-deger" data-c="lr">–</span>'
             '<span class="kpi-alt">Pozitif sonucun olasılığı ne kadar artırdığı</span></div>'
             '<div class="kpi"><span class="kpi-ad">Negatif olabilirlik oranı</span><span class="kpi-deger" data-c="lrn">–</span>'
             '<span class="kpi-alt">Negatif sonucun olasılığı ne kadar azalttığı</span></div></div>'
             '<p class="tarama-cumle" aria-live="polite"></p>'
             + olasilik +
             '<div class="tablo-kap"><table class="tablo tarama-tablo"><caption class="gizli">1000 çocukta test sonuçları</caption>'
             '<thead><tr><th scope="col">1000 çocuk</th><th scope="col">Durum var</th><th scope="col">Durum yok</th><th scope="col">Toplam</th></tr></thead>'
             '<tbody><tr><th scope="row">Test pozitif</th><td data-label="Durum var" data-h="gp" class="h-gp"></td>'
             '<td data-label="Durum yok" data-h="yp" class="h-yp"></td><td data-label="Toplam" data-h="poz"></td></tr>'
             '<tr><th scope="row">Test negatif</th><td data-label="Durum var" data-h="yn" class="h-yn"></td>'
             '<td data-label="Durum yok" data-h="gn" class="h-gn"></td><td data-label="Toplam" data-h="neg"></td></tr>'
             '<tr><th scope="row">Toplam</th><td data-label="Durum var" data-h="hasta"></td><td data-label="Durum yok" data-h="saglam"></td>'
             '<td data-label="Toplam">1000</td></tr></tbody></table></div>'
             '<div class="izgara-ust"><span class="kucuk">1000 çocuk; her kare bir çocuk.</span>'
             '<span class="izgara-sira" role="group" aria-label="Kareleri sırala">'
             '<button type="button" class="filtre" data-sira="durum" aria-pressed="true">Duruma göre</button>'
             '<button type="button" class="filtre" data-sira="sonuc" aria-pressed="false">Test sonucuna göre</button></span></div>'
             '<div class="tarama-izgara" aria-hidden="true"></div>'
             '<ul class="tarama-lejant"><li><span class="lj lj-gp"></span>Gerçek pozitif</li><li><span class="lj lj-yp"></span>Yanlış pozitif</li>'
             '<li><span class="lj lj-yn"></span>Yanlış negatif</li><li><span class="lj lj-gn"></span>Gerçek negatif</li></ul>'
             '<details class="ikinci-test"><summary>Pozitif çıkanlara ikinci bir test uygulanırsa ne olur?</summary>'
             '<p class="kucuk">Seri test: yalnızca ilk testte pozitif çıkan çocuklara ikinci bir test uygulanır; iki test de pozitifse sonuç '
             'pozitif sayılır.</p>'
             f'<div class="tarama-girdiler tarama-girdiler-2">{girdiler2}</div>'
             '<p class="ikinci-cumle" aria-live="polite"></p>'
             '<p class="not">İki testin hatalarının birbirinden bağımsız olduğu varsayılır. Aynı belirtilere dayanan iki ölçek benzer '
             'hatalar yapar; gerçek kazanç bu hesaplananın altında kalır.</p></details>'
             '<p class="sim-js-yok">Hesaplayıcı için tarayıcıda JavaScript açık olmalı. Örnek: yaygınlık %2, duyarlılık ve özgüllük %80 '
             'ise 1000 çocukta 16 gerçek pozitif ve 196 yanlış pozitif olur; pozitiflerin yalnızca %7,5’i gerçekten hastadır.</p>'
             '<p class="not">Değerler varsayımsaldır ve gerçek bir testin özelliklerini yansıtmaz. Sayılar yuvarlanmıştır.</p></div>'
             '<h3 class="tekrar-baslik"><span aria-hidden="true">🎯</span> Akılda kalsın</h3><ul class="akilda">'
             + "".join(f"<li data-ara>{md(x)}</li>" for x in A.TARAMA_AKILDA) + "</ul>")
tarama = dict(id="tarama", label="Tarama hesaplayıcısı",
              html=view("tarama", "Tarama hesaplayıcısı: 1000 çocukta ne olur?", "Araçlar", tarama_ic,
                        data_baslik="Tarama hesaplayıcısı"))

# ---------------------------------------------------------------- zor anlar
baglam("zor-anlar", "", "Zor anlar")
for d, s, dg, ac, ot in A.ZOR_ANLAR:
    assert len(s) == 4 and 0 <= dg < 4 and ot in OTAD, d
za_li = "".join(
    f'<li data-dogru="{dg}" data-oturum="{ot}" data-otad="{esc(OTAD[ot])}"><p class="za-durum">{md(d)}</p>'
    + "".join(f'<span class="za-secenek">{md(x)}</span>' for x in s)
    + f'<p class="za-aciklama">{md(ac)}</p></li>' for d, s, dg, ac, ot in A.ZOR_ANLAR)
za_ic = ('<p class="giris-metin">Görüşme, aile, sürtüşme ve açıklama oturumlarındaki ilkeleri kurgusal durumlarda deneyin. Her durumda en uygun '
         f'yanıtı seçin; açıklama ve ilgili oturum hemen ardından açılır. {len(A.ZOR_ANLAR)} durum, karışık sırayla.</p>'
         '<div class="tahmin za-oyun" id="za-oyun"><h3><span aria-hidden="true">🧯</span> Zor anlar</h3>'
         '<div class="za-alan" aria-live="polite"></div>'
         '<button type="button" class="dugme za-basla">Başlat</button>'
         '<p class="sim-js-yok">Bu alıştırma için tarayıcıda JavaScript açık olmalı.</p>'
         f'<ol class="za-veri" hidden>{za_li}</ol></div>'
         '<h3 class="tekrar-baslik"><span aria-hidden="true">🎯</span> Bu alıştırmanın ilkeleri</h3><ul class="akilda">'
         '<li data-ara>Önce duyguyu adlandırın, sonra soruyu sorun, en son bilgiyi verin.</li>'
         '<li data-ara>Reddederken anlayış, gerekçe ve bir alternatif sunun.</li>'
         '<li data-ara>Çatışmalı ailede taraf değil, çocuğun çıkarının sözcüsü olun.</li>'
         '<li data-ara>Hata yaptıysanız hızlı ve içten bir özür, savunmadan daha çok şey onarır.</li></ul>'
         '<p class="not">Durumlar kurgusaldır ve ilkeleri tartışmak için sadeleştirilmiştir; gerçek klinikte tek bir doğru yanıt nadirdir.</p>')
zor_anlar = dict(id="zor-anlar", label="Zor anlar", html=view("zor-anlar", "Zor anlar: en uygun yanıt hangisi?", "Araçlar", za_ic,
                                                              data_baslik="Zor anlar"))

# ---------------------------------------------------------------- vaka simülasyonu
baglam("simulasyon", "", "Vaka simülasyonu")


def sim_dogrula(s):
    """Hedefler var mı, puanlar geçerli mi, her sahneye ulaşılıyor mu, döngü var mı? En uzun karar yolunu döndürür."""
    sah = s["sahneler"]
    assert s["baslangic"] in sah, s["id"]
    assert all(n in OTAD for n in s["oturumlar"]), s["id"]
    for sid, x in sah.items():
        if "son" in x:
            assert x["son"] in ("iyi", "orta", "kotu") and x["baslik"] and x["metin"], (s["id"], sid)
            continue
        assert 2 <= len(x["secenekler"]) <= 4, (s["id"], sid)
        for metin, hedef, puan, gb in x["secenekler"]:
            assert hedef in sah and hedef != sid, (s["id"], sid, hedef)
            assert puan in SIM.PUAN_ETIKET and metin and gb, (s["id"], sid, puan)
    gorulen = set()

    def gez(sid, yigin):
        assert sid not in yigin, ("döngü", s["id"], sid)
        gorulen.add(sid)
        x = sah[sid]
        if "son" in x:
            return 0
        return 1 + max(gez(h, yigin | {sid}) for _, h, _, _ in x["secenekler"])
    en_uzun = gez(s["baslangic"], frozenset())
    assert gorulen == set(sah), ("ulaşılamayan sahne", s["id"], set(sah) - gorulen)
    assert any(x.get("son") == "iyi" for x in sah.values()), s["id"]
    return en_uzun


sim_veri, sim_kartlar = [], []
for s in SIM.SIMULASYONLAR:
    sim_dogrula(s)
    sahneler = {}
    for sid, x in s["sahneler"].items():
        if "son" in x:
            sahneler[sid] = {"son": x["son"], "baslik": esc(x["baslik"]), "metin": md(x["metin"])}
        else:
            sahneler[sid] = {"metin": md(x["metin"]), "secenekler": [[md(m), h, p, md(g)] for m, h, p, g in x["secenekler"]]}
    sim_veri.append({"id": s["id"], "baslik": esc(s["baslik"]), "baslangic": s["baslangic"], "sahneler": sahneler,
                     "oturumlar": [[n, esc(OTAD[n])] for n in s["oturumlar"]],
                     "sonSayi": sum(1 for x in s["sahneler"].values() if "son" in x)})
    bag = ", ".join(f'<a href="#/oturum-{n}">Oturum {n}</a>' for n in s["oturumlar"])
    sim_kartlar.append(f'<li class="sim-kart" data-ara><h3>{esc(s["baslik"])}</h3><p>{md(s["ozet"])}</p>'
                       f'<p class="ders-ref">İlgili oturumlar: {bag}</p><p class="sim-kart-durum kucuk" data-sim-durum="{s["id"]}"></p>'
                       f'<button type="button" class="dugme sim-basla" data-sim="{s["id"]}">Vakayı başlat</button></li>')
sim_json = json.dumps({"puan": {str(k): v for k, v in SIM.PUAN_ETIKET.items()}, "vakalar": sim_veri},
                      ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
sim_ic = (f'<p class="giris-metin">{len(SIM.SIMULASYONLAR)} kurgusal vakada kararları siz veriyorsunuz. Vaka seçtiğiniz yola göre dallanır '
          've farklı sonlara varır. Her karardan sonra seçiminizin gerekçesini, vakanın sonunda da izlediğiniz yolu puanlarıyla '
          'görürsünüz. Dilediğiniz karara dönüp başka bir yolu deneyebilirsiniz.</p>'
          '<p class="sim-lejant"><span class="sp sp-2">En uygun</span><span class="sp sp-1">Kabul edilebilir</span>'
          '<span class="sp sp-0">Zayıf</span><span class="sp sp-n">Zarar verebilir</span></p>'
          f'<div class="vs" id="sim"><ol class="sim-liste">{"".join(sim_kartlar)}</ol>'
          '<div class="sim-oyun" hidden></div>'
          '<p class="sim-js-yok">Simülasyon için tarayıcıda JavaScript açık olmalı.</p></div>'
          f'<script type="application/json" id="sim-veri">{sim_json}</script>'
          '<h3 class="tekrar-baslik"><span aria-hidden="true">🎯</span> Simülasyonların ilkeleri</h3><ul class="akilda">'
          '<li data-ara>Önce çerçeveyi kurun: kiminle, hangi sırayla konuşacaksınız ve gizliliğin sınırı nerede?</li>'
          '<li data-ara>Riski doğrudan sorun; dolaylı sorular dolaylı yanıtlar getirir.</li>'
          '<li data-ara>İsteğin altındaki ihtiyacı bulun; reddederken bir alternatif sunun.</li>'
          '<li data-ara>Devralınan tanı bir hipotezdir: zaman seyriyle sınayın, meslektaşı suçlamadan güncelleyin.</li></ul>'
          '<p class="not">Vakalar kurgusaldır ve ilkeleri tartışmak için sadeleştirilmiştir; kitabın vakalarından alınmamıştır. Puanlar '
          'öğretim amaçlıdır. Gerçek klinikte çoğu zaman birden fazla makul yol vardır ve kararlar kurumunuzun protokollerine göre verilir.</p>')
simulasyon = dict(id="simulasyon", label="Vaka simülasyonu",
                  html=view("simulasyon", "Vaka simülasyonu: kararları siz verin", "Araçlar", sim_ic, data_baslik="Vaka simülasyonu"))

# ---------------------------------------------------------------- formülasyon çalışma sayfası
baglam("formulasyon", "", "Formülasyon çalışma sayfası")
bolum_html = []
for fid, fbas, fipucu, alanlar in A.FORM_BOLUMLER:
    ic = []
    for k, et, tur, ek in alanlar:
        if tur == "metin":
            ic.append(f'<label class="alt-etiket" for="f-{k}">{esc(et)}</label><textarea id="f-{k}" data-form="{k}" rows="{ek}"></textarea>')
        elif tur == "satir":
            ic.append(f'<label class="alt-etiket" for="f-{k}">{esc(et)}</label><input id="f-{k}" type="text" data-form="{k}" placeholder="{esc(ek)}">')
        elif tur == "secim":
            kutu = "".join(f'<label class="secim"><input type="checkbox" value="{esc(x)}"> {esc(x)}</label>' for x in ek)
            sayac = '<p class="kaynak-sayi kucuk" aria-live="polite"></p>' if k == "kaynak" else ""
            ic.append(f'<div class="secim-grup" data-form-grup="{k}" role="group" aria-label="{esc(et)}">{kutu}</div>{sayac}')
        elif tur == "ayirici":
            satir = []
            for i in range(1, ek + 1):
                yer = "Belirgin bir bozukluk yok / normal varyant" if i == ek else f"Seçenek {i}"
                satir.append(f'<div class="dd-satir"><label class="gizli" for="dd-ad-{i}">Seçenek {i}</label>'
                             f'<input class="dd-ad" id="dd-ad-{i}" type="text" placeholder="{esc(yer)}">'
                             f'<label class="gizli" for="dd-y-{i}">Seçenek {i} olasılığı (yüzde)</label>'
                             f'<input class="dd-yuzde" id="dd-y-{i}" type="number" min="0" max="100" step="1" inputmode="numeric" placeholder="%"></div>')
            ic.append(f'<div class="dd">{"".join(satir)}</div><p class="dd-toplam" aria-live="polite">Toplam: –</p>')
        elif tur == "dongu":
            halka = "".join(f'<div class="dongu-kutu"><label class="gizli" for="dg-{i}">Halka {i}</label>'
                            f'<textarea class="dongu-halka" id="dg-{i}" rows="3" placeholder="Halka {i}"></textarea></div>'
                            + ('<span class="dongu-ok" aria-hidden="true">→</span>' if i < ek else
                               '<span class="dongu-ok dongu-don" aria-hidden="true">↺ başa döner</span>')
                            for i in range(1, ek + 1))
            ic.append(f'<div class="dongu-izgara">{halka}</div>')
    bolum_html.append(f'<fieldset class="form-alan form-bolum" id="fb-{fid}"><legend><span class="fb-ad">{esc(fbas)}</span></legend>'
                      f'<p class="form-ipucu">{esc(fipucu)}</p>{"".join(ic)}</fieldset>')
form_ic = ('<p class="giris-metin">Kendi vakanızı oturumlardaki araçlarla düşünmek için bir çalışma kâğıdı: zaman seyri, bağımsız '
           'kaynaklar, dört P, olasılıkları %100’e tamamlanan ayırıcı tanı, kısır döngü ve ölçülebilir hedef. Doldurdukça otomatik '
           'kaydedilir; yazdırabilir ya da PDF olarak kaydedebilirsiniz.</p>'
           '<aside class="uyari"><strong>Gerçek hasta bilgisi girmeyin.</strong> Ad, doğum tarihi, okul ya da adres gibi kimliği belli '
           'eden bilgiler yazmayın. Veriler yalnızca bu tarayıcıda saklanır, sunucuya gönderilmez.</aside>'
           '<div class="form-dugmeler"><button type="button" class="dugme dugme-ikincil form-ornek">Örnek vakayı yükle</button>'
           '<button type="button" class="dugme form-yazdir">Yazdır / PDF</button>'
           '<button type="button" class="dugme dugme-ikincil form-kopyala">Metni kopyala</button>'
           '<button type="button" class="sina-sifirla form-temizle">Formu temizle</button>'
           '<span class="form-durum kucuk" aria-live="polite"></span></div>'
           f'<p class="kucuk form-ornek-ad">Örnek: {esc(A.FORM_ORNEK_AD)}</p>'
           f'<form class="formulasyon" id="formulasyon" autocomplete="off" data-ornek="{esc(json.dumps(A.FORM_ORNEK, ensure_ascii=False))}">'
           f'{"".join(bolum_html)}</form>'
           '<div class="form-baski" aria-hidden="true"></div>')
formulasyon = dict(id="formulasyon", label="Formülasyon çalışma sayfası",
                   html=view("formulasyon", "Formülasyon çalışma sayfası", "Araçlar", form_ic))

# ---------------------------------------------------------------- kavram kartları
baglam("kavramlar", "", "Kavram kartları")
kav_li = []
for i, (terim, tanim, ornek, ots) in enumerate(A.KAVRAMLAR):
    assert all(n in OTAD for n in ots), terim
    bag = ", ".join(f'<a href="#/oturum-{n}">Oturum {n}</a>' for n in ots)
    kav_li.append(f'<li class="kavram" id="kavram-{i}" data-id="kavram-{i}" data-ara><p class="kavram-terim">{esc(terim)}</p>'
                  f'<p class="kavram-tanim">{md(tanim)}</p><p class="kavram-ornek"><span class="guncel-etiket">ÇRS’de</span> '
                  f'{md(ornek)}</p><p class="ders-ref">{bag}</p></li>')
kavram_ic = ('<p class="giris-metin">Rehberdeki temel kavramlar, kendi tanımlarımızla. Kartı çevirin, bildiklerinizi işaretleyin. '
             'Kartlar aralıklı tekrarla sıralanır: bilmedikleriniz ve tekrar zamanı gelenler önce gelir, bildikleriniz giderek daha seyrek '
             'sorulur. Boşluk tuşu kartı çevirir.</p>'
             '<div class="kart-araclar"><button type="button" class="dugme dugme-ikincil kart-karistir">Karıştır</button>'
             '<button type="button" class="sina-sifirla kart-sifirla">Bilinenleri sıfırla</button></div>'
             '<div class="kart-sahne" aria-live="polite"></div><p class="kart-ilerleme"></p>'
             '<p class="sim-js-yok">Kartlar için tarayıcıda JavaScript açık olmalı; aşağıdaki sözlük JavaScript olmadan da okunur.</p>'
             f'<h3 class="tekrar-baslik">Kavram sözlüğü <span class="sayi">{len(A.KAVRAMLAR)}</span></h3>'
             f'<ul class="kavramlar">{"".join(kav_li)}</ul>')
kavramlar = dict(id="kavramlar", label="Kavram kartları", html=view("kavramlar", "Kavram kartları", "Araçlar", kavram_ic))

# ---------------------------------------------------------------- Türkiye notları
baglam("turkiye", "", "Türkiye notları")
tr_bloklar = []
for o in OTURUM_SIRALI:
    maddeler = [x[3:] for x in o["crs"] if x.startswith("TR ")]
    if not maddeler:
        continue
    tr_bloklar.append(f'<section class="tema" aria-labelledby="tr-{o["no"]}-b"><h3 id="tr-{o["no"]}-b"><span class="tema-no">{o["no"]}</span> '
                      f'<a href="#/oturum-{o["no"]}/crs">{esc(o["kisa"])}</a></h3><ul class="crs-liste">'
                      + "".join(f"<li data-ara>{md(m)}</li>" for m in maddeler) + "</ul></section>")
sozluk = "".join(f'<div class="tr-terim" data-ara><dt>{esc(t)}</dt><dd>{md(a)}</dd></div>' for t, a in A.TURKIYE_SOZLUK)
turkiye_ic = (f'<p class="giris-metin" data-ara>{md(A.TURKIYE_GIRIS)}</p>'
              f'<h3 class="tekrar-baslik">Sistem sözlüğü</h3><dl class="tr-sozluk">{sozluk}</dl>'
              f'<h3 class="tekrar-baslik">Oturumlara göre notlar <span class="sayi">{sum(v["tr"] for v in oturum_views)}</span></h3>'
              + "".join(tr_bloklar))
turkiye = dict(id="turkiye", label="Türkiye notları",
               html=view("turkiye", "Türkiye notları: kitabı buradaki kliniğe taşımak", "Araçlar", turkiye_ic,
                         data_baslik="Türkiye notları"))

# ---------------------------------------------------------------- tekrar
baglam("tekrar", "", "Karışık test")
n_soru = sum(len(o["sorular"]) for o in O.OTURUMLAR)
akil = "".join(f'<li><a href="#/oturum-{o["no"]}">Oturum {o["no"]}</a> {md(o["akilda"])}</li>' for o in OTURUM_SIRALI)
LT_KUTU = [("0", "Yeniden", "aynı gün"), ("1", "Kutu 1", "1 gün sonra"), ("2", "Kutu 2", "3 gün sonra"),
           ("3", "Kutu 3", "7 gün sonra"), ("4", "Kutu 4", "21 gün sonra")]
lt_kutular = "".join(f'<li class="lt-kutu lt-k{k}"><span class="lt-ad">{ad}</span><span class="lt-sayi" data-lt-kutu="{k}">0</span>'
                     f'<span class="lt-aralik">{ar}</span></li>' for k, ad, ar in LT_KUTU)
tekrar_ic = ('<div class="lt-panel" id="lt-panel"><h3><span aria-hidden="true">🗓️</span> Aralıklı tekrar</h3>'
             '<p>Yanıtladığınız vaka soruları ve işaretlediğiniz kavram kartları beş kutuda izlenir. Bildiğiniz bir madde bir üst kutuya '
             'çıkar ve giderek daha seyrek sorulur; bilemediğiniz madde ilk kutuya döner ve aynı gün yeniden gelir. Her gün yalnızca tekrar '
             'zamanı gelenleri çalışmak yeterlidir.</p>'
             f'<ol class="lt-kutular" aria-label="Kutulara göre madde sayısı">{lt_kutular}</ol>'
             '<p class="lt-bilgi" aria-live="polite"></p></div>'
             '<div class="karisik" id="karisik"><h3><span aria-hidden="true">🎲</span> Karışık test</h3>'
             f'<p>Bütün oturumların {n_soru} vaka sorusu ya da yalnızca tekrar zamanı gelenler, karışık sırayla. Yanıtınızı verin; açıklama '
             'hemen ardından açılır. Yanıtlarınız aralıklı tekrar kutularını günceller.</p>'
             '<div class="karisik-alan" aria-live="polite"></div><p class="karisik-dugmeler">'
             f'<button type="button" class="dugme karisik-basla" data-tur="test">Bütün sorular ({n_soru})</button>'
             '<button type="button" class="dugme dugme-ikincil karisik-basla" data-tur="vade">Bugünün tekrarı</button>'
             '<button type="button" class="dugme dugme-ikincil karisik-basla" data-tur="yanlis">Yanlışlarım</button>'
             '<a class="dugme dugme-ikincil lt-kart-bag" href="#/kavramlar">Kavram kartları</a></p></div>'
             '<h3 class="tekrar-baslik"><span aria-hidden="true">🎯</span> Akılda kalsın: oturum oturum</h3>'
             f'<ul class="akilda akilda-kucuk akilda-liste">{akil}</ul>')
tekrar = dict(id="tekrar", label="Karışık test", html=view("tekrar", "Karışık test ve aralıklı tekrar", "Araçlar", tekrar_ic,
                                                           data_baslik="Karışık test ve tekrar"))

# ---------------------------------------------------------------- giriş
baglam("giris", "", "Giriş")
kesim_kartlari = {k: [] for k in O.KESIMLER}
for v in oturum_views:
    kesim_kartlari[v["kesim"]].append(
        f'<li><a class="kart" href="#/{v["id"]}" data-kart="{v["id"]}"><span class="kart-no" aria-hidden="true">{v["no"]}</span>'
        f'<span class="kart-govde"><span class="kart-ust">Oturum {v["no"]}</span><span class="kart-baslik">{esc(v["baslik"])}</span>'
        f'<span class="kart-slogan">{md(v["slogan"])}</span><span class="kart-meta">{v["n_tart"]} tartışma noktası · '
        f'{v["n_soru"]} vaka sorusu</span><span class="kart-durum" data-durum="{v["id"]}"></span></span></a></li>')
kesim_bolumleri = "".join(
    f'<section aria-labelledby="kes-{k}-b"><h2 id="kes-{k}-b" class="bolum-baslik">{esc(ad)}</h2><ol class="kartlar">'
    f'{"".join(kesim_kartlari[k])}</ol></section>' for k, ad in O.KESIMLER.items())
arac_kartlari = "".join(
    f'<li><a class="kart kart-arac" href="#/{i}"><span class="kart-no" aria-hidden="true">{ik}</span><span class="kart-govde">'
    f'<span class="kart-baslik">{esc(ad)}</span><span class="kart-slogan">{esc(ac)}</span></span></a></li>'
    for i, ik, ad, ac in [
        ("tarama", "🧮", "Tarama hesaplayıcısı", "Yaygınlık, duyarlılık ve özgüllükle 1000 çocukta ne olduğunu görün."),
        ("zor-anlar", "🧯", "Zor anlar", f"{len(A.ZOR_ANLAR)} kurgusal durumda en uygun yanıtı seçin."),
        ("simulasyon", "🎭", "Vaka simülasyonu", f"{len(SIM.SIMULASYONLAR)} dallanan vakada kararları siz verin; her yol başka bir sona varır."),
        ("formulasyon", "✎", "Formülasyon çalışma sayfası", "Zaman seyri, dört P, %100 ayırıcı tanı ve kısır döngü; yazdırılabilir."),
        ("kavramlar", "🃏", "Kavram kartları", f"{len(A.KAVRAMLAR)} temel kavram, kendi tanımlarımızla; aralıklı tekrarla."),
        ("turkiye", "🇹🇷", "Türkiye notları", "e-Nabız, ÇÖZGER, RAM ve diğer yerel konular tek sayfada."),
        ("tekrar", "🎲", "Karışık test ve tekrar", f"{n_soru} vaka sorusu; bildikleriniz seyrek, bilemedikleriniz sık sorulur."),
    ])
giris_ic = f"""
<div class="kahraman">
  <p class="ust-baslik"><span lang="en">Jonathan Williams · Peter Hill</span> · <i lang="en">The Art of Child and Adolescent Psychiatry</i> · <span lang="en">Cambridge</span>, 2025</p>
  <h1 tabindex="-1">Çocuk Psikiyatrisinin Sanatı</h1>
  <p class="alt-baslik">Okuma rehberi: görüşmeden formülasyona, oturum oturum</p>
  <p class="kahraman-metin" data-ara>Bu rehber, Williams ve Hill’in klinik bilgelik kitabını ({md("[@williams2025]")}) çocuk ve ergen ruh
  sağlığı ve hastalıkları (ÇRS) pratiğine çevirerek okumak için hazırlandı. Her oturumda okurken sorulacak sorular, ana fikirler,
  ÇRS’deki ve Türkiye’deki karşılığı, güncel kanıtla tartışmaya açık noktalar ve kurgusal vaka soruları var.</p>
  <p class="kahraman-dugmeler"><a class="dugme" href="#/oturum-1">Oturum 1’den başla <span aria-hidden="true">→</span></a>
  <a class="dugme dugme-ikincil" href="#/simulasyon">Vaka simülasyonu</a> <a class="dugme dugme-ikincil" href="#/tarama">Tarama hesaplayıcısı</a>
  <a class="dugme dugme-ikincil" href="#/zor-anlar">Zor anlar</a> <a class="dugme dugme-ikincil" href="#/formulasyon">Formülasyon çalışma sayfası</a></p>
  <aside class="yeni-not"><strong>Bu bir okuma rehberidir, kitabın yerine geçmez.</strong> Kitaptan alıntı, kitabın vakaları ya da
  bölümlerin ayrıntılı özeti yoktur; fikirler kendi sözcüklerimizle yazıldı. Her oturumun bölümlerini önce kitaptan okuyun, sonra buraya dönün.</aside>
</div>
<section class="ilerlemem" id="ilerlemem" hidden aria-labelledby="ilerleme-b"><h2 id="ilerleme-b" class="bolum-baslik">İlerlemem</h2>
<div class="ilerleme-kutular"></div>
<p class="kucuk">İlerleme yalnızca bu tarayıcıda saklanır. <button type="button" class="sina-sifirla hepsini-sil">Bütün ilerlemeyi sil</button></p></section>
<section class="verilerim js-gerek" id="verilerim" aria-labelledby="veri-b"><h2 id="veri-b" class="bolum-baslik">Verilerim</h2>
<p>İlerlemeniz, notlarınız ve formülasyon taslağınız yalnızca bu tarayıcıda saklanır, hiçbir sunucuya gönderilmez. Başka bir cihaza
taşımak ya da yedeklemek için dosya olarak indirin; öbür cihazda “Dosyadan yükle” ile geri alın.</p>
<p class="veri-dugmeler"><button type="button" class="dugme dugme-ikincil veri-indir">İlerlemeyi indir (.json)</button>
<button type="button" class="dugme dugme-ikincil veri-yukle">Dosyadan yükle</button>
<input type="file" class="veri-dosya" accept=".json,application/json" hidden aria-label="İlerleme dosyası seçin">
<button type="button" class="dugme dugme-ikincil notlar-indir">Notlarımı indir (.md)</button></p>
<div class="veri-onay uyari" hidden aria-live="polite"></div>
<p class="veri-durum kucuk" aria-live="polite"></p></section>
<section class="kurallar kullanim" aria-labelledby="kurallar-b"><h2 id="kurallar-b" class="bolum-baslik">Nasıl kullanılır?</h2>
<ol><li data-ara><span class="kural-no">1</span> Oturumun bölümlerini kitaptan okuyun; “Okurken” sorularını yanınızda tutun.</li>
<li data-ara><span class="kural-no">2</span> Buraya dönün: ana fikirleri kendi okumanızla karşılaştırın, ÇRS’deki karşılığını ve tartışmalı noktaları okuyun.</li>
<li data-ara><span class="kural-no">3</span> Vaka sorularıyla kendinizi sınayın; araçlarla kendi vakalarınız üzerine düşünün.</li></ol></section>
{kesim_bolumleri}
<p class="kucuk kapsam-not">Rehber, kitabın değerlendirme cildindeki B (Görüşme), C (Aile), D (Sürtüşme), E (Formülasyon) ve
F (Açıklamak) kesimlerinden {sum(1 for v in oturum_views if v["kesim"] != "R")} oturumu ve R (İşlev bozukluğu) kesiminden “Your
Competitors” bölümünü kapsar. A ve G kesimleri ile tedavi ve sistemler ciltleri ileride eklenebilir.</p>
<section aria-labelledby="arac-b"><h2 id="arac-b" class="bolum-baslik">Araçlar</h2><ol class="kartlar">{arac_kartlari}</ol></section>
"""
giris = dict(id="giris", label="Giriş",
             html=f'<section class="view aktif" id="v-giris" data-view="giris" data-baslik="Giriş" aria-label="Giriş">{giris_ic}</section>')

# ---------------------------------------------------------------- kaynakça (en son: kullanım bilgisi gerekiyor)
SIRA = ["giris"] + [v["id"] for v in oturum_views] + ["tarama", "zor-anlar", "simulasyon", "formulasyon", "kavramlar", "turkiye",
                                                       "tekrar"]
ETIKET = {"giris": "Giriş", "tarama": "Tarama hesaplayıcısı", "zor-anlar": "Zor anlar", "simulasyon": "Vaka simülasyonu",
          "formulasyon": "Formülasyon çalışma sayfası", "kavramlar": "Kavram kartları", "turkiye": "Türkiye notları",
          "tekrar": "Karışık test"}
ETIKET.update({v["id"]: f'Oturum {v["no"]}' for v in oturum_views})


def kaynak_li(k):
    r = KAYNAK[k]
    ek = []
    if r.get("doi"):
        ek.append(f'<a href="https://doi.org/{esc(r["doi"])}" target="_blank" rel="noopener">doi:{esc(r["doi"])}</a>')
    if r.get("pmid"):
        ek.append(f'<a href="https://pubmed.ncbi.nlm.nih.gov/{r["pmid"]}/" target="_blank" rel="noopener">PMID {r["pmid"]}</a>')
    yerler = sorted(KULLANIM.get(k, []), key=lambda y: SIRA.index(y[0]) if y[0] in SIRA else 99)
    gor = []
    for vid, ad, et in yerler:
        hedef = f"#/{vid}/{ad}" if ad else f"#/{vid}"
        if hedef not in [g[0] for g in gor]:
            gor.append((hedef, ETIKET.get(vid, et)))
    geri = (' <span class="kaynak-geri">Geçtiği yer: ' + ", ".join(f'<a href="{h}">{esc(e)}</a>' for h, e in gor) + "</span>") if gor else ""
    return f'<li id="k-{k}" data-ara>{esc(r["metin"])} {" · ".join(ek)}{geri}</li>'


kitaplar = sorted([k for k, r in KAYNAK.items() if r.get("tur") == "kitap" and k != KITAP], key=lambda k: KAYNAK[k]["metin"].lower())
makaleler = sorted([k for k, r in KAYNAK.items() if r.get("tur") != "kitap"], key=lambda k: KAYNAK[k]["metin"].lower())
pubmedsiz = [KAYNAK[k]["etiket"] for k in makaleler if not KAYNAK[k].get("pmid")]
kay_ic = ('<p class="giris-metin">Rehberde anılan bütün kaynaklar. Makalelerin künyeleri Kasım 2026’da PubMed’den doğrulandı; '
          f'PubMed’de dizinlenmeyen {len(pubmedsiz)} makale ({esc(", ".join(pubmedsiz))}) yayıncı kayıtlarından doğrulandı. '
          'Her kaynağın yanında DOI ve PubMed bağlantısı, rehberde geçtiği yerler var.</p>'
          '<p class="kaynak-ara"><label for="kaynak-suz">Kaynakçada süz</label>'
          '<input id="kaynak-suz" type="search" placeholder="Yazar, yıl ya da başlık" autocomplete="off"></p>'
          '<p class="kaynak-sonuc" aria-live="polite"></p>'
          f'<section class="kaynak-grup"><h3>Rehberin eşlik ettiği kitap <span class="sayi">1</span></h3><ol class="kaynaklar">{kaynak_li(KITAP)}</ol></section>'
          f'<section class="kaynak-grup"><h3>Diğer kitaplar <span class="sayi">{len(kitaplar)}</span></h3><ol class="kaynaklar">'
          + "".join(kaynak_li(k) for k in kitaplar) + "</ol></section>"
          f'<section class="kaynak-grup"><h3>Makaleler <span class="sayi">{len(makaleler)}</span></h3><ol class="kaynaklar">'
          + "".join(kaynak_li(k) for k in makaleler) + "</ol></section>")
kaynakca = dict(id="kaynakca", label="Kaynakça", html=view("kaynakca", "Kaynakça", "Araçlar", kay_ic))

ORDER = [giris] + oturum_views + [tarama, zor_anlar, simulasyon, formulasyon, kavramlar, turkiye, tekrar, kaynakca]


# ---------------------------------------------------------------- gezinti
def nav_item(vid, no, ad):
    return (f'<li><a href="#/{vid}" data-nav="{vid}"><span class="nav-no" aria-hidden="true">{esc(no)}</span>'
            f'<span class="nav-ad">{esc(ad)}</span><span class="nav-durum" data-durum-nav="{vid}"></span></a></li>')


nav = ('<nav class="yan" id="yan" aria-label="Rehber içeriği"><div class="yan-ic">'
       '<ol class="nav-liste"><li><a href="#/" data-nav="giris"><span class="nav-no" aria-hidden="true">⌂</span>'
       '<span class="nav-ad">Giriş</span></a></li></ol>'
       + "".join(f'<p class="nav-baslik">{esc(ad)}</p><ol class="nav-liste">'
                 + "".join(nav_item(v["id"], str(v["no"]), v["kisa"]) for v in oturum_views if v["kesim"] == k) + "</ol>"
                 for k, ad in O.KESIMLER.items())
       + '<p class="nav-baslik">Araçlar</p><ol class="nav-liste">'
       + nav_item("tarama", "🧮", "Tarama hesaplayıcısı") + nav_item("zor-anlar", "🧯", "Zor anlar")
       + nav_item("simulasyon", "🎭", "Vaka simülasyonu")
       + nav_item("formulasyon", "✎", "Formülasyon sayfası") + nav_item("kavramlar", "🃏", "Kavram kartları")
       + nav_item("turkiye", "TR", "Türkiye notları") + nav_item("tekrar", "🎲", "Karışık test ve tekrar")
       + nav_item("kaynakca", "§", "Kaynakça") + "</ol>"
       '<p class="ilerleme" data-ilerleme></p></div></nav>')

DESC = ("Williams ve Hill’in The Art of Child and Adolescent Psychiatry kitabına eşlik eden etkileşimli okuma rehberi: görüşme, aile, "
        f"sürtüşme, formülasyon ve açıklama kesimlerinden {len(oturum_views)} oturum için ana fikirler, ÇRS ve Türkiye karşılığı, tartışmaya açık "
        "noktalar, kurgusal vaka soruları, dallanan vaka simülasyonları, aralıklı tekrar, tarama hesaplayıcısı, zor anlar alıştırması ve "
        "formülasyon çalışma sayfası.")

page = f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{AD} · Doç. Dr. Miraç Barış Usta</title>
<meta name="description" content="{esc(DESC)}">
<meta name="author" content="Miraç Barış Usta">
<meta name="theme-color" content="#f7f6f1">
<meta property="og:title" content="{AD}">
<meta property="og:description" content="{esc(DESC)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{ADRES}">
<link rel="canonical" href="{ADRES}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Lora:ital,wght@0,600;0,700;1,500&amp;display=swap">
<link rel="stylesheet" href="rehber.css">
<script src="rehber.js" defer></script>
</head>
<body>
<a class="atla" href="#icerik">İçeriğe geç</a>
<header class="ust">
  <a class="geri" href="https://miracbarisusta.com/rehberler/"><span aria-hidden="true">←</span> Rehberler</a>
  <a class="marka" href="#/">Çocuk Psikiyatrisinin Sanatı</a>
  <div class="ara" role="search">
    <label class="gizli" for="ara">Rehberde ara</label>
    <input id="ara" type="search" placeholder="Rehberde ara…" autocomplete="off" aria-controls="ara-sonuc">
    <div class="ara-sonuc" id="ara-sonuc" hidden></div>
  </div>
  <button type="button" class="menu-dugme" aria-controls="yan" aria-expanded="false">Oturumlar</button>
</header>
<div class="duzen">
{nav}
<main id="icerik" tabindex="-1">
{"".join(v["html"] for v in ORDER)}
</main>
</div>
<footer class="alt">
  <p><strong>Hazırlayan:</strong> Doç. Dr. Miraç Barış Usta · Kasım 2026 · <a href="https://miracbarisusta.com">miracbarisusta.com</a></p>
  <p>Jonathan Williams ve Peter Hill’in <i lang="en">The Art of Child and Adolescent Psychiatry</i> (Cambridge University Press, 2025)
  kitabına eşlik eden bağımsız bir okuma rehberidir. Kitaptan alıntı ya da kitabın vakalarını içermez ve kitabın yerine geçmez.
  Yazarlar ya da yayıneviyle bağlantılı değildir.</p>
  <p>Eğitim amaçlıdır; bilgiler Kasım 2026 itibarıyladır. Vakalar ve hesaplayıcı değerleri kurgusaldır. Tanı ve tedavi kararları için
  güncel kılavuzlara, yerel mevzuata ve klinik değerlendirmeye başvurun.</p>
  <p>© 2026 Miraç Barış Usta · <a href="https://github.com/hypothermia15/cocuk-psikiyatrisi-sanati/blob/main/LICENSE">Kullanım koşulları</a></p>
</footer>
<div class="atif-pop" id="atif-pop" role="dialog" aria-label="Kaynak" hidden></div>
</body>
</html>
"""
(KOK / "index.html").write_text(page, encoding="utf-8")
kullanilmayan = sorted(k for k in KAYNAK if k not in KULLANIM and k != KITAP)
dagilim = [0, 0, 0, 0]
for q in _tum_sorular:
    dagilim[karistir_soru(q)[1]] += 1
n_sahne = sum(len(s["sahneler"]) for s in SIM.SIMULASYONLAR)
print(f"{len(ORDER)} görünüm, {len(oturum_views)} oturum, {n_soru} vaka sorusu (doğru şık dağılımı A–D: {dagilim}), "
      f"{sum(v['n_tart'] for v in oturum_views)} tartışma noktası, {len(SIM.SIMULASYONLAR)} simülasyon ({n_sahne} sahne), "
      f"{len(A.KAVRAMLAR)} kavram, {len(A.ZOR_ANLAR)} zor an, {sum(v['tr'] for v in oturum_views)} TR notu, {len(KAYNAK)} kaynak, "
      f"{page.count('class=\"atif\"')} atıf → {KOK / 'index.html'} ({len(page) // 1024} KB)")
if BILINMEYEN:
    print("BİLİNMEYEN ATIF:", ", ".join(sorted(BILINMEYEN)))
if kullanilmayan:
    print("Kullanılmayan kaynak:", ", ".join(kullanilmayan))

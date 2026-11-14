# Çocuk Psikiyatrisinin Sanatı · Okuma Rehberi

Doç. Dr. Miraç Barış Usta’nın, Jonathan Williams ve Peter Hill’in *The Art of Child and Adolescent Psychiatry* (Cambridge University Press, 2025) kitabını çocuk ve ergen psikiyatrisi pratiğine çevirerek okumak için hazırladığı etkileşimli okuma rehberi (Kasım 2026).

**Canlı sürüm:** https://miracbarisusta.com/cocuk-psikiyatrisi-sanati/

## İçerik

- Kitabın değerlendirme cildindeki B (Görüşme), C (Aile), D (Sürtüşme), E (Formülasyon) ve F (Açıklamak) kesimlerinden 18 oturum ve R (İşlev bozukluğu) kesiminden “Your Competitors” bölümü. Kasım 2026’da eklenen oturumlar: 15 Tanısız psikiyatri, 16 Formülasyonu sunmak, 17 Mektup ve rapor yazmak, 18 Sözcükler, 19 Etkilemek ve ikna etmek. Her oturumda yedi adım: kitapta ve okurken (okuma soruları) · ana fikirler · ÇRS’deki karşılığı · tartışmaya açık noktalar · üç kurgusal vaka sorusu · akılda kalsın · kendi notum.
- 74 “Tartışmaya açık” kutusu kitabın önerilerini güncel literatürle karşılaştırır; 75 kaynağın künyesi PubMed’den ya da yayıncı kayıtlarından doğrulanmış, DOI ve PubMed bağlantılarıyla verilmiştir. Kanıtlar Kasım 2026’da gözden geçirildi (ör. K-SADS-PL-DSM-5 ve SDQ 2-4’ün Türkçe uyarlamaları, psikotik deneyimlerin sonraki risk ile ilişkisi, çok bilgi verenli değerlendirme, alüminyum içeren aşılar, HiTOP, uzamış yas bozukluğu).
- “TR” etiketli maddeler Türkiye’deki uygulamaya (e-Nabız, ÇÖZGER, RAM, kırmızı reçete, Beyaz Kod, akraba evliliği, LGS ve YKS) özgü notlardır ve ayrı bir sayfada toplanır.
- Araçlar:
  - vaka simülasyonu: dört dallanan kurgusal vaka (konuşmak istemeyen ve ölüm düşünceleri olan bir ergen, bugün ilaç isteyen anne-baba, bekleme salonunda öfkeli bir baba, devralınan bir “bipolar” tanısı). Her karar puanlanır ve gerekçesi açıklanır; vaka seçilen yola göre farklı sonlara varır, istenen karara dönülüp başka yol denenebilir;
  - tarama hesaplayıcısı: yaygınlık, duyarlılık ve özgüllükle 1000 çocukta gerçek ve yanlış pozitifler, pozitif ve negatif öngörü değeri, pozitif ve negatif olabilirlik oranı, testten önce ve sonra olasılık çubukları, iki sıralı ızgara ve pozitiflere ikinci test uygulandığında ne olduğunu gösteren seri test hesabı (varsayımsal hazır örneklerle);
  - zor anlar: 21 kurgusal durumda en uygun yanıtı seçme alıştırması;
  - formülasyon çalışma sayfası: zaman seyri, bağımsız kaynaklar, dört P, %100’e tamamlanan ayırıcı tanı, kısır döngü, ölçülebilir hedef ve kalite kontrolü; tarayıcıda kaydedilir, yazdırılabilir;
  - 51 kavram kartı (kendi tanımlarımızla);
  - karışık test ve aralıklı tekrar: 57 vaka sorusu ve kavram kartları beş kutulu bir Leitner düzeninde izlenir (1, 3, 7 ve 21 gün); “Bugünün tekrarı” ve “Yanlışlarım” turları.
- Verilerim: ilerleme dosya olarak indirilip başka bir cihazda yüklenebilir; oturum notları ve formülasyon taslağı Markdown olarak indirilebilir.

## Kullanım

- Okundu işaretleri, vaka sorusu yanıtları, aralıklı tekrar kutuları, simülasyon sonuçları, notlar, hesaplayıcı değerleri ve formülasyon taslağı yalnızca kullanıcının tarayıcısında saklanır; hiçbir sunucuya gönderilmez. Formülasyon sayfasına ve notlara gerçek hasta bilgisi girilmemelidir.
- Bir atfa tıklayınca künyesi açılır; kaynakçada her kaynağın rehberde geçtiği yerler listelenir.
- `/` tuşu aramaya odaklanır. Doğrudan bağlantı örnekleri: `#/oturum-10`, `#/oturum-10/tartisma`, `#/simulasyon`, `#/tarama`, `#/zor-anlar`, `#/formulasyon`, `#/tekrar`, `#/turkiye`, `#/kaynakca`.

## Dosyalar

| Dosya | İçerik |
| --- | --- |
| `index.html` | Rehber; `tools/olustur.py` ile üretilir. |
| `rehber.css`, `rehber.js` | Görünüm ve etkileşim; dış betik ya da kütüphane kullanmaz. |
| `tools/icerik_oturumlar.py` | Oturum içerikleri: okuma soruları, ana fikirler, ÇRS ve Türkiye karşılıkları, tartışma noktaları, vaka soruları (oturum 1-14). |
| `tools/icerik_oturumlar_ek.py` | Kasım 2026’da eklenen oturumlar (15-19); listenin sonuna eklenir. |
| `tools/icerik_araclar.py` | Kavramlar, zor anlar, tarama hesaplayıcısı ayarları, formülasyon çalışma sayfası, Türkiye sözlüğü. |
| `tools/icerik_simulasyon.py` | Dallanan vaka simülasyonları (sahneler, seçenekler, puanlar, geri bildirimler); üretici her yolun bir sona vardığını ve döngü olmadığını denetler. |
| `tools/kaynaklar.json` | Doğrulanmış künyeler (PMID, DOI). |

## Kaynak ve sorumluluk

Bu bir okuma rehberidir, kitabın yerine geçmez. Kitaptan alıntı, kitabın vaka örnekleri ya da bölümlerin ayrıntılı özeti yoktur; fikirler kendi sözcüklerimizle yazılmış ve çocuk ve ergen ruh sağlığı pratiğine çevrilmiştir. Rehber yazarlar ya da yayıneviyle bağlantılı değildir. Eğitim amaçlıdır; bilgiler Kasım 2026 itibarıyladır. Vakalar, simülasyonlar, zor an senaryoları ve hesaplayıcı değerleri kurgusaldır.

Tarayıcıda kayıtlı vaka sorusu yanıtları şık konumuyla saklanır. Bu yüzden var olan oturumlara soru eklenmemeli ya da soruların sırası değiştirilmemelidir; yeni sorular yeni oturumlarla eklenir (`tools/olustur.py`, `ILK_SORU_SAYISI`).

## Lisans

© 2026 Miraç Barış Usta. Tüm hakları saklıdır; ayrıntılar için [LICENSE](LICENSE).

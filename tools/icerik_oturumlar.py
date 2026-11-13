# -*- coding: utf-8 -*-
"""Çocuk Psikiyatrisinin Sanatı · Okuma Rehberi: oturum içerikleri.

Williams ve Hill'in The Art of Child and Adolescent Psychiatry (Cambridge University Press, 2025) kitabına
eşlik eden okuma rehberi. Bütün metinler özgündür: kitaptan alıntı, kitabın numaralı vinyetleri ya da
bölümlerin ayrıntılı yeniden anlatımı yoktur. Vaka soruları kurgusaldır.

Atıf sözdizimi: [@anahtar] (tools/kaynaklar.json). "TR " ile başlayan ÇRS maddeleri Türkiye notlarına da toplanır.
"""

KESIMLER = {
    "B": "B · Görüşme",
    "C": "C · Aile",
    "D": "D · Sürtüşme",
    "E": "E · Formülasyon",
    "R": "R · Ekipte işlev bozukluğu",
}

# Kitabın yapısı (Cambridge University Press içindekiler sayfasından doğrulandı): Cilt 1 Değerlendirme (A The Child,
# B Interviewing, C The Family, D Friction, E Formulating, F Explaining, G This Shouldn’t Happen!), Cilt 2 Tedavi (H–K) ...
# Rehber B–E kesimlerinin ilk 13 oturumunu ve R. Dysfunction kesiminden “Your Competitors” bölümünü kapsar.
KAPSANMAYAN_E = "Psychiatry without Diagnoses (s. 218)"


def S(soru, secenekler, dogru, aciklama):
    return dict(soru=soru, secenekler=secenekler, dogru=dogru, aciklama=aciklama)


OTURUMLAR = [
    # ------------------------------------------------------------------ 1
    dict(
        no=1, kesim="B", kisa="Hazırlık ve ölçekler",
        baslik="Görüşmeye hazırlanmak ve ölçekleri yerinde kullanmak",
        kitapta_bolumler="B. Interviewing · Planning the Session; Questionnaires (s. 40–52)",
        slogan="İlk görüşmenin amacı tanı koymak değil, bu ailenin neden şimdi burada olduğunu anlamaktır.",
        kitapta=("İki bölüm ilk randevudan önce ve sırasında yapılacakları ele alır: bağımsız bilgi toplamak, aileyi karşılamak, "
                 "odayı ve süreyi göreve göre düzenlemek; ardından ölçeklerin neyi yapıp neyi yapamayacağını, tarama "
                 "matematiğini ve sık kullanılan araçların sınırlarını tartışır."),
        okurken=[
            "Yazarlar ilk görüşmenin amacını neden “öykü almak” ya da “tanı koymak” olarak tanımlamıyor?",
            "Bir ölçek hangi durumda klinisyeni yanılgıdan korur, hangi durumda yanıltır?",
            "Yaygınlığı düşük bir bozuklukta pozitif tarama sonucu neden çoğu zaman yanlış alarmdır?",
        ],
        fikirler=[
            ("Hazırlık görüşmenin parçasıdır", "Okul görüşü, önceki raporlar ve öğretmen formları randevudan önce istendiğinde görüşme "
             "tahmin yerine karşılaştırma üzerine kurulur. Ailenin ne bekleyeceğini bilmesi de kaygıyı ve “yanlış kapıya geldik” hissini azaltır."),
            ("Amaç anlamaktır", "İlk görüşmenin çıktısı bir etiket değil, “sorun ne ve bu aile neden şimdi burada?” sorusuna verilen "
             "bir yanıttır. Erken tanı koymak öteki açıklamaları düşünmeyi kapatabilir."),
            ("Oda ve süre birer klinik araçtır", "Oturma düzeni, görünür kâğıtlar, yaşa uygun oyuncaklar ve görüşme süresi ailenin "
             "ne kadar açılabileceğini etkiler. Süreyi alışkanlık değil görev belirlemelidir; ilk görüşmede acele, hata ve şikâyet üretir."),
            ("Bilgi taraması, başlangıçtan itibaren", "Karşılama anı, bekleme salonundaki düzen ve kimin kiminle nasıl konuştuğu, "
             "henüz soru sorulmadan toplanan gözlemlerdir. Sessiz kardeş çoğu zaman en dengeli tanıktır."),
            ("Ölçek tarar, tanı koymaz", "Ölçekler sistematik olmayı sağlar ve klinisyeni ilk izlenime takılmaktan korur; ama "
             "işlevselliği, bağlamı ve alternatif açıklamaları kendileri sorgulamaz."),
            ("Tarama matematiği sezgiye aykırıdır", "Yaygınlık düşükse, duyarlılığı ve özgüllüğü iyi bir ölçekte bile pozitif sonuçların "
             "çoğu yanlış pozitiftir. Ölçek sonucu, ön olasılıkla birlikte yorumlanmalıdır."),
        ],
        crs=[
            "Randevudan önce okul rehberlik servisinden kısa bir gözlem notu ve varsa önceki raporları isteyin; ilk görüşme karşılaştırma yapabileceğiniz bir zemine oturur.",
            "TR Poliklinik süreleri kısa olduğunda ilk görüşmeyi iki randevuya bölmek, uzun tek görüşmeden daha uygulanabilir olabilir; ikinci randevu ilk görüşmede eksik kalanları tamamlar.",
            "TR e-Nabız’a işlenen tanılar, raporlar ve reçeteler aileye, zamanla ergenin kendisine de görünür olabilir; kayda geçen ifadeleri yargısız ve betimleyici bir dille yazın.",
            "Aileyi bekleme salonundan kendiniz alın; kimin önce ayağa kalktığı, çocuğun kimin yanında yürüdüğü ilk formülasyon verileridir.",
            "Görüşmeye bütün kardeşleri davet etmeyi düşünün; “sorunsuz” kardeş evdeki gündelik hayata dair çoğu zaman en az taraflı bilgiyi verir.",
            "Ölçek puanını aileye açıklarken “bu bir tarama sonucu, tanı değil” cümlesini mutlaka kurun; aksi hâlde puan ailenin sorun haritasının merkezine yerleşir.",
            "Öğretmen formunu DEHB tedavisinde doz ayarı ve izlem için kullanın; tanı kararını tek başına ona dayandırmayın.",
            "Tedavi hedeflerini “daha az bağırmak” gibi bir şeyin yokluğu olarak değil, yapılacak bir davranış olarak tanımlayın; bir şeyin yokluğu tedavi hedefi olamaz.",
        ],
        tartisma=[
            ("Klinik yargı mı, mekanik tahmin mi?",
             "Tahmin görevlerinde istatistiksel formüllerin çoğu zaman klinik yargı kadar ya da ondan daha isabetli olduğu meta-analizle "
             "gösterilmiştir ([@grove2000]). Kitap ise klinisyenin rolünü savunur. Bu gerilim, yapay zekâ destekli değerlendirme araçlarının "
             "nerede yardımcı, nerede sınırlı olduğunu tartışmak için iyi bir başlangıçtır."),
            ("Ölçeklerin klinik örneklemdeki değeri",
             "Güçler ve Güçlükler Anketi (SDQ) İngiltere’deki ulusal bir toplum örnekleminde yeterli güvenilirlik göstermiş ve yüksek "
             "puanlar bağımsız konmuş tanıların olasılığını belirgin biçimde artırmıştır ([@goodman2001]). Ancak bir pozitif sonucun "
             "anlamı uygulandığı örneklemdeki ön olasılığa bağlıdır: aynı puan okulda ve uzman kliniğinde farklı şeyler söyler."),
            ("Hizmet gerçekliği",
             "Doksan dakikalık ilk görüşme ve bilgisayarsız oda önerisi, kısa poliklinik randevularının ve zorunlu elektronik kaydın "
             "olduğu sistemlere doğrudan aktarılamaz. Neyin vazgeçilmez çekirdek olduğu her klinikte ayrıca tanımlanmalıdır."),
        ],
        sorular=[
            S("Yaygınlığın %2 olduğu bir okulda, duyarlılığı ve özgüllüğü %80 olan bir depresyon ölçeği 1000 öğrenciye uygulanıyor. "
              "Pozitif çıkan bir öğrenci için en doğru yorum hangisidir?",
              ["Büyük olasılıkla depresyonu vardır; tedavi başlanmalıdır",
               "Pozitif sonuçların çoğu yanlış pozitiftir; klinik görüşmeyle değerlendirilmelidir",
               "Ölçek geçersizdir; sonuç dikkate alınmamalıdır",
               "Depresyon olasılığı tam olarak %80’dir"],
              1, "Bin öğrencide yaklaşık 20 gerçek vakadan 16’sı pozitif çıkar; hasta olmayan 980 kişiden yaklaşık 196’sı da pozitif "
                 "çıkar. Pozitiflerin yalnızca %7–8’i gerçekten depresyondur. Ölçek tarar; tanıyı klinik görüşme koyar. "
                 "Değerleri değiştirip sonucu <a href=\"#/tarama\">tarama hesaplayıcısında</a> görebilirsiniz."),
            S("DEHB şüphesiyle başvuran 9 yaşındaki bir çocuk için ilk randevudan önce yapılması en yararlı olan hangisidir?",
              ["Hiçbir ön bilgi istememek, böylece önyargısız görüşmek",
               "Okuldan öğretmen gözlemi ve formu, varsa önceki raporları istemek",
               "Aileden yalnızca internetten bulunan bir DEHB testini doldurmasını istemek",
               "Görüşmeyi beklemeden ilaç reçetesi hazırlamak"],
              1, "Bağımsız kaynaklardan gelen bilgi, ebeveyn anlatısını sınamayı ve durumlar arası tutarlılığı değerlendirmeyi sağlar. "
                 "Ön bilgi önyargı değil, karşılaştırma zemini yaratır."),
            S("Bir ergenin öz-bildirim ölçeği ağır depresyon gösteriyor; ancak görüşmede çökkünlük, anhedoni ve işlevsellik kaybı "
              "gözlenmiyor. Sosyal yargısı zayıf, değerlendirmelerinde abartıya yatkın. En uygun yaklaşım hangisidir?",
              ["Ölçek puanına göre antidepresan başlamak",
               "Puan ile klinik tablo arasındaki uyumsuzluğu araştırmak; tanıyı klinik değerlendirmeye ve işlevselliğe dayandırmak",
               "Ergenin yalan söylediğini düşünüp ölçeği tekrarlatmak",
               "Ailenin görüşünü almadan tanı koymak"],
              1, "Öz-bildirim, kişinin kendini değerlendirme biçimini yansıtır. Klinik bulgularla uyumsuz bir puan, bir bozukluktan çok "
                 "kalibre olmamış bir öz-değerlendirmeyi gösterebilir. Tanı ve tedavi işlevsellik ve klinik değerlendirmeyle belirlenir."),
        ],
        akilda="Ölçek tarar, klinisyen tanı koyar; ön olasılığı bilmeden sonucu yorumlamayın.",
    ),
    # ------------------------------------------------------------------ 2
    dict(
        no=2, kesim="B", kisa="Çocukla konuşmak",
        baslik="Çocukla konuşmak, düzenli kaos ve etkin dinleme",
        kitapta_bolumler="B. Interviewing · Talking to a Child; Regulated Chaos; Active Listening (s. 53–64)",
        slogan="Stresli çocukta koni ters çevrilir: önce kolay ve kapalı, sonra açık sorular.",
        kitapta=("Bölümler çocukla ilişki kurmayı ve onu konuşturmayı, rutini ne zaman koruyup ne zaman bozacağınızı, odadaki "
                 "gerilimin nasıl ayarlanacağını ve sözel ile sözel olmayan dinleme tekniklerini anlatır."),
        okurken=[
            "Erişkin görüşmesindeki “açıktan kapalıya” sıra, kaygılı bir çocukta neden ters çevrilebilir?",
            "Seansın sakin ya da gürültülü olması klinisyene hangi farklı bilgileri verir?",
            "Etkin dinleme tekniklerinin işe yaraması için teknik yeterli midir?",
        ],
        fikirler=[
            ("İlişki konuşmadan önce gelir", "Küçük çocukla göz hizasında, oyun ya da çizim üzerinden kurulan temas, doğrudan sorulardan "
             "daha çok bilgi getirir. Çocuğun dünyası ev, okul ve arkadaşlar/boş zaman üçgeninde gezilebilir."),
            ("Stres altında sıra değişir", "Kaygılı ya da konuşamayan çocukta açık uçlu sorular tıkanmayı artırır; basit, yanıtlanabilir "
             "sorularla başlayıp güven kuruldukça açılmak daha verimlidir."),
            ("“Neden” sorusu suçlar", "“Neden yaptın?” çocuğu savunmaya iter; davranışın arkasında makul bir neden olabileceğini varsayan "
             "bir dil, hikâyeyi anlatmayı kolaylaştırır."),
            ("Alakasız görünen söz bir ipucudur", "Çocuğun konuyla ilgisiz gibi duran bir cümlesi çoğu zaman aklındaki bir şeyin ucudur; "
             "geçiştirmek yerine devamını istemek gerekir."),
            ("Rutin de bozulmak için vardır", "Yapılandırılmış rutin karşılaştırmayı kolaylaştırır; ama beklenmedik bir durum, rutini "
             "bozmayı gerektirebilir. Odadaki gerilimi bastırmak her zaman doğru değildir: aile içi anlaşmazlık çoğu zaman meselenin özüdür."),
            ("Dinlemek bir tutumdur", "Yansıtma, özetleme ve sessizlik gibi teknikler, merak ve alçakgönüllülükle birleşmediğinde mekanikleşir; "
             "aile tekniği değil tutumu hisseder."),
        ],
        crs=[
            "Görüşmeyi ev, okul ve arkadaşlık üçgeninde yürütün; her köşe için 0–10 arası bir puan istemek, çocuğun kendi önceliğini görünür kılar.",
            "Zorbalık, okul değişikliği ya da ailede bir kayıp, kaygılı çocuğun susmasının sık nedenleridir; bunları basit sorularla erkenden yoklayın.",
            "Ebeveyn çocuğun yerine yanıt verdiğinde nazikçe çocuğa dönün; bu, ebeveyni dışlamadan çocuğun sesine alan açar.",
            "Görünüşe dayalı hızlı yargılardan kaçının; bakımsız görünen bir giysinin çocuk için bambaşka bir anlamı olabilir. Önce merakla sorun.",
            "TR Psikotik belirtileri sorarken kültürel açıklama modellerini (cin, nazar, rüya) yargılamadan dinleyin; ailenin kendi açıklaması, belirtinin anlamını ve tedavi uyumunu etkiler.",
            "Etkileşime girmeyen çocuğa “açılır” umuduyla çok sayıda seans vermek yerine, oyun, çizim ve bağımsız kaynaklarla bilgi akışını sürdürün.",
            "Seans sonunda çocuğa ne anladığınızı onun diliyle özetleyin ve tedavi planına katılmasını isteyin; kendi planı olduğunu hisseden çocuk daha çok iş birliği yapar.",
        ],
        tartisma=[
            ("Standart iletişim modelleriyle gerilim",
             "Calgary-Cambridge gibi yaygın görüşme modelleri açık uçlu sorulardan kapalı sorulara giden bir sırayı öğretir "
             "([@kurtz1996]). Kitabın stresli çocuk için önerdiği ters sıra, çocuk görüşmesinin eğitimde ve sınavlarda ayrı ölçütlerle "
             "değerlendirilmesi gerekip gerekmediği sorusunu doğurur."),
            ("Çocukta psikotik benzeri deneyimler",
             "Toplum çalışmalarının meta-analizinde psikotik belirtilerin ortanca yaygınlığı 9–12 yaş çocuklarda %17, 13–18 yaş "
             "ergenlerde %7,5 bulunmuştur ([@kelleher2012]). Bu nedenle tek bir “ses duyma” bildirimi tanı değil, bağlamıyla birlikte "
             "değerlendirilecek bir bulgudur."),
            ("Tutum ölçülebilir mi?",
             "Tutumun teknikten sezildiği uyarısı, yalnızca gözlenebilir davranışları sayan (yansıtma, empati cümlesi) her "
             "değerlendirme sisteminin, insan ya da yapay zekâ tabanlı olsun, ölçemediği bir boyuta işaret eder."),
        ],
        sorular=[
            S("Okula gitmek istemeyen 8 yaşındaki bir kız, görüşmede annesinin arkasına saklanıyor ve sorulara yanıt vermiyor. En "
              "uygun başlangıç hangisidir?",
              ["“Bana okulda neler hissettiğini anlat” diye açık uçlu bir soru sormak",
               "Yanıtlaması kolay, kapalı sorularla ya da birlikte çizim yaparak başlamak",
               "Çocuk konuşana kadar beklemek",
               "Annesini odadan çıkarıp çocuğu yalnız bırakmak"],
              1, "Stres altındaki çocukta açık uçlu sorular tıkanmayı artırabilir. Kolay sorular ve ortak bir etkinlik güven kurar; "
                 "çocuk rahatladıkça açık sorulara geçilir."),
            S("On yaşındaki bir erkek, kardeşini ittiğini anlatırken susuyor. Hangi ifade anlatmayı en çok kolaylaştırır?",
              ["“Neden ittin?”", "“Bunu yapmana yol açan iyi bir nedenin vardı herhalde, ne oldu?”",
               "“Kardeşini itmek yanlış, biliyorsun değil mi?”", "“Annen seni cezalandırdı mı?”"],
              1, "“Neden” sorusu suçlama gibi duyulur ve savunmayı artırır. Davranışın arkasında anlaşılabilir bir neden olabileceğini "
                 "varsayan bir dil, çocuğun kendi hikâyesini anlatmasına alan açar."),
            S("Aile görüşmesinde anne ve baba, çocuğun uyku saati konusunda yüksek sesle tartışmaya başlıyor. Klinisyenin en yararlı tutumu "
              "hangisidir?",
              ["Tartışmayı hemen durdurup konuyu çocuğa getirmek",
               "Tartışmayı güvenli sınırlar içinde bir süre gözlemek; anlaşmazlığın içeriğini ve örüntüsünü not etmek",
               "Ebeveynlerden birine hak vermek",
               "Görüşmeyi sonlandırmak"],
              1, "Odadaki gerilim çoğu zaman meselenin özünü gösterir. Güvenlik ve saygı sınırları korunarak gözlenen anlaşmazlık, "
                 "evdeki örüntüye dair değerli bir veridir; klinisyen ne kadar çok müdahale ederse aile o kadar az davranış sergiler."),
        ],
        akilda="Teknik sözcüklerde, tutum seste duyulur; çocuk ikisini de fark eder.",
    ),
    # ------------------------------------------------------------------ 3
    dict(
        no=3, kesim="B", kisa="İletişim ve öykü",
        baslik="İletişim becerileri ve öykü almak",
        kitapta_bolumler="B. Interviewing · Other Communication Skills; Taking a History (s. 65–81)",
        slogan="İyi soru somut bilgi arar; kötü soru yalana davet eder.",
        kitapta=("Bölümler beden dilini, söz kesmeyi, konuşmanın kendisi hakkında konuşmayı, risk ve prognozun nasıl iletileceğini, "
                 "seansı bitirmeyi ve mizahı; ardından öykü almada soru tiplerini, yanıtların ardındaki bilişsel yanılgıları ve "
                 "sezgi ile sistem arasındaki dengeyi ele alır."),
        okurken=[
            "Hangi soru tipleri yanıtlanamaz ya da dürüst olmayan yanıtlara davet eder?",
            "Olasılık sözcükleri (“nadir”, “olası”) aile tarafından nasıl farklı anlaşılabilir?",
            "Öykü almada tam yapılandırılmış ve yapısız görüşmenin ortasında nasıl bir yol önerilir?",
        ],
        fikirler=[
            ("Beden dili bir mesajdır", "Kapalı duruş, endişeli bir yüz ya da saatine bakmak aileye kötü bir haber ya da ilgisizlik "
             "mesajı verebilir. Empati cümlesinin zamanlaması da önemlidir: erken ve yoğun söylenen “anlıyorum” inandırıcı değildir."),
            ("Konuşmanın kendisi hakkında konuşmak", "Görüşme tıkandığında ya da tekrara düştüğünde, “şu an ne yaptığımıza bir bakalım” "
             "diyerek konuşmanın kendisini konu etmek döngüyü kırabilir."),
            ("Risk ve prognoz birer müdahaledir", "Olasılığı sözcüklerle değil somut sayılar ve karşılaştırmalarla anlatmak daha az "
             "yanlış anlaşılır. Aynı oran farklı çerçevelerle söylendiğinde farklı duygular uyandırır."),
            ("Soru tipi yanıtı belirler", "Ebeveynin yanıtlayamayacağı sorular ve evet/hayır beklentisi taşıyan suçlayıcı sorular "
             "güvenilmez yanıtlar üretir. Somut durumlar soran, davranışı normalleştiren sorular daha doğru bilgi getirir."),
            ("Yanıtların ardında yanılgılar vardır", "Ebeveynin sıklık tahmini çoğu zaman hatırladığı en kötü güne dayanır; soruların "
             "sırası da sonraki yanıtları etkiler."),
            ("Sezgi ile sistem birlikte", "Yalnızca kontrol listesine dayanan görüşme uyanıklığı azaltır; tümüyle yapısız görüşme "
             "güvenilmez tanıya götürür. Yarı yapılandırılmış bir çerçeve iki riski dengeler."),
        ],
        crs=[
            "“Ona bağırır mısınız?” yerine “Onunla çok gerildiğinizde ne olur?” diye sorun; davranışı varsayan ama suçlamayan soru daha dürüst yanıt getirir.",
            "Sıklık sorusunu “en kötü günü” değil, “geçen hafta kaç kez” gibi somut bir aralığa bağlayın; ebeveyn tahminleri en canlı anılara kayar.",
            "Evlat edinme ve ailede intihar öyküsü gibi utandırıcı ama kaçırılmaması gereken soruları kısa bir özürle doğrudan sorun.",
            "Riski “düşük” yerine “yüz çocuktan yaklaşık beşi” gibi doğal sıklıklarla anlatın ve aynı bilgiyi hem olumlu hem olumsuz çerçeveyle verin.",
            "Hassas bir gözlemi önce yüz yüze konuşun, sonra yazıya dökün; yazılı ifade bağlamından kopar ve sertleşir.",
            "TR Fiziksel cezayı sorarken klinisyenin dili onaylıyor gibi duyulmamalı; yasal çerçeveyi ve ebeveynlik desteğini aynı görüşmede konuşun.",
            "Seansı bitirmeden önce ailenin aklındaki ama sorulmamış soruyu davet edin: “Sormaya fırsat bulamadığınız bir şey kaldı mı?”",
        ],
        tartisma=[
            ("Çerçeveleme etkisi",
             "Aynı seçeneklerin kazanç ya da kayıp diliyle sunulması tercihleri değiştirir ([@tversky1981]). Bu bulgu, risk ve "
             "yan etki konuşmalarında klinisyenin seçtiği dilin etik bir boyutu olduğunu gösterir."),
            ("Yarı yapılandırılmış görüşmenin yeri",
             "Yarı yapılandırılmış tanı görüşmeleri tanı güvenilirliğini artırmak için geliştirilmiştir ([@kaufman1997]); kitabın "
             "önerdiği orta yol, bu araçların klinik merakla birlikte kullanılmasıdır."),
            ("Dolaylı tekniklerin etiği",
             "Mesajı asıl hedefin duyacağı biçimde başka birine söylemek gibi dolaylı teknikler pragmatik olabilir; ancak çocuğun "
             "güveni ve özerkliği açısından tartışmalıdır ve şeffaflık ilkesiyle birlikte düşünülmelidir."),
            ("Popüler psikoloji ile kanıt",
             "Beden dili ve ikna üzerine bazı öneriler ampirik olarak zayıftır. Okurken klinik bilgelik ile kanıta dayalı öneriyi ayırt "
             "etmek gerekir."),
        ],
        sorular=[
            S("Uyumsuzluk şikâyetiyle gelen 13 yaşındaki bir kızın annesine ilacı sorarken hangi soru en güvenilir yanıtı getirir?",
              ["“İlacı her gün düzenli veriyorsunuz, değil mi?”",
               "“Yoğun günlerde ilacın atlandığı oluyor mu, geçen hafta kaç kez oldu?”",
               "“İlacı vermeyi unutur musunuz?”",
               "“İlaç işe yaramıyor mu?”"],
              1, "Onay bekleyen soru, ebeveyni “evet” demeye davet eder. Atlanmayı olağan sayan ve somut bir zaman aralığı soran soru, "
                 "daha dürüst ve ölçülebilir bir yanıt getirir."),
            S("Bir ilacın yan etki riskini anlatırken yanlış anlaşılma olasılığı en düşük ifade hangisidir?",
              ["“Risk düşük.”", "“Nadiren olur.”",
               "“Bu ilacı alan yüz çocuktan yaklaşık üçünde görülür; doksan yedisinde görülmez.”",
               "“Olabilir ama endişelenmeyin.”"],
              2, "Sözel olasılık ifadeleri kişiden kişiye çok farklı anlaşılır. Doğal sıklıklar ve iki yönlü çerçeve (olanlar ve "
                 "olmayanlar) daha dengeli bir anlayış sağlar."),
            S("Bir baba, oğlunun öfke nöbetlerinin “her gün, saatlerce” sürdüğünü söylüyor. En uygun sonraki adım hangisidir?",
              ["Bu bilgiyi olduğu gibi kaydetmek",
               "Geçen haftayı gün gün birlikte gözden geçirip somut sayı ve süreleri sormak",
               "Babanın abarttığını söylemek",
               "Hemen ilaç başlamak"],
              1, "Ebeveyn tahminleri çoğu zaman en canlı hatırlanan kötü günlere dayanır. Yakın bir dönemi somut olarak gözden geçirmek "
                 "daha gerçekçi bir sıklık ve süre bilgisi verir."),
        ],
        akilda="Somut soru, dürüst yanıt getirir; olasılığı sayıyla, iki yönden anlatın.",
    ),
    # ------------------------------------------------------------------ 4
    dict(
        no=4, kesim="B", kisa="Gözlem ve tetkikler",
        baslik="Gözlemek, dinlemek ve tetkik istemek",
        kitapta_bolumler="B. Interviewing · Observing and Listening; Investigations (s. 82–96)",
        slogan="Göz bazen kontrol listesini yener; ama tetkik, düşünmenin yerine geçmez.",
        kitapta=("Bölümler görüşme boyunca çocukta ve ebeveynde gözlenebilecekleri, gözden kaçan ipuçlarını, ev ziyaretini ve "
                 "kırmızı bayrakları; ardından tetkiklerin kapsamını, genelden özele gitme ilkesini, çizim testlerini ve fizik "
                 "muayenenin çocukta nasıl yapılacağını anlatır."),
        okurken=[
            "Seans içi gözlem, ölçekler ve ebeveyn anlatısı çeliştiğinde hangisine nasıl ağırlık verilmeli?",
            "Hangi bulgular psikiyatrik bir açıklamadan önce fiziksel bir neden aramayı gerektirir?",
            "Klinisyenin kendi tepkileri ne zaman bir “sarı bayrak” olur?",
        ],
        fikirler=[
            ("Davranış odada da görülür", "Ebeveyn ile çocuk arasındaki etkileşim, odadaki hareketlilik ve seans boyunca değişen "
             "aktivite, anlatılandan bağımsız bir veri kaynağıdır."),
            ("Tırmanma ile sıkıntıyı ayırmak", "Kademeli olarak tırmanan, karşı tarafın tepkisini izleyen bir davranış ile gerçek acı ve "
             "sıkıntı ifadesi farklı müdahaleler gerektirir; bu ayrım ilaç kararlarını da etkiler."),
            ("Seans içi seyir", "Yeni bir ortamda ilk dakikalarda sakin kalabilen ama seans ilerledikçe hareketlenen çocuk, DEHB’nin "
             "az bilinen bir görünümünü gösterebilir; tersine, ilk dakikalardan bozulan davranış başka açıklamalar düşündürür."),
            ("Kırmızı bayraklar", "Kilo kaybı, fokal nörolojik bulgu, gece solunum sorunları ya da açıklanamayan fiziksel belirtiler "
             "fiziksel bir nedenin araştırılmasını gerektirir. Klinisyenin kendi aşırı kaygısı ya da kayıtsızlığı da dikkat edilmesi "
             "gereken bir işarettir."),
            ("Tetkik bir sorunun yanıtıdır", "Her tetkik belirli bir soruya yanıt vermelidir; genel testler özgül testlerden önce gelir. "
             "Rutin “her şeye bakalım” yaklaşımı yanlış pozitif ve gereksiz kaygı üretir."),
            ("Çocukta muayene bir ilişkidir", "Fizik muayene ve tansiyon ölçümü gibi işlemler çocuğa kontrol verilerek, önce ebeveynde "
             "gösterilerek ve oyunlaştırılarak yapılabilir."),
        ],
        crs=[
            "Ebeveynin anlattığı çocuk ile odada gördüğünüz çocuk arasındaki farkı not edin; fark tanısal değeri yüksek bir veridir.",
            "İlk 20 dakika sakin, sonrasında giderek hareketlenen çocukta DEHB’yi ayırıcı tanıda tutun; ilk dakikadan dağılan çocukta kaygı, travma ve dil sorunlarını da düşünün.",
            "İlaç etkisini seans içinde gözlemek mümkündür: aynı çocuğu ilaçlı ve ilaçsız dönemde aynı görevle görmek, ölçek puanından daha ikna edicidir.",
            "Anoreksiya şüphesinde kilo, nabız, kan basıncı ve ortostatik değişiklikleri ilk görüşmede kaydedin; tıbbi risk değerlendirmesi psikiyatrik değerlendirmeyle eş zamanlı yürür.",
            "Uyku apnesi, işitme kaybı ve absans epilepsi gibi dikkat sorunlarını taklit eden durumları DEHB tanısından önce sorgulayın.",
            "TR Genetik ve metabolik tetkikleri belirli bir klinik soruya bağlayarak isteyin; sonuçların aileye nasıl açıklanacağını tetkikten önce planlayın.",
            "Ev ziyareti ya da okul gözlemi mümkünse, klinikte görülmeyen örüntüleri ortaya çıkarabilir; değilse aileden kısa bir video istemek bir alternatiftir.",
        ],
        tartisma=[
            ("Gözlem ile kontrol listesi",
             "Seans içi gözlem ölçeklerin yakalayamadığını gösterebilir; ancak tek bir seanslık gözlem durumsaldır ve çocuğun başka "
             "ortamlardaki davranışını temsil etmeyebilir. İki kaynak birbirinin yerine değil, birbirini sınamak için kullanılmalıdır."),
            ("Tetkik isteme eşiği",
             "Hangi tetkikin kime isteneceği hizmetler arasında çok değişir. Rutin tarama yerine klinik soruya dayalı tetkik ilkesi, "
             "gereksiz yanlış pozitifleri ve aile kaygısını azaltır."),
            ("Dolaylı test tekrarı",
             "Bir testi çocuğun haberi olmadan farklı biçimde tekrarlamak gibi pragmatik çözümler etik açıdan gri alandadır; "
             "bilgilendirilmiş onam ve şeffaflık ilkeleriyle birlikte değerlendirilmelidir."),
        ],
        sorular=[
            S("Dikkat sorunlarıyla getirilen 7 yaşındaki bir çocuk muayenede sık ağızdan soluyor; annesi horladığını ve gündüz uykulu "
              "olduğunu söylüyor. İlk adım ne olmalıdır?",
              ["DEHB tanısı koyup stimülan başlamak",
               "Uykuda solunum bozukluğunu değerlendirmek için ilgili tetkik ve sevki planlamak",
               "Öğretmen formuna göre karar vermek",
               "Belirtileri kaygıya bağlamak"],
              1, "Uykuda solunum bozukluğu dikkat ve davranış sorunlarını taklit edebilir. Fiziksel nedenler dışlanmadan DEHB tanısı ve "
                 "stimülan kararı verilmemelidir."),
            S("Otizmli 12 yaşındaki bir çocuk istekleri karşılanmadığında fısıltıyla başlayıp giderek bağırmaya ve eşyaları itmeye "
              "geçiyor; tırmanırken ebeveynin yüzünü izliyor. Bu tablo en çok neyi düşündürür?",
              ["Ani ve kontrol edilemeyen bir panik atağı",
               "Sonucunu gözeten, kademeli tırmanan bir davranış örüntüsü; davranışsal bir yaklaşım öne çıkar",
               "Psikotik bir alevlenme",
               "Ağrıya bağlı sıkıntı"],
              1, "Karşı tarafın tepkisini izleyerek tırmanan davranış ile gerçek acı ve sıkıntı ifadesi farklı müdahaleler gerektirir. "
                 "Bu ayrım yapılmadan eklenen bir antipsikotik beklenen yararı sağlamayabilir; ağrı ve fiziksel sıkıntı yine de dışlanmalıdır."),
            S("Çocuğun tansiyonunu ölçmek gerekiyor ama çocuk çok korkuyor. Hangisi en uygun yaklaşımdır?",
              ["Ölçümü zorla yapmak", "Ölçümden vazgeçmek",
               "Önce annede ölçüp göstermek, çocuğun manşonu dokunarak tanımasına ve cihazı kendisinin açmasına izin vermek",
               "Çocuğa ölçüm yapılmazsa ilacın verilmeyeceğini söylemek"],
              2, "Kontrolün bir kısmını çocuğa vermek ve işlemi önce güvendiği birinde göstermek korkuyu azaltır. Zorlamak sonraki "
                 "ölçümleri de zorlaştırır."),
        ],
        akilda="Odada gördüğünüz çocuk, anlatılan çocuktan farklıysa, fark en değerli veridir.",
    ),
    # ------------------------------------------------------------------ 5
    dict(
        no=5, kesim="C", kisa="Aile öyküsü ve ilişki",
        baslik="Aile öyküsü ve klinik ilişki",
        kitapta_bolumler="C. The Family · The Family History; Clinical Relationships (s. 97–107)",
        slogan="Akrabanın tanı etiketi değil, hastalığının seyri bilgi verir.",
        kitapta=("Bölümler genogramın ne zaman ve kiminle alınacağını, aile öyküsünde seyir bilgisinin değerini ve kuşaklar arası "
                 "beklentileri; ardından klinik ilişkinin müşteri ilişkisinden farkını, sürekliliği, güveni kuran bileşenleri ve "
                 "dokunma, öz-açılım, hediye, tanıdıkların çocuklarını görmek gibi sınır sorularını ele alır."),
        okurken=[
            "Genogramı hazır bir formdan aktarmak yerine çocukla birlikte çizmek neler kazandırır?",
            "Bir akrabanın hastalığında tanı adı mı, seyri mi ayırıcı tanıya daha çok katkı verir?",
            "Aynı klinisyenin her zaman göremediği bir hizmette ilişki nasıl sürdürülebilir?",
        ],
        fikirler=[
            ("Genogram birlikte çizilir", "Erken alınan ve çocukla birlikte çizilen genogram yalnızca olguları değil, çocuğun aile "
             "üyelerini nasıl gördüğünü, kimi unuttuğunu ve kimi önce çizdiğini de gösterir. Önceden doldurulmuş bir şema bu fırsatı kaçırır."),
            ("Etiket değil seyir", "Akrabaya konmuş bir tanının adı yanlış olabilir. Hastalığın atak atak mı geldiği, aralarda iyileşip "
             "iyileşmediği ve hangi tedaviye yanıt verdiği, ayırıcı tanıda ve tedavi seçiminde daha değerlidir. Üç kuşağa bakmak bazen planı değiştirir."),
            ("Kan bağı ile hane ayrı çizilir", "Karmaşık ailelerde genetik ilişkileri gösteren çizim ile kimin kiminle yaşadığını gösteren "
             "sosyal çizimi ayırmak tabloyu okunur kılar. Evlat edinme ya da yardımla üreme gibi bilgiler için ebeveynlere, çocukların "
             "yanında yanıt vermek zorunda kalmayacakları bir kapı bırakılmalıdır."),
            ("Kuşaklar arası beklenti", "Çok başarılı ebeveynlerin çocukları, ortalamaya gerileme ve yüksek beklenti nedeniyle "
             "kazanamayacakları bir yarışa sokulabilir. Bazıları çabayı bırakır, bazıları karşı çıkar, bazıları rekabet dışı alanlara yönelir."),
            ("Hasta müşteri değildir", "Klinik ilişki bir işlemle bitmez. Arkadaşça ama profesyonel, açıklayıcı ama boğmayan, yön gösteren "
             "ama dayatmayan bir tutum çoğu zaman en iyisidir. Süreklilik sağlanamadığında son yazışmayı okumak ilişkinin kopmadığını hissettirir."),
            ("Güvenin bileşenleri", "Profesyonellik, nezaket, aileyi tanımak ve hem ebeveyne hem çocuğa özen göstermek güveni kurar. "
             "Aileler bilmemeyi affeder; bilmediği hâlde biliyormuş gibi yapmayı affetmez. Dokunma, öz-açılım ve hediye için ilkeleri önceden düşünmek gerekir."),
        ],
        crs=[
            "Genogramı ilk görüşmenin erken bir anında, çocuğun da katılımıyla çizin; kimi unuttuğunu ve kimi önce çizdiğini not edin.",
            "TR Akraba evliliğini genogramda rutin olarak sorun ve işaretleyin; nörogelişimsel ve metabolik ayırıcı tanıyı ve genetik danışmanlık kararını doğrudan etkiler.",
            "TR Çok kuşaklı hanelerde büyükanne ve büyükbabanın bakım ve disiplin rolünü ayrıca sorun; kuralları kimin koyduğu, tedavi önerilerinin evde uygulanıp uygulanmayacağını belirler.",
            "Akrabada geçmiş bir psikiyatrik tanı söylendiğinde seyri sorun: dönemler hâlinde mi geldi, aralarda iyileşti mi, hangi tedaviye yanıt verdi?",
            "Evlat edinme ya da yardımla üreme gibi bilgileri ön yazışmalardan öğrenmeye çalışın; görüşmede “Gebelikle ilgili ayrıca konuşmak istediğiniz bir şey var mı?” diye bir kapı bırakın.",
            "Her kontrol randevusundan önce son yazınızı okuyun; ailenin en iyi hatırladığı görüşme, son görüşmedir.",
            "Bilmediğiniz bir soruyu “araştırıp size döneceğim” diyerek not edin ve gerçekten dönün; bu cümle güveni azaltmaz, artırır.",
            "TR İlk görüşmelerde ebeveynlere adıyla birlikte “Hanım/Bey” diye hitap etmek onları bakımın yetişkin ortağı olarak konumlar; “anne/baba” hitabının sıcaklık mı, mesafesizlik mi olarak algılandığına dikkat edin.",
            "TR Bayramda ya da taburculukta getirilen küçük bir hediyeyi teşekkürle kabul etmek kültürel olarak uygundur; büyük ya da bir talebin habercisi olabilecek hediyeleri nazikçe geri çevirin.",
            "TR Tanıdık ya da meslektaş çocuğu görmeniz istendiğinde sırayı atlatmayın ve bakımın kapsamını da daraltmayın; ebeveyn ruh sağlığı ve çocuk koruma gibi alanları başka bir klinisyene bırakın.",
        ],
        tartisma=[
            ("İttifak mı, doğru tedavi mi?",
             "Çocuk ve ergen psikoterapisinde terapötik ittifak ile sonuç arasında küçük ama tutarlı bir ilişki meta-analizlerle "
             "gösterilmiştir (r≈0,14–0,19; [@mcleod2011]; [@karver2018]). Verilerin çoğu gözlemseldir: erken düzelmenin ittifakı "
             "güçlendirmesi dışlanmış değildir. Kitabın orta yolu, ittifakın yanlış tedaviyi telafi etmediğidir."),
            ("Süreklilik ve süreklilik hissi",
             "Son yazışmayı okuyarak ilişkiyi kesintisizmiş gibi yaşatmak pragmatik bir öneridir. Ancak gerçek ilgi ile bir müşteri "
             "yönetimi tekniği arasındaki sınırı bulanıklaştırabilir; kitap başka bir yerde tutumun teknikten sezildiğini vurgular."),
            ("Genogramın Türkiye bağlamı",
             "2003 Türkiye Nüfus ve Sağlık Araştırması verilerinde evliliklerin %22’si akraba evliliğiydi; birinci kuzen evliliklerinin "
             "payı kuşaktan kuşağa azalmaktadır ([@koc2008]). Bu nedenle genetik genogram ayrıntısı Türkiye’de, İngiliz uygulamasına "
             "göre daha merkezî bir yer almalıdır."),
        ],
        sorular=[
            S("Ağır depresif epizodla başvuran 14 yaşındaki bir kız için antidepresan başlamadan önce sorulması en kritik aile öyküsü "
              "bilgisi hangisidir?",
              ["Annede “depresyon” tanısı olup olmadığı",
               "Birinci ve ikinci derece akrabalarda uyku ihtiyacının azaldığı, enerjinin ve harcamanın arttığı dönemler olup olmadığı",
               "Babanın mesleği",
               "Kardeşlerin okul başarısı"],
              1, "Akrabadaki tanı etiketi yanıltıcı olabilir; seyir bilgisi daha değerlidir. Ailede iki uçlu bozukluğu düşündüren dönemler, "
                 "antidepresan kararında, izlem sıklığında ve aileye verilecek bilgide değişiklik gerektirir."),
            S("Sekiz yaşındaki bir çocuğun ilk görüşmesinde genogramı almanın en yararlı yolu hangisidir?",
              ["Ebeveynin önceden doldurduğu formu kayda aktarmak",
               "Çocukla birlikte çizmek ve aile üyelerini hangi sırayla, nereye yerleştirdiğini gözlemek",
               "Görüşmenin son birkaç dakikasında hızlıca sormak",
               "Yalnızca birinci derece akrabaları kaydetmek"],
              1, "Birlikte çizilen genogram olguların yanında çocuğun aile algısını, ittifakları ve unutulanları da gösterir; çocuklar bu "
                 "etkinlikten çoğu zaman keyif alır."),
            S("Bir anne, oğlunun kullandığı ilaçla nadir bir antiepileptiğin etkileşimini soruyor; yanıtı bilmiyorsunuz. En uygun yanıt hangisidir?",
              ["Genel bir güvence verip konuyu değiştirmek",
               "“Şu an emin değilim; kontrol edip bugün size döneceğim” deyip gerçekten geri dönmek",
               "Sorunun önemsiz olduğunu söylemek",
               "Anneyi yalnızca nöroloğa yönlendirip konuyu kapatmak"],
              1, "Aileler bilmemeyi affeder; bilmediği hâlde biliyormuş gibi yapmayı ya da araştırmaya zahmet etmemeyi affetmez. "
                 "Söz verip geri dönmek güveni güçlendirir."),
        ],
        akilda="Aile öyküsünde etiketi değil seyri sorun; güven, bilmemekle değil biliyormuş gibi yapmakla kaybedilir.",
    ),
    # ------------------------------------------------------------------ 6
    dict(
        no=6, kesim="C", kisa="Ebeveynler",
        baslik="Ebeveyn türleri ve ebeveynlerle konuşmak",
        kitapta_bolumler="C. The Family · Types of Parents; Talking to Parents (s. 108–125)",
        slogan="Bir ebeveynin sizde uyandırdığı duygu, büyük olasılıkla başkalarında da uyanıyordur.",
        kitapta=("Bölümler ebeveynleri kaba bir tipolojiyle (fazla yetkin, kaygılı, kendi psikopatolojisi olan, dezavantajlı, talepkâr, "
                 "pasif, zor, boşanmış ve çatışmalı) ele alır ve klinisyende uyanan tepkileri bilgi kaynağı olarak kullanmayı önerir; "
                 "ardından üslubu eşlemek, seansı başlatmak, ağlayan ya da çocuğunu aşağılayan ebeveyne yanıt, klinisyenin öfkesi ve "
                 "transaksiyonel analizin “oyunlar” çerçevesiyle ebeveyn görüşmesinin pratiğini anlatır."),
        okurken=[
            "Bir ebeveynin sizde uyandırdığı sıkıntı, korku ya da öfke hangi klinik bilgiyi taşıyor olabilir?",
            "Boşanmış ebeveynler tanı ya da ilaç konusunda ayrıştığında klinisyen nerede durmalı?",
            "Her öneriye “evet ama…” diye yanıt verilen bir görüşmede ne oluyor olabilir?",
        ],
        fikirler=[
            ("Karşı aktarım bir veridir", "Bir ebeveynin sizde uyandırdığı duygu muhtemelen öğretmende, eşte ve çocukta da uyanmaktadır. "
             "Ebeveynle ya da ergenle bir türlü ortak bir hedefte buluşulamıyorsa, bu durum çekirdek sorunlardan biri olabilir."),
            ("Fazla yetkin ve kaygılı ebeveyn", "Ölçütleri ezberlemiş ve çocuğu sürekli gözleyen ebeveyn hem yanlış pozitif hem yanlış "
             "negatif riskini artırabilir. Kaygılı ebeveynde felaket senaryolarını tek tek çürütmek yerine olasılıkları sakin bir dille "
             "yeniden çerçevelemek daha çok işe yarar."),
            ("Ebeveynin kendi güçlüğü", "Ebeveyndeki depresyon, otizm ya da tedavi edilmemiş DEHB, ebeveynlik tarzını ve tedaviye katılımı "
             "etkiler. Dezavantajlı, okuryazarlığı sınırlı ya da göçmen ailelerde engel çoğu zaman isteksizlik değil erişimdir."),
            ("Zarar ayrılıktan çok çatışmadan gelir", "Çocuğa zararın büyük kısmı ayrılığın kendisinden değil, süregiden ebeveyn "
             "çatışmasından kaynaklanır. Ebeveynler ayrıştığında klinisyen taraf olmamalı, iki ebeveyni de bilgilendirmeli ve çocuğun "
             "çıkarını merkezde tutmalıdır."),
            ("Önce çocuk, sonra ortak gündem", "Görüşmeyi çocukla başlatmak, ebeveynin kaygıları zihni doldurmadan çocuğu görmeyi sağlar. "
             "Kontrollerde “nasıl gidiyor?” yerine ortak bir gündem çıkarmak ve üslubu ebeveynin düşünme biçimine eşlemek mesajın ulaşmasını kolaylaştırır."),
            ("Aşağılamaya hemen, kınamadan müdahale", "Ebeveyn çocuğu odada aşağılıyorsa hemen araya girilir; ama ebeveyni yargılamak yerine "
             "çaresizliğini adlandırmak ilişkiyi korur. Klinisyenin kendi öfkesi de bir veridir. Transaksiyonel analizin “oyunları” kanıt "
             "değil, düşünmeye yardım eden bir mercektir."),
        ],
        crs=[
            "Bir ebeveyn sizde güçlü bir duygu uyandırdığında bunu kısa bir notla kaydedin ve öğretmenin ya da ekip üyelerinin deneyimiyle karşılaştırın.",
            "Çok sayıda uzmandan ayrı ayrı tanı almış bir çocukta tanıları tek tek değil, ortak bir işlev bozukluğu haritası üzerinde birleştirmeye çalışın.",
            "TR Okuryazarlığı sınırlı ailelerde yazılı broşür yerine sözlü özet ve resimli çizelge kullanın; doz talimatını aileye geri anlattırarak doğrulayın.",
            "TR Türkçeyi sınırlı konuşan göçmen ailelerle mesleki tercüman kullanın; çocuğu tercüman yapmak hem bilgiyi bozar hem aile hiyerarşisini zorlar.",
            "TR Boşanmış ebeveynlerde velayeti ve tıbbi karar yetkisini dosyaya not edin; Türkiye’deki düzenleme İngiliz hukukundan farklıdır, gerektiğinde kurumunuzun hukuk birimine danışın.",
            "Ebeveyn çocuğu odada aşağılarsa nazikçe araya girin ve duyguyu adlandırın; konuyu çocuğun yanında değil, ayrıca konuşmayı önerin.",
            "Kontrol görüşmelerini ebeveynin ve çocuğun gündem maddelerini listeleyerek başlatın; liste tamamlanmadan ilk maddeye dalmayın.",
            "“Evet ama…” döngüsü fark ettiğinizde öneri sıralamayı bırakın; ebeveyne neyin değişmesini en çok istediğini ve neyin değişmesinden çekindiğini sorun.",
        ],
        tartisma=[
            ("Ebeveyn çatışması ve çocuk ruh sağlığı",
             "Kanıtlar, ebeveynler arası çatışmanın aile yapısından bağımsız olarak çocuk psikopatolojisiyle ilişkili olduğunu gösterir "
             "([@harold2018]). Bu, boşanmayı değil çatışmayı hedef alan müdahalelerin gerekçesidir."),
            ("Ebeveyn depresyonu çocuğun tedavisinin parçasıdır",
             "Anne depresyonu çocukta içe ve dışa yönelim sorunlarıyla küçük ama tutarlı ilişkiler gösterir ([@goodman2011]). "
             "Ebeveynin ruh sağlığını sormak ve yönlendirmek, çocuğun tedavisinin bir bileşenidir."),
            ("Tanı bir sosyal araç olabilir mi?",
             "Kitap bir yerde yanlış pozitif DEHB tanısının başka tanıları gölgelediğini vurgular; başka bir yerde tanının dezavantajlı "
             "ailelerde suçluluğu azaltan ve okulu, aileyi ve ekibi aynı hedefe yönelten bir araç olabileceğini öne sürer. İki görüşün "
             "nasıl bağdaştırılacağı tartışmaya değerdir."),
            ("Bir mercek olarak transaksiyonel analiz",
             "Berne’in oyun modeli ([@berne1964]) klinik sezgiyi düzenler ama çağdaş ebeveyn eğitimi literatüründe ampirik temeli "
             "sınırlıdır. Babaların daha az bilgili olduğu gibi genellemeler de babaları sürece katmayan bir beklentiye dönüşebilir."),
        ],
        sorular=[
            S("On yaşındaki bir çocukta anne DEHB tanısını ve ilacı kabul ediyor; çocuğu yalnızca hafta sonları gören baba “bizde hiç "
              "sorun yok” diyerek ilaca karşı çıkıyor. En uygun yaklaşım hangisidir?",
              ["Anneyle devam edip babayı süreçten çıkarmak",
               "Babanın gözlemlerini dinlemek, iki ortamın farkını (ödev, yapı, süre) birlikte tartışmak ve karar yetkisini netleştirmek",
               "Babanın görüşüne göre tedaviyi durdurmak",
               "Çocuğa hangi ebeveyni haklı bulduğunu sormak"],
              1, "Yapılandırılmamış hafta sonları ile okul günleri farklı talepler doğurur; babanın gözlemi bir veridir. Taraf olmak "
                 "çatışmayı derinleştirir; çocuğu seçim yapmaya zorlamak ise zarar verir."),
            S("Bir babanın her sorunuza küçümseyici yanıt vermesi sizde öfke uyandırıyor. Bu duygunun en yararlı kullanımı hangisidir?",
              ["Aynı tonla karşılık vermek",
               "Öfkeyi, çocuğun ve öğretmenin bu babayla yaşadığı etkileşime dair bir veri olarak not etmek ve tepkisel yanıt vermemek",
               "Görüşmeyi kısa kesmek",
               "Duyguyu yok sayıp hiç düşünmemek"],
              1, "Klinisyende uyanan duygu, ebeveynin başkalarında da uyandırdığı tepkiye dair bir ipucudur. Fark edip kullanmak "
                 "hem formülasyonu zenginleştirir hem de tepkisel bir hatayı önler."),
            S("Görüşmede anne 12 yaşındaki kızı için “tembel ve aptal” diyor; kız başını önüne eğiyor. En uygun yanıt hangisidir?",
              ["Annenin sözlerini görmezden gelip öyküye devam etmek",
               "Nazikçe araya girip annenin yorgunluğunu adlandırmak ve bu konuyu kızın yanında değil, ayrıca konuşmayı önermek",
               "Anneyi kızın önünde sert biçimde eleştirmek",
               "Kıza annesinin haklı olup olmadığını sormak"],
              1, "Aşağılama karşısında hemen müdahale gerekir; ancak ebeveyni kınamak ilişkiyi koparır ve aileyi geri getirmez. "
                 "Duyguyu adlandırıp konuyu ayrı bir zamana taşımak hem çocuğu korur hem ebeveyni kazanır."),
        ],
        akilda="Ebeveynin sizde uyandırdığı duygu bir veridir; çatışmalı ailede taraf değil, çocuğun çıkarının sözcüsü olun.",
    ),
    # ------------------------------------------------------------------ 7
    dict(
        no=7, kesim="C", kisa="Beklentiler ve manipülasyon",
        baslik="Aile ne istiyor? Manipülasyon algısıyla çalışmak",
        kitapta_bolumler="C. The Family · What Do They Want?; D. Friction · Being Manipulated (s. 126–133)",
        slogan="Ne istediklerini sormadan neye ihtiyaçları olduğunu bilemezsiniz.",
        kitapta=("İlk bölüm ailelerin ve çocukların sağlık hizmetinden gerçekte ne istediğini, karara katılım tercihlerini, gerçekçi ve "
                 "ölçülebilir hedef koymayı, sevk sorusuna verilen farklı yanıt tarzlarını ve ailenin yanlış, sağlanamayan ya da "
                 "engelliliği “düzeltecek” bir tedavi istediği durumları ele alır. İkinci bölüm manipülasyonun tanımını, temaruzu, "
                 "abartıyı, tekrarlayan yardım arayışını ve klinisyenin sınırlarını koruma yollarını tartışır."),
        okurken=[
            "Ailenin istediği ile çocuğun ihtiyacı çatıştığında klinisyen neye göre karar verir?",
            "Bir tedavi hedefini ölçülebilir kılmak neden bu kadar önemlidir?",
            "“Manipülatif” sözcüğü klinik düşünmeye ne katar, neyi gizler?",
        ],
        fikirler=[
            ("Herkes karara aynı ölçüde katılmak istemez", "Bazı aileler ortak karar, bazıları net bir öneri, bazıları da kararı kendisi "
             "vermek ister. Hangisini istediklerini sormak, karar sürecini kişiye uyarlamanın en kısa yoludur."),
            ("Çocuk somut kazanç ister", "Çocuklar tanı ve damgalanma gibi soyut konulardan çok annenin daha az bağırması, öğretmenin daha "
             "az azarlaması gibi somut değişikliklerle ilgilenir. Ergenler ise tanıyı kimlikleriyle ilişkilendirebilir."),
            ("Gerçekçi ve ölçülebilir hedef", "Gerçekçi bir hedef çocuğun önceki en iyi hâline, güçlüğün nedenine ve tedavilerin olağan "
             "etkisine dayanır. Hedef çocuğun anlayacağı sayılara dönüştürülmeli ve tedavinin ne zaman biteceği baştan konuşulmalıdır. "
             "Ebeveynler bir değişiklikten sonra nasıl hissedeceklerini çoğu zaman yanlış tahmin eder."),
            ("Sevk sorusu bir başlangıçtır", "Klinisyenler sevk sorusuna farklı genişlikte yanıt verir: yalnızca sorulan kategoriye bakmaktan, "
             "sevk yazısını kapsamlı bir değerlendirmenin kaynaklarından biri saymaya kadar. Kendi varsayılan tarzınızı bilmek, neyi kaçırabileceğinizi gösterir."),
            ("Yanlış ya da sağlanamayan istek", "Ebeveyn yanlış bir tedavi istediğinde önce nedenini öğrenin; istek çoğu zaman yanlış bir "
             "bilgiye dayanır. Ucuz, risksiz ve güveni artıran bir isteği kabul etmek stratejik olabilir; etkili tedaviyi geciktiren istek ise gerekçesiyle reddedilir."),
            ("“Manipülatif” bir hipotezdir", "Çocuklar yetişkinlerden daha manipülatif değildir; çoğu, önceki davranışlarının sonuçlarına yanıt "
             "verir. Abartı çoğu zaman kandırmak için değil duyulmak için yapılır. “Kendini şu yolla korumaya çalışıyor” demek, çözülmesi gereken asıl sorunu görünür kılar."),
        ],
        crs=[
            "İlk planı yapmadan önce ailenin karara nasıl katılmak istediğini sorun: “Seçenekleri birlikte mi tartalım, yoksa size en uygun olanı mı önereyim?”",
            "Hedefi çocuğun anlayacağı bir sayıya bağlayın (ör. “haftada kaç sabah okula zamanında gidiyorsun?”) ve her kontrolde aynı sayıyı sorun.",
            "Tedavinin ne zaman başarılı sayılacağını ve ne zaman sonlanacağını ilk planda yazın; bitiş noktası olmayan tedavi kendiliğinden uzar.",
            "Sevk sorusunu yanıtlayın, ama yanında öğrenme, duygudurum ve aile ortamı gibi birkaç standart alanı her zaman tarayın.",
            "TR Aile “rapor için” tanı istediğinde hangi hakka ulaşmayı umduğunu sorun; ÇÖZGER ve RAM süreçlerinde belirleyici olan yalnızca tanının adı değil, işlevsellik ve eğitim gereksinimidir.",
            "Ekip toplantısında ve yazılarda “manipülatif” yerine “kendini … yoluyla korumaya çalışıyor” gibi betimleyici bir dil kullanın.",
            "Abartıldığını düşündüğünüz bir öyküde önce ailenin neden duyulmadığını hissettiğini sorun; abartı çoğu zaman bir yardım çağrısıdır.",
            "Tekrarlayan ve verimsiz yardım arayışında tıbbi çocuk istismarını ayırıcı tanıda tutun; şüpheyi klinisyen olmayanlarla paylaşmayın, kayıtları toplayın ve kurumunuzun çocuk koruma prosedürüne göre kıdemli bir meslektaşla görüşün.",
        ],
        tartisma=[
            ("Klinik bilgelik mi, kanıt mı?",
             "Yazarlar bu bölümde cinsiyet kimliği hizmetlerine ilişkin genel ve güçlü bir eleştiriyi birkaç klinik gözleme dayandırır. "
             "Alan bilimsel ve toplumsal olarak tartışmalıdır: İngiltere’de 2024’te yayımlanan bağımsız değerlendirme (Cass Review) "
             "ergenlere yönelik endokrin müdahalelerin kanıt temelini zayıf bulmuş ve bu tedavilerin araştırma çerçevesinde sunulmasını "
             "önermiştir ([@cheung2025]); değerlendirmenin yöntemi ve sonuçları ise başka araştırmacılarca eleştirilmiştir ([@noone2025]). "
             "Bu bölümü kanıta dayalı bir öneri olarak değil, yazarların klinik görüşü olarak okumak gerekir."),
            ("Körlemeli denemenin etiği",
             "İlaç yanıtını çift kör, tek hastalı (n-of-1) denemelerle sınamak günlük pratikte uygulanabilir ve tedavi kararlarını "
             "değiştirebilir ([@nikles2006]). Ancak deneme ailenin dürüstlüğünü sınamaya dönüşmemelidir; tasarım ve amaç aileyle "
             "paylaşılmalı, onam alınmalıdır."),
            ("Temaruzu aramak mı, aramamak mı?",
             "Gerçek bir sıkıntıyı yanlışlıkla temaruz sayıp suçlamanın zararı, gerçek bir temaruzu kaçırmanın zararından büyük olabilir. "
             "Öte yandan aynı bölüm sınırları korumayı da önerir; iki tutumun aynı vakada nasıl birlikte uygulanacağı tartışmaya açıktır."),
            ("Stratejik olarak kabul etmek",
             "Ucuz ve risksiz ama etkisiz bir tedaviye izin vermek güveni artırabilir. Ancak neyin risksiz olduğuna klinisyen karar verir; "
             "zaman kaybı ve etkili tedavinin gecikmesi de gerçek maliyetlerdir."),
        ],
        sorular=[
            S("Obsesif-kompulsif belirtileri olan 11 yaşındaki bir çocukta tedavinin etkisini izlemek için en uygun hedef hangisidir?",
              ["Annenin genel olarak “daha iyi” hissetmesi",
               "Haftalık olarak yıkanmaya harcanan süre ve ritüeller nedeniyle okula geç kalınan sabah sayısı",
               "Çocuğun görüşmelere gelmeye istekli olması",
               "Çocuğun “artık sorun yok” demesi"],
              1, "İyi bir hedef sayılabilir, çocuğun anlayacağı ve işlevsellikle bağlantılı olmalıdır. Genel izlenimler ve tek bir "
                 "davranışın görünür olmaması, belirtilerin başka bir ortama taşınmasını gizleyebilir."),
            S("Davranış önerilerini uygulamakta zorlanan bir ebeveyn, 6 yaşındaki çocuğunun gece uyuması için “güçlü bir sakinleştirici” "
              "istiyor. En uygun yaklaşım hangisidir?",
              ["İstenen ilacı hemen reçete etmek",
               "İsteğin ardındaki beklentiyi ve zorluğu anlamak, önerileri uygulanabilir küçük adımlara bölmek ve sakinleştiricinin risklerini açıklamak",
               "İsteği tartışmadan reddedip görüşmeyi bitirmek",
               "Aileyi başka bir hekime yönlendirmek"],
              1, "Yanlış bir tedavi isteğinin ardında çoğu zaman tükenmişlik ya da yanlış bilgi vardır. Nedeni anlamak ve uygulanabilir "
                 "bir alternatif sunmak, hem ilişkiyi korur hem de gereksiz ilaç maruziyetini önler."),
            S("Serviste yatan 16 yaşındaki bir ergen, her taburculuk planı konuşulduğunda kendine zarar verme düşüncelerini dile getiriyor. "
              "Bir ekip üyesi onu “manipülatif” olarak tanımlıyor. En yararlı yaklaşım hangisidir?",
              ["Riski göz ardı etmek",
               "Taburculuğu süresiz ertelemek",
               "Riski ciddiye alarak değerlendirmek ve davranışın taburculukla ilgili hangi korkuyu ya da gereksinimi dile getirdiğini formüle edip planı buna göre düzenlemek",
               "Ergene manipülatif olduğunu açıkça söylemek"],
              2, "“Manipülatif” etiketi riski küçümsetebilir ve asıl sorunu gizler. Davranışın işlevini anlamak (ör. eve dönüş korkusu, "
                 "destek kaybı) hem güvenliği hem de gerçekçi bir taburculuk planını mümkün kılar."),
        ],
        akilda="Ne istediklerini sorun, hedefi sayıya bağlayın; “manipülatif” demeden önce çözmeye çalıştıkları sorunu arayın.",
    ),
    # ------------------------------------------------------------------ 8
    dict(
        no=8, kesim="D", kisa="Yanlış kanılar, reddetmek",
        baslik="Yaygın yanlış kanılar ve nasıl reddedilir",
        kitapta_bolumler="D. Friction · Common Misconceptions; How to Refuse or Disagree (s. 134–152)",
        slogan="Bir kapıyı kapatırken başka bir kapı açın.",
        kitapta=("İlk bölüm ebeveynlerin sık rastlanan yanlış kanılarına (özel yetenekler, izole bir sorun, ilacın çocuğu uyuşturması, "
                 "stimülan ve bağımlılık, aşı ve otizm, aşırı ilaçlandırma, otizmin hiç değişmeyeceği) nasıl yanıt verileceğini ve "
                 "yazarların tanı kategorileri için öznel “puan kartlarını” ele alır. İkinci bölüm doğrudan reddetmeye alternatifleri, "
                 "atılganlığı, hafiften serte yüzleşme biçimlerini ve ailenin kanıtsız bir tanıda ısrar ettiği ya da tanıyı reddettiği durumları anlatır."),
        okurken=[
            "Bir yanlış kanıyı düzeltmek her zaman değer mi; hangi durumda konuşmamak daha iyidir?",
            "Bir tanının güvenilirliği ile tedaviye yol gösterip göstermemesi neden ayrı ayrı sorgulanmalı?",
            "“Hayır” demeden reddetmenin hangi yolları ilişkiyi korur?",
        ],
        fikirler=[
            ("Yanlış kanıyı olasılıkla yanıtlamak", "“İlaç çocuğu uyuşturur” kaygısı inkâr edilmemeli; bunun ilaca ve doza bağlı olduğu ve "
             "önlenmesinin klinisyenin işi olduğu söylenmelidir. Kısa ve izlenen bir deneme çoğu zaman tartışmadan daha ikna edicidir."),
            ("İzole sorun nadirdir", "Okuma ya da aritmetik güçlüğü olan çocukların çoğunda başka alanlarda da güçlük vardır; motor "
             "bozukluklara sıklıkla bilişsel güçlükler eşlik eder. “Sadece okuma sorunu” çerçevesi desteği daraltabilir."),
            ("Gelişim sürer", "Zihinsel yetersizlik yaşam boyu sürer; otizm belirtileri ise yaşla genellikle bir ölçüde hafifler ve uyumsal "
             "beceriler ergenlik boyunca gelişmeyi sürdürebilir. “Asla değişmez” ve “tamamen geçer” iki uç yanlıştır."),
            ("Tanıların sağlamlığı eşit değildir", "Bazı tanılar güvenilirdir ve tedaviye yol gösterir; bazıları bulanık, suçlayıcı ya da "
             "tedaviye katkısızdır. Her tanıyı güvenilirlik, tedavi edilebilirlik ve yaygınlık açısından ayrı ayrı sorgulamak, aşırı kullanılan etiketlerin asıl nedenleri gizlemesini önler."),
            ("Çıplak “hayır” yerine bir yelpaze", "Tartışmasız bir olguya inmek, seçenek sunmak, kesinlik dilini yumuşatmak, kuralın kaynağını "
             "dışarıya yüklemek, kaygıyı dile getirmek ya da taleplerin bir kısmını kabul etmek ilişkiyi koruyarak sınır koymayı sağlar. "
             "Atılganlık saldırganlık değildir; klinisyenler daha çok aşırı uyum tarafında hata yapar."),
            ("Tanıya itiraz bir bilgi olabilir", "Formülasyona itiraz eden aile sizin bilmediğiniz bir şeyi biliyor olabilir. Kanıtsız bir "
             "tanıda ısrar ya da tanıyı reddetme karşısında ret ifadelerini hafiften serte basamaklandırmak, ölçütleri aileyle birlikte "
             "işlemek ve gerekirse ikinci görüş almak yol gösterir."),
        ],
        crs=[
            "TR “İlaç bağımlılık yapar mı?” sorusunu inkâr etmeden yanıtlayın: kötüye kullanım riskini, saklamayı ve gözetimi konuşun; metilfenidatın neden kırmızı reçeteyle verildiğini açıklayın.",
            "Aşı ve otizm kaygısında önce ailenin yaşadığı zamanlamayı dinleyin; canlı bir anı istatistikten güçlüdür, bu yüzden bilgi verin ama her seferinde ikna etmeye çalışmayın.",
            "Okuma güçlüğü olan çocukta dil, dikkat, motor ve aritmetik becerileri de değerlendirin.",
            "Ailenin “çok zeki” algısına doğrudan karşı çıkmayın; test sonuçları ve öğretmen gözlemi gibi olgulara odaklanın, beklenti çocuğa zarar veriyorsa bunu ayrıca konuşun.",
            "Reddederken üç parçalı bir cümle kurun: anlayış, gerekçe ve yapabileceğiniz alternatif (“Bunu yapamam, ama şunu yapabilirim”).",
            "Kontrollü bir ilacın başka bir hekimce başlatılmış reçetesini yenileme talebini reddederken gerekçeyi, kayda geçen kararı, alternatifi ve kibar bir kapanışı içeren kısa bir yanıt yazın.",
            "TR Aile sorunu cin ya da nazara bağlıyor ve dua ya da muska gibi zararsız bir uygulama sürdürüyorsa bununla çatışmayın; tıbbi değerlendirmeyi geciktiren ya da çocuğa zarar veren uygulamalar karşısında ise açık olun.",
            "Çocuk açıkça zarar görmüyorsa ebeveyni her konuda ikna etmek zorunda değilsiniz; tartışmayı tedaviyi etkileyen konulara saklayın.",
            "Ebeveyne çocuğun önünde “yanılıyorsunuz” demeyin; anlaşmazlığı ayrı bir görüşmeye taşıyın.",
        ],
        tartisma=[
            ("Stimülanlar madde kullanım riskini artırır mı?",
             "Meta-analiz, çocuklukta stimülan tedavisinin madde kullanım sonuçlarıyla ilişkili olmadığını, yani riski artırmadığını "
             "göstermiştir ([@humphreys2013]). ABD sağlık sigortası kayıtlarına dayanan bir çalışmada ilaç kullanılan aylarda madde "
             "kullanımıyla ilişkili acil başvuruları daha az görülmüştür ([@quinn2017]). Uzun dönemde koruyucu bir etki olup olmadığı ise "
             "çalışma tasarımına ve karıştırıcılara bağlı olarak belirsizdir."),
            ("Aşı ve otizm",
             "Ulusal kohort verileri MMR aşısı ile otizm arasında ilişki göstermemiştir ([@hviid2019]). Japonya’da MMR kullanımının "
             "bırakılmasından sonra otizm sıklığı azalmamıştır ([@honda2005])."),
            ("“Bağlanma sorunu” jargonu ve resmî tanı",
             "Reaktif bağlanma bozukluğu ve disinhibe sosyal angajman bozukluğu, belirgin bakım yoksunluğu öyküsü ve ayırıcı tanı "
             "gerektiren dar tanılardır ([@zeanah2016]). Yazarların bu etiketin klinikte gevşek kullanımına yönelik eleştirisi bu "
             "ölçütlerle uyumludur; Türkiye’de de “bağlanma sorunu” ifadesi sıklıkla tanı ölçütlerinden bağımsız kullanılır."),
            ("Kolaylaştırılmış iletişim",
             "Bir yardımcının elini destekleyerek yazdırdığı iletişim yönteminde mesajların çoğunlukla yardımcıdan geldiği kontrollü "
             "çalışmalarla gösterilmiştir ([@schlosser2014]). Ailenin umudunu desteklemek ile bilimsel olarak geçersiz bir yöntemi "
             "onaylamak arasındaki gerilim bu bölümün en zor etik sorularındandır."),
        ],
        sorular=[
            S("Bir baba, DEHB tanısı alan 9 yaşındaki oğlu için “İlaç onu uyuşturur, kuzenime öyle oldu” diyor. En uygun yanıt hangisidir?",
              ["Bunun asla olmayacağını söylemek",
               "Bunun olabileceğini kabul edip ilaca ve doza bağlı olduğunu, izlenerek önlenebileceğini anlatmak ve kısa, izlenen bir deneme önermek",
               "Babanın görüşünü bilimsel olmadığı için reddetmek",
               "İlaç seçeneğini tamamen gündemden çıkarmak"],
              1, "İnkâr güveni zedeler; aile bu durumu gerçekten görmüş olabilir. Endişeyi kabul edip neye bağlı olduğunu açıklamak ve "
                 "kısa bir denemeyle birlikte değerlendirmek, tartışmadan daha ikna edicidir."),
            S("Bir ebeveyn, davranış sorunları olduğu açık olan 7 yaşındaki çocuğu için internette okuduğu ve kanıta dayalı karşılığı "
              "olmayan bir etiketle tanı konmasını istiyor. İlk yanıt olarak en uygun hangisidir?",
              ["“Böyle bir şey yok” deyip konuyu kapatmak",
               "Bir sorun olduğunu gördüğünüzü ama bu açıklamadan emin olmadığınızı söylemek ve gözlenen davranışları birlikte tanımlamak",
               "Ailenin istediği tanıyı rapora yazmak",
               "Aileyi başka bir hekime yönlendirmek"],
              1, "Ret ifadelerinin en yumuşak basamağı sorunu kabul edip açıklamayı sorgulamaktır. Davranışları birlikte tanımlamak, "
                 "tartışmayı etiketten işlevselliğe ve tedaviye taşır."),
            S("Disleksi tanısı almış 10 yaşındaki bir çocuğun ailesi “Onun tek sorunu okuma” diyor. En doğru yaklaşım hangisidir?",
              ["Aileye katılıp yalnızca okuma desteği planlamak",
               "Okuma güçlüğünün sıklıkla dil, dikkat, motor ya da aritmetik güçlükleriyle birlikte görüldüğünü açıklayıp bu alanları da değerlendirmek",
               "Disleksi tanısını geri almak",
               "Ailenin beklentilerini düşürmek için zekâ testi sonucunu vurgulamak"],
              1, "Okuma becerisi birçok bilişsel bileşene dayanır; bu nedenle izole bir öğrenme güçlüğü nadirdir. Eşlik eden alanları "
                 "değerlendirmek desteğin kapsamını doğru belirler."),
        ],
        akilda="Yanlış kanıyı inkârla değil olasılıkla yanıtlayın; reddederken bir kapıyı kapatıp başka bir kapı açın.",
    ),
    # ------------------------------------------------------------------ 9
    dict(
        no=9, kesim="D", kisa="Ajitasyon ve öfke",
        baslik="Ajite düşünce, öfke ve kabalık",
        kitapta_bolumler="D. Friction · Agitated Thinking; Anger and Rudeness (s. 153–159)",
        slogan="Öfkeli olan hastadır, siz değil.",
        kitapta=("İlk bölüm ailede ajitasyonun görünmeyen ve görünen kaynaklarını, ajite bir aileyle çalışmayı ve ailenin hastalığa "
                 "tepkilerini; ikinci bölüm öfkenin uyarı işaretlerini, sözel ve sözel olmayan yatıştırmayı, durumu kötüleştirmemeyi, "
                 "bir şikâyetten sonraki ilk saatleri ve klinisyenin kendi tetikleyicilerini yönetmesini ele alır."),
        okurken=[
            "Ajitasyon klinik düşünmeyi nasıl etkiler ve görüşmede nasıl azaltılabilir?",
            "Öfkeli bir ebeveyne karşı ilk dakikalarda neler yapılmalı, neler yapılmamalı?",
            "Bir şikâyetten sonra “hata mı yaptım?” sorusunu nasıl dürüstçe yanıtlarsınız?",
        ],
        fikirler=[
            ("Ajitasyon sezgiyi daraltır", "Tehdit altında hisseden zihin esnekliğini kaybeder ve aynı anda çok fazla çözüm dener; bu hem "
             "aile hem klinisyen için geçerlidir. Çocuk psikiyatrisi en iyi sakin ve iş birliğine dayalı bir ortamda yapılır."),
            ("Görünmeyen kaynaklar", "Aile ilgisiz sandığı için bir yazışmadaki ifadeye kırılmayı, evdeki bir hastalığı ya da ekonomik bir "
             "sorunu söylemeyebilir. Çözümsüz bir çatışmada sıkışmak kendine zarar verme gibi davranışları tetikleyebilir; sınav "
             "dönemlerinde ağlama, uykusuzluk ve kaçınma birbirini besleyen bir döngü oluşturur."),
            ("Önce duygu, sonra çerçeve, sonra bilgi", "Ajite ebeveynin duygusunu gerekirse büyüterek sözcüklere dökmek anlaşıldığını "
             "hissettirir. Davranışı, gelişimi ya da hizmet sistemini anlamlandıracak bir çerçevesi olmayan ebeveyn bilgiyi tutamaz."),
            ("Aileler hastalığa farklı tepki verir", "Bazı aileler hasta çocuğun çevresinde kenetlenir ve çocuk iyileşince ortak hedef "
             "ortadan kalkar; çocuk düzeldikçe aile kötüleşiyormuş gibi görünebilir. Büyük değişikliklerde görüşler önce aşırıya kaçar, sonra dengelenir."),
            ("Öfkeyi büyütmemek", "Gülümsememe, dudak büzme, göz kaçırma ve kendi gerginliğiniz kaynama evresinin işaretleridir. Fazladan "
             "öngörülebilir ve yargısız olmak, güvenli bir oturma düzeni ve tek konuşmacı ilkesi tırmanmayı önler; karşılık olarak kabalık ya da babacanlık durumu kötüleştirir."),
            ("Şikâyetten sonra dürüst bir bakış", "Önce gerçekten hata yapıp yapmadığınızı sorun: dinlediniz mi, açıkladınız mı, beklettiniz "
             "mi, ekrana mı baktınız, çocukla konuştunuz mu? Hata varsa ilk gün içinde içten bir özür, yoksa saygılı bir yazı ve net "
             "seçenekler. Kendi tetikleyicilerinizi izlemek tükenmişliği önler."),
        ],
        crs=[
            "Kaynama evresindeki bir ebeveynle görüşürken çıkışın kolay erişilebilir olduğu bir oturma düzeni seçin ve odada yalnızca bir kişinin konuşmasını sağlayın.",
            "Bağıran bir ebeveyne sakin bir sesle durumu tarif edin: “Bağırılırken iyi düşünemiyorum; baştan başlayalım mı, yoksa kısa bir ara mı verelim?”",
            "TR Sağlıkta şiddet riski olan durumlarda kurumunuzun Beyaz Kod prosedürünü önceden bilin; güvenliği çağırmak bir başarısızlık değil, herkesin güvenliği için bir önlemdir.",
            "TR LGS ve YKS dönemlerinde ağlama, uykusuzluk ve kaçınmanın birbirini beslediği döngüyü erken fark edin; uyku düzenini ve sınav günü planını aileyle somut olarak konuşun.",
            "Aile içinde bir suçlama döngüsü varsa sorunu kişiden ayırıp adlandırmak (dışsallaştırma) suçlamayı azaltabilir.",
            "Bir şikâyetten sonra hata mı yaptığınızı dürüstçe gözden geçirin; hata varsa ilk gün içinde içtenlikle özür dileyin ve gerekirse özrü yazılı olarak tekrarlayın.",
            "Ekip toplantılarında aileleri “iyi, zor, kötü” diye değil, “bitkin, hasta, yardıma muhtaç, travmatize” gibi gereksinim odaklı sözcüklerle tartışın.",
            "Sizi sinirlendiren küçük durumları birkaç ay boyunca not edin; tekrarlayan örüntüler tükenmişliğin erken işaretidir. Sık karşılaşılan küçük kabalıklar için sakin, hazır yanıtlarınız olsun.",
        ],
        tartisma=[
            ("Yas aşamaları ve kronik keder",
             "Kitap ebeveynlerin çocuktaki yetersizliğe tepkisini klasik yas aşamalarıyla anlatır. Ancak aşama modelleri yas "
             "araştırmalarında eleştirilmektedir: insanlar aşamaları sırayla yaşamayabilir ve modelin sağlık çalışanlarını yanıltabileceği "
             "vurgulanmıştır ([@stroebe2017]). Zihinsel yetersizliği olan çocukların ebeveynleri, zamanla sınırlı bir uyum yerine "
             "gelişim dönemeçlerinde yineleyen krizler yaşadıklarını bildirmiştir; profesyoneller ise sonraki dönemlerin etkisini "
             "küçümseme eğilimindedir ([@wikler1981]). Bu bulgu Olshansky’nin “kronik keder” kavramıyla uyumludur."),
            ("Karşı aktarımda nefret",
             "Kitapta aktarılan bir örnekte klinisyen bir çocuğa yönelik yoğun olumsuz duygular nedeniyle vakayı bırakır. Winnicott, "
             "bu tür duyguların incelendiğinde terapötik süreç için bilgi taşıyabileceğini öne sürmüştür ([@winnicott1994]). "
             "Vakayı bırakmak ile bu duygularla süpervizyonda çalışmak arasındaki denge tartışılmaya değerdir."),
            ("Bir bardak çay neyi değiştirir?",
             "Sıcak bir içeceğin kişilerarası sıcaklık algısını artırdığı bulgusu ([@williams2008]) sonraki replikasyon çalışmalarında "
             "doğrulanamamıştır ([@chabris2019]). İkramın bir nezaket jesti olarak değeri klinik gözleme dayanabilir; ama özrün ya da "
             "dinlemenin yerine geçmez."),
            ("Türkiye’de sağlık çalışanına şiddet",
             "Türkiye’de 12.944 sağlık çalışanıyla yapılan ulusal bir çalışmada çalışanların %44,7’si son 12 ayda işyerinde şiddete "
             "(en sık sözel) maruz kaldığını bildirmiştir ([@pinar2017]). Bu nedenle kitabın öfkenin uyarı işaretleri ve yatıştırma "
             "önerileri, Türkiye’deki eğitimde sistematik olarak öğretilmeyi hak eder."),
        ],
        sorular=[
            S("Görüşmenin ortasında bir baba sesini yükseltip “Aylardır bekliyoruz, kimse bir şey yapmıyor!” diye bağırıyor. İlk yanıt "
              "olarak en uygun hangisidir?",
              ["Aynı tonda bekleme listesinin sizin suçunuz olmadığını açıklamak",
               "Sakin bir sesle duyguyu adlandırmak (“Aylarca beklemek çok yıpratıcı olmalı”) ve ardından şu an en acil olanın ne olduğunu sormak",
               "Hemen bir içecek ikram etmek",
               "Görüşmeyi derhal sonlandırıp güvenliği çağırmak"],
              1, "Duyguyu adlandırmak ve ortak bir sorun tanımına geçmek tırmanmayı azaltır. Karşılık vermek durumu kötüleştirir; ikram "
                 "dinlemenin yerine geçmez. Güvenlik, gerçek bir tehdit belirdiğinde çağrılır."),
            S("Bir anne şikâyette bulunuyor: görüşmede bilgisayara yazarken çocuğa hiç dönmediğinizi ve sorularını yanıtlamadığınızı söylüyor. "
              "Notlarınızdan bunun doğru olduğu anlaşılıyor. En uygun adım hangisidir?",
              ["Ayrıntılı bir savunma yazısı hazırlamak",
               "Kısa sürede anneyle iletişime geçip içtenlikle özür dilemek, sorularını yanıtlamak ve sonraki görüşmede neyi farklı yapacağınızı somutlaştırmak",
               "Şikâyeti görmezden gelmek",
               "Vakayı hemen başka bir hekime devretmek"],
              1, "Hata varsa en etkili yanıt hızlı ve içten bir özürdür. Savunmaya geçmek ya da görmezden gelmek güveni daha da zedeler; "
                 "devretmek ancak ilişki onarılamazsa gündeme gelir."),
            S("Lise giriş sınavına hazırlanan 14 yaşındaki bir kız son iki haftadır her akşam ağlıyor, geç uyuyor ve deneme sınavlarına "
              "girmek istemiyor; aile çok gergin. En yararlı ilk yaklaşım hangisidir?",
              ["Sınavdan çekilmesini önermek",
               "Hemen bir benzodiazepin başlamak",
               "Ağlama, uykusuzluk ve kaçınmanın birbirini beslediği döngüyü aileyle tanımlamak, uyku düzenini ve somut bir sınav planını ele almak, kaygı ve duygudurum belirtilerini değerlendirmek",
               "Aileye baskıyı azaltmasını söyleyip görüşmeyi bitirmek"],
              2, "Sınav dönemindeki ajitasyon kendini besleyen bir döngüdür. Döngüyü görünür kılmak ve somut bir plan yapmak, aceleyle "
                 "bulunan kötü “çözümlerin” (sınavı bırakmak, gereksiz ilaç) önüne geçer."),
        ],
        akilda="Öfkeli olan hastadır, siz değil: duyguyu adlandırın, tırmanmayı beslemeyin; hata varsa hemen ve içtenlikle özür dileyin.",
    ),
    # ------------------------------------------------------------------ 10
    dict(
        no=10, kesim="E", kisa="Nedenler ve şimdiki durum",
        baslik="Nedenleri bulmak ve şimdiki durumu betimlemek",
        kitapta_bolumler="E. Formulating · Finding Causes; Describing the Current State (s. 160–177)",
        slogan="Yaygın bir belirti, nadir bir açıklamadan sizi asla tek başına emin kılmamalı.",
        kitapta=("İlk bölüm çocuk psikiyatrisinin neden arayışını, nedenselliğin ilkelerini, nomotetik ve idiografik bilgiyi, "
                 "olasılıkları yazılı olarak %100’e tamamlamayı, Bayesçi düşünmeyi, birden fazla bilgi kaynağını birleştirmeyi ve "
                 "bireysel çocuğa uyarlanmış nedensellik ölçütlerini ele alır. İkinci bölüm fenomenolojiyi, kategori ile spektrum "
                 "ayrımını, DSM eleştirilerini, kontrol listesi kültürünü, komorbiditeyi ve tanı hiyerarşisini tartışır."),
        okurken=[
            "“Ne zaman başladı, ne iyileştiriyor ya da kötüleştiriyor, ailede ne var?” soruları neden bu kadar güçlüdür?",
            "Yaygın bir belirti, nadir bir açıklama için ne kadar kanıt sağlar?",
            "“Komorbid” sözcüğü iki sorun arasındaki ilişki hakkında ne söyler, neyi söylemez?",
        ],
        fikirler=[
            ("Çocuk psikiyatrisi neden arar", "Çocuklar çoğu değiştirilebilir etkilerden oluşan bir ortamda gelişir. Her ilk görüşmenin "
             "çekirdeğinde üç soru vardır: ne zaman başladı, ne iyileştiriyor ve ne kötüleştiriyor, ailede başka kimde benzer güçlükler var? "
             "İşlevsellik kaybının asıl kaynağını da ayrıca sormak gerekir."),
            ("Nedenselliğin ilkeleri", "Klinikte görülenin çoğu durumun kendisi değil, çocuğun ona verdiği tepkidir. Olağandışı her olayın "
             "özgül bir nedeni olmayabilir; çoğu sorunun birden fazla küçük nedeni vardır ve bir neden bulmak aramayı bitirmemelidir. "
             "Tutarsızlıklar ve istisnalar çoğu zaman çocuğu anlamanın anahtarıdır."),
            ("Olasılıkları %100’e tamamlamak", "Ayırıcı tanıyı yazılı yapmak ve olasılıkların toplamını %100’e tamamlamak “belirgin bir "
             "sorun yok” seçeneğini hesaba katmayı sağlar ve nadir açıklamaları şişirme eğilimini dizginler. Tek bir belirti iki ayrı "
             "tanının kanıtı olarak iki kez sayılmamalıdır."),
            ("Bayes ve bağımsız kaynaklar", "En sık hata tek bir bilgi kaynağına dayanmaktır. Bağımsız kaynakların uyuşması ve yalnızca "
             "nadir tanı doğruysa gerçekleşecek riskli bir tahmin güveni artırır. Bireysel çocukta nedensellik için zamansal sıra, "
             "doz-yanıt ilişkisi ve bırakıp yeniden başlama sınanabilir."),
            ("Kategori ve spektrum birlikte", "Spektrumlar biyolojik gerçekliğe daha yakındır ve şiddeti gösterir; kategoriler karar vermeyi "
             "kolaylaştırır. DSM kuramsız değildir; asıl sorun onun yönetimin merkezine yerleştirilmesi, nedensel ilişkilerin ihmal "
             "edilmesi ve kontrol listesi kültürünün doğrulama yanlılığını beslemesidir."),
            ("Komorbidite bir sorudur", "İki tanının birlikteliği farklı ilişkiler anlamına gelebilir: biri ötekinin ağır biçimi, parçası "
             "ya da başka bir görünümü olabilir; ikisi ortak bir nedenden doğabilir ya da biri ötekinin riskini artırabilir. "
             "Değerlendirmede önce zihinsel yaş gelir: diğer bulgular ona göre yorumlanır."),
        ],
        crs=[
            "Her ilk görüşmenin başına üç soru koyun: Ne zaman başladı? Ne iyileştiriyor, ne kötüleştiriyor? Ailede başka kimde benzer güçlükler var?",
            "Ayırıcı tanınızı vaka notuna yüzdelerle yazın, toplamı %100’e tamamlayın ve “belirgin bir bozukluk yok” seçeneğini de listeye ekleyin.",
            "Asistan bir görüşünü onaylatmak istediğinde “Kaç bağımsız bilgi kaynağın var?” diye sorun.",
            "Nadir bir tanıdan şüphelendiğinizde yalnızca o tanı doğruysa görülecek bir bulguyu önceden yazın ve onu arayın.",
            "Bir gıda, ilaç ya da uyku değişikliğinin etkisini değerlendirirken zamansal sıraya, doza ve bırakıp yeniden başlamaya bakın; değişiklikleri tek tek yapın.",
            "Nörogelişimsel değerlendirmede önce zihinsel yaşı kestirin; dikkat ve sosyal beceri bulgularını takvim yaşına değil zihinsel yaşa göre yorumlayın.",
            "Gelişimsel bir tanı (DEHB, otizm, öğrenme güçlüğü, tik) koyduğunuzda başka birini de arayın; birliktelik istisna değil kuraldır.",
            "Yetersiz uyku ya da ebeveynler arası gerginlik gibi sık görülen olguları bulduğunuzda hemen nedensel açıklamaya bağlamayın; aynı olgular sorunu olmayan çocuklarda da sıktır.",
            "TR Tanı ÇÖZGER ya da RAM yönlendirmesi gibi haklarla bağlantılı olduğunda, yanlış olduğunu düşündüğünüz bir tanıyı “çocuğun yararına” koruma baskısı doğabilir; böyle bir kararı açıkça kayda geçirin ve ekiple tartışın.",
        ],
        tartisma=[
            ("Hekimler olasılıkları nasıl değerlendiriyor?",
             "Klasik bir çalışmada hekimlerin ve tıp öğrencilerinin çoğu, düşük yaygınlıkta pozitif bir test sonucunun anlamını "
             "belirgin biçimde abartmıştır ([@casscells1978]). Bilgiyi oranlar yerine doğal sıklıklarla sunmak bu hatayı azaltır "
             "([@hoffrage2000])."),
            ("DSM eleştirisi ve boyutsal modeller",
             "Yazarların eleştirisi (keyfi eşikler, yapay komorbidite, boyutsal gerçeklik) RDoC ([@insel2010]) ve HiTOP ([@kotov2017]) "
             "gibi boyutsal yaklaşımların çıkış noktasıyla örtüşür; ancak kitap bu alternatiflere değinmez. Kitap neden arayışını, "
             "boyutsal modeller ise taksonomiyi yeniden kurmayı önerir."),
            ("Cinselleşmiş davranış tek başına tanısal mı?",
             "45 çalışmanın derlemesinde cinselleşmiş davranış istismara uğramış çocuklarda en sık görülen belirtiler arasında yer "
             "almış; ancak hiçbir belirti bu çocukların çoğunluğunu tanımlamamış ve yaklaşık üçte birinde belirti saptanmamıştır "
             "([@kendalltackett1993]). Bu nedenle cinselleşmiş davranış tek başına bir sonuç değil, dikkatli bir değerlendirmenin başlangıcıdır."),
            ("Önce zihinsel yaş",
             "Kısa bir zihinsel yaş kestirimini her nörogelişimsel değerlendirmenin ilk adımı yapmak, takvim yaşına göre yorumlanan "
             "otizm ya da DEHB bulgularından kaynaklanan hataları önleyebilir. Bu ilke tanı ölçütlerinin “gelişim düzeyine göre "
             "beklenenden fazla” koşuluyla da uyumludur."),
        ],
        sorular=[
            S("DEHB tanılı 12 yaşındaki bir çocukta “kolay sinirlenme” bulgusu, iki uçlu bozukluk olasılığını ne kadar artırır?",
              ["İki uçlu bozukluk tanısı için yeterlidir",
               "Pek çok durumda yaygın bir bulgu olduğundan nadir bir tanıyı tek başına belirgin biçimde olası kılmaz; epizodik seyir gibi daha özgül bulgular aranmalıdır",
               "DEHB tanısını dışlar",
               "Hiçbir bilgi taşımaz"],
              1, "Bir bulgunun değeri, rakip açıklamalara göre ne kadar özgül olduğuna bağlıdır. Yaygın bir belirti olasılıkları ancak "
                 "az değiştirir; nadir bir tanıyı destekleyen daha özgül veriler aranmalıdır."),
            S("Bir vaka sunumunda asistan, 13 yaşındaki bir ergende hem sosyal anksiyete hem otizm tanısını, her ikisi için de kanıt "
              "olarak “göz teması kurmaması”nı gösteriyor. Hangi akıl yürütme hatası söz konusudur?",
              ["Çift sayım: tek bir bulgu iki ayrı tanının kanıtı olarak kullanılmıştır",
               "Bayes kuralına uygun düşünme",
               "Zamansal sıranın ihlali",
               "Ortalamaya gerileme"],
              0, "Bir bulgu iki ayrı tanıyı aynı anda desteklemek için iki kez sayılamaz. İki tanı birlikte olabilir; ama her biri için "
                 "kendine özgü kanıt gerekir."),
            S("Bir asistan, yalnızca annenin anlatımına dayanarak 10 yaşındaki bir çocuğa DEHB tanısı koymak istiyor; okuldan bilgi "
              "yok ve çocuk seansta sakin. En yararlı süpervizyon sorusu hangisidir?",
              ["“Anne güvenilir biri mi?”",
               "“Kaç bağımsız bilgi kaynağın var ve birbirleriyle uyuşuyor mu?”",
               "“Stimülan dozu ne olacak?”",
               "“Ölçek puanı eşiği geçti mi?”"],
              1, "En sık hata tek bir kaynağa dayanmaktır. Okuldan bağımsız bilgi ve kaynakların uyuşması tanıya güveni artırır; "
                 "seans içi sakinlik tek başına DEHB’yi dışlamaz ama bağımsız kanıt ihtiyacını vurgular."),
        ],
        akilda="Ne zaman başladı, ne değiştiriyor, ailede ne var? Olasılıkları %100’e tamamlayın ve bağımsız kaynaklarınızı sayın.",
    ),
    # ------------------------------------------------------------------ 11
    dict(
        no=11, kesim="E", kisa="Formülasyon ve zaman seyri",
        baslik="Formülasyon üzerine düşünmek ve zaman seyri",
        kitapta_bolumler="E. Formulating · Thinking about the Formulation; Timecourses (s. 178–192)",
        slogan="Tedaviye yön verecek kadar kesin olun; ondan fazla değil.",
        kitapta=("İlk bölüm iyi bir formülasyonun niteliklerini, basit formülasyonları, dört P çerçevesinin inceliklerini, "
                 "kalıtılabilirliği, etkileşen süreçleri, grafiksel formülasyonu, metaforları ve birleştirme–bölme ikilemini ele alır. "
                 "İkinci bölüm zaman seyrinin tanıdaki değerini, değişime dayalı tanıyı, karşıtlığın haritasını, çoklu denge "
                 "düzeylerini, iki aşamalı formülasyonları, kısır ve erdemli döngüleri ve nedensellik diyagramlarını anlatır."),
        okurken=[
            "Bir formülasyon ne zaman “doğru ama yararsız”, ne zaman “yararlı ama insancıl değil” olur?",
            "Daha ayrıntılı bir formülasyon neden daha ikna edici ama daha az olası olabilir?",
            "Zaman seyri, kesitsel bir değerlendirmenin göremediği hangi bilgileri verir?",
        ],
        fikirler=[
            ("Doğru, yararlı, insancıl", "İyi bir formülasyon doğru ve yeterince kesindir; evde, okulda ve terapide işe yarar; aile için "
             "kabul edilebilir bir dille kurulur. Ayırıcı tanıyı zorunlu tutmak doğruluğun en güçlü güvencesidir; formülasyon normali de içermelidir."),
            ("Önce basit", "Aynı olguları daha az bileşenle açıklayan formülasyon tercih edilir; bir davranış daha basit bir süreçle "
             "açıklanabiliyorsa daha karmaşık bir süreç varsayılmamalıdır. Yine de biyoloji her zaman basit değildir: basitlik bir başlangıç noktasıdır."),
            ("Dört P’nin incelikleri", "Yatkınlaştırıcılar çoğu zaman değiştirilemez ve tek başına yetmez; tekrarlayan bir tetikleyici bir "
             "yatkınlığa işaret eder; sürdürücüler çoğu zaman küçük güçlükleri büyüten alevlendiricilerdir; koruyucular yalnızca kısmen "
             "koruyucu olsalar da güçlendirilmelidir."),
            ("Birleştirmek mi, bölmek mi?", "Daha ayrıntılı bir açıklama daha ikna edici görünür ama daha az olasıdır. Belirsiz ama doğru "
             "bir şemsiye tanı, kesin ama yanlış bir tanıdan iyidir; bazı dar tanılar ise çocuğun sorunlarının genişliğini hiçbir zaman kapsamaz."),
            ("Zaman seyri tanıdır", "Ne zaman başladığı, nerede ve ne zaman kötüleşip iyileştiği, tatillerde nasıl olduğu ve kendiliğinden "
             "düzelip düzelmediği nedenleri ayırt etmenin en güçlü verisidir. Uzun süreli özellikler, geçici durumların yokluğunda en "
             "güvenilir biçimde tanınır."),
            ("Döngüler ve süreçler", "Kaçınma, depresyon, anksiyete ya da okul başarısızlığı kısır döngüler hâlinde kendini sürdürür; "
             "döngünün herhangi bir noktasındaki müdahale etkili olabilir. Karmaşık sistemlerde bir yerdeki değişiklik başka yerlerde "
             "öngörülmesi güç telafi edici değişikliklere yol açar."),
        ],
        crs=[
            "Formülasyonu yazdıktan sonra üç soru sorun: Doğru mu? Ailenin, okulun ve terapistin işine yarar mı? Aile bu dille kendini suçlanmış hisseder mi?",
            "Tetikleyici tekrar ediyorsa “geçmişte kaldı” diye geçmeyin; tekrarlayan tetikleyici bir yatkınlığa işaret eder.",
            "Ergenlerde zaman seyrini görünür kılmak için haftanın günlerine ya da derslere göre basit 0–10 puanlamalar isteyin.",
            "Okul tatillerinde, akraba evinde ve hafta sonlarında belirtilerin nasıl değiştiğini mutlaka sorun; ortamlar arası fark nedenler hakkında bilgi verir.",
            "Karşıtlık şikâyetinde bir harita çıkarın: Hangi görevler, kişiler, saatler ve talimat biçimleri en çok karşı çıkmaya yol açıyor? Yoğunlaştığı yerde çoğu zaman tanınmamış bir öğrenme ya da dikkat güçlüğü vardır.",
            "Kısır döngüyü aileyle birlikte çizin; döngünün herhangi bir yerinden kırılabileceğini göstermek suçlamayı azaltır.",
            "Uzun süreli bir anksiyete tedavi edildiğinde beklenmedik bir disinhibisyon ortaya çıkabilir; aileyi önceden bilgilendirin.",
            "Donanım–yazılım metaforunu kullanırken “yazılım” sorununun daha az gerçek ya da iradeyle düzeltilebilir olduğu izlenimini vermemeye dikkat edin.",
        ],
        tartisma=[
            ("Birleşim yanılgısı",
             "Ayrıntı eklendikçe bir senaryo daha ikna edici ama olasılık açısından daha zayıf hâle gelir ([@tversky1983]). Vaka "
             "sunumlarında en ayrıntılı formülasyonun en olası formülasyon sanılması bu yanılgının klinik karşılığıdır."),
            ("Kalıtılabilirlik nedir, ne değildir?",
             "Yazarların bazı durumlarda genetik katkının küçük olduğu yorumu literatürle tam örtüşmez; elli yıllık ikiz çalışmalarının "
             "meta-analizi incelenen özelliklerin çoğunda orta düzeyde kalıtılabilirlik bildirir ([@polderman2015]). Kalıtılabilirlik "
             "bir popülasyon istatistiğidir; tek bir çocuğun sorununun ne kadarının genetik ya da değiştirilebilir olduğunu söylemez."),
            ("Otizm tek bir varlık mı?",
             "İkiz verileri otizmin belirti alanlarının kısmen ayrı kalıtıldığını düşündürür ([@ronald2006]); öte yandan otizm spektrum "
             "bozukluğunun bütün olarak yüksek kalıtılabilirliği de iyi belgelenmiştir ([@tick2016]). Yazarların tutumu bu tartışmanın bir ucunu temsil eder."),
            ("Bir metaforun sınırı",
             "Donanım–yazılım metaforu aileler tarafından iyi karşılanır; ancak psikolojik sorunları iradeye bağlayan ailelerde "
             "“yazılım” sorununun kolayca değiştirilebileceği düşüncesini güçlendirerek ters tepebilir."),
        ],
        sorular=[
            S("Okula başlamakta zorlanan 11 yaşındaki bir çocuk için önerilen aşağıdaki formülasyonlardan hangisinin doğru olma olasılığı en yüksektir?",
              ["Bir anksiyete bozukluğu",
               "Okul değişikliğiyle tetiklenen sosyal anksiyete bozukluğu",
               "Okul değişikliğiyle tetiklenen ve annenin aşırı korumasıyla sürdürülen sosyal anksiyete bozukluğu",
               "Okul değişikliğiyle tetiklenen, annenin aşırı korumasıyla sürdürülen ve zorbalıkla alevlenen sosyal anksiyete bozukluğu"],
              0, "Her ek ayrıntı formülasyonu daha ikna edici ama daha az olası kılar; en genel seçenek ötekilerin hepsini kapsar. "
                 "Ayrıntılar tedavi için yararlı olabilir, ama her biri ayrıca kanıt gerektirir."),
            S("Ödev saatlerinde ve özellikle yazma görevlerinde belirgin karşı gelme gösteren, ama futbol antrenmanında ve oyunlarda "
              "uyumlu olan 9 yaşındaki bir çocuk için en uygun sonraki adım hangisidir?",
              ["Karşıt olma karşı gelme bozukluğu tanısı koyup yalnızca ebeveyn eğitimine yönlendirmek",
               "Karşıtlığın yoğunlaştığı görevler üzerinden yazma ve öğrenme becerilerini değerlendirmek",
               "Çocuğu futboldan alıp ödeve daha çok zaman ayırmak",
               "Antipsikotik başlamak"],
              1, "Karşıtlığın haritası, sürekli başarısızlık ya da eleştiri yaşanan alanı gösterir. Yazma görevlerinde yoğunlaşan "
                 "karşı gelme, tanınmamış bir öğrenme ya da motor güçlüğün işareti olabilir."),
            S("Son üç yıldır her okul döneminin başında karın ağrısı ve okula gitmeme yaşayan 10 yaşındaki bir çocukta en doğru düşünce hangisidir?",
              ["Her dönem başı ayrı bir tetikleyici olduğundan kalıcı bir sorun yoktur",
               "Tekrarlayan tetikleyici altta yatan bir yatkınlığa (ör. ayrılık ya da sosyal kaygı, öğrenme güçlüğü) işaret eder; bu yatkınlık araştırılmalıdır",
               "Karın ağrısı organik bir hastalığın kanıtıdır",
               "Tek çözüm okul değiştirmektir"],
              1, "Tetikleyiciyi geçmişte kalmış bir olay saymak, tekrarlama örüntüsünün taşıdığı bilgiyi kaçırır. Fiziksel nedenler "
                 "uygun biçimde değerlendirilirken, dönem başlarına bağlı yatkınlık da araştırılmalıdır."),
        ],
        akilda="Doğru, yararlı, insancıl; tedaviye yetecek kadar kesin. Zaman seyrini sormadan nedenden söz etmeyin.",
    ),
    # ------------------------------------------------------------------ 12
    dict(
        no=12, kesim="E", kisa="Zor formülasyonlar",
        baslik="Zor formülasyonlar ve formülasyon araçları",
        kitapta_bolumler="E. Formulating · Difficult Formulations; Tools for Formulation (s. 193–207)",
        slogan="Bir vaka inanılmaz derecede karmaşık görünüyorsa, çoğu zaman kilit bir bilgi eksiktir.",
        kitapta=("İlk bölüm formülasyonun neden zorlaştığını, daha güvenilir formülasyonlar için sezgisel kuralları, hangi bilgiye "
                 "ağırlık verileceğini, takıldığınızda ne yapılacağını, onurlu bir yenilgiyi, ön ve yarı tanıları, dikkatsizler için "
                 "tuzakları ve betimleme düzeylerini ele alır. İkinci bölüm kendini yanlışlamayı, doğrulama yanlılığını gösteren "
                 "deneyleri, otomatik tanının sınırlarını, ölçek ve kontrol listelerini ve biyopsikososyal ile dört P çerçevelerini tartışır."),
        okurken=[
            "Bir vaka “inanılmaz derecede karmaşık” göründüğünde bu bize ne söyler?",
            "Hangi bilgiye daha çok, hangisine daha az ağırlık vermek gerekir?",
            "Kendi tanınızı doğrulamak yerine yanlışlamaya çalışmak pratikte nasıl görünür?",
        ],
        fikirler=[
            ("Karmaşıklık çoğu zaman eksik bilgidir", "Yönetilemez görünen bir vakada önceki yazışmalar, okul ve aile öyküsü, görüşmeye "
             "hiç gelmeyen bir aile üyesi, alkol, uyku ve fizik muayene yeniden gözden geçirilmelidir; tutarsızlık eksik bir parçaya işaret eder."),
            ("Veriyi budamak", "En çok dikkati hak eden bilgi önemli konularda, güvenilir ve öngörü değeri yüksek olandır: tanıdığınız "
             "kaynaklardan birinci elden bilgi, üzerinde uzlaşılan olgular, gözlenen davranış. İstatistiksel olarak anlamsız bilgi "
             "mantıken etkilememesi gerekse de sezgiyi saptırır."),
            ("Takıldığınızda", "Sesli düşünmek, sorunu ailenin önünde yapılandırmak, durumsallığı (zaman ve kaynaklar arasındaki değişkenlik) "
             "incelemek ve formülasyonu düzenli olarak gözden geçirmek yol açar. Kapsamlı bir formülasyon mümkün değilse onurlu bir "
             "yenilgi seçilir: ailenin en büyük endişesine odaklanmak, büyük ve küçük sorunları ayırmak."),
            ("Ön ve yarı tanılar", "Kademeli olarak güçlendirilebilen ön tanılar aileye öğrenme ve uyum için zaman tanır; ama gereksiz "
             "bekleme destek ve haklara erişimi geciktirerek bedel de doğurabilir."),
            ("Düşünmeyi durduran tuzaklar", "Haksız kesinlik, birlikte var olabilecek seçeneklere zorunlu seçim uygulamak, “A mı B mi?” "
             "diye tercih etmeye çalışmak (oysa ikisinden de biraz olabilir), ölçütlere aşırı katı bağlılık ve kurama uymayan olguları "
             "halının altına süpürmek düşünmeyi durdurur. Her disiplin kendi odak düzeyine alışmıştır; doğru ölçekten bakmak gerekir."),
            ("Kendinizi yanlışlayın", "Tanıyı doğrulamaya değil çürütmeye çalışmak kanıta daha çok yaklaştırır. Bir hipotezi sınamak için "
             "karşılaştırma grubuna da bakmak gerekir. Mekanik tahmin çoğu zaman klinik yargı kadar iyidir; ama çocuk psikiyatrisinde "
             "veri girişi, olasılıkların yokluğu ve yeni durumlar otomatik tanıyı zorlaştırır."),
        ],
        crs=[
            "Vaka “çok karmaşık” göründüğünde kontrol sorularını geçin: Önceki yazışmalar istendi mi? Okul ve aile bilgisi yeterli mi? Hiç görmediğimiz önemli bir aile üyesi var mı? Alkol, uyku ve aile işlevi soruldu mu? Fizik muayene yapıldı mı?",
            "Vaka tartışmalarında bilgileri üç süzgeçten geçirin: güvenilir mi, öngörü değeri yüksek mi, önemli bir konuyla mı ilgili?",
            "Tanı için çocuğun en iyi hâlini, risk için en kötü hâlini esas alın.",
            "Takıldığınızda düşüncenizi aileyle sesli yapılandırın: “Büyük meseleleri benim gördüğüm şekliyle sıralayayım; eksik ya da yanlış olanı siz düzeltin.”",
            "Formülasyonun ardındaki akıl yürütmeyi ve kanıtı kayda geçirin; bir sonraki görüşmede neyin değiştiğini ancak böyle fark edebilirsiniz.",
            "Vaka sunumlarında “A mı, B mi?” sorusunu “A’dan ve B’den ne kadar?” sorusuna dönüştürün.",
            "TR Ön tanılar aileye zaman tanır; ancak RAM yönlendirmesi ve ÇÖZGER gibi destekler kesinleşmiş bir değerlendirmeye bağlı olduğundan, beklemenin bedelini ve izlem planını açıkça konuşun.",
            "Çocuk ve ergen depresyonunu değerlendirirken anhedoniyi ve çökkün duygudurumun yerini alabilen irritabiliteyi mutlaka sorun; bu ölçütler kolayca atlanır.",
        ],
        tartisma=[
            ("Doğrulama yanlılığı",
             "Wason’un klasik deneyinde katılımcılar bir kuralı sınamak için çoğunlukla hipotezlerini doğrulayan örnekler seçmiştir "
             "([@wason1960]). Tanıyı doğrulayan bulgular aramak, onu çürütebilecek bir bulguyu aramaktan daha az bilgi verir."),
            ("Sözde tanısallık",
             "Tıp öğrencileriyle yapılan bir çalışmada katılımcıların %83’ü iki tanıyı ayırt etmek için gereken bilgiyi seçmemiş, "
             "yalnızca tek bir tanıyla ilgili veriyi aramıştır ([@kern1982]). Bir bulgunun tanısal değeri, rakip açıklamalar altındaki "
             "olasılıklarla karşılaştırıldığında ortaya çıkar."),
            ("Gözlenen mi, söylenen mi?",
             "Gözlenen davranışı söylenenden daha güvenilir sayan ilke dışa yönelim sorunlarında güçlüdür; ancak anksiyete ve depresyon "
             "gibi içe yönelim sorunlarında öz bildirim tanının merkezindedir. Ebeveyn, öğretmen ve çocuk bildirimleri arasındaki "
             "uyumsuzluk kuraldır ve kendisi bir bilgidir ([@achenbach1987]; [@delosreyes2005])."),
            ("Meehl ve yapay zekâ",
             "Mekanik tahmin çoğu görevde klinik yargıya eşit ya da üstündür ([@grove2000]). Kitap çocuk psikiyatrisinde otomatik "
             "tanının veri girişi, yayımlanmış olasılıkların yokluğu ve yeni durumlar nedeniyle zor olduğunu savunur. Serbest metni "
             "işleyebilen yeni araçlar veri girişini kolaylaştırsa da diğer iki engel büyük ölçüde sürmektedir."),
        ],
        sorular=[
            S("Bir ekip üyesi “Günde dört saatten fazla ekran kullanan ergenlerin hepsinde uyku sorunu görüyorum” diyor. Bu gözlemi "
              "değerlendirmek için en gerekli bilgi hangisidir?",
              ["Bu ergenlerdeki uyku sorununun şiddeti",
               "Ekran süresi düşük ergenlerde uyku sorununun ne sıklıkta görüldüğü",
               "Hangi uygulamaları kullandıkları",
               "Ekip üyesinin kaç yıllık deneyimi olduğu"],
              1, "Bir bulgunun değeri, karşılaştırma grubundaki sıklıkla birlikte anlaşılır. Uyku sorunu ekran süresi düşük ergenlerde de "
                 "sıksa gözlem ekran süresine özgü bir ilişki göstermez (sözde tanısallık)."),
            S("Görüşmeye hiç katılmamış bir üvey ebeveynin olduğu, okul raporlarının istenmediği ve uyku öyküsünün alınmadığı bir vaka "
              "ekipte “çok karmaşık” olarak tanımlanıyor. İlk adım hangisidir?",
              ["Daha kapsamlı bir kuramsal formülasyon geliştirmek",
               "Eksik bilgiyi tamamlamak: üvey ebeveyni davet etmek, okul raporlarını istemek, uyku ve alkol öyküsünü almak",
               "Vakayı hemen bir süper uzmana göndermek",
               "Yeni bir ilaç eklemek"],
              1, "Karmaşıklık çoğu zaman eksik bilginin işaretidir. Temel bilgiler tamamlanmadan formülasyonu karmaşıklaştırmak ya da "
                 "tedaviyi değiştirmek hatayı büyütür."),
            S("Bir vaka toplantısında “Bu çocukta DEHB mi var, yoksa travma mı?” diye tartışılıyor. En yararlı yeniden çerçeveleme hangisidir?",
              ["Hangisinin daha olası olduğuna karar verip ötekini dışlamak",
               "İki etkenin birlikte bulunabileceğini kabul edip her birinin katkısını ve tedavi sonuçlarını ayrı ayrı değerlendirmek",
               "Tanıyı ertelemek ve izlem planı yapmamak",
               "Ölçek puanı daha yüksek olanı seçmek"],
              1, "“Tercih etme” hatası, birlikte var olabilen durumları birbirinin alternatifi gibi ele alır. Her etkenin ne kadar katkı "
                 "verdiğini sormak tedaviyi daha doğru yönlendirir."),
        ],
        akilda="Karmaşıklık çoğu zaman eksik bilgidir; kendinizi doğrulamaya değil yanlışlamaya çalışın.",
    ),
    # ------------------------------------------------------------------ 13
    dict(
        no=13, kesim="E", kisa="Nadir sorunlar, tanıyı geri almak",
        baslik="Nadir sorunlar ve tanıyı geri almak",
        kitapta_bolumler="E. Formulating · Rare Problems; Undiagnosing (s. 208–217)",
        slogan="Kırmızı bayrak bir kesinlik değil, sınanacak bir hipotezdir: “Zebra!” değil, “Zebra?”",
        kitapta=("İlk bölüm nadir bir sorunun nasıl fark edileceğini, “at sesi duyunca zebra” ilkesinin Bayesçi okumasını, düşük "
                 "yaygınlıkta testlerin yorumunu, uzman ile asistanın nadir olaylara farklı ağırlık vermesini, nadirlik düzeylerine göre "
                 "hizmet örgütlenmesini ve tekrarlanan nadir olayların yorumunu ele alır. İkinci bölüm tanıyı geri almayı: alçakgönüllülüğü, "
                 "ikincil kazancı, insanları kırmadan başka bakış açıları göstermeyi, seansta iletişimi ve kendi ya da başkalarının "
                 "tanılarını düzeltmeyi tartışır."),
        okurken=[
            "Kırmızı bayrak bulunduğunda “Zebra!” ile “Zebra?” arasındaki fark nedir?",
            "Tekrarlanan nadir bir olay neden bağımsız olasılıkların çarpımıyla değerlendirilmemelidir?",
            "Bir tanıyı geri almak neden çoğu zaman tanı koymaktan daha zordur?",
        ],
        fikirler=[
            ("Önce at, sonra zebra sorusu", "Çocuklarda nadir davranışlar sıktır ve çoğu yaygın nedenlerden kaynaklanır. Önce yaygın "
             "açıklama düşünülür, ama geniş sorularla kırmızı bayraklar aranır. Tek tek nadir olan hastalıklar toplamda azımsanmayacak bir yük oluşturur."),
            ("Düşük yaygınlıkta test", "Nadir bir nedeni araştıran testte sınırda anormal sonuçlar çoğu zaman yanlış alarmdır. Testi daha "
             "yararlı kılmak için alt popülasyona uygun referans aralığı laboratuvarla konuşulabilir ve nadir nedeni destekleyen başka bulgular aranabilir."),
            ("Uzman ve asistan farkı", "Deneyime dayalı seçim nadir olayları küçümser; betimlemeye dayalı seçim ise özellikle akılda kalıcı "
             "etiketleri olan nadir olayları büyütür. Bir şeyi düşünürken o şey sandığımızdan önemli görünür; yaygın formülasyonların "
             "doğru olma olasılığı daha yüksektir."),
            ("Tekrarlanan nadir olay ortak bir neden arar", "İki nadir olayın bir arada görülmesi bağımsız olasılıkların çarpımıyla "
             "değerlendirilmemelidir; ortak bir neden ya da birbirini izleyen bir risk zinciri çok daha olası olabilir. Küçük bir olasılık "
             "her zaman rakip açıklamanın olasılığıyla karşılaştırılmalıdır."),
            ("Tanıyı geri almak bir beceridir", "Önceki klinisyen sizin bilmediğinizi biliyor olabilir; tanıların öznel yanı vardır ve "
             "hata bakımı etkilemiyorsa esnek olmak gerekir. Hatanın nedenini nazik ve kendine hizmet etmeyen bir dille açıklayamıyorsanız "
             "geri alma ikna edici olmaz."),
            ("İkincil kazanç ve zamanlama", "Tanı haklara ve kimliğe bağlandığında geri almak bir kayıp yaratır; bu kaybı adlandırmak "
             "gerekir. Kendi hatanızı düzeltmenin en iyi zamanı aileye söylenmeden, ikinci en iyi zamanı yazıya dökülmeden öncesidir."),
        ],
        crs=[
            "Kırmızı bayrak bulduğunuzda yalnızca nadir tanı doğruysa görülecek bir bulgu tanımlayın ve onu arayın.",
            "Nadir bir neden için test istemeden önce sınırda bir sonucun ne anlama geleceğini ve bir sonraki adımı planlayın.",
            "Sendromik özellikler, gelişimsel gerileme ya da ailede benzer tablolar varsa genetik değerlendirmeyi düşünün.",
            "TR Akraba evliliği olan ailelerde otozomal çekinik nadir hastalıkların ön olasılığı yükselir; bu bilgi genetik değerlendirme eşiğinizi düşürmelidir.",
            "Aynı çocukta tekrarlayan nadir bir olay (ör. ikinci psikotik epizod) gördüğünüzde olasılıkları çarpmak yerine ortak bir neden arayın.",
            "Tanıyı geri alırken önceki klinisyeni küçük düşürmeyin, aileyle aynı tarafta durun ve tanıyı birlikte yeniden düşünün: “Çocuklar değişir; erken konan tanılar daha az kesindir.”",
            "TR ÇÖZGER raporu ve RAM yönlendirmesi tanıya bağlı haklar doğurduğundan, bir tanıyı geri almadan önce bunun ailenin haklarına etkisini açıkça konuşun; kayıt sistemlerine işlenmiş tanıların kalıcılığını da hesaba katın.",
            "Kendi tanınızdan şüphelendiğinizde aileye söylemeden ve rapora yazmadan önce bir meslektaşla ya da süpervizörünüzle konuşun.",
            "Yeni bir işe başladığınızda tanı geri alma olasılığınız en yüksektir; selefinizin akıl yürütmesini anlamadan değişiklik yapmayın ve önce en çözülebilir sorunlara odaklanın.",
        ],
        tartisma=[
            ("Tanıların güvenilirliği",
             "DSM-5 saha çalışmalarında iki klinisyenin aynı hastayı ayrı ayrı görüşerek ulaştığı tanı uyumu tanıdan tanıya belirgin "
             "biçimde değişmiştir: değerlendirilen tanıların bir kısmı çok iyi ya da iyi, bir kısmı ise sorgulanabilir ya da kabul "
             "edilemez düzeyde kalmıştır ([@regier2013]). Bu veriler tanının öznelliğini aileye anlatırken somut bir dayanak sağlar."),
            ("Bağımsızlık varsayımı",
             "Bir ailedeki birden fazla ani bebek ölümünü bağımsız olaylar gibi çarpmak istatistiksel bir hatadır: ölümler ortak genetik "
             "ve çevresel etkenler nedeniyle ilişkili olabilir ve küçük olasılık rakip açıklamaların olasılığıyla karşılaştırılmalıdır ([@hill2004])."),
            ("Yeniden mağduriyet",
             "Meta-analiz verilerine göre çocuklukta cinsel istismara uğrayanların yaklaşık yarısı (%47,9) sonraki yaşamda yeniden "
             "cinsel mağduriyet yaşamaktadır ([@walker2019]). Tekrarlanan olayları “bağımsız şanssızlıklar” gibi değerlendirmek "
             "yanıltıcıdır; ortak etken çoğu zaman ilk travmanın kendisi ve sonuçlarıdır."),
            ("Nadir hastalıkların toplam yükü",
             "Orphanet verileriyle yapılan bir analiz nadir hastalıkların toplam nokta yaygınlığını nüfusun %3,5–5,9’u olarak "
             "kestirmiştir ([@nguengangwakap2020]). Kitabın psikiyatriye sevk edilen çocuklarda bu oranın daha yüksek olduğu tahmini "
             "mantıklıdır, ama doğrudan bir veriye dayanmaz."),
        ],
        sorular=[
            S("Hiperaktivite nedeniyle değerlendirilen 7 yaşındaki bir çocukta, nadir bir metabolik nedeni araştıran testte sınırda düşük "
              "bir değer saptanıyor; destekleyen başka bir klinik bulgu yok. En uygun yorum hangisidir?",
              ["Hiperaktivitenin nedeni bulunmuştur; buna yönelik tedaviye başlanmalıdır",
               "Düşük ön olasılıkta sınırda değerler çoğu zaman yanlış alarmdır; referans aralığı sorgulanmalı, test gerekirse tekrarlanmalı ve destekleyici bulgular aranmalıdır",
               "Test tamamen anlamsızdır; hiç dikkate alınmamalıdır",
               "Aileye kesin bir metabolik hastalık olduğu söylenmelidir"],
              1, "Nadir bir nedenin ön olasılığı düşük, sınırda değerlerin sıklığı ise yüksektir; bu nedenle pozitif sonuçların çoğu "
                 "yanlış pozitiftir. Destekleyici bulgular ve uygun referans aralığı testi anlamlı kılar."),
            S("Başka bir merkezde 3 yaşında otizm tanısı almış, şimdi 8 yaşında olan ve değerlendirmenizde otizm ölçütlerini karşılamayan "
              "bir çocuğun ailesine en uygun yaklaşım hangisidir?",
              ["Önceki tanının yanlış olduğunu ve önceki hekimin hata yaptığını açıkça söylemek",
               "Erken çocukluk tanılarının daha az kesin olduğunu, çocukların geliştiğini ve bazı çocuklarda belirtilerin belirgin biçimde azalabildiğini anlatmak; tanının haklara etkisini de birlikte konuşmak",
               "Hiçbir şey söylemeden önceki tanıyı rapora aynen yazmak",
               "Tanıyı geri almak için mutlaka pahalı bir test gerektiğini söylemek"],
              1, "Tanıyı geri alırken önceki klinisyeni suçlamak ikna etmez ve aileyi savunmaya iter. Gelişimsel değişimi ve tanıların "
                 "öznelliğini anlatmak, haklara etkisini konuşmakla birlikte, aileyle aynı tarafta kalmayı sağlar."),
            S("Bir ergen 18 ay içinde, birbirinden bağımsız görünen iki ayrı psikotik epizod geçiriyor. En doğru akıl yürütme hangisidir?",
              ["İki nadir olayın birlikte görülme olasılığı çok düşük olduğundan ikinci epizod muhtemelen yanlış tanıdır",
               "Tekrarlanan nadir bir olay ortak bir neden arar: madde kullanımı, iki uçlu bozukluk, nöbet bozukluğu ya da başka bir altta yatan durum araştırılmalıdır",
               "Her epizod ayrı ele alınmalı, aralarında bağlantı aranmamalıdır",
               "Epizodlar rastlantıdır; izlem gerekmez"],
              1, "Nadir olayların tekrarı bağımsız şans olaylarının çarpımıyla değil, ortak bir nedenle açıklanmaya daha yatkındır. "
                 "Bu, altta yatan bir durumun araştırılmasını gerektirir."),
        ],
        akilda="Önce at; ama kırmızı bayrakta “Zebra?” diye sorun. Tanıyı geri alırken haklı olmak değil, ikna edici olmak gerekir.",
    ),
    # ------------------------------------------------------------------ 14
    dict(
        no=14, kesim="R", kisa="Rakipleriniz",
        baslik="Rakipleriniz: meslektaşlar arasındaki görünmeyen rekabet",
        kitapta_bolumler="R. Dysfunction · Your Competitors (s. 702–708)",
        slogan="Meslektaş aynı zamanda rakiptir; bunu kabul etmek kinizm değil, gerçekçiliktir.",
        kitapta=("Bölüm meslektaş ilişkilerinin az konuşulan yanını, rekabeti ele alır: neyin rekabet konusu olduğunu, uzmanların yine de "
                 "nasıl iyi geçindiğini, adil ve adil olmayan rekabet yollarını, yönetimin yarattığı rekabeti, iş paylaşımını, zor ve "
                 "endişe verici meslektaşlarla çalışmayı, tırmandırma eşiğini, hekim kalitesini ölçmenin güçlüğünü ve rakiplerle iş birliğini tartışır."),
        okurken=[
            "“Meslektaş” ile “rakip” arasındaki gerilim ekip kararlarını nasıl etkiler?",
            "Bir meslektaşın hatalarında ne zaman özel bir konuşma, ne zaman bildirim gerekir?",
            "Hekim kalitesini ölçmeye çalışan sistemler hangi istenmeyen davranışları doğurabilir?",
        ],
        fikirler=[
            ("Rekabet sınırlarda yaşanır", "Kadrolar, odalar, asistanlar, itibar, hasta sayısı ve ödüller rekabet konusudur; rekabet ekiplerin "
             "içinden çok sınırlarında, özellikle tartışmalı sınırlarda yaşanır."),
            ("Barış nasıl korunur?", "Uzmanlar birbirini az görür, benzer geçmişlere sahiptir ve en önemlisi aynı kırılganlıkları paylaşır. "
             "Kıdem farkı belirgin ya da karşılıklı saygı yüksek olduğunda akran gözlemi iyi işler."),
            ("Adil rekabet", "Müttefik edinmek, bilgi biriktirmek, aynı alanda kararlılıkla kalmak ya da olağandışı bir hedef seçmek önerilen "
             "yollardır. İyi niyet ve çok çalışma tek başına rekabet aracı değildir; sınırlarla dengelenmezse insanı tüketir. Böbürlenmek "
             "ve “kalite” söylemini statü aracına çevirmek ters teper."),
            ("Karar toplantıdan önce verilir", "Çok disiplinli toplantılarda kararlar çoğu zaman önceden yapılan hazırlık ve ilişkilerle "
             "şekillenir. Odadaki en ağır ses, aileyi gerçekten görmüş olanınki olmalıdır."),
            ("Endişe verici meslektaş", "İlk soru hasta güvenliğidir: meslektaş hasta mı, uygunsuz mu, yetersiz mi? Hafif durumlarda özel ve "
             "nazik bir konuşma, tekrarlayan bir örüntüde tırmandırma gerekir. Hataların sayısı ve ortak teması, eksik bilgiyi yetersiz öğrenmeden ayırt etmeye yardım eder."),
            ("Kaliteyi ölçmek zordur", "Hekim kalitesini bireysel olarak yargılamak yanıltıcıdır; ölçütleri siz seçerseniz hep siz "
             "kazanırsınız. Bireysel karneler oyuna getirmeye yol açabilir; ekip verileri ve anonim rastgele denetimler daha güvenlidir. "
             "Rakiplerle iş birliği sıfır toplamlı bir oyun değildir."),
        ],
        crs=[
            "Çok disiplinli bir toplantıda tartışmalı bir karar bekleniyorsa aileyi gerçekten görmüş olan meslektaşlarla önceden konuşun ve gözlemlerinizi yazılı hazırlayın.",
            "TR Kamu hastanelerindeki performansa dayalı ek ödeme sistemi nicelik odaklı bir rekabet yaratabilir; uzun ilk görüşme gerektiren vakaların yükünü ekip içinde açık ve adil biçimde paylaşın.",
            "TR Akademik yükseltme ölçütleri yayın sayısını öne çıkardığında rekabet akademiye de taşınır; ortak projeler ve paylaşılan veri tabanları bu rekabeti iş birliğine dönüştürebilir.",
            "Bir meslektaşın tekrarlayan hatalarını fark ettiğinizde önce özel ve nazik bir konuşma yapın; hasta güvenliği risk altındaysa beklemeden kurumsal yollarla bildirin.",
            "Ekip istatistiklerini yöneticiler istemeden önce kendiniz derleyin ve meslektaşlarınızla paylaşın; neye göre değerlendirildiğinizi bilmek rekabeti şeffaflaştırır.",
            "Klinisyenlerin atlamaya eğilimli olduğu işleri (sosyal ve aile öyküsü gibi) iş bölümünde görünür kılın; görünmeyen eksik iş başkasının yüküne dönüşür.",
            "Sizi düşünmeye zorlayan meslektaşlarla düzenli tartışın; fikir ayrılığı bir tehdit değil, gelişme aracıdır.",
        ],
        tartisma=[
            ("Halka açık sonuç raporlaması",
             "ABD’de girişimsel kardiyolojide halka açık raporlamanın en ağır hastalarda riskten kaçınmaya yol açabileceği tartışılmıştır "
             "([@resnic2009]). Londra’da operatör düzeyinde raporlamaya geçiş ise riskten kaçınma kanıtı olmadan mortalitede düşüşle "
             "ilişkili bulunmuştur ([@jones2019]). Kitabın “karneler performansı bozar” mesajı bir olasılıktır, bir yasa değil; "
             "belirleyici olan ölçüm sisteminin tasarımıdır."),
            ("Türkiye’de rekabetin mimarisi",
             "Kitaptaki rekabet büyük ölçüde İngiltere’deki sevk ve hasta sayısı düzenine dayanır. Türkiye’de performansa dayalı ek "
             "ödeme ve akademik yükseltme ölçütleri rekabeti farklı biçimde yapılandırır; kitabın önerileri bu bağlamda yeniden düşünülmelidir."),
            ("Adil olmayan yöntemleri saymak",
             "Yazarlar seçici istatistik ya da işi ölçüte göre ayarlamak gibi yöntemleri açıkça sıralar. Bunun bir öneri mi, yoksa "
             "tanınmaları için bir uyarı mı olduğu metinde belirsiz kalır; kitabın stratejik iletişim etiğine ilişkin gerilimlerinden biridir."),
            ("Çocuğun sesi nerede?",
             "Kararın toplantı öncesi hazırlık ve ilişkilerle şekillendiğini kabul etmek dürüsttür; aileyi görenlerin görüşüne ağırlık "
             "vermek de güven vericidir. Ancak bu süreçte çocuğun kendi görüşünün nasıl temsil edileceği ayrıca sorulmalıdır."),
        ],
        sorular=[
            S("Bir meslektaşınızın son aylarda üç kez aynı türde reçete hatası yaptığını fark ediyorsunuz; hastalardan biri hafif bir yan "
              "etki yaşamış. İlk adım hangisidir?",
              ["Herkes hata yaptığı için hiçbir şey yapmamak",
               "Durumu koridorda diğer meslektaşlarla konuşmak",
               "Meslektaşla özel ve nazik bir görüşme yapıp ortak temayı (ör. bir bilgi eksikliği) birlikte belirlemek; risk sürüyorsa kurumsal yollarla bildirmek",
               "Durumu kurum dışında kamuoyuyla paylaşmak"],
              2, "Önce hasta güvenliği ve meslektaşa saygı birlikte gözetilir. Ortak bir tema, giderilebilir bir bilgi eksikliğine işaret "
                 "edebilir; örüntü sürüyorsa tırmandırmak gerekir."),
            S("Bir yönetici bireysel hekim “başarı karnesi” uygulaması önerir. Bunun en olası istenmeyen sonucu hangisidir?",
              ["Hekimlerin karmaşık ve ağır vakaları üstlenmekten kaçınması",
               "Hasta memnuniyetinin kesin olarak artması",
               "Ekip içi iş birliğinin kendiliğinden güçlenmesi",
               "Hiçbir davranış değişikliği olmaması"],
              0, "Ölçüm davranışı değiştirir. Risk ayarlaması yetersiz bireysel karneler, sonucu kötü olabilecek vakalardan kaçınmayı "
                 "ödüllendirebilir; ekip verileri ve anonim denetim daha güvenlidir."),
            S("Çok disiplinli bir çocuk koruma toplantısında iki kıdemli uzman güçlü ve zıt görüşler savunuyor. Kararın sağlıklı olması "
              "için en önemli etken hangisidir?",
              ["En kıdemli kişinin görüşü",
               "Aileyi ve çocuğu doğrudan görmüş olan profesyonellerin gözlemlerine ağırlık verilmesi ve kanıtların açıkça tartışılması",
               "Toplantıda en çok konuşan kişinin görüşü",
               "Önceki toplantılarda verilen kararlar"],
              1, "Kıdem ya da ses yüksekliği kanıtın yerini tutmaz. Doğrudan gözleme dayanan bilgi ve açık tartışma, toplantı öncesi "
                 "ilişkilerin kararı belirleme riskini azaltır."),
        ],
        akilda="Meslektaş aynı zamanda rakiptir; en iyi rekabet aracı müttefik edinmektir ve odadaki en ağır ses aileyi gerçekten görmüş olanınki olmalıdır.",
    ),
]

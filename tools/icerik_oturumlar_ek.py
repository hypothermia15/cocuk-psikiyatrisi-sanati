# -*- coding: utf-8 -*-
"""Çocuk Psikiyatrisinin Sanatı · Okuma Rehberi: Kasım 2026'da eklenen oturumlar (E kesiminin son bölümü, F ve G kesimleri).

Yapı icerik_oturumlar.py ile aynıdır. Kitaptan alıntı ya da kitabın vakaları yoktur; fikirler kendi sözcüklerimizle yazılmıştır,
vaka soruları kurgusaldır. Bu dosyadaki oturumlar OTURUMLAR listesinin sonuna eklenir; var olan oturumlara soru eklenmez.
"""


def S(soru, secenekler, dogru, aciklama):
    return dict(soru=soru, secenekler=secenekler, dogru=dogru, aciklama=aciklama)


OTURUMLAR_EK = [
    # ------------------------------------------------------------------ 15
    dict(
        no=15, kesim="E", kisa="Tanısız psikiyatri",
        baslik="Tanısız psikiyatri: tanı ne zaman yardım eder, ne zaman engel olur?",
        kitapta_bolumler="E. Formulating · Psychiatry without Diagnoses (s. 218–226)",
        slogan="Tanı bir anahtardır: koymadan önce kaç kapıyı açacağını sorun.",
        kitapta=("Bölüm, tanı koymadan çocuk psikiyatrisi yapmanın ne zaman mümkün ve yararlı olduğunu sorar. Tanının aileye ve hekime "
                 "sağladığı yararları (bilme hakkı, anlam, hizmetlere erişim, suçlamanın kalkması, sorunun dışsallaştırılması) ve yol "
                 "açabildiği sorunları (dikkati çocuğun kendine özgü durumundan uzaklaştırması, zayıf öngörü gücü, zamanla genişleyen "
                 "tanılar, damgalanma) tartışır. Tanının maliyetini kararın büyüklüğüyle tartmayı, çok sayıda tanının karıştırdığı "
                 "aileleri, tanı dışı düşünme yollarını, stratejik olarak tanı koymamayı ve belirsizliği aileye ve ekibe nasıl ifade "
                 "edeceğimizi ele alır."),
        okurken=[
            "Bu çocuğa tanı koyduğunuzda tanının yararlarından kaçını gerçekten kullanacak? Tek bir yarar için bütün tanı sürecine gerek var mı?",
            "Bir tanı yönetimi değiştirmiyorsa, onu kesinleştirmek için harcanan zaman ve emek neye mal oluyor?",
            "Emin olmadığınızda bunu aileye ve okula nasıl söylersiniz, nasıl söylemezsiniz?",
        ],
        fikirler=[
            ("Yanıltıcı kesinlik",
             "Tanılar sanıldığı kadar keskin değildir; yönetilen bir belirsizliği bazen sahte bir kesinliğe çevirir. Nedeni bilinen "
             "fiziksel tanılarla yüzeydeki davranış örüntülerini tanımlayan sendromlar aynı sözcükle anılsa da farklı türden bilgilerdir. "
             "Tanısız düşünmeyi denemek zor vakada yaratıcılığı artırır ve tanıları daha iyi kullanmayı öğretir."),
            ("Tanının yararları",
             "Aile için bilme hakkı, belirsizliğin bitmesiyle gelen rahatlama, hayal edilen çocuğun yasını tutabilmek, genetik "
             "danışmanlık, destek ağları ve erken müdahale; hekim için düşünceyi düzenlemek ve bazen gidişi öngörmek. Tanı eğitim ve "
             "sosyal desteğe giriş bileti olabilir, suçlamayı kaldırır ve sorunu çocuğun dışına koyar: “Bu OKB; sen ona karşı "
             "mücadele ediyorsun.”"),
            ("Kaç yarara ihtiyaç var?",
             "Çocuğun bu yararlardan birkaçına ihtiyacı varsa resmî tanı muhtemelen gereklidir. Yalnızca bir ya da ikisine ihtiyaç "
             "varsa o hizmete doğrudan ulaşmanın yolları aranabilir: gereksinime göre çalışmak. Tanının sorunu bir olaya bağlaması da "
             "yön gösterir: aynı tablo depresyon diye çerçevelenince ilaç ve terapi protokolüne, uyum sorunu diye çerçevelenince "
             "sorunun kendisine yönelinir."),
            ("Tanının bedeli",
             "Tanı dikkati çocuğun gözle görülen sorunlarından ve kendine özgü durumundan uzaklaştırabilir, büyük gruplarda işe yarayan "
             "tedavilere çeker. Psikiyatrik tanıların çoğu tedavi yanıtını zayıf öngörür. Öznel tanılar zamanla daha çok kişiye konur; "
             "bu yüzden bir tanının ne zaman ve nerede konduğunu bilmek gerekir. Ciddi ve kalıcı sayılan tanılar suçlamayı azaltırken "
             "damgalanmayı artırabilir."),
            ("Kararın büyüklüğü",
             "Bilgi toplamak kesinliği sıfırdan yüze çıkarmaz, olsa olsa birkaç basamak artırır. Zararsız genel müdahaleler için tanı "
             "beklemeye gerek yoktur. Nedeni ve tedavisi aynı olan iki tanıyı ayırmak az kazandırır. Ağır zihinsel yetersizlikte ya da "
             "çok sayıda eş tanıda ek bir etiket çoğu zaman yeni bir yardım getirmez; baskın ya da en tedavi edilebilir soruna yönelik "
             "bir deneme daha bilgilendirici olabilir."),
            ("Tanı dışında düşünmek",
             "Nedenleri bulmak, tanı sistemlerinde yer almayan basit fikirler, zararsız müdahaleler, istenen sonuçla eldeki "
             "müdahaleleri eşleştirmek ve şimdiki durumdan istenen duruma doğru yön tutmak, düşünceyi tanı olmadan da düzenler. "
             "Özellikler derecelidir: yatkınlık çok sayıda küçük etkenin toplamıdır. Bazen en doğru hamle stratejik olarak tanı "
             "koymamak ve ortamı değiştirmektir."),
            ("Belirsizliği söylemek",
             "Bilmediğini söylemek ayıp değildir; mesele bunu nasıl ifade edip sonra ne yapacağınızdır. Tanının belirsiz olduğunu "
             "okulun ya da sosyal hizmetin zihnine yerleştirmek gereksiz ikinci görüş ya da yatış baskısı doğurabilir. Yönetim tanının "
             "adına değil, çocuğun davranış sorunlarına ve gelişimsel gereksinimlerine dayanır. Kısmi ya da geçici bir tanı aileye "
             "zaman tanır ve verileri düzenli toplamayı sağlar."),
        ],
        crs=[
            "Tanı görüşmesinden önce bu çocuğun tanıdan hangi somut yararları göreceğini yazın: eğitim desteği, ilaç, rapor, destek ağı, suçluluğun azalması.",
            "Aile tanılara inanmıyorsa açıklamayı tanısız kurun: davranış, tetikleyiciler, sürdürücü etkenler ve yapılacaklar.",
            "Çok sayıda tanı almış çocukta aileye ve okula tanıları birleştiren tek bir sade açıklama ve iki üç öncelikli hedef verin.",
            "İlaca yanıtı tanının kanıtı gibi sunmayın; denemeyi önceden tanımlanmış hedeflerle ve mümkünse öğretmen bilgisiyle değerlendirin.",
            "Belirsiz durumlarda geçici bir çalışma tanısı ve tarihi belli bir yeniden değerlendirme planı yazın.",
            "Belirsizliği üç düzeyde ifade etmeyi deneyin: güvenle (“Temel özelliklerin hepsi var”), kısmen emin (“Bütün tabloya bakınca "
            "bu tanıyı hak ettiğini düşünüyorum”) ve belirsiz (“Bazı özellikleri var, izleyeceğiz”). Hangisini seçeceğiniz plana bağlıdır.",
            "Ağır zihinsel yetersizliği olan ve zaten özel eğitim alan bir çocukta ek tanı için uzun bir değerlendirme planlamadan önce, ek "
            "tanının hangi kapıyı açacağını aileyle konuşun.",
            "TR Türkiye’de ÇÖZGER ve RAM süreçleri tanı koduna dayandığı için tanının giriş bileti işlevi daha belirgindir. Yalnızca "
            "hizmete erişim için “kolaylaştırıcı” bir tanı yazmak, çocuğun kaydında sonradan düzeltilmesi zor bir etiket bırakır.",
            "TR e-Nabız’da muayene tanıları aile tarafından görülebilir. Geçici düşündüğünüz bir tanıyı kodlamadan önce aileye anlatın ve "
            "kayda gerekçenizi yazın.",
        ],
        tartisma=[
            ("Yaygınlık artışının ne kadarı tanı değişikliği?",
             "Danimarka’da 1980-1991 doğumlu çocuklarda bildirilen otizm yaygınlığındaki artışın yaklaşık %60’ı, tanı ölçütlerindeki "
             "değişiklik ve ayaktan başvuruların kayda girmesiyle açıklanmıştır ([@hansen2015]). Bulgu, bir tanının ne zaman ve nerede "
             "konduğunu bilmek gerektiği uyarısını destekler; ancak artışın tamamını açıklamaz."),
            ("Biyolojik açıklamanın iki yüzü",
             "28 deneysel çalışmanın meta-analizinde biyogenetik açıklamalar suçlamayı azaltmış, ancak gidişe ilişkin karamsarlığı ve "
             "tehlikelilik kalıp yargısını artırmıştır ([@kvaale2013]). Kitabın, ciddi ve kalıcı sayılan tanıların suçlamayı azaltıp "
             "damgalanmayı artırabileceği uyarısı bu bulgularla uyumludur."),
            ("İlaca yanıt tanı değildir",
             "Tek doz uyarıcı, DEHB tanısı olmayan çocuklarda da motor etkinliği azaltmış ve bilişsel test performansını artırmıştır "
             "([@rapoport1978]). Bu yüzden ilaca yanıt tanının değil, ilacın o çocukta işe yarayıp yaramadığının kanıtıdır; tek hasta "
             "denemeleri bunu sistemli biçimde sınamanın bir yoludur ([@nikles2006])."),
            ("Tanısız çalışmanın alanı",
             "Kitap tanısız çalışmayı savunurken bile tanının araştırma ve hizmet planlaması için vazgeçilmez olduğunu kabul eder. "
             "Boyutsal yaklaşımlar (Oturum 10) bu gerilime başka bir yanıt arar. Türkiye’de raporlama, ilaç geri ödemesi ve özel "
             "eğitim tanı koduna bağlı olduğu için tanısız çalışmanın alanı İngiltere’dekinden daha dardır."),
        ],
        sorular=[
            S("Ağır zihinsel yetersizliği olan ve zaten özel eğitim kurumunda desteklenen 13 yaşındaki bir çocuk için aile, okulun önerisiyle "
              "“otizm de var mı?” diye kapsamlı bir değerlendirme istiyor. Ek tanının yeni bir hizmet getirmeyeceği biliniyor. En uygun "
              "yaklaşım hangisidir?",
              ["Saatler süren standart otizm değerlendirmesini hemen planlamak",
               "Ek tanının neyi değiştireceğini aileyle konuşmak, değerlendirmeyi kısa tutmak ve asıl sorunlara yönelik müdahaleleri öne almak",
               "Aileye sorunun anlamsız olduğunu söyleyip görüşmeyi kapatmak",
               "Kesin sonuç için çocuğu birkaç haftalığına yatırmak"],
              1, "Ağır zihinsel yetersizlikte ek davranışsal tanılar daha zor konur, daha az kesindir ve bu grupta daha az araştırılmıştır. "
                 "Ek tanının açacağı bir kapı yoksa değerlendirmeyi kısaltıp işlevsel hedeflere yönelmek daha yararlıdır; ailenin sorusu "
                 "yine de ciddiye alınır."),
            S("Okul, 9 yaşındaki bir öğrenci için “Tanı kesin değil mi?” diye soruyor. Tablonun eşikte olduğunu düşünüyorsunuz ama yönetim "
              "planınız net. Okula en uygun yanıt hangisidir?",
              ["“Tanı belirsiz, başka bir uzmana da gösterin.”",
               "“Tanıdan bağımsız olarak çocuğun gereksinimleri şunlar ve sınıf içi plan bu; üç ay sonra birlikte gözden geçireceğiz.”",
               "“Kesinlikle otizm.”",
               "Okulla hiç konuşmamak"],
              1, "Yönetim tanının adından çok çocuğun davranış sorunlarına ve gereksinimlerine dayanır. Belirsizliği gereksiz yere "
                 "vurgulamak ikinci görüş ve yatış baskısını artırabilir; yanlış bir kesinlik ise ileride güveni sarsar."),
            S("Bir çocuğun dosyasında DEHB, özgül öğrenme güçlüğü, duyusal işleme sorunu, kaygı bozukluğu ve tik bozukluğu tanıları var. "
              "Aile ve öğretmenler hangi sorunun neye ait olduğunu anlayamadıklarını söylüyor. İlk adım hangisidir?",
              ["Her tanı için ayrı bir uzmana yönlendirmek",
               "Tanıları birleştiren sade bir açıklama yapmak ve aileyle iki üç öncelikli işlevsel hedef belirlemek",
               "Yeni bir tanı aramak için ek testler istemek",
               "Bütün tanıları kayıttan silmek"],
              1, "Betimleyici tanı sistemi yapay eş tanılar üretebilir. Birden çok etiket aileyi ve okulu karıştırıyorsa ortak bir "
                 "açıklama ve öncelikli hedefler daha işlevseldir; tanılar başka amaçlar için korunabilir."),
        ],
        akilda="Tanı bir anahtardır: kaç kapıyı açacağını sorun. Emin değilseniz belirsizliği değil, planınızı öne çıkarın.",
    ),
    # ------------------------------------------------------------------ 16
    dict(
        no=16, kesim="F", kisa="Formülasyonu sunmak",
        baslik="Formülasyonu sunmak: ailenin düşüncesini bir adım ileri taşımak",
        kitapta_bolumler="F. Explaining · Presenting the Formulation (s. 227–234)",
        slogan="Formülasyonu sunmazsınız; ailenin düşüncesini bulunduğu yerden alıp ileri taşırsınız.",
        kitapta=("Bölüm formülasyonu aileye açıklamayı bir sunum olarak değil, ailenin düşüncesini dönüştürme işi olarak ele alır: "
                 "zamanlama ve güven, ailenin önceki kuramını ve beklentilerini öğrenmek, ağır tanılara dereceli bir dille yaklaşmak, "
                 "duyguyu gözetmek, açık ve somut konuşmak, gen-çevre etkileşimini suçlamadan anlatmak, temel mesajlar, hatırlamayı "
                 "kolaylaştırmak, gelecek için gerçekçi bir umut, kesinliğin dili, anlaşılıp anlaşılmadığını sınamak ve açıklayıcı "
                 "metaforlar."),
        okurken=[
            "Aile sizin formülasyonunuzu duymadan önce ne düşünüyordu ve söyleyeceğiniz bunun neresine oturuyor?",
            "Söylediklerinizden ailenin evde hatırlaması gereken üç şey hangileri?",
            "Kötü bir haberi verirken umudu nereden kuracaksınız?",
        ],
        fikirler=[
            ("Önce güven, sonra açıklama",
             "Aile hikâyesinin tamamının dinlendiğini ve acısının duyulduğunu hissetmeden yapılan açıklama inandırıcı olmaz. Görüşmeye "
             "gelmeyen ya da sonradan katılan aile üyeleri planlara daha az güvenir. İyi sunulan bir formülasyon uyumsuz fikirleri "
             "değiştiren bir müdahaledir; yalnızca bir tanı adı söylemek ise ailenin inançlarıyla ve tedaviyle kurulacak bağı koparır."),
            ("Ailenin kuramından başlamak",
             "Sonuçları anlatmadan önce ailenin fikirlerini, kaygılarını ve beklentilerini öğrenmek gerekir; sorulan soru çoğu zaman "
             "asıl kaygı değildir. Ciddi bir tanıyı söylemeden önce ailenin o konuda ne düşündüğünü bilmek gerekir: örneğin zihinsel "
             "yetersizlikte çocuğu kaç yaşında gördüklerini, gerekirse dil, sosyal beceri ve davranış alanlarına bölerek sormak."),
            ("Dereceli dil ve kabul edilebilirlik",
             "Şok içindeki insan düşünemez; hedef terime adım adım yaklaşılır. Ailelerin tanıları kabul etme sırası vardır: damgası "
             "az, gidişi iyi, biyolojik görünen, nadir ve sorumluluk yüklemeyen tanılar daha kolay kabul edilir. Bu sırada yukarı "
             "çıkmak kolaydır, aşağı inmek zaman ve şefkat ister. Ebeveynle ilgili sorunlar çoğu zaman yeniden çerçevelemeyle "
             "kabul edilir."),
            ("Açık, somut, az",
             "Jargondan kaçının, en önemli şeyi önce söyleyin, hatırlanması gereken bilgiyi üçle sınırlayın ve tekrarlayın. Göstermek "
             "anlatmaktan güçlüdür: çocuğun odada yaptığı bir şeyi işaret ederek açıklamak. Ailenin yanıt araması gereken sorular: "
             "Tanı neyi açıklıyor, neden şimdi, ne kadar sürecek, etkileri ne olacak, ne yapılabilir? Örtmeceli dil sorunu ciddiye "
             "almadığınız izlenimi verir."),
            ("Gelecek ve umut",
             "Gelecek bugünü biçimlendiren bir fikirdir. Altın kural: umudu asla elinden almayın. İşler düzelmeyecekse kolaylaşacağını, "
             "kriz anında ortalamaya dönüşün düzelme getirebileceğini anlatın. Aileyi güvenilmez büyük umutlardan güvenilir küçük "
             "umutlara taşıyın ve süren desteği somutlaştırın."),
            ("Kesinlik, anlama ve metafor",
             "“Eminim” çoğu zaman yeterlidir; abartılı kesinlik inandırıcı değildir. Zor değerlendirmelerde formülasyonu kesinlik "
             "sırasına göre sunmak dürüsttür. “Tamam mı?” anlaşıldığını göstermez; aileden eşine ya da çocuğuna ne anlatacağını "
             "söylemesini istemek daha iyidir. İyi metafor canlı, tanıdık, basit ve açıkça ilgilidir; zorlama metaforlar küçümseyici "
             "gelebilir."),
        ],
        crs=[
            "Açıklamaya geçmeden önce fikirleri, kaygıları ve beklentileri sorun: “Sizce neden oluyor? En çok neyden korkuyorsunuz? Bugün "
            "buradan ne bekliyorsunuz?” Bu üçlü Calgary-Cambridge görüşme modelinin de parçasıdır ([@kurtz1996]).",
            "Zihinsel yetersizlik gibi zor bir tanıyı söylemeden önce ailenin çocuğu kaç yaşında gördüğünü alan alan sorun ve onların "
            "gözleminden yola çıkın.",
            "Ebeveynlik sorunlarını suçlamayan bir dille çerçeveleyin: herkesin bir “alet çantası” vardır ve bazı durumlar için yeni bir "
            "alet edinmek gerekir.",
            "Görüşmede mümkünse iki yetişkin bulunsun, çocuk dikkatlerini dağıtmasın; söylediklerinizi konuşurken kısa bir yazılı özete dökün.",
            "Gen-çevre etkileşimini anlatmadan önce bunun yardım edip etmeyeceğini düşünün; depresif ya da önceki hekimlerle kırılmış bir "
            "ebeveyne suçlayıcı gelebilir. Üç kuşaklık bir genogram anlatmayı kolaylaştırır.",
            "Yinelenme riski yüksek bir sorunu olan çocukta (ör. mani öyküsü) aileye önceliklerin sırasını gösteren kısa bir yazılı “temel "
            "mesaj” verin; sonraki hekimlerin dikkati günün kaygısına kaymasın.",
            "Ergenlere hafif bir tonla sorun: “Biliyorum, yanıtlaması zor ama sence ne yapmalıyız?”",
            "TR Kısa poliklinik sürelerinde açıklamayı tek görüşmeye sıkıştırmak yerine iki kısa görüşmeye bölün. Aile tanı kodunu "
            "e-Nabız’da sizden önce görürse hazırlıksız yakalanabilir; kodlamadan önce anlatın.",
            "TR Aileyle farklı bir dili konuşuyorsanız ya da tercüman kullanıyorsanız anahtar terimleri doğrudan çevirtmek yerine örnek ve "
            "metaforla anlatın, ardından geri anlatma isteyin.",
        ],
        tartisma=[
            ("Ne kadarı hatırlanıyor?",
             "Hastaların sağlık çalışanından duyduğu bilginin önemli bir kısmını kısa sürede unuttuğu, hatırladıklarının bir kısmının da "
             "yanlış olduğu bildirilmiştir; bilgi arttıkça doğru hatırlanan oran düşer, yazılı ya da görsel destek hatırlamayı artırır "
             "([@kessels2003]). Kitabın “en fazla üç bilgi ve yazılı özet” önerisi bu bulgularla uyumludur."),
            ("Geri anlatma",
             "Kronik hastalıklarda hasta eğitimine geri anlatmayı ekleyen çalışmaların sistematik derlemesinde hastalık bilgisi, uyum "
             "ve öz yeterlikte olumlu sonuçlar bildirilmiş, ancak bulgular her zaman anlamlı ve tutarlı olmamıştır ([@hadinh2016]). "
             "Derleme yetişkin hastaları kapsar; ebeveynlere yapılan açıklamalara genellemek bir çıkarımdır."),
            ("Kötü haberin yapılandırılmış dili",
             "Onkolojide geliştirilen SPIKES protokolü ortamı hazırlamayı, kişinin ne bildiğini ve ne kadar bilmek istediğini sormayı, "
             "bilgiyi parça parça vermeyi, duyguya yanıt vermeyi ve planı birlikte kurmayı önerir ([@baile2000]). Kitabın önerileri "
             "bu adımlarla örtüşür; protokolün ebeveyne çocuk psikiyatrisi tanısı bildirmeye uyarlanması ise klinik bir çıkarımdır."),
            ("Biyolojik basitleştirmenin bedeli",
             "Tourette ve DEHB’de sorunu bütünüyle biyolojik anlatmak çocuğu suçlanmaktan korur. Ancak biyogenetik açıklamalar "
             "gidişe ilişkin karamsarlığı artırabilir ([@kvaale2013]); biyolojik açıklamaya değişebilirlik ve tedavi edilebilirlik "
             "vurgusu eklemek gerekir."),
        ],
        sorular=[
            S("Anne, 9 yaşındaki oğlunun okuma güçlüğü için “disleksi” tanısı bekliyor; değerlendirmeniz ise hafif düzeyde genel zihinsel "
              "yetersizliği gösteriyor. Açıklamaya en uygun başlangıç hangisidir?",
              ["Görüşmenin başında “Oğlunuzda zihinsel yetersizlik var” demek",
               "Önce annenin oğlunu dil, sosyal beceri ve günlük işler açısından kaç yaşında gördüğünü sormak ve onun gözlemlerinden yola "
               "çıkarak adım adım genel öğrenme güçlüğüne ilerlemek",
               "Disleksi tanısıyla yetinmek",
               "Yalnızca yazılı raporu göndermek"],
              1, "Kabul edilebilirlik sırasında aşağı inmek zaman ister. Annenin kendi gözlemlerinden başlamak, şok yaratmadan hedef "
                 "terime ulaşmayı ve onu tedavi planına bağlamayı kolaylaştırır. Yanlış ama kabul edilebilir bir tanıda kalmak çocuğun "
                 "gereksinimlerini karşılamaz."),
            S("DEHB tanısı alan 7 yaşındaki bir çocuğun babasına tedavi planını anlattınız. Anlaşılıp anlaşılmadığını sınamanın en iyi "
              "yolu hangisidir?",
              ["“Tamam mı?” diye sormak",
               "“Anlaşılmayan bir şey var mı?” diye sormak",
               "“Eve gidince eşinize bugün ne konuştuğumuzu nasıl anlatacaksınız?” diye sormak",
               "Broşür verip görüşmeyi bitirmek"],
              2, "Kapalı onay soruları anlaşıldığını göstermez. Geri anlatma yanlış anlaşılan noktaları görüşme bitmeden yakalar; yazılı "
                 "özetle birlikte hatırlamayı da güçlendirir."),
            S("Otizm tanısı yeni konan 3 yaşındaki bir çocuğun annesi “Konuşabilecek mi, kendi başına yaşayabilecek mi?” diye soruyor. "
              "En uygun yanıt hangisidir?",
              ["“Hayır, bağımsız yaşaması mümkün değil.”",
               "“Kesinlikle tamamen düzelecek.”",
               "Belirsizliği dürüstçe kabul edip birçok çocuğun zamanla belirgin ilerleme gösterdiğini, erken desteğin önemini ve ailenin "
               "bu yolda yalnız olmayacağını anlatmak",
               "Soruyu yanıtlamayıp konuyu değiştirmek"],
              2, "Altın kural umudu elinden almamaktır; ama umut gerçekçi olmalıdır. Güvenilmez büyük vaatler de kesin karamsar "
                 "kehanetler de ailenin bugün yapabileceklerini zayıflatır."),
        ],
        akilda="Formülasyonu sunmazsınız, ailenin düşüncesini taşırsınız: önce onların kuramını dinleyin, en önemli şeyi önce söyleyin, "
               "umudu asla almayın.",
    ),
    # ------------------------------------------------------------------ 17
    dict(
        no=17, kesim="F", kisa="Mektup ve rapor yazmak",
        baslik="Mektup ve rapor yazmak: görüşmeden geriye kalan sözcükler",
        kitapta_bolumler="F. Explaining · Writing Letters and Reports (s. 235–246)",
        slogan="Görüşme biter, mektup kalır: aynı cümle evde, okulda ve başka bir hekimin masasında yeniden okunur.",
        kitapta=("Bölüm mektubun yararlarını ve risklerini; kapsamlı, gerekçeli ve kısa mektup türlerini; okunabilirliği; mektubun ikna "
                 "ve güven amaçlarını; farklı okurlar için birden çok sürüm hazırlamayı; üslubu; verimliliği (uzunluk, şablonlar, yazma ya "
                 "da dikte etme, aşamalar ve denetim); uzun ve çok yazarlı raporların sorunlarını; diplomasiyi ve aşırı diplomasiyi; "
                 "gizliliği, ergenlerde mahremiyeti ve hassas bilgiyi metinden ayıklamayı ele alır."),
        okurken=[
            "Bu mektubu kimler okuyacak ve her biri ondan ne bekliyor?",
            "Mektuptaki hangi cümleyi ailenin yüzüne söyleyemezdiniz?",
            "Raporunuzun en değerli kısmı neresi: bulgular mı, tartışma mı?",
        ],
        fikirler=[
            ("Mektup görüşmeyi dondurur",
             "Mektup düşünmeyi ve yazmayı eğitir, görüşmeden sonra da kalır, yeniden okunur, bir kayıt hatta bir sözleşme olur ve "
             "aileye bilginin getirdiği yetkiyi verir. Riskleri de vardır: gizlilik, yanlışın kalıcı olması, okunduğu anı ve ortamı "
             "denetleyememek, yanlış anlaşılma ve mektubun görüşmenin yerine geçmesi. Odada düzeltilebilecek bir yanlış anlama, "
             "mektupla tek başına kalan ailede düzeltilemez."),
            ("Üç tür mektup",
             "Kapsamlı rapor resmîdir ve büyük kaynakların bağlı olduğu kararlar için yazılır; en değerli kısmı tartışmadır: tanıları "
             "sıralamak yetmez, göreli önemlerini, aralarındaki ilişkiyi ve yönetimlerini yorumlamak gerekir. Gerekçeli mektup yazması "
             "en zor ama okurun düşüncesini en çok etkileyen türdür; iki tarafı tartıp neden birini daha ikna edici bulduğunuzu söyler. "
             "Kısa notlar öykü, bulgu, değerlendirme ve plan gibi başlıklarla düzenlenir; çok kısa iletiler kolayca yanlış anlaşılır."),
            ("Okunabilirlik",
             "Ruh sağlığı mektupları alıcıları için çoğu zaman fazla zordur. Kısa sözcük, kısa cümle, kısa paragraf; jargon yerine "
             "gündelik dil, çünkü insan davranışını betimlerken gündelik dil teknik dilden daha kesin olabilir. Mektubu aileye yazıp "
             "aile hekimine kopyalamak sadeleştirmeyi kendiliğinden sağlar. Görüşmede konuşmadığınız bir görüşü mektupta ilk kez dile "
             "getiriyorsanız bunu açıkça belirtin."),
            ("Kime, hangi sürüm?",
             "Aile hekimi tek sayfa ister, aile daha ayrıntılı bir metin, çocuk ise kendisine yazılmış bir mektup. Aile öyküsünü ayrı "
             "bir sayfaya koymak, o sayfa çıkarılarak okula verilebilecek bir sürüm hazırlamayı kolaylaştırır. Tanının da sürümleri "
             "olabilir: aklınızdaki çalışma formülasyonu, aileyle uzlaşılan ve kurumlara giden; ama terimleri alışılmış anlamlarıyla "
             "kullanmak itibarınızı korur."),
            ("Verimlilik",
             "Uzunluk amaca göre değişir: basit raporlar birkaç sayfa, izlem mektupları çok daha kısa, hukuki ya da mali sonuçları olan "
             "raporlar daha ayrıntılı olur. Araştırdığınız ama ilgisiz çıkan alanları yazmayın. Görüşme formu ile rapor şablonu aynı "
             "yapıyı paylaşsın, gözlem ile yorum ayrı başlıklarda dursun, şablon fazla doldurulmasın. Sayıları, ilaç adlarını ve "
             "dozları ayrıca denetleyin; başka raporlardan kopyalamak yerine onlara atıf yapın."),
            ("Diplomasi ve aşırı diplomasi",
             "Aileye okutmaktan mutlu olmayacağınız bir mektup yazmayın; herkesin her şeyi okuyacağını varsayın. Görüşten çok olgu "
             "yazın, kimin neyi yanlış yaptığından çok ne yapılması gerektiğini anlatın, alıntı yerine dolaylı anlatım kullanın, "
             "gönderim listesini kısa tutun. Ama kimse sizden hiç şikâyet etmiyor ve meslektaşlarınız onlarla aynı fikirde "
             "olmadığınızı hiç anlamıyorsa fazla diplomatiksiniz: görüş ayrılığını nazik ama açık söylemek gerekir."),
            ("Gizlilik ve ayıklama",
             "Kimliği belirleyen bilgi onam olmadan klinik ekibin dışına çıkmaz; güvenlik gibi daha yüksek bir öncelik varsa paylaşım "
             "endişenin düzeyiyle orantılı olur. Hassas konular açıkça belirsiz bırakılabilir: “ailenin özel kalmasını istediği "
             "konuları konuştuk” gibi. Vaka tartışmasındaki beyin fırtınası sonuç gibi kaydedilmemeli, ergenle mahremiyet konuşulurken "
             "tutulamayacak sözler verilmemelidir."),
        ],
        crs=[
            "Mektuba başlamadan önce okurları sıralayın: aile, aile hekimi, okul, kurum. Her birinin neye ihtiyacı olduğunu bir satırla yazın.",
            "Raporun tartışma bölümünde tanıları yalnızca sıralamayın; hangisinin daha önemli olduğunu, birbirlerini nasıl etkilediklerini "
            "ve yönetimi yazın.",
            "Aile öyküsünü ayrı bir sayfada tutun; okula giden sürümde o sayfayı çıkarın ve aileye hangi sürümün nereye gittiğini söyleyin.",
            "Ebeveynin sözlerini doğrudan alıntılamak yerine dolaylı aktarın: “Aile, son aylarda evde çok zorlandıklarını anlattı.”",
            "Gözlemi ve yorumu ayrı başlıklarda yazın; bulguyu sonuçla karıştırmayın.",
            "Hassas ailelere mektubu önce taslak olarak gönderin ve “Eklemek istediğiniz bir şey olursa bildirin” diye sorun; düzeltme "
            "isteklerine teşekkürle ve gözden geçirilmiş bir taslakla yanıt verin.",
            "Doz ve sayıları ayrıca denetleyin. Ses tanıma yazılımlarının ve yazım denetiminin yol açtığı sözcük değişimleri en zor fark "
            "edilen hatalardır.",
            "TR Sağlık verisi 6698 sayılı KVKK’da özel nitelikli kişisel veridir. Okula ya da başka bir kuruma rapor gönderirken ailenin "
            "açık rızasını alın ve yalnızca gereken bilgiyi paylaşın.",
            "TR Türkiye’de 18 yaşından küçüklerin tedavisinde kural olarak veli ya da vasinin onamı gerekir. Ergene ailesinden tümüyle gizli "
            "bir tedavi sözü vermeyin; görüşmede konuşulanlardan hangilerinin paylaşılacağını onunla birlikte belirleyin.",
            "TR e-Nabız’a düşen rapor ve epikrizleri aile okuyabilir; resmî metinleri de aile okuyacakmış gibi yazın.",
        ],
        tartisma=[
            ("Notları hastalar da okuyor",
             "Hastalara hekim notlarını açan bir yıllık bir uygulamada notu okuyan hastaların çoğu bakımları üzerinde daha fazla denetim "
             "hissettiğini bildirmiş, küçük bir kısmı notlardan kaygılanmış ya da incinmiş, hekimlerin iş yükü belirgin artmamıştır "
             "([@delbanco2012]). Çalışma yetişkin birinci basamak hastalarındadır; çocuk psikiyatrisi kayıtlarında ailenin, çocuğun ve "
             "ergenin farklı mahremiyet beklentileri ayrıca düşünülmelidir."),
            ("Jargon yanlış anlaşılır",
             "Tıp dışından 215 yetişkinle yapılan bir çalışmada bazı yaygın tıbbi ifadeler sık sık, kimi zaman tam tersi anlamda "
             "yanlış anlaşılmış; jargonsuz eş ifadeler her karşılaştırmada daha iyi anlaşılmıştır ([@gotlieb2022]). Bulgu, kitabın kısa "
             "ve jargonsuz yazma uyarısını destekler."),
            ("Mahremiyet güvencesi",
             "Lise öğrencileriyle yapılan randomize bir çalışmada mahremiyet güvencesi, cinsellik, madde kullanımı ve ruh sağlığı "
             "hakkında bilgi vermeye istekli ergenlerin ve yeniden başvurmayı düşünenlerin oranını artırmıştır ([@ford1997]). "
             "Güvencenin sınırlarını ergenin başvurma isteğini düşürmeden açıklamak ayrı bir beceridir."),
            ("Rapor dili ve resmî kalıplar",
             "Kitap rapor dilini İngiltere’deki hukuki ölçütler ve kurumlar üzerinden tartışır. Türkiye’de adli raporlar ve sağlık kurulu "
             "raporları kendi biçim kurallarına bağlıdır; bölümdeki diplomasi ve ayıklama önerileri bu resmî kalıpların içinde "
             "uygulanmalıdır."),
        ],
        sorular=[
            S("Anne, 10 yaşındaki oğlu için okula verilecek bir rapor istiyor. Ailede süren bir boşanma ve annenin depresyon tedavisi var; "
              "anne bunların okula gitmesini istemiyor. En uygun yaklaşım hangisidir?",
              ["Raporun tamamını, aile öyküsüyle birlikte okula göndermek",
               "Aile öyküsünü ayrı bir sayfaya koymak, okula bu sayfanın çıkarıldığı ve sınıf içi önerileri içeren bir sürüm göndermek ve "
               "bunu anneyle önceden konuşmak",
               "Okula hiçbir yazı vermemek",
               "Aile öyküsünü olduğundan farklı yazmak"],
              1, "Ailelerin çoğu aile öyküsünün okula gitmesini istemez. Ayrı sayfa ve ayıklanmış sürüm hem gizliliği hem de okulun "
                 "ihtiyacı olan bilgiyi korur; olguları değiştirmek ise kabul edilemez."),
            S("Bir ebeveynin anlattıklarını mektuba aktarırken aşağıdakilerden hangisi bilgiyi doğru verip ebeveyni en az incitir?",
              ["“Annenin iddiasına göre çocuk geceleri hiç uyumuyor.”",
               "“Anne ‘Bu çocuk beni deli ediyor’ dedi.”",
               "“Anne, çocuğun geceleri uzun süre uyuyamadığını anlattı. Okul gündüz uykululuk gözlemlemiyor; bu farkı uyku günlüğüyle "
               "birlikte izlemeyi kararlaştırdık.”",
               "“Anne abartıyor, çocukta uyku sorunu yok.”"],
              2, "Dolaylı aktarım ebeveyni mercek altında hissettirmez. Görüş ayrılığını nazik ama açık yazmak, şüphe ima eden "
                 "kalıplardan ya da alay gibi duyulabilecek alıntılardan hem daha dürüst hem daha az kırıcıdır."),
            S("Görüşmeden sonra dosyayı yeniden incelerken görüşmede konuşmadığınız bir olasılık (ör. öğrenme güçlüğü) aklınıza geldi ve "
              "mektuba eklemek istiyorsunuz. En uygun yol hangisidir?",
              ["Olasılığı kesin bir tanı gibi mektuba yazmak",
               "Hiç yazmamak",
               "Bunun görüşmede konuşulmadığını açıkça belirtip bir olasılık olarak yazmak ve konuşmak için bir görüşme önermek",
               "Yalnızca aile hekimine giden kopyaya eklemek"],
              2, "Görüşmede konuşulmamış bir görüş aile tarafından sınanmamış ve benimsenmemiştir; bu yüzden diğer bilgilerden daha az "
                 "güvenilirdir. Açıkça belirtmek ve konuşmayı önermek güveni korur; gizlice eklemek ya da kesinmiş gibi yazmak sarsar."),
        ],
        akilda="Görüşme biter, mektup kalır: ailenin yüzüne söyleyemeyeceğiniz cümleyi yazmayın; söylemeniz gerekeni nazik ama açık söyleyin.",
    ),
    # ------------------------------------------------------------------ 18
    dict(
        no=18, kesim="F", kisa="Sözcükler",
        baslik="Sözcükler: kesinlik, yoğunluk ve yararlı belirsizlik",
        kitapta_bolumler="F. Explaining · Words (s. 247–254)",
        slogan="Sözcük bir araçtır: ne söylediğine değil, karşıdakinde ne yaptığına bakın.",
        kitapta=("Bölüm tek tek sözcüklere ve kısa ifadelere odaklanır: ailenin kullandığı sözcüklerin anlamını sormak, sözcüklerin "
                 "düşünceyi nasıl yönlendirdiği, doğru yoğunlukta sözcük seçmek ve sayıların yeri, kaçınılması gereken sözcükler, bulanık "
                 "terimler ve yararlı belirsizlik, yönetim ve eğitim dünyasının kendine özgü sözcükleri, normalliğin tonlarını anlatan "
                 "ince ayrımlı bir dağarcık ve düşünmeyi zenginleştiren birkaç sevimli sözcük."),
        okurken=[
            "Aile “hiperaktif”, “depresif” ya da “saplantılı” dediğinde neyi kastediyor?",
            "Bir riski anlatırken sözcük mü, sayı mı kullanıyorsunuz; karşınızdaki bunu nasıl anlıyor?",
            "Bir şeye ad koymak onu daha gerçek ve daha kalıcı yapabilir mi?",
        ],
        fikirler=[
            ("Önce anlamı sorun",
             "Aileler ve çocuklar sözcükleri bizden farklı anlamlarda kullanır: “Hiperaktif derken heyecanlı mı, yerinde duramayan mı?” "
             "diye sormak gerekir. “Saplantı” gündelik dilde her türlü yineleyen düşünce ya da davranıştır; aileyi psikiyatrik anlamı "
             "kullanmaya zorlamak gereksizdir. Bir sözcüğün anlamı onunla ne yapıldığıdır; hekim, aile ve istatistikçi aynı tanı adını "
             "farklı işler için kullanır."),
            ("Sözcükler düşünceyi yönlendirir",
             "Duygu yüklü, şaşırtıcı ve akılda kalıcı sözcükler dikkati üzerine çeker ve cümlenin geri kalanını gölgeler. Etiketler "
             "gerçekte olmayan keskin kategoriler izlenimi verir. İlaç sınıflarının hastalık merkezli adları hem tanıyı hem tedaviyi "
             "olduğundan net gösterir. Sık tekrarlanan bir ifade (“Ali’nin sorunu”) zihinlerde açıklama bekleyen bir şeye dönüşür; "
             "ahlaki yargı taşıyan suçlayıcı sözcükler ise tartışmayı kilitler."),
            ("Doğru yoğunluk ve sayılar",
             "“Çok mutlu” ya da “depresif”, kime ve hangi zamana göre olduğu söylenmezse belirsizdir. Sıklık ve olasılık sözcükleri "
             "kişiden kişiye çok farklı anlaşılır; insanlar olasılığı sözle anlatmayı ama sayıyla duymayı tercih eder. Önemli bir sayıyı "
             "bilmiyorsanız sorun ya da bakın. Standart bir dil yoksa sözcükleri derecelendirerek kullanın: olağan, rahatsız edici, can "
             "sıkıcı, sıkıntı veren, katlanılmaz."),
            ("Bulanık terimler",
             "“Manipülasyon”, “travmatize” ve “dışa vurma” gibi terimler aşırı ve özensiz kullanılır. “Spektrumda” demek matematikte "
             "herkesi, psikiyatride ise yalnızca işlevi bozulanları kapsar. “Özellik” sözcüğü ise yararlı bir koddur: davranışın "
             "olağan dışı olduğunu kabul ederken tanı eşiğine ulaşmadığını söyler. “Etkiler” ya da “değiştirir” yerine yönü belirtin: "
             "artırır mı, azaltır mı?"),
            ("Yararlı belirsizlik",
             "Belirsiz bir şeye ad koymak onu somut, kesin ve kalıcı yapar; genel bir aile huzursuzluğu adı konmuş bir düşmanlığa "
             "dönüşebilir. Erken kesinlik özellikle şizofreni, kişilik bozukluğu ve “geri kazanılmış anılar” gibi alanlarda zarar "
             "verebilir. Belirsizlik öngörüde, risk anlatmada, açık uçlu sorularda, sır saklamada ve çatışmadan kaçınmada işe yarar: "
             "“Ben göremiyorum” demek, yeni bir tanı önermekten daha az tartışma doğurur."),
            ("Kurumların sözlüğü",
             "Yönetim ve eğitim dünyası sözcükleri yeniden tanımlar: “seçim”, “esneklik”, “en az kısıtlayıcı ortam” ya da “kişi "
             "merkezli” gibi sözcükler kimi zaman maliyeti düşürmenin örtüsü olur. Okulda “ortalama” çok geniş bir aralığı kapsayabilir "
             "ve “beklenen düzeyde ilerliyor” çocuğun başlangıç düzeyine göre ölçülüyor olabilir. Kurumlar arası anlaşmazlıkların "
             "çoğu, aynı sözcüğün farklı anlamlarda kullanılmasından doğar."),
            ("Normallik için de sözcük",
             "Anormalliği anlatan sözcüklerimiz kadar normalliğin tonlarını anlatan sözcüklere de ihtiyacımız var: biraz tuhaf, otistik "
             "özellikleri olan, eşiğe ulaşmayan; neşeli, coşkulu, hipomanik; içe dönük, sakin, çekingen. “Huysuz bir ergen” gibi bir "
             "betim sorunu adlandırırken onu olağanlaştırır ve hastalaştırmaz."),
        ],
        crs=[
            "Ailenin kullandığı yüklü sözcükleri (hiperaktif, depresif, kriz, travma, saplantı) somut bir örnekle açın: “Son bir haftadan "
            "bir örnek verebilir misiniz?”",
            "Yan etki ve gidiş risklerini sözcüğün yanında sayıyla da verin: “100 çocuktan yaklaşık 5’inde.”",
            "Tanı eşiğine ulaşmayan durumlarda “Özellikleri var ama işlevini bozacak düzeyde değil” cümlesini kullanın ve neyi "
            "izleyeceğinizi söyleyin.",
            "Mektup ve notlarda “durum”, “görüşüldü”, “manipülatif” gibi uzak, edilgen ya da suçlayıcı sözcüklerden kaçının.",
            "Ekip toplantısında ahlaki yargı taşıyan bir sözcük (ör. birini “ailenin tarafını tutmakla” suçlamak) tartışmayı kilitliyorsa "
            "kişiden kanıta ve çocuğun çıkarına dönün.",
            "İlaç anlatırken sınıf adının yanında etkisini de söyleyin; “antidepresan” adı, kaygı bozukluğu için ilaç başlanan bir aileyi "
            "şaşırtabilir.",
            "TR Okulla konuşurken “kaynaştırma”, “bütünleştirme”, “BEP” ya da “destek eğitim odası” gibi terimlerin o okulda ve RAM’da tam "
            "olarak neye karşılık geldiğini sorun.",
            "TR “Sinir krizi geçirdi”, “depresyona girdi”, “travma oldu” gibi ifadeler gündelik Türkçede geniş anlamlarda kullanılır; "
            "öykü alırken olanı davranış düzeyinde betimletin.",
        ],
        tartisma=[
            ("Olasılık sözcükleri",
             "Sözel olasılık ifadelerinin sayısal karşılığını inceleyen çalışmaların meta-analizinde ortak bir sıralama bulunmuş, ancak "
             "çalışmalar arasındaki farklılık çok yüksek çıkmıştır ([@vogel2022]). Klinik risk iletişimi üzerine bir derleme, sözcükleri "
             "sayısal aralıklarıyla birlikte ve “100 kişiden X” biçiminde sunmayı önerir ([@hashim2024]). Kitabın sayı kullanma önerisi "
             "bu bulgularla uyumludur."),
            ("Etiket algıyı biçimlendirir",
             "Öğretmenlerle yapılan bir vinyet çalışmasında aynı belirtiler “DEHB” etiketiyle sunulduğunda çocuk daha bozulmuş görülmüş "
             "ve daha olumsuz duygular uyandırmış, ancak müdahale uygulama isteği de artmıştır ([@ohan2011]). Etiket hem kapı açar hem "
             "de algıyı biçimlendirir."),
            ("İlaç adlarını değiştirmek",
             "Endikasyona dayalı ilaç adlarının yerine farmakolojik etki alanını ve mekanizmayı öne çıkaran nörobilim temelli bir "
             "adlandırma önerilmiştir ([@zohar2015]). Öneri kitabın hastalık merkezli ilaç adları eleştirisiyle örtüşür; ancak ailelere "
             "anlatırken mekanizma adları da yeni bir jargona dönüşebilir."),
            ("Belirsizlik ve onam",
             "Yararlı belirsizlik çatışmayı azaltır ve erken etiketlemeyi önler, ama bilgilendirilmiş onamın gerektirdiği açıklıkla "
             "gerilim içindedir. Belirsiz dil bilgi saklamak için değil, kesinliği abartmamak için kullanılmalıdır."),
        ],
        sorular=[
            S("Bir anne “Kızım çok hiperaktif” diyor. Öyküyü sürdürmek için en iyi soru hangisidir?",
              ["“Yani DEHB olduğunu düşünüyorsunuz?”",
               "“Hiperaktif derken neyi kastediyorsunuz? Son bir haftadan bir örnek verebilir misiniz?”",
               "“Bütün çocuklar hareketlidir.”",
               "“Önce ölçeği doldurun, sonra konuşalım.”"],
              1, "Aileler sözcükleri farklı anlamlarda kullanır: yerinde duramamak, çok heyecanlanmak, söz dinlememek. Somut bir örnek "
                 "istemek varsayımı değil davranışı ortaya çıkarır; erken bir tanı adı ya da güvence bu bilgiyi kaçırır."),
            S("Başlayacağınız bir ilacın bir yan etkisi yaklaşık 100 çocuktan 1’inde görülüyor. Aileye en iyi anlatım hangisidir?",
              ["“Nadir görülür.”",
               "“Pek önemli değil.”",
               "“100 çocuktan yaklaşık 1’inde görülür; görülürse şu belirtilerle fark edersiniz ve bizi ararsınız.”",
               "“Olasılığı yüzde 0,01.”"],
              2, "Sözel olasılık ifadeleri kişiden kişiye çok farklı anlaşılır. “100 çocuktan X” biçimindeki doğal sıklık ve ne "
                 "yapılacağına ilişkin somut bilgi yanlış anlamayı azaltır. Son seçenekteki oran da yanlıştır: 100’de 1, yüzde 1 eder."),
            S("Okul, 8 yaşındaki bir çocuk için otizm tanısı istiyor. Çocukta sosyal iletişimde bazı tuhaflıklar var, ama günlük işlevselliği "
              "bozulmamış ve tablo tanı eşiğine ulaşmıyor. Okula en uygun ifade hangisidir?",
              ["“Spektrumda.”",
               "“Hiçbir sorunu yok.”",
               "“Bazı otistik özellikleri var, ama işlevselliğini bozacak düzeyde değil ve tanı eşiğine ulaşmıyor; şu destekler yararlı "
               "olur ve altı ay sonra yeniden değerlendireceğiz.”",
               "“Hafif otizm.”"],
              2, "“Özellik” sözcüğü gözlemi kabul ederken tanı eşiğine ulaşılmadığını söylemeye yarar. “Spektrumda” belirsiz bir "
                 "kısaltmadır; olmayan bir tanıyı koymak ya da gözlemi yok saymak ise güveni zedeler."),
        ],
        akilda="Sözcük bir araçtır: karşıdakinde ne yaptığına bakın. Önemli bir sayıyı biliyorsanız sözcükle değil sayıyla söyleyin.",
    ),
    # ------------------------------------------------------------------ 19
    dict(
        no=19, kesim="F", kisa="Etkilemek ve ikna etmek",
        baslik="Etkilemek ve ikna etmek: seçimi elden almadan yön göstermek",
        kitapta_bolumler="F. Explaining · Influencing; Persuading (s. 255–270)",
        slogan="Nezaket bazen ikna etmeyi gerektirir; dürüstlük, ikna ederken seçimi elden almamayı.",
        kitapta=("İlk bölüm etkilemeyi, kişiye bıraktığı özgürlüğe göre sıralanan yöntemlerle ele alır: ne yapacağını söylemek, ortamı "
                 "düzenlemek, öyküyü yeniden yazdırmak, dürtmeler ve varsayılan seçenekler, motivasyonel görüşme ve motivasyon artırıcı "
                 "terapi, ergenlerde madde kullanımı ve tehditler. İkinci bölüm ikna etmeyi ele alır: ne kadar emek verileceği, bilgi ile "
                 "özgürlüğün dengesi, tipik ikna durumları, görüşmenin havası, konuya özgü teknikler (ailenin beklentilerinden başlamak, "
                 "“karar sizin” demek, küçük bir taahhüt, karşıtlık etkisi, sayıların algısı, çerçeveleme), kaçınılması gerekenler (baskı, "
                 "ders vermek, sahte denge, etik dışı teknikler, istemeden düğmeye basmak, dırdır) ve müzakere."),
        okurken=[
            "Bu aileyi ikna etmeye mi çalışıyorsunuz, yoksa yalnızca bilgi verdiğinizi mi sanıyorsunuz?",
            "Önerdiğiniz seçeneği hangi seçeneklerle karşılaştırarak sunuyorsunuz?",
            "Hangi ikna yöntemi etik sınırı aşar?",
        ],
        fikirler=[
            ("Ne kadar özgürlük bırakıyorsunuz?",
             "Etkileme yöntemleri kişiye bıraktıkları özgürlüğe göre sıralanır: ne yapacağını söylemek, güçlü bir yönlendirmeyle "
             "seçenek sunmak, rehberli seçenekler, bütün seçenekleri serbestçe sunmak ve kişinin kendi kararını vermesine tarafsızca "
             "yardım etmek. Özerklik tek değer değildir; hastalar hekimden en çok yetkinlik ve nezaket bekler. Nezaket bazen ağır bir "
             "kararı üstlenmeyi ya da korkulan bir tedaviye ısrarla yönlendirmeyi gerektirir."),
            ("Ortamı ve öyküyü değiştirmek",
             "Çocuğu değiştirmeye çalışmak yerine onun kendiliğinden doğru davranacağı bir ortam kurulabilir: tutarlı kurallar, uygun "
             "okul, olumlu arkadaşlar, alternatif etkinlikler; kötü örneklerden, silaha erişimden ve çelişen ebeveyn tutumlarından "
             "korumak. Öyküyü yeniden yazdırmak, ebeveynin çocuğu suçlayan açıklamasının yerine kendi bulduğu, değiştirilebilir bir "
             "açıklamayı ve çözümü koymasına yardım eder."),
            ("Dürtmeler",
             "Dürtmeler seçimi kaldırmadan ya da belirgin bir bedel yüklemeden kişiyi bir seçeneğe yöneltir. Varsayılan seçenek "
             "güçlüdür: “İstemiyorsanız bildirin” biçimi, “İstiyorsanız bildirin” biçiminden çok daha fazla katılım sağlar. Evde "
             "yapılacak bir şeyi kolay, çekici, sosyal ve zamanında kılmak, çıpalar ve olumlu adlandırmalar da dürtmedir. Bu araçlar "
             "kolayca etik sınırı aşabilir."),
            ("Motivasyonel görüşme",
             "Ergenin yetişkinlerle aynı öncelikleri taşıdığını varsaymayın. Karşı çıkmayın ve tartışmanın tek tarafını doldurmayın; "
             "kişiyi öbür tarafa itersiniz. Empati, kişinin istediği ile yaptığı arasındaki çelişkiyi fark ettirmek, tartışmadan "
             "kaçınmak, dirence karşı koymak yerine onunla birlikte ilerlemek, kararsızlığı olağan saymak ve öz yeterliği desteklemek "
             "temel ilkelerdir. Karar dengesi tablosu değişimin artılarını ve eksilerini kişinin kendi sözcükleriyle görünür kılar."),
            ("Madde kullanımında ölçü",
             "Denemek ile bağımlılık farklı şeylerdir; asıl ölçüt madde aramaya harcanan zamandır. “Yasal” maddeler güvenli değildir. "
             "Gencin hayatı iyileştiğinde madde kullanımı çoğu zaman azalır. Akranların ne kadar kullandığına dair abartılı inancı "
             "düzeltmek, ebeveynle birlikte vakit geçirmek ve kullanan arkadaş çevresine alternatif bulmak tedavinin parçasıdır."),
            ("Tehdit ve ikna",
             "Tehdit, karşı taraf uymazsa kötü bir şey yapılacağının önceden söylenmesidir. Ebeveynin tehdidi inandırıcı, orantılı ve "
             "yinelenebilir olmalı, ama acımasız olmamalıdır. Tehdide dayalı düzenler alışverişe ya da ilişkiye dayalı düzenlerden daha "
             "az kararlıdır: itaat üretir ama fikir değiştirmez. İkna ise daha müdahaleci ve kişiseldir; çok etkili olabildiği için "
             "seçimi elden almamaya özen gerektirir."),
            ("İknanın teknikleri ve sınırları",
             "Güvenilir ve açık bilgi çoğu zaman yeter. Önce ailenin önceliklerine yanıt verin; “Karar sizin” demek öneriye uyma "
             "olasılığını artırır. Küçük bir taahhüt büyüğünü kolaylaştırır; tek seçenek yerine iki üç seçenek sunmak ve önermediğiniz "
             "seçeneği de göstermek ikna edicidir. Baskı, ders vermek, hızlı konuşmak, sahte denge kurmak, yanlış bilgi vermek, kafa "
             "karıştırarak ikna etmek ve seçenekleri haksız yere daraltmak ise kabul edilemez. Görüşleri ortadan bölen uzlaşmalar bazen "
             "saçmadır; ilkelerden ödün verilmez."),
        ],
        crs=[
            "Bir tedaviyi önermeden önce iki üç seçeneği (ör. davranışçı ebeveyn eğitimi, okul düzenlemesi, ilaç) artıları ve eksileriyle "
            "masaya ayrı kâğıtlarda koyun; hangisini neden önerdiğinizi ve hangisini önermediğinizi söyleyin.",
            "Kararsız bir ergenle değişimin artılarını ve eksilerini onun sözcükleriyle dört kutulu bir karar dengesi tablosuna yazın.",
            "Ebeveynin çocuğu suçlayan açıklamasına (“İnadına yapıyor”) “Başka ne olabilir?” diye sorun; değiştirilebilir bir açıklamaya ve "
            "uygulanabilir bir plana birlikte ulaşın, bir sonraki görüşmede sonucunu sorun.",
            "Riskleri “100 çocuktan X” biçiminde verin ([@hoffrage2000]); aynı riski yüzdeyle ya da tek bir çocuğun öyküsüyle anlatmanın "
            "algıyı nasıl değiştirdiğini bilin ve bunu dengeli kullanın.",
            "“Bu ilaç tehlikeli değil” yerine “Bu ilacı kullanan çocukların çoğunda ciddi bir sorun görülmez; en sık yan etkiler şunlar” "
            "deyin; olumsuz cümle tehlike fikrini çağırır.",
            "Aile ikna olmadıysa ısrar etmek yerine dosyayı birkaç ay açık tutup kapıyı açık bırakın.",
            "Ebeveynlere dırdır yerine açık bir kural, tutarlı sonuç ve gerçekçi beklenti önerin; bazı konuların ergen için ebeveynden "
            "daha önemli olduğunu kabul etmek çatışmayı azaltır.",
            "TR Ergen madde kullanımında ailelerin ilk kaygısı çoğu zaman yasal sonuçlar ve çevredir. Kaygıyı adlandırın, ardından ÇEMATEM "
            "gibi uzman birimlerin ne zaman gerektiğini somut ölçütlerle anlatın.",
            "TR Randevu ve görüşme düzenlerinde varsayılan seçenek katılımı artırır; ama bilginin okulla ya da başka kurumlarla "
            "paylaşılması gibi açık rıza gerektiren konularda (KVKK) varsayılan onay kullanılmamalıdır.",
        ],
        tartisma=[
            ("Öyküyü yeniden yazdırmak işe yarıyor mu?",
             "Riskli ailelerle yapılan randomize bir ev ziyareti çalışmasında, annelerin bebeğin davranışına ilişkin suçlayıcı "
             "açıklamalarını ele alan bilişsel bir bileşen eklendiğinde ilk yıldaki fiziksel istismar sıklığı %4 olmuş; kontrol grubunda "
             "%26, standart ev ziyaretinde %23 bulunmuştur ([@bugental2002]). Çalışma küçüktür (96 aile) ve bebeklik dönemindedir; "
             "daha büyük çocuklara genellemek bir çıkarımdır."),
            ("Motivasyonel görüşmenin etki büyüklüğü",
             "21 çalışmanın meta-analizinde ergenlerde madde kullanımına yönelik motivasyonel görüşmenin etkisi küçük ama anlamlı "
             "bulunmuş ve izlemde de sürmüştür ([@jensen2011]). Yöntem yararlıdır; ama tek başına büyük bir değişim beklemek "
             "gerçekçi değildir."),
            ("Akran normlarını düzeltmek",
             "Kitap, akranların ne kadar madde kullandığına dair abartılı inancı düzeltmeyi önerir. Üniversite öğrencilerinde sosyal norm "
             "bilgisine dayalı müdahalelerin Cochrane derlemesi bazı istatistiksel etkiler bulmuş, ama bunları uygulama için anlamlı "
             "sayılmayacak kadar küçük değerlendirmiştir ([@foxcroft2015]). Norm düzeltmesi tek başına değil, diğer bileşenlerle birlikte "
             "düşünülmelidir."),
            ("Deneme her zaman masum mu?",
             "Kitap denemenin çoğu zaman bağımlılığa ilerlemediğini vurgular. Ancak ulusal bir ABD araştırmasında alkol kullanımına "
             "başlama yaşı her bir yıl geç olduğunda yaşam boyu bağımlılık olasılığı %14 azalmıştır ([@grant1997]). Erken başlangıç "
             "panik nedeni değil, izlem ve erteleme nedenidir."),
            ("Varsayılanların gücü ve etiği",
             "Organ bağışında varsayılan seçeneğin bağışçı olmak olduğu ülkelerde onay oranları çok daha yüksektir ([@johnson2003]). "
             "Aynı güç klinikte bilgi paylaşımı ya da eğitim amaçlı kayıt için kullanılırsa onamın gerçekliği sorgulanır."),
        ],
        sorular=[
            S("15 yaşındaki bir ergen sigarayı bırakmak istemediğini söylüyor; babası sizden “ona akciğer kanserini anlatmanızı” istiyor. "
              "Motivasyonel görüşme açısından en uygun ilk adım hangisidir?",
              ["Kanser riskini ayrıntılı ve korkutucu biçimde anlatmak",
               "Ergenin sigarada sevdiği ve sevmediği şeyleri sorup değişimin onun için artılarını ve eksilerini birlikte konuşmak",
               "Sigarayı bırakmazsa telefonunun alınacağını söylemek",
               "Konuyu hiç açmamak"],
              1, "Ergenin öncelikleri çoğu zaman uzak sağlık riskleri değil, arkadaşları ve görünüşüdür. Tartışmanın tek tarafını "
                 "doldurmak onu öbür tarafa iter; kendi artılarını ve eksilerini dile getirmesi kararsızlığı değişime doğru taşır."),
            S("DEHB tanısı alan 8 yaşındaki bir çocuğun ailesine tedavi önereceksiniz. Aşağıdaki sunuşlardan hangisi hem etik hem de ikna "
              "edici olmaya en yakındır?",
              ["“Bu ilaç tehlikeli değil, hemen başlayalım.”",
               "Yalnızca ilacı anlatıp başka seçenekten söz etmemek",
               "Davranışçı ebeveyn eğitimi, okul düzenlemesi ve ilaç seçeneklerini artı ve eksileriyle sunmak, hangisini neden önerdiğinizi "
               "açıklamak ve “Karar sizin; isterseniz bir ay deneyip birlikte değerlendirelim” demek",
               "Seçenekleri eşit derecede iyiymiş gibi sunup tercihi tamamen aileye bırakmak"],
              2, "Birkaç seçeneği gerekçesiyle sunmak, önerinizi açıkça söylemek ve seçimi aileye bırakmak hem ikna edici hem dürüsttür; "
                 "küçük ve geri alınabilir bir deneme kararı kolaylaştırır. Olumsuz cümleler tehlike fikrini çağırır; sahte denge ise yol "
                 "gösterme görevinden kaçmaktır."),
            S("Bir anne, 2 yaşındaki oğlunun her market ziyaretinde bağırıp yere yatmasını “İnadına yapıyor, beni rezil etmek istiyor” "
              "diye açıklıyor. Öyküyü yeniden yazdırma yaklaşımına en uygun yanıt hangisidir?",
              ["“Hayır, bu yaşta çocuklar inat etmez.”",
               "“Başka ne olabilir? Hangi saatlerde, ne kadar süren alışverişlerde oluyor?” diye sorup annenin bulduğu değiştirilebilir "
               "bir açıklamadan (ör. yorgunluk, açlık, uzun bekleme) birlikte bir plan çıkarmak",
               "Annenin sabırsız olduğunu söylemek",
               "Konuyu geçiştirmek"],
              1, "Hazır bir açıklama vermek yerine ebeveynin kendisinin suçlamayan ve değiştirilebilir bir açıklama bulmasına yardım "
                 "etmek, hem açıklamayı hem davranışı daha kalıcı biçimde değiştirir. Doğrudan itiraz ya da eleştiri savunma yaratır."),
        ],
        akilda="İkna etmek nezaketin bir parçasıdır: menüyü dürüstçe sunun, önerinizi açıkça söyleyin ve son sözü aileye bırakın.",
    ),
    # ------------------------------------------------------------------ 20
    dict(
        no=20, kesim="G", kisa="Risk olayları",
        baslik="Risk olayları: korkuyu ve sorumluluğu ölçüsünde tutmak",
        kitapta_bolumler="G. This Shouldn’t Happen! · Risk Events (s. 271–278)",
        slogan="Sorumluluğunuzun sınırı bellidir: mesleğin ve toplumun kabul ettiği önlemleri özenle uygulamak.",
        kitapta=("Bölüm, intihar ve dava gibi kaçınmaya çalıştığımız büyük olayları ele alır. Çocuk psikiyatrisinin komşu alanlara "
                 "göre neden daha az riskli olduğunu, meslek kuruluşlarına ve şikâyet birimlerine en sık hangi olayların ulaştığını, "
                 "acil bir tehlikenin düşünmeyi nasıl kilitlediğini ve ahlaki tehlikeyi tartışır. Klinisyenin riski neden abarttığını "
                 "(kullanılabilirlik yanılgısı, kesinlik ve olasılık etkileri), ara düzeydeki kaygının neden yararlı bir işaret olduğunu, "
                 "hataların kaçınılmazlığını ve nedenlerini, nörogelişimsel değerlendirmede sık görülen hataları anlatır. Son kısım "
                 "alışılmadık kararların hukuki dayanaklarını (Bolam ve Bolitho ölçütleri; kılavuz, kabul gören uygulama ve uzmanlık) "
                 "ve yöneticilerin riski klinisyenlerden neden farklı gördüğünü açıklar."),
        okurken=[
            "Son kaygılandığınız vakada kaygınızın ne kadarı vakanın kendisinden, ne kadarı aklınızda kalmış eski bir olaydan geliyordu?",
            "Alışılmadık bir kararınızı biri sorgulasa hangi dayanağı gösterirdiniz: kılavuzu, meslektaşlarınızın kabul gören "
            "uygulamasını, yoksa uzmanlığınızı?",
            "Yöneticinize bir riski anlatırken genel bir uyarı yerine hangi sayıyı ve hangi çözümü getirebilirsiniz?",
        ],
        fikirler=[
            ("Çocuk psikiyatrisinde risk neden daha düşük?",
             "Psikiyatri, malpraktis davalarının en seyrek açıldığı ve tazminatların en küçük kaldığı alanlardandır. İntihar riski de "
             "çocuk psikiyatrisinde, özellikle küçük çocuklarla çalışırken, erişkin psikiyatrisine göre çok düşüktür. Bunun başlıca "
             "nedeni çocuğu her gün izleyen anne-baba, öğretmen, akraba ve komşulardır: kaygı verici gelişmeleri bize taşırlar ve "
             "bizim uygulamamızı da izlerler. Vakaların çok disiplinli ekipte konuşulması ek bir güvenlik denetimidir. Bunun bir bedeli "
             "de vardır: risk, yöneticilerin ve politikacıların dikkatini çekmek için kullanılamaz ve fon verenler bizi riski daha "
             "yüksek olan pediatri ve erişkin psikiyatrisiyle karşılaştırır."),
            ("Hangi olaylar gerçekten yaşanıyor?",
             "Meslek kuruluşlarına ulaşan olayların başında cinsel nitelikli uygunsuz davranışlar gelir; hastaya kişisel mesajlar "
             "göndermek de bunlara dahildir. Reçeteyle ilgili sorunlar da sıktır: bağımlılık yapan ilaçları aile hekimine bildirmemek, "
             "başkası adına reçete yazmak, ilaç firmalarından çıkar sağlamak. İstismar iddialarını bildirmemek, kayıtlara yetkisiz "
             "erişim, sahte faturalama ve madde kullanımı da listededir. İngiltere’de bir ruh sağlığı kurumuna gelen şikâyetlerin "
             "yaklaşık yarısı klinik dışı konulardaydı; çocuk ve ergen ayaktan hastalarının yaklaşık beş yüzde biri, yatan hastaların "
             "ise onda biri şikâyette bulunmuştu. Araştırmacılara göre şikâyetlerin birçoğunun kökünde büyük olasılıkla kötü iletişim vardı."),
            ("Önce tehlikeyi durdurmak",
             "Yola fırlayan ya da başını cama vuran bir çocuk, diyabet krizlerine kendisi yol açan bir ergen, çevresindekilerde sistemli "
             "düşünmeyi neredeyse imkânsız kılan bir kaygı uyandırır. Önce tehlike hemen denetim altına alınır; yetişkinler "
             "sakinleştikten sonra davranış planı yapılır. Daha küçük risklerde acele gerekmez. Başını vurarak istediğini almayı "
             "öğrenmiş bir çocuğun annesine görmezden gelmesini söylemek işe yaramaz, çünkü bunu yapamaz. Ona yapacak bir iş vermek "
             "(ör. vurduğu yere yumuşak bir örtü koymak) kaygısını yatıştırır ve sönme planının uygulanmasını kolaylaştırır. Ahlaki "
             "tehlike de akılda tutulmalıdır: riskten korunduğunu bilen kişi daha az özen gösterebilir. Bulunacağını bilen bir ergen, "
             "uzun vadeli izlemi kendisine kalmayacak geçici bir hekim ya da yardım geleceğini bekleyen bir ekip buna örnektir."),
            ("Riski neden abartırız?",
             "Riski çoğu zaman kullanılabilirlik yanılgısıyla değerlendiririz: sık duyduğumuz ya da kendi yaşadığımız çarpıcı olaylar "
             "akla kolay gelir ve olduğundan sık görünür. Yıllar önce bir hastanın intiharı, istatistiklerin gerektirdiğinden fazla "
             "kaygı uyandırmayı sürdürür. Neredeyse emin olduğumuz iyi bir sonucu kesinleştirmek için orantısız çaba harcarız "
             "(kesinlik etkisi); kaçınılmaz görünen kötü bir sonuca karşı küçük bir şans yaratmak için de çok çalışırız (olasılık "
             "etkisi). Bazı meslektaşlar bir felaketten sonra fazla savunmacı olur, gereksiz tetkik ister ya da ilaç yazmaktan "
             "kaçınır. Oysa kişisel sorumluluğumuz mesleğin ve toplumun seçtiği risk yönetimi yöntemlerini özenle uygulamakla "
             "sınırlıdır. Kimse zihin okumamızı, geleceği görmemizi ya da her riski önleyen bir sistem kurmamızı beklemez."),
            ("Kaygı bir işarettir",
             "Kıdemsiz bir hekim sık sık kaygılanıyorsa bunun nedeni yeterince desteklenmemesi olabilir. Bir yöneticiyle her "
             "konuşmada kaygı ya da öfke duyuyorsanız, büyük olasılıkla başkalarında da aynı etkiyi uyandırıyordur ve kendisi de "
             "kaygılı ya da öfkeli olabilir. Kaygınızın yakın nedenini görmek hem kendinizi hem onu daha az suçlamanızı sağlar. "
             "Uygulanamaz biçimde kurulmuş bir görevde klinisyen, kaybettiğini kabul edemeyen bir kumarbaz gibi giderek daha çok emek "
             "harcar. Ara düzeyde bir kaygı ise yararlıdır: parçaların birbirine uymadığını, yeterli ek bilgi kaynağına "
             "başvurulmadığını ya da vakanın öncekilerden farklı olduğunu haber verebilir. Bu durumda bir meslektaşla konuşmak "
             "gerekir. Belli bir noktadan sonra kaygı verimi ve keyfi azaltır; o zaman işi sadeleştirmek, uyku ve izin düşünülmelidir."),
            ("Hatalar ve nedenleri",
             "Hata kaçınılmazdır ve gelişmenin bir parçasıdır, ama sayısı az olmalıdır. Hatalar ağırlık, önlenebilirlik, "
             "öngörülebilirlik ve fark edilebilirlik bakımından ayrışır. Küçük şeylerdeki hatalar büyük şeylerde daha dikkatli "
             "olmamızı sağlamalıdır. Kıdemli görüşü sık sık istediğiniz hâlde yanıt hep zaten bildiğinizi yineliyorsa kendi "
             "yargınıza biraz daha güvenebilirsiniz. Ana akımdan uzaklaşmamak için ara sıra ikinci görüş almak gerekir. Nedenler üç "
             "düzeyde aranabilir: kişinin içinde (mantık yerine sezgiye güvenmek, aşırı güven), kendi çalışma düzenimizde (acele "
             "etmek, başkalarının hatalarından habersiz kalmak, az okumak, dar düşünmek) ve en sık olarak kurumun düzeninde. Kitap, "
             "otizm ve zihinsel yetersizlik değerlendirmesinde bu düzenin ürettiği sistemli hatalardan uzun bir liste verir."),
            ("Alışılmadık kararların hukuku",
             "İngiltere’de Bolam ölçütüne göre sorumlu bir meslektaş grubunun destekleyeceği biçimde davranan hekim ihmalkâr sayılmaz; "
             "aynı kararı vermeyecek meslektaşların bulunması kararı ihmal yapmaz. Bolitho ölçütü, dayanılan görüşün mantıksal "
             "sınamaya da dayanması koşulunu ekler. Kılavuzlara ve yayımlanmış kanıta katı biçimde bağlı kalmak, olağandışı vakada "
             "protokolün akılcı biçimde genişletilmesini ve yeniliği engeller. Bir kararı savunmanın üç yolu vardır: saygın bir "
             "kılavuza uymak, meslektaşların kabul gören uygulamasına uymak ve okuma ya da deneyimle edinilmiş uzmanlığa dayanmak. "
             "Aynı şeyi yapan iki üç meslektaş bulmak tek başına yetmez, çünkü onlar da sıra dışı olabilir."),
            ("Yöneticinin riski",
             "Yöneticiler çoğu zaman yetersiz eğitimli ve aşırı yüklüdür, işlerini kaybetme riskiyle yaşarlar. Tek bir ölüm ilgili "
             "klinisyenleri derinden sarsar, en alt düzeydeki yöneticiyi kaygılandırır ve hiyerarşide yukarı çıktıkça daha az kaygı "
             "yaratır. Yinelenen ölümler ise kurumun tepesini etkiler, çünkü önlenmesi gereken ortak bir neden düşündürür. Pek çok "
             "riskli kararı birlikte değerlendiren geniş çerçeve daha iyi kararlar doğurur, ama çalışanlar geri görüşle "
             "yargılanacaklarını bilir. Risk kayıtları riskin büyüklüğünü olasılığıyla çarpar ve alınan önlemleri sıralar. "
             "Yöneticiye yalnızca “Bu güvenli değil” demek çoğu zaman duyulmaz. Kurumun tepesinde üç tür risk yoğunlaşır: medyaya "
             "yansıyan bir felaket, mali çöküş ve birbirinden bağımsız sanılan ama birlikte gerçekleşen riskler (ör. antipsikotik "
             "kullanan çok sayıda gencin yıllar içinde diyabet geliştirmesi ve bunun toplu davaya dönüşmesi)."),
        ],
        crs=[
            "Acil bir tehlikede (yola fırlayan çocuk, kendine ağır zarar veren ergen) önce ortamı güvenli kılın; davranış planını "
            "herkes sakinleştikten sonra birlikte yapın.",
            "Başını vuran bir çocuğun annesine, sönme planı sürerken yapabileceği zararsız bir iş verin (ör. vurduğu yere yumuşak bir "
            "örtü koymak); yalnızca “görmezden gelin” demek uygulanamaz bir öneridir.",
            "Bir vaka hakkında ara düzeyde bir kaygı duyduğunuzda üç soru sorun: Parçalar birbirine uyuyor mu? Yeterli ek bilgi "
            "kaynağına başvurdum mu? Bu vaka öncekilerden farklı mı? Yanıtlardan biri sizi rahatsız ediyorsa bir meslektaşla konuşun.",
            "Nörogelişimsel değerlendirmede gözlem ölçeğini çocuk öfkeli ya da çökkünken uygulamayın, bakım ortamı yeni değişmiş bir "
            "çocuğa hemen zekâ testi yapmayın, otizm ya da dil bozukluğu düşünürken zihinsel yetersizliği ayrıca değerlendirin ve "
            "tanıyı yalnızca ebeveyn anketine dayandırmayın ([@havdahl2016]).",
            "Alışılmadık bir kararın gerekçesini kayda geçirin: dayandığınız kılavuz ya da yayımlanmış kanıt, danıştığınız meslektaş, "
            "aileyle konuşulan riskler ve izlem planı.",
            "Yöneticiye bir riski somut sayılar ve önerilen bir önlemle yazılı olarak bildirin (ör. bekleme süresi, izlemsiz kalan "
            "hasta sayısı, gereken ek seans). Yazılı bildirim riskin bir kısmını da karar verene taşır.",
            "Kendi yaşadığınız çarpıcı bir olayın bugünkü kararlarınızı orantısız biçimde etkileyip etkilemediğini sorun; gerekiyorsa "
            "vakayı ekipte konuşarak riski yeniden tartın ([@alexander2000]).",
            "TR Ruhsatlı bir ilacı onaylı endikasyonu dışında kullanacaksanız, ilaç Türkiye İlaç ve Tıbbi Cihaz Kurumunun ek onay "
            "gerektirmeyen endikasyon dışı kullanım listesinde değilse hasta bazında Kurum onayı ve bilgilendirilmiş hasta olur formu "
            "gerekir. Gerekçe, literatür ve aileyle yapılan konuşmanın kaydı hem başvuruda hem olası bir hukuki incelemede işe yarar.",
            "TR Hasta ve yakınlarının şikâyetleri kurumun hasta hakları birimine ya da CİMER’e de ulaşabilir. Yanıt hazırlarken önce "
            "iletişimde neyin aksadığını sorun; şikâyet konularının yaklaşık üçte ikisi klinik kararlardan çok yönetim ve ilişki "
            "sorunlarıyla ilgilidir ([@reader2014]).",
        ],
        tartisma=[
            ("Psikiyatride dava riski gerçekten düşük mü?",
             "ABD’de büyük bir sigorta şirketinin 40.916 hekimine ait 1991-2005 verilerinde, her yıl dava açılan hekim oranı beyin "
             "cerrahisinde %19,1, pediatride %3,1 ve psikiyatride %2,6 bulunmuştur. Ortalama tazminatın en yüksek olduğu alan "
             "pediatridir. Düşük riskli alanlarda çalışan hekimlerin de %75’inin 65 yaşına kadar en az bir davayla karşılaştığı "
             "kestirilmiştir ([@jena2011]). Yıllık risk düşük olsa da meslek ömrü boyunca birikir."),
            ("Şikâyetlerin konusu",
             "59 çalışmada 88.069 şikâyeti birleştiren sistematik derlemede şikâyet konularının %33,7’si klinik bakımın güvenliği ve "
             "kalitesiyle, %35,1’i kurumun yönetimiyle, %29,1’i sağlık çalışanı ile hasta arasındaki ilişkiyle ilgiliydi "
             "([@reader2014]). Kitabın vurguladığı iletişim sorunları şikâyetlerin önemli bir kaynağıdır; ama şikâyetlerin üçte biri "
             "doğrudan klinik bakımla ilgilidir ve görmezden gelinmemelidir."),
            ("Bir hastanın intiharı hekimi nasıl etkiler?",
             "İskoçya’da yanıt veren 247 konsültan psikiyatristin %68’i bakımı altındaki bir hastayı intihar nedeniyle kaybetmişti. "
             "Bunların üçte biri çökkün duygudurum, uyku sorunu ya da çabuk öfkelenme gibi kişisel etkiler, %42’si uygulamasında "
             "değişiklik (ör. riskli hastalarda daha yapılandırılmış yaklaşım, yasal yetkilerin daha sık kullanımı) bildirmiş, %15’i "
             "bu nedenle erken emekliliği düşünmüştü ([@alexander2000]). En yararlı destek meslektaşlardan, aileden ve ekip ya da olay "
             "incelemelerinden gelmişti. Kitabın kullanılabilirlik ve aşırı savunmacılık uyarısı bu verilerle uyumludur."),
            ("Otizm ölçekleri yalnızca otizmi mi ölçer?",
             "2-13 yaşlarında 388 çocukta SRS, ADI-R ve ADOS’un ayırt ediciliği zekâ düzeyinden ve duygusal-davranışsal sorunlardan "
             "etkilenmiştir. Otizmi olmayan zihinsel yetersizlikli çocuklarda SRS ve ADI-R kesme puanlarının özgüllüğü %27-42’ye, "
             "duygusal ve davranışsal sorunları belirgin çocuklarda üç ölçeğin özgüllüğü %36-59’a düşmüştür ([@havdahl2016]). "
             "Kitaptaki hata listesiyle örtüşen bu bulguya göre ölçek puanı, çocuğun bilişsel düzeyi ve o günkü duygusal durumuyla "
             "birlikte yorumlanmalıdır."),
            ("Riskin algısı",
             "Kullanılabilirlik, temsil edicilik ve çıpalama sezgileri belirsizlik altında hızlı ve çoğu zaman işe yarayan yargılar "
             "sağlar, ama sistemli ve öngörülebilir hatalara da yol açar ([@tversky1974]). Klinik risk kararlarında bu yanlılığı "
             "azaltmanın pratik bir yolu, tek bir çarpıcı anıyla verilen kararı taban oranlarla ve ekip görüşüyle sınamaktır."),
        ],
        sorular=[
            S("Otizmi olan 7 yaşındaki bir çocuk son iki haftadır öfkelendiğinde başını pencere camına vuruyor. Anne ve baba çok kaygılı "
              "ve görüşmede bir davranış planını konuşabilecek durumda değiller. İlk adım olarak en uygunu hangisidir?",
              ["İşlevsel analiz için iki hafta boyunca ayrıntılı kayıt tutmalarını istemek",
               "Camı korumaya almak ve çocuğun bu dönemde güvende kalmasını sağlayacak düzenlemeleri hemen yapmak; aile sakinleştikten "
               "sonra davranış planını birlikte hazırlamak",
               "Davranışı tamamen görmezden gelmelerini söylemek",
               "Ailenin kaygısının abartılı olduğunu söyleyip güvence vermek"],
              1, "Acil bir tehlike yetişkinlerde sistemli düşünmeyi engelleyen bir kaygı yaratır. Önce tehlike denetim altına alınır; "
                 "ardından aile daha sakin bir zihinle plana katılabilir. Bu aşamada görmezden gelme önerisi uygulanamaz, güvence vermek "
                 "de tehlikeyi ortadan kaldırmaz."),
            S("İki yıl önce bir hastasını intihar nedeniyle kaybeden bir meslektaşınız, o günden beri hafif depresyonu olan bütün "
              "ergenleri acil yatışa yönlendiriyor ve kanıta dayalı tedavileri başlatmaktan kaçınıyor. Bu tutumu en iyi açıklayan "
              "hangisidir?",
              ["Riskin doğru ve güncel bir değerlendirmesi",
               "Çarpıcı bir kişisel deneyimin riski olduğundan büyük göstermesi (kullanılabilirlik yanılgısı) ve buna bağlı aşırı "
               "savunmacı bir tutum",
               "Ahlaki tehlike",
               "Ergenlerde intihar riskinin erişkinlere göre daha yüksek olması"],
              1, "Kişisel ve çarpıcı olaylar akla kolay gelir ve riski olduğundan sık gösterir; sonuç gereksiz yatışlar ve geciken "
                 "tedavilerdir. Klinisyenin sorumluluğu kabul görmüş yöntemleri özenle uygulamaktır. Meslektaşın desteklenmesi ve "
                 "vakaların ekipte konuşulması bu dengeyi yeniden kurmaya yardım eder."),
            S("Kendine ağır zarar veren, zihinsel yetersizliği olan 15 yaşındaki bir ergende iki ilaç yetersiz kalmış. Kılavuzlarda "
              "açıkça yer almayan bir ilaç birleşimini düşünüyorsunuz. Kararınızı savunulabilir kılmak için en uygun yol hangisidir?",
              ["“Bunu yapan birkaç meslektaşım var” diyerek başlamak",
               "Kılavuz dışı olduğu için hiçbir koşulda denememek",
               "Yayımlanmış kanıtı ve saygın merkezlerdeki uygulamayı araştırmak, deneyimli bir meslektaşa danışmak, gerekçeyi, aileyle "
               "konuşulan riskleri ve izlem planını kayda geçirmek",
               "Aileyi kaygılandırmamak için ayrıntı vermeden başlamak"],
              2, "Bir kararı savunmanın yolları kılavuz, meslektaşların kabul gören uygulaması ve uzmanlıktır; dayanılan görüş mantıksal "
                 "sınamaya da dayanmalıdır. Birkaç meslektaşın aynı şeyi yapması tek başına yetmez. Kılavuz dışı her seçeneği "
                 "yasaklamak olağandışı vakada yeniliği engeller; aileyi bilgilendirmeden başlamak ise hem etik hem hukuki açıdan "
                 "kabul edilemez."),
        ],
        akilda="Önce tehlikeyi durdurun, sonra düşünün; ara düzeydeki kaygıyı bir meslektaşa danışma işareti sayın.",
    ),
    # ------------------------------------------------------------------ 21
    dict(
        no=21, kesim="G", kisa="Risk politikaları",
        baslik="Risk politikaları: özür, güvenlik ağları ve kontrol listelerinin bedeli",
        kitapta_bolumler="G. This Shouldn’t Happen! · Risk Policies (s. 279–287)",
        slogan="Hata olduğunda sıra değişmez: özür dileyin, düzeltin, sonra sistemi değiştirin.",
        kitapta=("Bölüm önce bir şey ters gittiğinde ne yapılacağını anlatır: özür dilemek, sorunu hemen düzeltmek, yinelenmesini "
                 "önleyecek bir düzenek kurmak ve ciddi olayları geri görüş ve sonuç yanlılığına düşmeden incelemek. Ardından bireysel "
                 "klinisyen için risk azaltma yollarını ele alır: önlem hiyerarşisi, güvenlik ağları, akıllı yedeklilik ve İsviçre "
                 "peyniri modeli, küçük olaylar ve kırmızı bayraklar, kişisel olay günlüğü, kısa ve uzun vadeli etkilerin tartılması, "
                 "savunmacı hekimliğin ölçüsü ve hataları önleme sezgileri. Son kısım kurum ve toplum düzeyine geçer: toplumun koyduğu "
                 "risk kuralları, klinik yönetişim, riskin aşağıya devredilmesi, riskin ekipte paylaşılması, risk değerlendirme "
                 "sistemlerine ve kontrol listelerine yöneltilen eleştiriler ve iyileştirmelerin ters tepebilmesi."),
        okurken=[
            "Son hatanızda ilk tepkiniz ne oldu: açıklamak mı, savunmak mı, susmak mı?",
            "Ekibinizin güvenlik ağları birbirinden bağımsız mı, yoksa hepsi aynı zayıflığı mı paylaşıyor?",
            "Son doldurduğunuz risk formu çocuk hakkındaki düşüncenizi derinleştirdi mi, yoksa dikkatinizi forma mı çekti?",
        ],
        fikirler=[
            ("Özür ve düzeltme",
             "Bir şey ters gittiğinde özür dileyin. Özür insanlığı ve üzüntüyü ifade eder; suçun kabulü sayılmaz. Kaçamak yanıtlar, "
             "olanı açıklamamak ve hatayı kabul etmemek aileleri davaya iter. Ne olduğunu açıkça anlatmak ise sorunun büyümesini "
             "çoğu zaman önler. Davaya giden yol genellikle kötü bir ilişki, yanıtsız kalan telefonlar ve bir hatayla başlar; eksik "
             "kayıtlar ve savunulamayan bir uygulamayla kaybedilir. Önce eldeki sorun düzeltilir: yanlış doz yazıldıysa, önemli bir "
             "tanı ya da ilaç etkileşimi atlandıysa aile hemen aranır, denetim adımları eklenir ve özür dilenir. Ardından yinelenmesini "
             "önleyecek, mümkünse başka klinisyenleri de koruyacak bir düzenek aranır."),
            ("Olayı incelemek",
             "Klinik hataların çoğunda tek bir sorumlu yoktur; hatayı çoğu zaman kurumun yapısı kaçınılmaz kılar. Geri görüş ve sonuç "
             "yanlılığı, bir kararı verildiği andaki makul inançları bir yana bırakıp sonucunun iyi ya da kötü olmasına göre "
             "değerlendirmemize yol açar. Ciddi olaylara kendiliğinden verdiğimiz tepki genellikle aşırıdır: aynı olayın yinelenme "
             "olasılığını abartır, birilerini suçlar ve küçük sorunlara pahalı çözümler öneririz. Kararlarının geri görüşle "
             "inceleneceğini bilen klinisyenler bürokratik çözümlere ve aşırı riskten kaçınmaya yönelir. Bu düzenekler bazen hastadan "
             "çok hekimi ve kurumu korur."),
            ("Önlem hiyerarşisi",
             "Risk azaltma yöntemleri etkiye göre sıralanır ve sisteme yönelik olanlar en etkilidir. Ortadan kaldırma: bıçakları ve "
             "ilaçları kilit altında tutmak, askı noktalarını gidermek, çocuğu istismarcı ebeveynden ayırmak. Yerine koyma: daha "
             "güvenli ilaçlar, standart reçeteler. Mühendislik: haftalık ilaç kutuları, basılı reçeteler, sekreterlik denetimleri. "
             "İdari önlemler: kontrol listeleri, her noktanın düşünüldüğünü denetleyen formlar, hatırlatıcılar. Davranış: eğitim ve "
             "riskleri akılda tutan canlı öyküler. Koruyucu donanım: alarm düğmesi, cam bölme, priz kapakları. Eğitim ve uyarılar "
             "sıralamanın alt basamaklarındadır."),
            ("Güvenlik ağları, akıllı yedeklilik ve İsviçre peyniri",
             "Çoğu plana bir güvenlik ağı eklenebilir: ana plan aksarsa devreye giren bir yedek. Aileye bir yan etki ortaya çıkarsa ne "
             "yapacağını söylemek, kendine zarar verme sonrasında izlem randevusu vermek, acil bir randevu verilse bile iptal "
             "edilebilecek ileri tarihli bir kontrol randevusu planlamak buna örnektir. Bir işi iki kez yapmak çoğu zaman israftır, "
             "ama iki farklı yolla yapmak riski azaltır. Geçen yılın beş öğretmenine ulaşmak verimsizdir; çocuktan, iki ebeveynden ve "
             "bir kardeşten ya da yakın bir akrabadan bilgi almak daha iyidir. İsviçre peyniri modelinde her güvenlik katmanının "
             "delikleri vardır; kaza, delikler nadiren aynı hizaya geldiğinde olur ve çoğu zaman tek bir suçlusu yoktur. Personel "
             "eksikliği yüzünden vakalar uzmanlık alanı dışındaki kişilere verildiğinde ise yanlış tedavi riski, kişilerin özeninden "
             "bağımsız olarak sistemli biçimde yükselir."),
            ("Küçük olaylar, kırmızı bayraklar ve olay günlüğü",
             "Küçük kötü olaylar düşük maliyetli birer öğrenme penceresidir ve aşırı özgüveni önler: çocuğun okuldan eve gönderilmesi, "
             "ailenin başka bir uzmana başvurması, sözlü yakınmalar, ramak kala olaylar, geri bildirim formlarındaki yorumlar, tedavi "
             "başarısızlığı, yatışlar, yan etkiler, mektuptaki yazım hataları. Kişisel kırmızı bayraklar arasında aileye, "
             "sekreterlere ya da hastalara karşı sabırsızlaşmak, meslektaşlardan uzun çalışmak, biriken yazışmalar, işe gitmekte "
             "zorlanmak ve yalnızca hafta sonlarını beklemek vardır. Ekipte büyüyen bekleme listesi, neşesini yitiren bir meslektaş, "
             "artan izinler ve istifalar uyarıdır. Ramak kala olayların çoğu korku, zaman darlığı ya da önceki bildirimlerin sonuçsuz "
             "kalması yüzünden hiç bildirilmez. Yıllar boyunca tutulan kişisel bir olay günlüğü (tarih, katkıda bulunan etkenler, "
             "alınan önlem, sonuç) örüntüleri görünür kılar; hata sayısı artıyorsa nedeni reçete düzeninde, yorgunlukta ya da "
             "ana akımdan uzaklaşmış bir çalışma tarzında aranır."),
            ("Kısa ve uzun vade, savunmacı hekimlik",
             "Bir ilacın kısa ve uzun vadeli yararları ve riskleri ayrı ayrı tartılır. Kitaba göre stimülanların kısa vadeli yararı "
             "büyük, uzun vadeli riskleri şimdilik çok küçük görünür. Antipsikotiklerin kısa vadeli yararı büyük olabilir, ama obezite "
             "ve diyabet gibi uzun vadeli riskleri vardır; ailede güçlü diyabet öyküsü varsa süreyi baştan sınırlamak akılcıdır. "
             "Savunmacı hekimlik riski özenle yönetmektir, ama ölçüsü kaçabilir. Aşırısı: daha önce yapmadığı hiçbir şeyi yapmamak, "
             "ailenin istediği her şeyi ya da gösterdiği her protokolü uygulamak. Tartışmalı olanı: aile istediği için çok sayıda "
             "tetkik istemek, uzak gelecekteki riskler yüzünden yararlı bir tedaviden kaçınmak. Akılcı olanı: yapılanları kaydetmek, "
             "yeni ilaçlarda “düşük başla, yavaş artır”, öfkeli ailelerle ilişkiyi onarmak için çaba göstermek ve rahat olunmayan "
             "alanlarda danışmak."),
            ("Kurumda risk",
             "Bazı riskler için toplum, profesyonellerden ne beklediğine önceden karar vermiştir. Bu kurallar ilk ilkelerden "
             "çıkarılamaz; öğrenilip uygulanır: morluk bırakan bir vurmayı sosyal hizmetlere bildirmek, kişisel veri taşıyan "
             "bellekleri şifrelemek, kontrole tabi ilaçlarda özel kurallara uymak, çocuk birimlerini kilitli ve izlenir tutmak, kalp "
             "öyküsü varsa kalbi etkileyen bir ilaçta QTc’ye bakmak. Hükümetler riski düzenleyicilere ve yöneticilere, onlar da "
             "klinisyenlere devreder; klinisyen de yetersiz koşulları yöneticilere yazılı bildirerek riskin bir kısmını geri "
             "taşıyabilir. Kılavuzlar riski yazarları ve önceki kullanıcılarıyla paylaştırır; büyük ve nadir riskler onlarla her gün "
             "karşılaşan uzmanlara bırakılır. Kitaba göre gruplar, üyelerinin tek başına alacağından daha riskli kararlar alabilir. "
             "İkili çalışma karar sorumluluğunu paylaşmaya yarar; değerlendirmede ve tedavide yararı daha az açıktır. Tek başına "
             "değerlendirip planı bir kıdemliyle tartışmak hem uyum kurmayı kolaylaştırır hem daha çok öğretir."),
            ("Risk değerlendirme sistemlerine kuşku",
             "Bazı yöneticiler ve kurumlar risk yönetimini psikiyatrinin özü sayar. Pek çok klinisyen ise risk değerlendirmesine "
             "fazla ağırlık verildiğini ve bunun hastanın bütününe bakmayı engellediğini düşünür. Kendine zarar verme sonrasında risk "
             "ölçekleri, klinisyenin genel yargısından daha iyi öngörü sağlamamıştır; NICE de risk araçlarının ileride intiharı ya da "
             "kendine zarar vermeyi öngörmek için kullanılmamasını önerir. Riski sayıya dökmek yerine standart klinik görüşmeyle "
             "ihtiyaçları değerlendirmek daha yararlıdır. Kontrol listeleri en güvenilmez klinisyenleri daha güvenli kılar, ama "
             "zaten güvenilir olanı daha az düşünen ve daha az iş birliği yapan birine dönüştürebilir. Toplanması kolay veri "
             "toplanır; bilinmeyen riskleri yönetme yükü, raporlanabilir bir işle yer değiştirir. İnsanlar başka alanlarda daha çok "
             "risk alarak toplam riski eski düzeyine getirebilir. Formu doldurduktan sonra düşünce çocuktan forma kayar. Dışarıdan "
             "dayatılan risk standartlarının bir terapötik toplulukta hastalar ile personel arasındaki güveni aşındırdığı da "
             "bildirilmiştir."),
        ],
        crs=[
            "Bir hata fark ettiğinizde aileyi hemen arayın: ne olduğunu açıkça anlatın, özür dileyin, şimdi ne yapılacağını ve "
            "yinelenmemesi için neyi değiştirdiğinizi söyleyin; konuşmayı kayda geçirin ([@kachalia2010]).",
            "Güvenlik ağını yazılı kurun. Yan etki anlatırken “Şu olursa ilacı kesin ve şu numarayı arayın” deyin; kendine zarar "
            "verme sonrasında erken bir randevu verseniz bile iptal edilebilecek ileri tarihli bir yedek kontrol randevusu planlayın.",
            "Reçetelerinizin ne kadarının eczaneden sorgulandığını izleyin; %1-5’ten fazlası sorgulanıyorsa kayıtlarınızın genelinde "
            "de bir güvenilirlik sorunu arayın. Dozları hem mektupta hem reçetede, sonraki randevuyu hem takvimde hem son mektupta "
            "yazın; bir kayıt kaybolursa öbüründen yeniden kurulabilir.",
            "Kendinize özel bir istenmeyen olay günlüğü tutun (tarih, olay, katkıda bulunan etkenler, alınan önlem, sonuç) ve yılda "
            "bir örüntülere bakın.",
            "Ayda bir ekipçe sorun: “İyi bakım vermemizin önündeki en sık engel ne? Bu çocuk yakınımız olsaydı neyi farklı "
            "yapardık?”",
            "Kendine zarar veren bir ergeni ölçek puanıyla “düşük” ya da “yüksek risk” diye sınıflamayın. İhtiyaçları ve "
            "değiştirilebilir etkenleri görüşmeyle değerlendirin, aileyle bir güvenlik planı yapın ve izlem randevusu verin "
            "([@quinlivan2017]; [@carter2017]).",
            "Uzun vadeli ilaç risklerini izlemde tutun: antipsikotik kullanan çocukta kilo, bel çevresi, kan basıncı, açlık kan şekeri "
            "ve lipitler ([@bobo2013]); stimülan kullanan çocukta her kontrolde kan basıncı ve nabız ([@zhang2024]).",
            "TR Görevi sırasında bir suç belirtisiyle karşılaşan sağlık çalışanının bunu yetkili makamlara bildirme yükümlülüğü vardır "
            "(TCK 280). İstismar kuşkusunda hastanenin sosyal hizmet birimiyle ve gerektiğinde Çocuk İzlem Merkeziyle çalışın; "
            "bildirimin zamanlamasını ve aileye ne söyleneceğini ekipçe planlayın.",
            "TR Sağlık verisi özel nitelikli kişisel veridir (KVKK m. 6). Kişisel Verileri Koruma Kurulunun 2018/10 sayılı kararı, bu "
            "verilerin taşınabilir bellek, CD ya da DVD ile aktarılması gerekiyorsa kriptografik yöntemlerle şifrelenmesini ve "
            "anahtarın ayrı bir ortamda tutulmasını ister.",
            "TR Hastanelerde istenmeyen olaylar ve ramak kala olaylar kurumun olay bildirim sistemine (birçok hastanede Güvenlik "
            "Raporlama Sistemi, GRS) bildirilir. Bildirimlerin öğrenmeye dönüşmesi için ramak kala olayları ekip toplantılarında "
            "isim vermeden konuşun.",
        ],
        tartisma=[
            ("Açıklama ve özür davayı artırır mı?",
             "Michigan Üniversitesi sağlık sisteminde hataları açıkça bildirme ve tazminat önerme programından sonra 100.000 hasta "
             "başvurusu başına aylık yeni talep sayısı 7,03’ten 4,52’ye, dava sayısı 2,13’ten 0,75’e inmiş ve toplam sorumluluk "
             "maliyeti azalmıştır ([@kachalia2010]). Önce-sonra tasarımı nedensellik kanıtlamaz ve aynı dönemde eyalette davalar genel "
             "olarak azalmıştır. Perinatal yaralanma sonrası dava açan ailelerin yaklaşık yarısı hekimlerin kendilerini yanıltmaya "
             "çalıştığını, üçte biri açık konuşmadığını düşünmüştü ([@hickson1992]). İki çalışma kitabın uyarısıyla uyumludur: "
             "iletişimin kopması dava kararında önemli bir etkendir."),
            ("Sonuç yanlılığı",
             "112 anestezi uzmanına aynı vakalar yalnızca sonucun ağırlığı değiştirilerek verildiğinde, sonuç geçiciden kalıcıya "
             "çevrilince bakımı uygun bulanların oranı 31 yüzde puan azalmış, tersine çevrilince 28 yüzde puan artmıştır "
             "([@caplan1991]). Olay incelemelerinde kararı, verildiği andaki bilgiyle yeniden kurmak bu yüzden gereklidir."),
            ("Risk ölçekleri öngörüyor mu?",
             "Kitaptaki şekilde yer alan ölçekleri sınayan çok merkezli bir kohortta, kendine zarar veren erişkinlerde altı ay "
             "içinde yinelemeyi öngörmede ölçeklerin çoğu klinisyenin ya da hastanın kendi risk tahmininden daha iyi değildi ve "
             "bazıları belirgin biçimde daha kötüydü. Eğri altındaki alan en yüksek klinisyenin genel değerlendirmesinde (0,74) "
             "bulundu ([@quinlivan2017]). Pozitif öngörü değerlerini birleştiren meta-analizde bütün ölçekler birlikte "
             "değerlendirildiğinde yüksek risk sınıfının intihar için pozitif öngörü değeri %5,5’ti ve hiçbir yüksek risk "
             "sınıflaması klinik olarak yararlı bulunmadı ([@carter2017]). Kohort erişkinlerden oluşur; ergenlere genellemek bir "
             "çıkarımdır."),
            ("Kontrol listeleri her yerde işe yarar mı?",
             "Dünya Sağlık Örgütü’nün cerrahi güvenlik kontrol listesi sekiz hastanede uygulamaya konduktan sonra ölüm oranı %1,5’ten "
             "%0,8’e, komplikasyonlar %11’den %7’ye inmiştir ([@haynes2009]). Ontario’da bir politikayla bütün hastanelerde kontrol "
             "listesine geçildikten sonra ise 101 hastanede ölüm ve komplikasyonlarda anlamlı bir azalma görülmemiştir "
             "([@urbach2014]). İki sonuç arasındaki fark, kontrol listesinin etkisinin uygulanma biçimine bağlı olabileceğini "
             "düşündürür. Kitabın uyarısıyla uyumlu olarak, dışarıdan dayatılan bir form kendiliğinden güvenlik üretmeyebilir."),
            ("Uzun vadeli ilaç riskleri ne kadar uzak?",
             "Kitap antipsikotiklerin diyabet riskini yıllar sonra ortaya çıkabilecek uzak bir risk örneği olarak verir. Tennessee "
             "Medicaid kohortunda 6-24 yaşlarında antipsikotiğe yeni başlayanlarda tip 2 diyabet riski yaklaşık üç kat artmış, artış "
             "ilk yıl içinde görülmüş ve birikimli dozla yükselmiştir; risperidonla sınırlı kullanımda da risk artmıştır "
             "([@bobo2013]). Stimülanların uzun vadeli riskinin çok küçük olduğu yargısı da yeniden düşünülmelidir: İsveç’te bir "
             "vaka-kontrol çalışmasında DEHB ilacının her ek kullanım yılı kardiyovasküler hastalık riskinde %4’lük bir artışla "
             "ilişkili bulunmuş, artış en çok hipertansiyon ve arter hastalığında görülmüş ve ilk üç yılda belirginleşmiştir "
             "([@zhang2024]). İki çalışma da gözlemseldir ve karıştırıcı etkenler tümüyle dışlanamaz; yine de izlemin uzun vadede "
             "sürmesi gerektiğini gösterir."),
        ],
        sorular=[
            S("Bir ergenin reçetesine yanlışlıkla on kat yüksek doz yazdığınızı ertesi sabah fark ediyorsunuz. En uygun ilk adım "
              "hangisidir?",
              ["Bir sonraki randevuda konuyu açmak",
               "Eczacının zaten fark edeceğini düşünüp beklemek",
               "Aileyi hemen arayıp ilacın alınıp alınmadığını öğrenmek, gerekiyorsa tıbbi değerlendirmeye yönlendirmek, olanı açıkça "
               "anlatıp özür dilemek, olayı kaydetmek ve yinelenmemesi için bir denetim adımı eklemek",
               "Özür suç kabulü sayılacağı için yalnızca düzeltilmiş reçeteyi göndermek"],
              2, "Önce eldeki sorun düzeltilir: aile hemen aranır. Özür dilemek suç kabulü sayılmaz; kaçamak davranmak ise aileleri "
                 "davaya iter. Ardından aynı hatanın yinelenmemesi için bir düzenek kurulur."),
            S("Ergen servisinde bir hastanın kapı menteşesini askı noktası olarak kullanmaya çalışmasından sonra yönetim önlem arıyor. "
              "Önlem hiyerarşisine göre en etkili seçenek hangisidir?",
              ["Personele kendine zarar verme konusunda yeni bir eğitim vermek",
               "Askı noktası olabilecek menteşe ve bağlantıları değiştirmek ya da kaldırmak",
               "Her vardiyada doldurulacak yeni bir risk formu eklemek",
               "Koridorlara kuralları hatırlatan afişler asmak"],
              1, "Tehlikeyi ortadan kaldırmak hiyerarşinin en etkili basamağıdır. Eğitim ve afişler davranışa, formlar idari önlemlere "
                 "dayanır; bunlar alt basamaklardır ve tek başlarına aynı korumayı sağlamaz."),
            S("Acil serviste kendine zarar verme sonrası görülen 15 yaşındaki bir ergen bir risk ölçeğinden düşük puan alıyor. Ekip bu "
              "puana dayanarak izlem randevusu vermeden taburcu etmeyi öneriyor. En uygun yaklaşım hangisidir?",
              ["Ölçek puanına göre izlemsiz taburcu etmek",
               "Ölçeği bir kez daha uygulayıp puan yükselirse izlem vermek",
               "Puandan bağımsız olarak ihtiyaçları, bağlamı ve değiştirilebilir etkenleri görüşmeyle değerlendirmek, aileyle bir "
               "güvenlik planı yapmak ve izlem randevusu vermek",
               "Ölçek puanına bakmadan her ergeni yatırmak"],
              2, "Risk ölçeklerinin öngörü gücü düşüktür ve yüksek ya da düşük risk sınıflamaları klinik kararı taşıyacak kadar "
                 "güvenilir değildir. Görüşmeye dayalı ihtiyaç değerlendirmesi, güvenlik planı ve bir güvenlik ağı olarak izlem "
                 "randevusu daha akılcıdır."),
        ],
        akilda="Formu doldurduktan sonra yeniden çocuğu düşünün; güvenliği en çok tehlikeyi kaldıran düzenlemeler ve dikkatli bir "
               "görüşme sağlar.",
    ),
    # ------------------------------------------------------------------ 22
    dict(
        no=22, kesim="G", kisa="Öngörülemeyeni öngörmek",
        baslik="Öngörülemeyeni öngörmek: küçük hatalar, kara kuğular ve risk pencereleri",
        kitapta_bolumler="G. This Shouldn’t Happen! · Predicting the Unpredictable (s. 288–292)",
        slogan="Büyük felaketler çoğu zaman küçük hatalarla aynı kökten beslenir; küçükleri azaltan büyükleri de azaltır.",
        kitapta=("Bölüm, bir klinisyenin karşılaştığı olayların sıklığı ile ağırlığı arasındaki ilişkiyi güç yasasıyla açıklar: sık "
                 "görülen küçük aksaklıklar nadir ve ağır olayların habercisidir ve çoğu zaman aynı nedenlerden doğar. Asla olmaması "
                 "gereken olayları, çocuk ve ergen ruh sağlığı hizmetlerinde küçük sorunlardan değer çıkarmanın yollarını, hata "
                 "sayısını bilerek artırmayı (yedeklilik) ve hata oranının fazla düşük olmasının ne anlama gelebileceğini tartışır. "
                 "Ardından risk ile belirsizlik arasındaki farkı, kara, gri ve beyaz kuğuları, kötü kara kuğulara karşı konum almayı ve "
                 "iyi kara kuğulara yer açmayı ele alır. Son olarak birikimli riskleri (psikoz için ultra yüksek risk ölçütleriyle "
                 "bilişsel bozulmaların birlikteliği) ve risk pencerelerini (ilaca başlama ya da ilacı kesme, büyük yaşam olayları, "
                 "gebeliğin ilk üç ayı, sınav dönemleri) anlatır."),
        okurken=[
            "Son bir yılda yaşadığınız küçük aksaklıkları sayabilir misiniz? Hangisi daha büyük bir olayın habercisi olabilir?",
            "Ekibinizde hiç şikâyet almayan biri varsa bu her zaman iyi bir işaret midir?",
            "Kliniğinizi bir anda alt üst edebilecek, ama bugüne kadar hiç düşünmediğiniz bir olay ne olabilir?",
        ],
        fikirler=[
            ("Güç yasası",
             "Bir klinisyenin karşılaştığı olaylarda sıklık ile ağırlık ters orantılıdır: hoşnutsuz bir aile hemen her gün görülebilir, "
             "ağır bir olay meslek ömründe belki bir kez. Neredeyse her gün hastaları kızdıran, sık reçete hatası yapan ve yılda "
             "birkaç şikâyet alan bir klinisyenin dava ve hasta ölümü gibi ağır olaylarla karşılaşma olasılığı da yüksektir. "
             "Karmaşık sistemler çoğu zaman küçük sorunların birleşmesiyle çöker ve en büyük sorunlar genellikle küçüklerle aynı "
             "nedenlerden doğar. Bu yüzden küçük hatalar görmezden gelinmez. Annenin yarım tablet mi yarım miligram mı verdiğini "
             "bilmediğini fark ettiğinizde yazılı bir hatırlatıcı verip daha sık kontrol etmek, büyük bir hatanın olasılığını da "
             "azaltır. Bunun duygusal bir yararı da vardır: felaketleri gerçekten azaltan önlemleri aldığınızı bilmek, kendinizi "
             "gereksiz yere hırpalamanızı önler."),
            ("Ailede ve klinikte küçük işaretler",
             "Güç yasası aileler için de geçerlidir. Ağır cezaları yalnızca uç davranışlara saklayan anne-babalar, ara basamaklardaki "
             "küçük ihlalleri fark etmez: genç sorunlu bir arkadaş grubuna kayarken hiçbir şey olmaz, polisle eve geldiğinde ağır bir "
             "ceza gelir. Küçük olaylar için de kullanılabilen sonuçlar büyük krizleri önler. Klinikte de aynı mantık işler: iki "
             "yıldır kimseye ciddi zarar vermediği için antipsikotiği kesilen otizmli bir ergende birkaç ayda bir eşya kırması, "
             "birkaç yıl içinde daha ağır bir olayın habercisi olabilir. Geçmiş olayların gelecekteki riski öngördüğü kuralı "
             "ortalamalar ve eğilimler için geçerlidir; ama asıl önemli olan nadir büyük olayları kaçırır."),
            ("Asla olmaması gerekenler ve küçük sorunlardan öğrenmek",
             "Önceden kestirilebilen, ağır ve önlenebilir olaylara asla olmaması gereken olaylar denir: bilinen alerjisi olan çocuğa "
             "aynı ilacı yazmak ya da yatan bir hastanın kaçırılması gibi. Ciddi intihar niyetinin gözden kaçması ve serviste cinsel "
             "saldırı, önlenmesi biraz daha zor olaylardır. Çocuk ve ergen ruh sağlığı hizmetlerinde büyük felaketler nadir olduğundan, risk denetiminin "
             "çalışır kalması için küçük sorunlardan bütün değeri çıkarmak gerekir. Önce kendi küçük hatalarınızla başlayın ve "
             "danışmayı örnek olarak gösterin; reçete hataları iyi bir uyarı işaretidir. Ardından ön değerlendirmede yapılıp sonradan "
             "yanlış çıkan yorumlara, ekip toplantılarındaki ani yargılara ve yeniden başvurulara bakın."),
            ("Hata oranını bilerek artırmak ya da fazla düşürmek",
             "Bazen küçük hataları artırmak büyükleri azaltır. Uzay mekiğindeki beş özdeş bilgisayar bir bilgisayarın arızalanma "
             "olasılığını artırıyor, ama arızayı atlatılabilir kılıyordu; hastanelerde iki kimlik bileziği takılması da böyledir. "
             "Mektupların, reçetelerin ve notların kopyalarını tutmak birinin kaybını telafi etmeyi sağlar. Bu tür küçük ve "
             "düzeltilebilir hataların sayısını izlemek, aşırı yüklenmenin ya da güvenilirliğin azalmasının erken bir uyarısıdır. "
             "Tersini de sormak gerekir: hata oranınız fazla mı düşük? Hiç şikâyet almayan bir klinisyen hastalara fazla esnek "
             "davranıyor, hiç geç kalmayan biri çok az sorumluluk alıyor, mektuplarında hiç yazım hatası olmayan biri de zamanını "
             "takıntılı denetimlere harcıyor olabilir."),
            ("Risk, belirsizlik ve kara kuğular",
             "Olasılıkları hesaplanabilen risk ile hayatın daha derin bilinemezliği olan belirsizlik farklı şeylerdir: riski "
             "yönetebiliriz, belirsizliği aynı kesinlikle yönetemeyiz. Kara kuğu çok nadir, hiç düşünülmemiş ve etkisi ezici olan "
             "olaydır. İyi kara kuğu beklenmedik büyük bir fırsattır, beyaz kuğu hiçbir şeyin olmamasıdır, gri kuğu ise nadir ama "
             "beklenen, modellenebilen uç olaydır. Taleb’e göre bilmediklerimiz bildiklerimizden daha önemlidir; bu çekici ama "
             "herkesin kabul etmediği bir görüştür. Kara kuğu beklentiye görelidir: kasap için olağan olan, hindi için felakettir. "
             "Çocuk ve ergen ruh sağlığında örnekler: bir skandal yüzünden birimin kapanması, olumlu bir haber yüzünden başvuruların "
             "on katına çıkması, kişisel yaşamda birkaç büyük olayın aynı haftaya denk gelmesi, birkaç hastanın intihar etmesi. Tek "
             "bir hastanın intiharı ise sık düşündüğümüz gerçek bir olasılıktır, kara kuğu sayılmaz."),
            ("Kötü kara kuğulara karşı konum almak",
             "Önce donanın: güncel ve geniş bilgi edinin, hastalarınızla ilgili sorulara hakemli yayınlarda yanıt arama alışkanlığını "
             "sürdürün, dünyada ve yakınınızdaki önemli gelişmeleri (gençlerde intihar, kesintiler, yeniden yapılanma, skandal, yeni "
             "alt kültürler) haber taramasıyla izleyin, kurumsal akıl dışılığın ve sürdürülemezliğin işaretlerine karşı uyanık olun, "
             "ilişki ağınızı geliştirin. İkinci olarak kara kuğulardan kaçının: klinik işte kötü sürprizler iyilerinden çok daha "
             "sıktır, bu yüzden klinikte riskten kaçınmak akılcıdır. Üçüncü olarak gri kuğulara hazırlanın: sakinleştirme "
             "(de-eskalasyon) eğitimleri, ilaçların olağandışı yan etkilerine hazırlık, kendine zarar veren hastalara kendini koruma "
             "stratejileri öğretmek, her risk türünü izleyecek bir ekip üyesi belirlemek ve ayda bir “Burada bir sonraki hata ne "
             "olabilir?” diye sormak. Son olarak öngörülemeyeni öngörmeye çalışın: olağandışı vakalara fazladan dikkat gösterin. "
             "Öyküdeki sürprizler çoğu zaman formülasyonun anahtarıdır; annenin bildirdiği ve sizin olamaz dediğiniz bir yan etki "
             "gerçek olabilir."),
            ("İyi kara kuğulara yer açmak",
             "Maaşlı çalışmak olağanüstü başarı olasılığını büyük ölçüde sınırlar; daha çok hasta görme baskısı da klinik bir felaket "
             "riskini artırırken iyi sürprizlere yer bırakmaz. Yine de iyi sürprizler gelir. Şaşırtıcı klinik gözlemler kaydedilmeli, "
             "tartışılmalı ve araştırılmalıdır, çünkü sürprizler klinik düşünceyi en çok kışkırtan şeydir. Meta-analizlerdeki uç "
             "değerler yayımlanan sonuçlardan daha ilginç olabilir. Tedavileri rastgele denemek kabul edilemez; ama sürprizlerin "
             "olumlu olabileceği alanlarda (ders vermek, araştırma, yazı, medya) belirsizliğe yer açılabilir. Kısmi çalışma ya da "
             "serbestçe kullanılabilecek zaman, fırsatları yakalamayı kolaylaştırır. Neredeyse her zaman kazanılan bir işte riskten "
             "fazla kaçınmaya kayarız; bu tutum hayatın her alanına yayılmamalıdır."),
            ("Birikimli riskler ve risk pencereleri",
             "Ailelere aktarmak üzere risk ve gidişe ilişkin güvenilir bilgileri bilmek gerekir. Kitabın örneğinde genç erişkinlerde "
             "psikoza geçiş riski, ultra yüksek risk ölçütleriyle bilişsel bozulmalar birlikte bulunduğunda belirgin biçimde yükselir; "
             "ikisi birlikte olanların yaklaşık üçte ikisi dört yıl içinde psikoz geliştirmiştir. Risk sabit de değildir. Yeni bir "
             "ilaca başlarken ya da ilacı keserken, okula başlama ya da bir ebeveynin cezaevinden çıkması gibi büyük yaşam olaylarının "
             "öncesinde, sırasında ve sonrasında, gebeliğin ilk üç ayında (malformasyon riski) ve sınav dönemlerinde (kaygı ve kendine "
             "zarar verme) risk penceresi açılır. Bunların bir kısmı önceden planlanabilir."),
        ],
        crs=[
            "Ebeveynin dozdan emin olmadığını fark ettiğinizde (yarım tablet mi, yarım miligram mı?) dozu tablet sayısıyla ve yazılı "
            "olarak verin; bir sonraki görüşmede yeniden sorun.",
            "Ekip toplantısındaki ilk izlenimleri (ör. “Bu bir aile sorunu”, “Bu DEHB”) kısa bir notla kaydedin; değerlendirme ve "
            "tedaviden sonra hangilerinin doğru çıktığına dönemsel olarak bakın.",
            "Yeniden başvuran her çocukta sorun: Tedaviye katılım mı yetersizdi, tedavi mi işe yaramadı, yoksa taburculuk mu erkendi?",
            "Antipsikotiği kesilen bir ergende küçük saldırgan davranışları (eşya kırma, itme) aile ve okulla birlikte izleyin; "
            "sıklıktaki bir artışı tedaviyi yeniden değerlendirme işareti sayın.",
            "Ebeveynlere küçük ihlaller için de orantılı ve tutarlı sonuçlar önerin; ağır cezaları yalnızca büyük olaylara saklamak "
            "gidişi fark etmeyi geciktirir.",
            "Ekipte her risk türü için (ilaç güvenliği, kendine zarar verme, çocuk koruma, veri güvenliği) bir izleyici belirleyin ve "
            "ayda bir “Burada bir sonraki hata ne olabilir?” diye sorun.",
            "Ailenin bildirdiği beklenmedik bir yan etkiyi hemen reddetmeyin: ayrıntısıyla kaydedin, zamanlamasını ve başka "
            "açıklamaları sorun, literatürü tarayın ve gerekirse dozu azaltıp etkisine bakın.",
            "Risk pencerelerini takvime yazın: yeni ilaca başlama ve ilacı kesme, okul değişikliği, sınav dönemi, aile içi büyük "
            "değişiklikler. Antidepresan başlanan ergeni ilk haftalarda daha sık görün ve aileyle uyarı işaretlerini yazılı olarak "
            "konuşun ([@hammad2006]; [@bridge2007]).",
            "Psikiyatrik yatıştan taburcu olan bir gencin ilk ayaktan randevusunu taburculuktan önce ve ilk yedi gün içine verin "
            "([@fontanella2020]).",
            "TR LGS ve YKS dönemleri, kitabın sözünü ettiği sınav pencerelerinin Türkiye’deki karşılığıdır. Kendine zarar verme öyküsü "
            "olan gençlerde sınav öncesinde ve sonuç döneminde izlemi sıklaştırın, güvenlik planını güncelleyin ([@rodway2016]).",
            "TR Beklenmedik ya da ciddi bir yan etkiyi Türkiye Farmakovijilans Merkezine (TÜFAM) bildirin; nadir yan etkiler ancak "
            "bildirimler biriktikçe görünür hâle gelir.",
        ],
        tartisma=[
            ("Şikâyetler büyük olayları öngörüyor mu?",
             "645 hekimin altı yılı aşkın verilerinde, kendiliğinden gelen hasta şikâyetlerinin sayısı klinik iş yükü hesaba "
             "katıldığında da risk yönetimi dosyaları ve davalarla ilişkili bulunmuştur ([@hickson2002]). Avustralya’da 11 yılda "
             "hekimlere yönelik 18.907 resmî şikâyetin %49’u hekimlerin %3’üne aitti ve yeni şikâyet riski önceki şikâyet sayısıyla "
             "doz-yanıt ilişkisi gösteriyordu ([@bismark2013]). Bu bulgular güç yasasının klinisyen düzeyindeki öngörüsüyle "
             "uyumludur. Yine de her şikâyet kötü bakımı göstermez; şikâyetlerin önemli bir kısmı iletişim ve yönetimle ilgilidir "
             "([@reader2014])."),
            ("Psikoz riskinde gerçekçi oranlar",
             "Kitaptaki şekil, iki ölçüt kümesi birlikte bulunduğunda psikoza geçiş oranının çok yükseldiğini gösterir. 130 çalışmayı "
             "ve 9222 kişiyi kapsayan güncel bir meta-analizde klinik yüksek risk altındaki bireylerin %15’i bir yılda, %25’i üç "
             "yılda psikoz geliştirmiş ve risk dördüncü yıla kadar artmayı sürdürmüştür; çalışmalar arasındaki farklılık çok "
             "büyüktür ([@salazar2021]). Meta-analizdeki bireylerin yaş ortalaması 20’dir; daha küçük yaşlara genellerken dikkatli "
             "olmak gerekir. Aileye risk anlatılırken ortalama ile belirsizlik birlikte verilmelidir."),
            ("İlaca başlama penceresi",
             "ABD Gıda ve İlaç Dairesi’nin 24 randomize çalışmayı (4582 hasta) kapsayan analizinde antidepresan kullanan çocuk ve "
             "ergenlerde intihar düşüncesi ve davranışı riski plaseboya göre yaklaşık iki kat (risk oranı 1,95), mutlak fark yaklaşık "
             "%2 bulunmuş; hiçbir çalışmada tamamlanmış intihar görülmemiştir ([@hammad2006]). 27 çalışmanın meta-analizinde ise "
             "tedaviye yanıt için tedavi edilmesi gereken hasta sayısı majör depresyonda 10, OKB dışı kaygı bozukluklarında 3 iken, "
             "bir hastada intihar düşüncesi ya da girişimi görülmesi için gereken sayı 143’tür ([@bridge2007]). Pencere gerçektir; "
             "yanıtı başlangıçta daha sık izlem ve aileyle konuşulmuş uyarı işaretleridir."),
            ("Taburculuk sonrası pencere",
             "ABD’de 33 eyalette psikiyatrik yatıştan taburcu olan 10-18 yaşlarındaki 139.694 gencin %56,5’i ilk yedi gün içinde "
             "ayaktan ruh sağlığı izlemine gelmiş; bu gençlerde taburculuktan sonraki 8-180 gün içinde intihar riski yarıdan fazla "
             "düşük bulunmuştur ([@fontanella2020]). Çalışma gözlemseldir, ama erken izlem randevusunu en somut güvenlik ağlarından "
             "biri olarak destekler."),
            ("Sınav dönemi ve gençlerde intihar",
             "İngiltere’de 20 yaşından küçük 145 gencin intiharını inceleyen ulusal vaka serisinde, bilgisine ulaşılan 130 gencin "
             "%27’sinde akademik baskı, özellikle sınavlar, öncül etkenler arasındaydı. Gençlerin %43’ünün sağlık, sosyal hizmet ya "
             "da adalet kurumlarıyla bilinen bir teması yoktu ([@rodway2016]). Sınav dönemi bir risk penceresidir; okul ve birinci "
             "basamak da bu pencerenin planlamasına katılmalıdır."),
        ],
        sorular=[
            S("Bir meslektaşınızın son altı ayda üç reçetesi doz hatası nedeniyle eczaneden geri dönmüş, iki aile randevu "
              "karışıklığından yakınmış ve mektupları sık sık gecikiyor. Ciddi bir olay yaşanmamış. En uygun yorum hangisidir?",
              ["Ciddi bir olay olmadığına göre önlem gerekmez",
               "Bu küçük aksaklıklar büyük olaylarla aynı nedenlerden beslenebilir; iş yükü, reçete düzeni ve yorgunluk birlikte "
               "gözden geçirilmelidir",
               "Eczacılar gereğinden titiz davranıyor",
               "Ailelere daha nazik davranması yeterlidir"],
              1, "Güç yasasına göre sık görülen küçük hatalar nadir ve ağır olayların habercisidir ve çoğu zaman aynı nedenlerden doğar. "
                 "Küçükleri azaltan önlemler büyük bir olayın olasılığını da azaltır."),
            S("Ekibinizdeki bir uzman yıllardır hiç şikâyet almamış; bütün mektuplarını üç kez okuyor ve ailelerin her isteğini kabul "
              "ediyor. Bekleme listesi ise ekipteki en uzun liste. En uygun yorum hangisidir?",
              ["En güvenli uzman odur; herkes onu örnek almalıdır",
               "Hata oranının bu kadar düşük olması aşırı esnekliğin ve aşırı denetimin bedelini gizliyor olabilir; zaman kullanımı ve "
               "sınırlar konuşulmalıdır",
               "Şikâyet almadığına göre iş yükü artırılmalıdır",
               "Mektuplarını başka birinin denetlemesi gerekir"],
              1, "Hata oranının fazla düşük olması da bir işarettir: hiç şikâyet almamak aşırı esneklikten, hiç yazım hatası yapmamak "
                 "takıntılı denetimden kaynaklanabilir. Bunun bedelini çoğu zaman bekleyen başka çocuklar öder."),
            S("Kendine zarar verme öyküsü olan 16 yaşındaki bir ergende, YKS’ye üç ay kala orta düzeyde depresyon için antidepresan "
              "başlıyorsunuz. Aşağıdakilerden hangisi en uygundur?",
              ["Rutin olarak üç ay sonra kontrole çağırmak",
               "İlk haftalarda ve sınav döneminde izlemi sıklaştırmak, aileyle uyarı işaretlerini ve ne yapacaklarını yazılı olarak "
               "konuşmak, güvenlik planını güncellemek",
               "Risk penceresi olduğu için ilacı başlamaktan vazgeçmek",
               "Sınava girmemesini önermek"],
              1, "İlaca başlama ve sınav dönemi üst üste binen iki risk penceresidir. Bunun yanıtı izlemi sıklaştırmak ve aileyle bir "
                 "güvenlik ağı kurmaktır; meta-analizlerde antidepresanların yararı riskinden belirgin biçimde büyük bulunmuştur."),
        ],
        akilda="Küçük hataları sayın, büyükleri azaltın; olağandışı vakaya olağandışı dikkat gösterin.",
    ),
]

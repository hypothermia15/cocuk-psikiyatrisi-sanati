# -*- coding: utf-8 -*-
"""Çocuk Psikiyatrisinin Sanatı · Okuma Rehberi: Kasım 2026'da eklenen oturumlar (E kesiminin son bölümü ve F kesimi).

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
]

# -*- coding: utf-8 -*-
"""Çocuk Psikiyatrisinin Sanatı · Okuma Rehberi: dallanan vaka simülasyonları.

Her senaryo bir sahneler grafiğidir. Karar sahnesi: {"metin", "secenekler": [(seçenek, sonraki sahne, puan, geri bildirim)]}.
Son sahnesi: {"son": "iyi" | "orta" | "kotu", "baslik", "metin"}.
Puan: 2 en uygun, 1 kabul edilebilir, 0 zayıf, -1 zarar verebilir.
Bütün vakalar kurgusaldır; kitabın vakalarından alınmamıştır. Atıflar ([@anahtar]) biçimindedir ve kaynaklar.json'da olmalıdır.
"""

PUAN_ETIKET = {2: "En uygun", 1: "Kabul edilebilir", 0: "Zayıf", -1: "Zarar verebilir"}

SIMULASYONLAR = [
    # ------------------------------------------------------------------ 1
    dict(
        id="ela",
        baslik="Ela, 15 yaş: “Bir şeyim yok”",
        ozet="Okul rehber öğretmeninin yönlendirmesiyle annesiyle gelen, konuşmak istemeyen bir ergen. Görüşmeyi yapılandırmak, "
             "gizliliğin sınırları, ölüm düşüncesini doğrudan sormak ve aileyle güvenlik planı.",
        oturumlar=[2, 3, 5],
        baslangic="giris",
        sahneler={
            "giris": dict(
                metin="Ela 15 yaşında. Okul rehber öğretmeni, son iki ayda notlarının düştüğünü ve teneffüslerde yalnız kaldığını fark "
                      "edip aileyi aramış. Ela odaya kapüşonu başında giriyor, annesinin yanına oturup telefonuna bakıyor. Annesi hemen "
                      "söze giriyor: “Bize de hiç konuşmuyor. Siz bir şey söyleyin, belki size anlatır.”",
                secenekler=[
                    ("Kendinizi ikisine de tanıtıp görüşmenin nasıl ilerleyeceğini anlatmak: önce birlikte, sonra ayrı ayrı. Gizliliğin "
                     "sınırını da baştan söylemek: “Konuştuklarımız aramızda kalır. Yalnızca senin ya da bir başkasının güvenliği söz "
                     "konusu olursa bunu birlikte paylaşırız.”", "yalniz", 2,
                     "Görüşmenin nasıl ilerleyeceğini bilmek ergenin kaygısını azaltır. Gizliliğin sınırını en başta söylemek, ileride "
                     "bir bilgiyi paylaşmanız gerektiğinde güveni korur."),
                    ("Ela’ya dönüp “Neden konuşmuyorsun?” diye sormak", "gergin", 0,
                     "“Neden” soruları ergeni susmasını savunmaya iter. Gönülsüz gelen bir ergende önce görüşmenin çerçevesini kurmak "
                     "daha iyi işler."),
                    ("Önce anneyle konuşup Ela’yı görüşmenin sonuna bırakmak", "yalniz", 1,
                     "Annenin anlattıkları değerlidir; ama Ela kendisi hakkında, kendisi yokmuş gibi konuşulan biri olur. Kısa bir ortak "
                     "giriş ve ardından ayrı görüşme bu riski azaltır."),
                    ("Ela’dan telefonu bırakmasını istemek", "gergin", 0,
                     "İlk dakikada başlayan bir güç savaşını çoğu zaman klinisyen kaybeder. Telefon, ergenin kendini güvende hissettiği "
                     "bir dayanak da olabilir."),
                ]),
            "gergin": dict(
                metin="Ela omuz silkiyor: “Konuşacak bir şey yok.” Annesi gözlerini deviriyor: “Görüyor musunuz, evde de böyle.” "
                      "Odadaki gerginlik artıyor.",
                secenekler=[
                    ("Ortamı değiştirmek: annesine bir süre dışarıda beklemesini önerip Ela’ya “Seninle biraz yalnız konuşalım. Neyi "
                     "anlatıp neyi anlatmayacağına sen karar verirsin” demek", "yalniz", 2,
                     "Kontrolün bir kısmını ergene bırakmak, iş birliğinin en kısa yoludur. Ortamı değiştirmek, kurulmakta olan kısır "
                     "döngüyü de kırar."),
                    ("Ela’ya, annesinin ne kadar endişeli olduğunu ve onun için buraya geldiklerini anlatmak", "yalniz", 0,
                     "Ergen bunu annenin tarafını tutmak olarak duyar. Klinisyen ailenin elçisi gibi görünürse ergen susmayı sürdürür."),
                    ("Görüşmeyi bugün kısa tutup başka bir güne randevu vermek", "son-erken", -1,
                     "Gerginlik görüşmeyi bitirmek için bir gerekçe değildir. Okulun fark ettiği değişiklikler bugün konuşulması gereken "
                     "bir risk de taşıyabilir."),
                ]),
            "yalniz": dict(
                metin="Annesi dışarı çıktı. Ela bir süre susuyor, sonra telefonunu bırakmadan konuşuyor: “Annem abartıyor. Bir şeyim "
                      "yok. Sadece canım sıkılıyor.”",
                secenekler=[
                    ("Sessizliğe izin verip duyguyu kabul etmek ve daha az tehdit edici bir yerden açmak: “Buraya gelmeyi sen seçmedin, "
                     "sıkılman çok anlaşılır. Okulda günlerin nasıl geçiyor?”", "acilis", 2,
                     "Duyguyu kabul etmek ve tarafsız bir konudan başlamak, açık uçlu konuşmanın kapısını aralar. Kısa sessizliklere "
                     "dayanabilmek de bir beceridir."),
                    ("Uyku, iştah, enerji ve ilgi kaybı için kısa evet-hayır sorularını sırayla sormak", "acilis", 1,
                     "Bilgi toplar; ama ilişki kurulmadan arka arkaya sorulan kapalı sorular tek kelimelik yanıtlar getirir. Aynı "
                     "konular açık uçlu sorularla daha iyi açılır."),
                    ("“Bir şeyin yoksa bugün erken bitirebiliriz” demek", "son-erken", -1,
                     "Ergenin ilk savunması görüşmenin sonu değil, başıdır. Okuldan gelen gözlemler konuşulmadan görüşmeyi bitirmek, "
                     "bir riskin gözden kaçması demektir."),
                ]),
            "acilis": dict(
                metin="Konuşma yavaş yavaş açılıyor. Ela bir arkadaş grubundan dışlandığını, geceleri uyuyamadığını, sabahları okula "
                      "gitmek istemediğini anlatıyor. Sonra sesini alçaltıyor: “Bazen uyusam da hiç uyanmasam diyorum.”",
                secenekler=[
                    ("Sakin ve doğrudan sormak: “Böyle düşündüğünde, kendine zarar vermeyi ya da hayatına son vermeyi düşündüğün "
                     "oluyor mu?”", "risk", 2,
                     "İntiharı açıkça sormak bu düşünceyi artırmaz ([@dazzi2014]). Lise öğrencileriyle yapılan randomize bir çalışmada "
                     "intihar sorularını içeren tarama, ne sıkıntıyı ne de intihar düşüncesini artırmıştır ([@gould2005]). Dolaylı sorular "
                     "dolaylı yanıtlar getirir."),
                    ("“Bu yaşta herkes bazen böyle hisseder, geçer” diye güvence vermek", "son-kacan", -1,
                     "Erken güvence, ergenin zorlukla açtığı kapıyı kapatır. Bu cümleden sonra çoğu ergen konuyu bir daha açmaz."),
                    ("Görüşmeyi durdurup durumu hemen bildirmek için annesini içeri çağırmak", "habersiz", 0,
                     "Güvenlik önemlidir; ama riskin ne olduğunu anlamadan görüşmeyi kesmek, Ela’ya “söylediğin her şey hemen dışarı "
                     "taşınır” mesajını verir."),
                    ("Uykusuzluğa odaklanıp uyku düzeni için öneriler vermek", "son-kacan", -1,
                     "Uyku sorunu gerçektir ama asıl söylenen ölüm düşüncesidir. Konuyu değiştirmek, ergene bunun konuşulamayacak bir "
                     "şey olduğunu öğretir."),
                ]),
            "risk": dict(
                metin="Ela birkaç haftadır bu düşüncelerin geldiğini, bir plan yapmadığını, daha önce kendine zarar vermediğini "
                      "söylüyor. Bir gece internette bu konuda arama yaptığını da ekliyor. Evde annesinin düzenli kullandığı ilaçlar var. "
                      "Sonra yüzünüze bakıyor: “Anneme söylemeyeceksin, değil mi?”",
                secenekler=[
                    ("“Merak etme, söylemem” diye söz vermek", "son-guven", -1,
                     "Tutamayacağınız bir söz, daha sonra güveni çok daha fazla yıkar. Güvenlik riski olduğunda gizliliğin sınırı "
                     "değişir ve bunu açıkça söylemek gerekir."),
                    ("Gizliliğin sınırını hatırlatıp paylaşmayı birlikte planlamak: “Annene bir şey söylememiz gerekiyor; ama neyi ve "
                     "nasıl söyleyeceğimizi birlikte seçebiliriz. İstersen sen başlarsın, ben yanında olurum.”", "aile", 2,
                     "Ergen paylaşımın kendisini değil, biçimini seçebilir. Böylece güvenlik sağlanırken ilişki de korunur."),
                    ("Ela’ya bir şey söylemeden annesini içeri çağırıp her şeyi anlatmak", "habersiz", 0,
                     "Bilgiyi paylaşmak gerekir; ama Ela’nın haberi ve katılımı olmadan yapılırsa kendini dışlanmış hisseder ve bir "
                     "sonraki görüşmede daha az şey anlatır."),
                    ("Konuyu bir sonraki görüşmede ele almak üzere ertelemek", "son-ertelenen", -1,
                     "İnternette arama yapmış olması ve evdeki ilaçlar bugün konuşulması gereken risklerdir. Yönteme erişimi "
                     "kısıtlamak ertelenmemesi gereken bir adımdır."),
                ]),
            "habersiz": dict(
                metin="Annesi içeri giriyor ve olanları sizden duyuyor. Ela kollarını kavuşturup başını çeviriyor. Annesi önce ağlıyor, "
                      "sonra öfkeleniyor: “Bunu bize nasıl yaparsın?”",
                secenekler=[
                    ("Ela’ya dönüp bu adımı onunla konuşmadan attığınız için kısa bir özür dilemek, sonra annenin korkusunu adlandırıp "
                     "güvenlik planına geçmek", "plan", 1,
                     "Onarım mümkündür: kısa ve içten bir özür ergenin dışlanma duygusunu azaltır. Yine de en iyisi, paylaşımı en baştan "
                     "ergenle birlikte planlamaktır."),
                    ("Anneye, kızını suçlamaması gerektiğini sert bir dille söylemek", "son-kopuk", 0,
                     "Ela’yı korumak istersiniz; ama annesini onun yanında azarlamak bir güç çatışması yaratır ve güvenlik planı için "
                     "gereken iş birliğini zayıflatır."),
                ]),
            "aile": dict(
                metin="Ela, annesine kendisinin söylemek istediğini söylüyor. Birkaç cümle kurabiliyor, gerisini sizden istiyor. Annesi "
                      "önce ağlıyor, sonra öfkeleniyor: “Neden bize hiç söylemedin?”",
                secenekler=[
                    ("Annenin korkusunu adlandırmak, Ela’nın bugün anlatmasının cesaret gerektirdiğini söylemek ve somut güvenlik "
                     "adımlarına geçmek", "plan", 2,
                     "Ebeveynin öfkesi çoğu zaman korkunun dışa vurumudur. Duyguyu adlandırmak ve hemen yapılabilecek şeylere geçmek, "
                     "aileyi çaresizlikten eyleme taşır."),
                    ("Anneye, kızını suçlamaması gerektiğini sert bir dille söylemek", "son-kopuk", 0,
                     "Ela’yı korumak istersiniz; ama annesini onun yanında azarlamak bir güç çatışması yaratır ve güvenlik planı için "
                     "gereken iş birliğini zayıflatır."),
                    ("Ayaktan izlem yerine hemen yatışı önermek", "son-yatis", 0,
                     "Plan ve girişim yokken, destekleyici bir aile ve yakın izlemle yapılan ayaktan güvenlik planı bu tabloda daha "
                     "orantılıdır. Yatış kararı riskin düzeyine göre verilir."),
                ]),
            "plan": dict(
                metin="Herkes biraz yatıştı. Görüşmenin son on dakikası kaldı.",
                secenekler=[
                    ("Birlikte yazılı bir güvenlik planı yapmak: uyarı işaretleri, Ela’nın kendini yatıştırmak için yapabilecekleri, "
                     "ulaşabileceği kişiler, kriz anında 112 ve acil servis; ilaçların ve kesici aletlerin kilit altına alınması; bir "
                     "hafta içinde yeni randevu", "son-iyi", 2,
                     "Güvenlik planı ve yönteme erişimin kısıtlanması, risk görüşmesinin somut çıktısıdır. Yakın bir randevu, planın "
                     "işleyip işlemediğini görmeyi sağlar."),
                    ("Uyku için bir ilaç yazıp üç ay sonraya randevu vermek", "son-ertelenen", -1,
                     "Evde ilaç bulunan ve ölüm düşünceleri olan bir ergene yeni bir ilaç vermek ve izlemi aylar sonraya bırakmak, "
                     "riski artırır."),
                    ("Anneye “Gözünüzü dört açın” deyip görüşmeyi bitirmek", "son-ertelenen", 0,
                     "Genel bir uyarı aileye ne yapacağını söylemez. Kaygılı bir ebeveyn somut adımlara ihtiyaç duyar."),
                ]),
            "son-iyi": dict(son="iyi", baslik="Bir planla ayrılmak",
                            metin="Ela ve annesi yazılı bir güvenlik planıyla ayrılıyor. Annesi ilaçları kilitli bir dolaba kaldıracağını "
                                  "söylüyor. Kapıdan çıkarken Ela, bir dahaki sefere konuşmaya kendisinin başlayacağını söylüyor. Gerçek "
                                  "klinikte risk değerlendirmesi kurumunuzun protokolüne göre yapılır ve kayda geçirilir."),
            "son-erken": dict(son="kotu", baslik="Erken biten görüşme",
                              metin="Ela neden geldiğini konuşmadan çıkıyor. Okulun fark ettiği değişiklikler, uykusuzluğu ve düşünceleri "
                                    "konuşulmadan kalıyor. Bir sonraki başvuru ilkinden daha zor olacak."),
            "son-kacan": dict(son="kotu", baslik="Kapanan kapı",
                              metin="Ela başını sallıyor ve konuyu değiştiriyor. Ölüm düşünceleri, plan olup olmadığı ve evdeki riskler "
                                    "sorulmadan görüşme bitiyor. Ergenin zorlukla açtığı bir kapı aynı görüşmede yeniden açılmayabilir."),
            "son-guven": dict(son="kotu", baslik="Bozulan söz",
                              metin="Görüşmenin sonunda güvenlik için annesine bilgi vermek zorunda kalıyorsunuz. Ela bunu ihanet olarak "
                                    "yaşıyor ve sonraki randevulara gelmiyor. Gizliliğin sınırını baştan söylemek bu çıkmazı önlerdi."),
            "son-ertelenen": dict(son="kotu", baslik="Ertelenen güvenlik",
                                  metin="Görüşme, evdeki ilaçlara erişim ve kriz anında ne yapılacağı konuşulmadan bitiyor. Risk "
                                        "konuşuldu ama somut bir adıma dönüşmedi."),
            "son-kopuk": dict(son="orta", baslik="Kopan iş birliği",
                              metin="Annesi savunmaya geçiyor, Ela susuyor. Güvenlik planı yarım kalıyor, randevu tarihi belirsiz. "
                                    "Duygular yatışmadan yapılan bir planın uygulanma şansı düşüktür."),
            "son-yatis": dict(son="orta", baslik="Orantısız adım",
                              metin="Yatış önerisi aileyi şaşırtıyor, Ela korkuyor ve aile öneriyi kabul etmiyor. Görüşme, somut bir "
                                    "ayaktan plan yapılmadan bitiyor. Müdahalenin yoğunluğu riskin düzeyine göre seçilmelidir."),
        }),
    # ------------------------------------------------------------------ 2
    dict(
        id="can",
        baslik="Can, 8 yaş: “Bugün ilacı yazarsanız”",
        ozet="İnternette yaptıkları testle gelen ve bugün tanı ile ilaç isteyen anne-baba. Beklentiyi anlamak, çatışmalı ailede taraf "
             "tutmamak, zaman seyriyle ayırıcı tanı ve alternatif sunan bir ret.",
        oturumlar=[6, 7, 8, 11],
        baslangic="giris",
        sahneler={
            "giris": dict(
                metin="Can 8 yaşında, ikinci sınıfta. Annesi elinde bir çıktıyla oturuyor: “İnternetteki DEHB testini yaptık, yüksek "
                      "çıktı. Haftaya okulda toplantı var. Bugün ilacı yazarsanız okula rahat gideriz.” Babası kollarını kavuşturmuş, Can "
                      "köşede oyuncaklarla oynuyor.",
                secenekler=[
                    ("Önce beklentiyi anlamak: “Okuldaki toplantıdan ne bekliyorsunuz? İlacın neyi değiştirmesini umuyorsunuz?”",
                     "baba", 2,
                     "Ailenin asıl ihtiyacı çoğu zaman okulun baskısını hafifletmektir. İsteğin arkasındaki ihtiyacı görmek, ilaç "
                     "dışındaki çözümleri de konuşmayı mümkün kılar."),
                    ("Çıktı için teşekkür edip kendi değerlendirmenizi başlatmak", "baba", 1,
                     "Doğru bir yön; ama beklenti sorulmazsa değerlendirmenin sonunda aynı istekle yeniden karşılaşırsınız."),
                    ("“İnternet testleriyle tanı konmaz” diye uzun bir açıklama yapmak", "baba", 0,
                     "Bilgi doğru; ama ilişki kurulmadan verildiğinde azar gibi duyulur ve ailenin emeğini küçümser."),
                    ("Testi yeterli sayıp reçeteyi yazmak", "son-hizli", -1,
                     "Tek bir çevrimiçi test tanı için yeterli değildir. DEHB tanısı, belirtilerin birden fazla ortamda ve uzun "
                     "süredir var olduğunun öyküyle ve birden çok bilgi kaynağıyla gösterilmesini gerektirir."),
                ]),
            "baba": dict(
                metin="Babası söze giriyor: “Bence hiçbir şeyi yok. Annesi şımartıyor, biz de böyleydik.” Annesi sesini yükseltiyor: "
                      "“Sen hiç ödevine oturdun mu ki?” Can oyuncağını bırakıp ikisine bakıyor.",
                secenekler=[
                    ("İki bakışı da değerli bulduğunuzu söyleyip ortak hedefe dönmek: “İkiniz de Can’ın okulda zorlanmasını "
                     "istemiyorsunuz. Ne olup bittiğini birlikte anlamaya çalışalım; babanın gözlemleri de annenin gözlemleri kadar "
                     "önemli.”", "oyku", 2,
                     "Çatışmalı ailede taraf tutmamak ve ortak hedefi adlandırmak ittifakı korur. Babayı sürece katmak, ileride "
                     "önerilecek her müdahalenin evde uygulanma şansını artırır."),
                    ("Babaya DEHB’nin gerçek bir bozukluk olduğunu anlatmak", "oyku", 0,
                     "Babayı ikna etmeye çalışmak onu karşı tarafa iter. Önce onun gözlemlerini sormak hem bilgi verir hem direnci "
                     "azaltır."),
                    ("Anneyle aynı fikirde olduğunuzu belli etmek", "oyku", -1,
                     "Klinisyen taraf tuttuğunda dışarıda kalan ebeveyn sürecin dışına çekilir. Babanın desteği olmadan evde "
                     "uygulanacak bir planın şansı azdır."),
                    ("Tartışmanın bir süre sürmesine izin verip etkileşimi gözlemek", "oyku", 1,
                     "Ebeveynler arasındaki etkileşimi görmek değerli bir bilgidir; ama uzarsa Can’ın önünde süren bir kavgaya dönüşür. "
                     "Kısa bir gözlemden sonra yapı kurmak gerekir."),
                ]),
            "oyku": dict(
                metin="Öyküde öğrendikleriniz: Birinci sınıfta öğretmeni Can’dan memnunmuş. Sorunlar bu yıl, 38 kişilik yeni bir sınıf "
                      "ve yeni bir öğretmenle başlamış. Evde ödev kavgaları var, Can gece yarısına kadar tablette. Annesi bu yıl işe "
                      "dönmüş. Öğretmenin notunda “derste sık sık dalıp gidiyor” yazıyor.",
                secenekler=[
                    ("Aileyle geçici bir formülasyon paylaşıp değerlendirme planı yapmak: öğretmenden yapılandırılmış form, uyku ve "
                     "ekran günlüğü, işitme ve görme kontrolü, gerekirse öğrenme güçlüğü açısından değerlendirme. Karar bir sonraki "
                     "görüşmede birlikte verilecek.", "okul", 2,
                     "Zaman seyri ve bağlam ayırıcı tanıyı genişletir: bu yıl başlayan sorunlar, kalabalık sınıf ve uyku eksikliği "
                     "dikkat sorununu açıklayabilir. Tanı için belirtilerin birden fazla ortamda ve uzun süredir var olduğunu görmek "
                     "gerekir."),
                    ("Bugün tanı koyup ilaca başlamak; ilaç işe yararsa tanı doğrulanmış olur", "son-hizli", -1,
                     "İlaca yanıt tanının kanıtı değildir. Tek doz uyarıcı, DEHB tanısı olmayan çocuklarda da motor etkinliği azaltıp "
                     "bilişsel test performansını artırmıştır ([@rapoport1978])."),
                    ("Ailenin isteğini reddedip başka bir merkeze yönlendirmek", "okul", 0,
                     "Gerekçesi ve alternatifi olmayan bir ret, aileyi aynı istekle başka bir kapıya gönderir."),
                    ("Yalnızca ebeveyn eğitimi önerip görüşmeyi kapatmak", "okul", 1,
                     "Ebeveyn eğitimi değerli bir müdahaledir; ama değerlendirme tamamlanmadan tek öneri olarak sunulursa aile "
                     "duyulmadığını düşünür."),
                ]),
            "okul": dict(
                metin="Annesi endişeyle soruyor: “Ama haftaya toplantı var. Eli boş gidersek öğretmen Can’ın başka bir okula gitmesini "
                      "isteyecek.”",
                secenekler=[
                    ("Okul için bugün yazılı bir bilgilendirme hazırlamak: değerlendirmenin sürdüğü, sınıf içi öneriler (öne oturma, "
                     "görevleri parçalara bölme, kısa molalar) ve öğretmenin doldurması istenen form. Gerekirse RAM yönlendirmesini de "
                     "konuşmak.", "son-iyi", 2,
                     "Ret, bir alternatif sunduğunda ilişkiyi korur. Aile toplantıya somut bir belgeyle gider, değerlendirme ise "
                     "aceleye getirilmeden sürer."),
                    ("“Okulun baskısı tıbbi kararı belirleyemez” deyip konuyu kapatmak", "son-kirgin", -1,
                     "Cümle doğru ama ailenin gerçek sorununu yanıtsız bırakır. Aile kendini yalnız hisseder ve başka bir hekime gider."),
                    ("Aileyi rahatlatmak için “şimdilik” düşük dozda ilaç yazmak", "son-hizli", -1,
                     "“Şimdilik” başlanan ilaç kolayca kalıcı olur, değerlendirme de yarım kalır. Bir sonraki görüşmede neyin ilaca, "
                     "neyin uykuya ya da sınıfa bağlı olduğunu ayıramazsınız."),
                    ("Toplantıya kendiniz katılacağınıza söz vermek", "son-soz", 0,
                     "İyi niyetli ama yoğun bir poliklinikte tutulması zor bir söz. Yazılı bilgilendirme ve gerekirse öğretmenle telefon "
                     "görüşmesi daha gerçekçidir."),
                ]),
            "son-iyi": dict(son="iyi", baslik="Ortak bir plan",
                            metin="Aile toplantıya yazılı bilgilendirmeyle gidiyor. Babası bir sonraki randevuya geleceğini söylüyor. Üç "
                                  "hafta sonra elinizde öğretmen formu, uyku günlüğü ve işitme testi sonucu var: tanı kararı artık bir "
                                  "tahmin değil, bir sentez."),
            "son-hizli": dict(son="kotu", baslik="Hızlı reçete",
                              metin="İlaç başlandı. İki ay sonra öğretmen pek değişiklik görmediğini söylüyor, babası ilacı vermeyi "
                                    "bırakmış. Uyku, sınıf ve ev düzeni hiç konuşulmadığı için neyin işe yarayıp neyin yaramadığını kimse "
                                    "ayıramıyor."),
            "son-kirgin": dict(son="kotu", baslik="Kırgın aile",
                               metin="Aile kırgın ayrılıyor ve bir hafta sonra başka bir hekimden reçete alıyor. Değerlendirme hiç "
                                     "tamamlanmıyor, okulla da kimse konuşmuyor."),
            "son-soz": dict(son="orta", baslik="Tutulamayan söz",
                            metin="Toplantı günü poliklinik dolu ve gidemiyorsunuz. Aile ve öğretmen sizi bekliyor. Yazılı bir "
                                  "bilgilendirme bu boşluğu doldururdu; verilen söz ise yeni bir hayal kırıklığı yarattı."),
        }),
    # ------------------------------------------------------------------ 3
    dict(
        id="emre",
        baslik="Bekleme salonunda öfkeli bir baba",
        ozet="Doksan dakikalık gecikmeden sonra bekleme salonunda bağıran bir baba ve sesten rahatsız olan otizmli oğlu. Yatıştırma, "
             "duyguyu adlandırma, meslektaşı kötülememe ve öfkenin altındaki ihtiyaca somut bir plan.",
        oturumlar=[5, 9, 14],
        baslangic="giris",
        sahneler={
            "giris": dict(
                metin="Poliklinik doksan dakika gecikmeli. Bekleme salonundan bağırışlar geliyor: Emre’nin babası sekretere “Bu ne "
                      "biçim hastane!” diye bağırıyor. Otizm tanılı, 12 yaşındaki Emre kulaklarını kapatmış, ileri geri sallanıyor. "
                      "Babası kimseyi tehdit etmiyor ama sesi giderek yükseliyor.",
                secenekler=[
                    ("Babaya sakin ve yavaş yaklaşmak, araya güvenli bir mesafe koymak, kendinizi tanıtıp önce gecikmeyi kabul etmek: "
                     "“Doksan dakikadır bekliyorsunuz. Haklısınız, bu çok uzun.”", "oda", 2,
                     "Öfkenin haklı bir çekirdeği varsa onu ilk cümlede kabul etmek, tırmanmayı en hızlı durduran adımdır. Yavaş "
                     "konuşmak ve mesafeyi korumak hem yatıştırır hem güvenliği sağlar."),
                    ("Kapıdan “Burası hastane, bağırmayın!” diye seslenmek", "tirmanma", -1,
                     "Herkesin önünde yapılan uyarı utanç yaratır ve öfkeyi tırmandırır. Kaynama evresinde ilk cümle belirleyicidir."),
                    ("Güvenliği çağırıp odanıza dönmek", "tirmanma", 0,
                     "Fiziksel tehdit ya da şiddet varsa güvenlik ve Beyaz Kod ilk adımdır. Burada baba bağırıyor ama kimseyi tehdit "
                     "etmiyor; önce yatıştırmayı denemek gerekir."),
                    ("Emre’nin zorlandığını fark edip hemen sessiz bir oda önermek", "oda", 1,
                     "Çocuğu korumak doğru bir sezgi; ama babanın öfkesi kabul edilmeden yapılırsa “beni susturmaya çalışıyorlar” diye "
                     "algılanabilir. En iyisi ikisini birleştirmek: önce gecikmeyi kabul etmek, sonra Emre için sessiz odayı önermek."),
                ]),
            "tirmanma": dict(
                metin="Babası daha da yükseliyor: “Bana bağırmayın diyemezsiniz!” Bekleyen diğer aileler size bakıyor. Emre ağlamaya "
                      "başladı.",
                secenekler=[
                    ("Sesinizi alçaltıp kısa bir özür dilemek ve Emre için sessiz bir oda önermek: “Haklısınız, bu bekleyiş çok uzun "
                     "sürdü. Emre bu gürültüde çok zorlanıyor, isterseniz hemen yan odaya geçelim.”", "oda", 1,
                     "Kötü bir başlangıç çoğu zaman onarılabilir. Kısa ve içten bir özür, savunmadan daha çok şey onarır."),
                    ("Güvenlik görevlisinden babayı dışarı çıkarmasını istemek", "son-tirmanma", -1,
                     "Tehdit yokken zorlamaya geçmek krizi büyütür ve Emre görüşme yapılmadan eve döner."),
                    ("Sessizce bekleyip babanın yorulmasını beklemek", "son-tirmanma", 0,
                     "Herkesin önünde sürmesine izin verilen bir öfke kendiliğinden sönmeyebilir. Ortamı değiştirmek gerekir."),
                ]),
            "oda": dict(
                metin="Sessiz bir odadasınız. Emre köşede, kulaklıklarını takmış. Babası hâlâ öfkeli: “Sizin gibi doktorlar umursamıyor! "
                      "Geçen sefer de bir doktor ‘sonra bakarız’ deyip bizi gönderdi.”",
                secenekler=[
                    ("Savunmaya geçmeden dinlemek ve yaşantıyı adlandırmak: “Defalarca beklemek ve sonunda duyulmadığınızı hissetmek "
                     "çok yıpratıcı olmalı.”", "ihtiyac", 2,
                     "Duyguyu ve yaşantıyı adlandırmak, öfkeli bir ebeveynin en çok ihtiyaç duyduğu şeyi verir: duyulmak. Açıklamalar "
                     "ancak bundan sonra işe yarar."),
                    ("Gecikmenin nedenlerini ayrıntılı açıklamak: acil hastalar, eksik personel", "ihtiyac", 1,
                     "Açıklama gerekebilir; ama erken gelirse savunma gibi duyulur. Önce dinlemek, sonra kısaca açıklamak daha iyi işler."),
                    ("Önceki hekimi eleştirmek: “Haklısınız, o doktor işini iyi yapmamış.”", "ihtiyac", -1,
                     "Meslektaşı kötülemek kısa vadede yakınlık kurar; ama aileye sistemin güvenilmez olduğu mesajını verir ve bir gün "
                     "aynı eleştiri size döner."),
                    ("“Bu tonla konuşmaya devam ederseniz görüşmeyi yapamam” demek", "ihtiyac", 0,
                     "Hakaret ya da tehdit varsa sınır koymak gerekir. Baba yatışmaya başlamışken ilk hamle sınır olursa öfke yeniden "
                     "alevlenebilir."),
                ]),
            "ihtiyac": dict(
                metin="Babası derin bir nefes alıyor: “Okul Emre’yi istemiyor. Rapor yenilenmezse destek eğitimi de kesilecek. Bugün "
                      "ona yetişmek için geldik.”",
                secenekler=[
                    ("Gecikme için kısa ve içten bir özür dilemek, görüşmeyi bugün yapmak ve rapor sürecinin adımlarını somut olarak "
                     "anlatmak: hangi değerlendirmeler gerekiyor, sağlık kurulu ne zaman, okula hangi yazı verilecek. Şikâyetini "
                     "iletebileceği yolu da söylemek.", "son-iyi", 2,
                     "Öfkenin altındaki ihtiyaç bulunduğunda somut bir planla karşılanır. Şikâyet yolunu göstermek, öfkeyi meşru bir "
                     "kanala taşır."),
                    ("Değerlendirme yapmadan “Raporu bugün hallederiz” diye söz vermek", "son-soz", 0,
                     "ÇÖZGER bir sağlık kurulu raporudur, bugün tek başınıza çıkaramazsınız. Tutulamayan bir söz bir sonraki öfkenin "
                     "tohumudur."),
                    ("Yalnızca Emre’yle ilgilenip babanın okul kaygısını sonraki randevuya bırakmak", "son-yarim", 1,
                     "Emre’yi görmek önemlidir; ama babanın asıl kaygısı konuşulmazsa görüşme yarım kalır ve öfke bir sonraki randevuya "
                     "taşınır."),
                    ("Babaya bir dahaki sefere daha sakin olmasını öğütlemek", "son-yarim", 0,
                     "Öğüt, yatışmaya başlamış bir ebeveyne yeniden suçlanmış hissettirir. Tekrarı önlemenin yolu gecikme sorununu ve "
                     "ihtiyacı ele almaktır."),
                ]),
            "son-iyi": dict(son="iyi", baslik="Yatışan bir oda",
                            metin="Emre sessiz odada sakinleşiyor ve görüşme yapılıyor. Babası ayrılırken rapor sürecinin takvimini not "
                                  "ediyor, bekleme süresiyle ilgili geri bildirimini de yazılı iletiyor. Öfkenin haklı çekirdeği kabul "
                                  "edildi, altındaki ihtiyaç karşılandı."),
            "son-tirmanma": dict(son="kotu", baslik="Tırmanan kriz",
                                 metin="Güvenlik görevlisi geliyor, baba daha da öfkeleniyor ve Emre ağlayarak salondan çıkıyor. Görüşme "
                                       "yapılamıyor. Kaynama evresinde atılan ilk adım krizin yönünü belirledi."),
            "son-soz": dict(son="orta", baslik="Tutulamayan söz",
                            metin="Raporun bugün çıkamayacağı anlaşılınca baba yeniden öfkeleniyor, bu kez hem gecikmeye hem size. "
                                  "Gerçekçi bir takvim, iyi niyetli bir sözden daha çok güven verir."),
            "son-yarim": dict(son="orta", baslik="Yarım kalan görüşme",
                              metin="Emre’yi değerlendiriyorsunuz ama babanın okul kaygısı yanıtsız kalıyor. Bir sonraki randevuya aynı "
                                    "öfkeyle gelme olasılığı yüksek."),
        }),
    # ------------------------------------------------------------------ 4
    dict(
        id="deniz",
        baslik="Deniz, 11 yaş: devralınan bir tanı",
        ozet="İki yıl önce “bipolar bozukluk” tanısı almış, iki ilaç kullanan ve kilo alan bir çocuk. Devralınan tanıyı zaman seyriyle "
             "yeniden değerlendirmek, meslektaşı suçlamadan tanıyı geri almak ve ilaçları kademeli azaltmak.",
        oturumlar=[10, 11, 13, 14],
        baslangic="giris",
        sahneler={
            "giris": dict(
                metin="Deniz 11 yaşında. Aile yeni taşınmış, sizi ilk kez görüyor. Dokuz yaşında öfke nöbetleri nedeniyle başka bir "
                      "klinikte “bipolar bozukluk” tanısı almış; valproat ve risperidon kullanıyor, iki yılda 12 kilo almış. Annesi: "
                      "“Bipolar olduğu için böyle. İlaçları ömür boyu kullanacakmış.”",
                secenekler=[
                    ("Tanının nasıl konduğunu ve belirtilerin zaman seyrini ayrıntılı çıkarmak: belirgin dönemler mi var, yoksa süreğen "
                     "bir tablo mu? Uyku ihtiyacı azaldı mı? Öfke nöbetleri ne kadar sürüyor, neyle başlıyor?", "seyir", 2,
                     "Devralınan tanı da bir hipotezdir. Bipolar bozuklukta belirtiler günler süren ve çocuğun olağan hâlinden ayrışan "
                     "dönemler hâlinde gelir; zaman seyri ayırıcı tanının merkezindedir."),
                    ("Önceki tanıyı sorgulamadan tedaviyi aynen sürdürmek", "seyir", 0,
                     "Ağır yan etkileri olan bir tedavi sürüyorsa tanının dayanağını yeniden gözden geçirmek hekimin sorumluluğudur."),
                    ("Aileye ilk dakikada “Bu bipolar değil” demek", "seyir", 0,
                     "Kanıt toplanmadan verilen kesin bir yargı aileyi savunmaya iter ve iki hekim arasında bırakır. Önce bulguları "
                     "birlikte toplamak gerekir."),
                    ("İlaçları bugün kesmek", "son-ani", -1,
                     "Valproat ve risperidonun birden kesilmesi yoksunluk ve geri tepme belirtilerine yol açabilir. İlaç değişikliği "
                     "planlı ve kademeli olmalıdır."),
                ]),
            "seyir": dict(
                metin="Öyküde öğrendikleriniz: Öfke nöbetleri altı yaşından beri haftada üç-dört kez oluyor, ödev ya da ekran yasağıyla "
                      "başlıyor ve yirmi-otuz dakika sürüyor. Nöbetler arasında da çoğu gün huysuz. Uykusu düzenli; günlerce süren "
                      "taşkınlık ya da az uykuyla dolaşma dönemleri hiç olmamış. Sekiz yaşından beri okulda zorbalığa uğruyor.",
                secenekler=[
                    ("Bulguları aileyle birlikte bir zaman çizelgesine dökmek ve olası açıklamaları yan yana koymak: süreğen huysuzluk "
                     "ve sık öfke nöbetleri (yıkıcı duygudurum düzenleyememe bozukluğu tanımına daha yakın), kaygı, öğrenme güçlüğü ve "
                     "akran zorbalığı", "anne", 2,
                     "Ayırıcı tanıyı aileyle birlikte kurmak, tanının değişmesini bir “hata” olarak değil, yeni bilgiyle yapılan bir "
                     "güncelleme olarak sunar. Belirgin dönemler olmadan bipolar bozukluk tanısını savunmak zorlaşır."),
                    ("Yeni bir etiket koyup eskisini silmek: “Bu DEHB”", "anne", 0,
                     "Bir etiketi başka bir etiketle değiştirmek, aileye aynı kesinlik hatasını yeniden yaşatır."),
                    ("Önce EEG ve MR istemek, sonuçları beklemek", "anne", 0,
                     "Yol gösterici bir bulgu yokken tetkik, öyküden daha az bilgi verir ve kararı erteler."),
                    ("Aileye “Önceki doktor yanlış tanı koymuş” demek", "anne", -1,
                     "Meslektaşı suçlamak aileyi iki hekim arasında bırakır. Tanılar o günkü bilgiyle konur; yeni bilgi yeni bir karar "
                     "getirir."),
                ]),
            "anne": dict(
                metin="Annesinin gözleri doluyor: “Yani iki yıldır boşuna mı ilaç içti? Kilo aldı, okulda bununla da alay ediyorlar.”",
                secenekler=[
                    ("Kızgınlığı ve üzüntüyü kabul etmek, geçmişi suçlamadan geleceğe dönmek: o günkü bilgiyle verilen kararla bugün "
                     "elimizdeki bilgiyi ayırmak ve kilo ile metabolik izlemi hemen planlamak", "plan", 2,
                     "Annenin duygusu meşrudur. Geçmişi yargılamadan bugünden bakmak hem aileyi hem tedavi ilişkisini korur. Kilo artışı "
                     "ertelenmeden ele alınmalıdır."),
                    ("“İlaçlar işe yaradı, yoksa daha kötü olurdu” diye savunmak", "plan", 0,
                     "Bunu bilemezsiniz. Savunma annenin kaygısını küçümser ve konuşmayı kapatır."),
                    ("Annenin kızgınlığını önceki hekime yönlendirmek: “İsterseniz şikâyet edebilirsiniz.”", "plan", -1,
                     "Öfkeyi bir meslektaşa yöneltmek aileye yardım etmez ve bütün sisteme duyulan güveni sarsar."),
                ]),
            "plan": dict(
                metin="Aile değişikliğe hazır görünüyor ama korkuyor: “İlaçları bırakırsa nöbetler artar mı?”",
                secenekler=[
                    ("Kademeli bir plan yapmak: ilaçları birer birer ve yavaşça azaltmak, her adımda belirti günlüğü ve kilo izlemi; "
                     "aynı dönemde ebeveyn eğitimi ve okulla zorbalık üzerine iş birliği; nöbetler artarsa ne yapılacağını önceden "
                     "konuşmak", "son-iyi", 2,
                     "Her seferde tek bir değişiklik, neyin neye yol açtığını görmeyi sağlar. Öfke nöbetleri için ebeveyn eğitimi ve "
                     "okulda zorbalığın ele alınması, ilaçtan daha fazlasını değiştirebilir."),
                    ("İki ilacı da bir hafta içinde kesmek", "son-ani", -1,
                     "Hızlı ve eş zamanlı kesme yoksunluk ve geri tepme belirtilerini artırır. Bir şey kötüleşirse nedenini "
                     "ayıramazsınız."),
                    ("İlaçları aynen sürdürüp yalnızca tanıyı değiştirmek", "son-yarim", 0,
                     "Tanı değişti ama tedavi değişmediyse aile yeni tanının ne anlama geldiğini göremez ve yan etkiler sürer."),
                    ("Kararı aileye bırakmak: “İsterseniz kesebilirsiniz.”", "son-ani", -1,
                     "Ortak karar, kararı aileye devretmek değildir. Azaltma planı ve izlem hekimin sorumluluğudur."),
                ]),
            "son-iyi": dict(son="iyi", baslik="Güncellenen tanı",
                            metin="Aylar içinde iki ilaç sırayla azaltılıp kesiliyor, kilo artışı duruyor. Ebeveyn eğitimi ve okulla "
                                  "yapılan görüşmelerden sonra öfke nöbetleri seyreliyor. Dosyada tanının nasıl ve neden değiştiği açıkça "
                                  "yazıyor; aile bunu bir yenilgi olarak değil, bir güncelleme olarak anlatıyor."),
            "son-ani": dict(son="kotu", baslik="Ani kesme",
                            metin="İlaçlar hızla kesiliyor. İki hafta sonra huysuzluk ve uyku sorunları artıyor, aile acil servise "
                                  "başvuruyor. Kötüleşmenin bozukluktan mı yoksa kesmeden mi kaynaklandığını kimse ayıramıyor ve ailenin "
                                  "değişikliğe güveni sarsılıyor."),
            "son-yarim": dict(son="orta", baslik="Yarım kalan geri alma",
                              metin="Dosyada tanı değişti ama tedavi aynı kaldı. Kilo artışı sürüyor, aile ise ilaçların neden hâlâ "
                                    "gerekli olduğunu anlamıyor. Bir tanıyı geri almak, sonuçlarını da ele almayı gerektirir."),
        }),
]

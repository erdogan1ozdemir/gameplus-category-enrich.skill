# -*- coding: utf-8 -*-
"""Kategori içeriği geliştirme katmanı (v12) - EKLEMELİ.

Yazarın mevcut cümlelerine dokunulmaz; üzerine şunlar EKLENİR:

1. ALT_TUR_TANIM  : her H4 alt türünün hemen altına "tanım-önce" cümlesi.
   AI Overview ve "X nedir" sorguları bu kalıbı doğrudan çekiyor.
   Biçim: <strong>{Alt tür} nedir?</strong> {tek cümlelik tanım} {kimin için / ne bekler}

2. EK_FAQ         : alt tür ve arama niyeti odaklı yeni SSS soruları.
   Mevcut SSS'lerin sonuna eklenir, FAQ Schema'ya da girer.

Kaynak: oyun türlerinin yerleşik tanımları. Belirli bir oyuna dair DOĞRULANMAMIŞ
iddia eklenmez; tanımlar tür mekaniği düzeyinde kalır.
"""

# =============================================================================
# 1) ALT TÜR TANIMLARI  {(slug, h4_metni): "tanım cümlesi (HTML)"}
# =============================================================================

ALT_TUR_TANIM = {

    # ---------------------------------------------------------------- aile-dostu
    ("aile-dostu", "Kooperatif Aile Macerası"):
        "İki oyuncunun aynı hikâyeyi birlikte ilerlettiği, bölümlerin çoğunun tek başına "
        "çözülemediği yapımlardır. Bölünmüş ekran ya da çevrimiçi eşleşme ile oynanır ve "
        "genellikle bulmacalar iki farklı yeteneğin birleşmesini gerektirir.",
    ("aile-dostu", "LEGO ve Lisanslı Çocuk Oyunları"):
        "Tanıdık film ve çizgi film evrenlerini basit dövüş, toplama ve bulmaca döngüsüyle "
        "birleştiren yapımlardır. Ölüm cezası neredeyse yoktur; çocuk oyuncu takılırsa oyun "
        "kaldığı yerden devam eder, bu da birlikte oynamayı kolaylaştırır.",
    ("aile-dostu", "Cozy ve Çiftlik Yaşam Simülasyonu"):
        "Zaman baskısı ve kaybetme koşulu olmayan, ekim-hasat, dekorasyon ve kasaba ilişkileri "
        "üzerine kurulu yapımlardır. Oturumlar istenildiği kadar kısa tutulabilir, bu yüzden "
        "kısa akşam seanslarına uygundur.",
    ("aile-dostu", "Aile Dostu Platform ve Klasik Macera"):
        "Zıplama, tırmanma ve keşif üzerine kurulu, bölüm bölüm ilerleyen yapımlardır. "
        "Kontrol şeması birkaç tuşla sınırlıdır; yeni başlayan bir oyuncu ilk bölümde "
        "temel hareketleri öğrenir.",

    # ------------------------------------------------------------------- aksiyon
    ("aksiyon", "Battle Royale Oyunları"):
        "Onlarca oyuncunun daralan bir haritada son kalan olmak için yarıştığı türdür. Her "
        "maç eşyasız başlar, ekipman harita üzerinden toplanır; bu yüzden iki maç birbirinin "
        "aynısı olmaz.",
    ("aksiyon", "Soulslike Oyunlar"):
        "Zamanlamaya dayalı dövüş, yüksek ceza ve tekrar ederek öğrenme üzerine kurulu alt "
        "türdür. Ölünce toplanan kaynak düştüğün yerde kalır ve geri alınması gerekir; "
        "ilerleme hız değil, kalıp öğrenme meselesidir.",
    ("aksiyon", "Hack-and-Slash Oyunları"):
        "Kalabalık düşman gruplarına karşı kesintisiz kombo kurmaya dayanan alt türdür. "
        "Puanlama genelde saldırı çeşitliliğini ödüllendirir, aynı hareketi tekrarlamak "
        "düşük skor verir.",
    ("aksiyon", "Açık Dünya Aksiyon Oyunları"):
        "Ana görevin yanında haritayı serbestçe gezmeye ve yan içeriği istediğin sırayla "
        "açmaya izin veren yapımlardır. Oyun süresinin büyük kısmı ana hikâyenin dışında "
        "geçebilir.",
    ("aksiyon", "FPS ve TPS Oyunları"):
        "Nişan alma ve mevzi kullanmanın merkezde olduğu, birinci ya da üçüncü şahıs kamerayla "
        "oynanan yapımlardır. Kamera farkı sadece görüntü değil, kapak arkasından görüş "
        "açısını da değiştirir.",
    ("aksiyon", "Aksiyon-Macera Oyunları"):
        "Çatışmayı keşif, bulmaca ve hikâye anlatımıyla dengeleyen türdür. Saf aksiyona göre "
        "temposu daha değişkendir; sakin keşif bölümleriyle yoğun çatışmalar sırayla gelir.",

    # -------------------------------------------------------------------- arcade
    ("arcade", "Klasik Arcade Dövüş Derlemeleri"):
        "Salon makinelerindeki dövüş oyunlarının orijinal haliyle bir araya getirildiği "
        "paketlerdir. Genellikle çevrimiçi eşleşme ve geri sarma (rollback) desteği eklenir, "
        "oyunun kendisi değişmez.",
    ("arcade", "Modern Arcade-Stili Dövüş"):
        "Klasik salon temposunu koruyup güncel grafik ve eğitim modlarıyla birleştiren "
        "yapımlardır. Giriş bariyeri kasıtlı olarak düşük tutulur, karmaşık giriş dizileri "
        "sadeleştirilir.",
    ("arcade", "Pac-Man ve BANDAI NAMCO Klasikleri"):
        "Tek ekranlık, yüksek skor odaklı klasiklerin yeniden yayımlandığı gruptur. Oyun "
        "döngüsü birkaç saniyede anlaşılır; derinlik kural sayısında değil, kalıpları "
        "ezberlemekte saklıdır.",
    ("arcade", "Retro Beat 'em Up Yeniden Yapımları"):
        "Yan kaydırmalı dövüş formülünü modern kontrol ve kooperatif desteğiyle yeniden "
        "kuran yapımlardır. İki ile dört oyuncu aynı ekranda ilerler.",
    ("arcade", "Modern Arcade-Stili İndie Yapımlar"):
        "Küçük stüdyoların arcade temposunu güncel mekaniklerle birleştirdiği yapımlardır. "
        "Oturumlar kısadır ve genellikle her denemede harita ya da düşman dizilimi değişir.",
    ("arcade", "Modern Arcade-Sports ve Live Service"):
        "Gerçekçi kural setleri yerine abartılı fizik ve hızlı maçlara odaklanan spor "
        "yapımlarıdır. Sezonluk içerik güncellemeleriyle uzun süre desteklenirler.",

    # ------------------------------------------------------------------ bagimsiz
    ("bagimsiz", "Metroidvania ve 2D Aksiyon-Macera"):
        "Birbirine bağlı tek bir haritada, yeni yetenek kazandıkça daha önce geçilemeyen "
        "yerlerin açıldığı alt türdür. İlerleme seviye atlamakla değil, yetenek kazanmakla "
        "olur.",
    ("bagimsiz", "Roguelike ve Roguelite"):
        "Her denemede bölüm düzeninin yeniden üretildiği, ölümün turu sıfırladığı türdür. "
        "Roguelite'ta denemeler arasında kalıcı gelişim vardır; roguelike'ta genellikle yoktur.",
    ("bagimsiz", "Hikaye Odaklı Bağımsız RPG"):
        "Küçük ekiplerin yazıya ve karakter ilişkilerine ağırlık verdiği rol yapma "
        "yapımlarıdır. Savaş sistemi sade tutulur, asıl ağırlık seçimlerin sonuçlarındadır.",
    ("bagimsiz", "Yaşam Simülasyonu ve Çiftlik Yapımları"):
        "Günlük döngü, üretim ve kasaba ilişkileri üzerine kurulu, kaybetme koşulu olmayan "
        "yapımlardır. Oyuncu kendi hedefini belirler.",
    ("bagimsiz", "Kooperatif ve Sosyal İndie"):
        "Birlikte oynandığında anlam kazanan, çoğu zaman sesli iletişim gerektiren "
        "yapımlardır. Mekanikler basittir; zorluk koordinasyondan gelir.",
    ("bagimsiz", "Atmosferik ve Sanatsal İndie"):
        "Anlatımı diyalogdan çok görsel tasarım, ses ve mekan üzerinden kuran yapımlardır. "
        "Oyun süresi genellikle kısadır ve tek oturumda bitirilebilir.",
    ("bagimsiz", "Viral İndie Hitler"):
        "Yayıncı ve topluluk üzerinden hızla yayılan, çoğu zaman tek bir güçlü fikir üzerine "
        "kurulu yapımlardır. Öğrenme süresi kısa, tekrar oynanabilirliği yüksektir.",

    # ------------------------------------------------------------- basit-eglence
    ("basit-eglence", "Party ve Sosyal Casual"):
        "Kalabalık grupla kısa turlar hâlinde oynanan yapımlardır. Kurallar bir turda "
        "öğrenilir; oyuncu sayısı arttıkça kaos ve eğlence de artar.",
    ("basit-eglence", "Cozy ve Rahatlatıcı Yaşam Simülasyonu"):
        "Zaman baskısı, ölüm ve başarısızlık olmayan, düzenleme ve bakım üzerine kurulu "
        "yapımlardır. Amaç ilerlemek değil, oturumun kendisidir.",
    ("basit-eglence", "İş ve Yönetim Simülasyonu (Job Sim)"):
        "Gerçek bir mesleğin rutinini sadeleştirip oyunlaştıran yapımlardır. Görevler kısa "
        "ve tekrarlıdır; ilerleme ekipman ve alan büyütmeyle gelir.",
    ("basit-eglence", "Roguelite ve Bağımlılık Yaratan Casual"):
        "Kısa turlar ve her turda değişen ödüllerle kurulu, \"bir tur daha\" hissi veren "
        "yapımlardır. Tek oturum birkaç dakikadır, üst üste oynanır.",
    ("basit-eglence", "Sandbox ve Yaratıcı Casual"):
        "Hedef dayatmayan, inşa ve deneme üzerine kurulu yapımlardır. Oyuncu ne yapacağına "
        "kendi karar verir.",
    ("basit-eglence", "Mini-Oyun Koleksiyonu ve Hibrit Casual"):
        "Tek pakette birden çok kısa oyun sunan yapımlardır. Her mini-oyun bağımsızdır, "
        "sıkılınca diğerine geçilir.",

    # ------------------------------------------------------------------- bulmaca
    ("bulmaca", "Birinci Şahıs Fizik Bulmacası"):
        "Bölümlerin fizik kurallarını kullanarak çözüldüğü, birinci şahıs kamerayla oynanan "
        "türdür. Refleks değil, mekaniğin sınırlarını anlamak gerekir.",
    ("bulmaca", "Felsefi ve Anlatı Tabanlı 3D Bulmaca"):
        "Bulmaca çözümünün yanında bir metin ya da sesli anlatı katmanı taşıyan yapımlardır. "
        "Bölümler ilerledikçe hikâye de açılır.",
    ("bulmaca", "Mühendislik ve Programlama Bulmacası"):
        "Çözümün tek doğrusu olmayan, sistem kurma ve optimize etme üzerine kurulu türdür. "
        "Aynı bölüm farklı verimlilikte pek çok şekilde çözülebilir.",
    ("bulmaca", "Kooperatif Bulmaca ve Escape Room"):
        "İki ya da daha çok oyuncunun farklı bilgi parçalarına sahip olduğu, çözümün "
        "konuşarak bulunduğu yapımlardır. Tek başına oynanamaz.",
    ("bulmaca", "Anlatı Tabanlı Bulmaca ve Walking Sim Variant"):
        "Keşif ve çevreyi okuma üzerine kurulu, bulmacaların hikâyeyi ilerletmeye hizmet "
        "ettiği yapımlardır. Tempo kasıtlı olarak yavaştır.",
    ("bulmaca", "Cozy Brain Teaser ve Düzenleme Bulmacası"):
        "Süre sınırı ve başarısızlık olmadan, eşya yerleştirme ve düzen kurma üzerine "
        "çalışan yapımlardır. Kısa molalara uygundur.",

    # --------------------------------------------------------------- canlandirma
    ("canlandirma", "Klasik CRPG (Computer Role-Playing Game)"):
        "Karakter yaratma, parti yönetimi ve kural tabanlı savaş üzerine kurulu rol yapma "
        "türüdür. Diyalog seçimleri ve karakter özellikleri kimi çözüm yollarını açıp "
        "kimilerini kapatır.",
    ("canlandirma", "JRPG (Japon Rol Yapma Oyunu)"):
        "Belirlenmiş bir kadro ve güçlü anlatı çizgisiyle ilerleyen, savaşın çoğunlukla sıra "
        "tabanlı ya da yarı gerçek zamanlı olduğu alt türdür. Karakter gelişimi hikâyeye "
        "bağlıdır.",
    ("canlandirma", "Açık Dünya Aksiyon RPG"):
        "Rol yapma sistemlerini serbest gezilebilen bir haritayla birleştiren türdür. Seviye "
        "ve ekipman ilerlemesi keşifle beraber yürür.",
    ("canlandirma", "Aksiyon RPG (ARPG) ve Hack-and-Slash"):
        "Gerçek zamanlı savaş ve yoğun ekipman toplama döngüsü üzerine kurulu türdür. Oyunun "
        "asıl uzun vadeli hedefi karakteri belirli bir yapıya (build) oturtmaktır.",
    ("canlandirma", "Sinematik Hikaye Odaklı RPG"):
        "Sahne yönetimi ve seslendirmeye ağırlık veren, seçimlerin anlatıyı belirgin biçimde "
        "değiştirdiği yapımlardır. Tek oyunculu ve senaryo eksenlidir.",
    ("canlandirma", "Soulslike ve Souls-RPG Hibrit"):
        "Rol yapma ilerlemesini yüksek cezalı, zamanlama odaklı dövüşle birleştiren alt "
        "türdür. Zorluk ayarı yerine öğrenme eğrisi vardır.",
    ("canlandirma", "MMO RPG ve Çevrimiçi RPG"):
        "Kalıcı bir dünyada başka oyuncularla birlikte ilerlenen rol yapma türüdür. İçerik "
        "genellikle grup halinde açılır ve sezonluk güncellemelerle genişler.",
}

ALT_TUR_TANIM.update({

    # ---------------------------------------------------------------------- demo
    ("demo", "Aksiyon ve Korku"):
        "Tam sürümün ilk bölümünü ya da özel hazırlanmış bir kesitini oynatan denemelerdir. "
        "Amaç dövüş hissini ve atmosferi satın almadan önce test etmektir.",
    ("demo", "JRPG ve Aksiyon-RPG"):
        "Savaş sistemini ve karakter gelişimini tanıtan denemelerdir. Bu türde demo "
        "ilerlemesi çoğu zaman tam sürüme aktarılır.",
    ("demo", "Açık Dünya ve Macera"):
        "Haritanın sınırlı bir bölgesini açan denemelerdir. Keşif temposunu ve hareket "
        "hissini ölçmeye yarar.",
    ("demo", "Strateji ve Bulmaca"):
        "Birkaç senaryo ya da ilk bölümlerle sınırlı denemelerdir. Kural setinin ne kadar "
        "derin olduğunu görmek için yeterlidir.",
    ("demo", "Bilim-Kurgu ve Hızlı Aksiyon"):
        "Kısa ve yoğun bir kesit sunan denemelerdir. Tempo ve nişan hissi ön plandadır.",

    # --------------------------------------------------------------------- diger
    ("diger", "Blizzard ve Battle.net Kataloğu"):
        "Battle.net hesabıyla açılan yapımlardır. Oynamak için GeForce NOW hesabına ayrıca "
        "Battle.net bağlantısı kurulur.",
    ("diger", "Call of Duty Serisi"):
        "Yıllık çıkan nişancı serisinin bulutta desteklenen sürümleridir. Kampanya, çok "
        "oyunculu ve sezonluk modlar aynı istemci üzerinden açılır.",
    ("diger", "HoYoverse Evreni"):
        "Karakter toplama ve sezonluk bölge güncellemeleri üzerine kurulu yapımlardır. "
        "İlerleme hesap bazlıdır, cihaz değiştirince kaldığın yerden devam eder.",
    ("diger", "MMO ve Sandbox Yayıncıları"):
        "Kendi başlatıcısını kullanan, kalıcı dünyalı yapımlardır. Oturumlar uzundur ve "
        "kararlı bağlantı ister.",
    ("diger", "Ücretsiz Looter ve Kooperatif"):
        "Ekipman toplama döngüsünü grup halinde oynanan görevlerle birleştiren ücretsiz "
        "yapımlardır. Giriş maliyeti yoktur, ilerleme oynadıkça gelir.",
    ("diger", "Savaş Aracı Simülasyonu"):
        "Tank, uçak ve gemi gibi araçların ayrı ayrı modellendiği çok oyunculu yapımlardır. "
        "Araç seçimi ve harita bilgisi maçın seyrini belirler.",

    # --------------------------------------------------------------- dovus-oyunu
    ("dovus-oyunu", "Klasik 2D Dövüş Oyunları"):
        "İki karakterin yan görünümde karşılaştığı, giriş dizileri ve mesafe yönetimi üzerine "
        "kurulu türdür. Rekabetçi sahnenin temeli bu alt türdür.",
    ("dovus-oyunu", "3D Arena ve Silahlı Dövüş"):
        "Karakterlerin üç boyutlu alanda yana kaçabildiği dövüş türüdür. Yan hareket, 2D "
        "dövüşten farklı bir mesafe oyunu yaratır.",
    ("dovus-oyunu", "Platform Brawler ve Party Fighter"):
        "Amacın rakibi sahadan dışarı atmak olduğu, can barı yerine hasar yüzdesi kullanan "
        "alt türdür. Dört oyuncuya kadar aynı anda oynanır.",
    ("dovus-oyunu", "Beat 'em Up Klasikleri"):
        "Tek yönde ilerlerken düşman dalgalarını temizlemeye dayanan türdür. Rakip oyuncu "
        "değil, yapay zekâ kontrollü gruplardır.",
    ("dovus-oyunu", "Martial Arts Aksiyonu ve Tek Oyunculu Dövüş"):
        "Dövüş mekaniğini hikâye modu içinde sunan yapımlardır. Rekabetçi eşleşme yerine "
        "kampanya ilerlemesi vardır.",
    ("dovus-oyunu", "Spor ve Wrestling Simülasyonu"):
        "Güreş ve dövüş sporlarını kural setiyle birlikte modelleyen yapımlardır. Kariyer "
        "modu ve karakter düzenleme öne çıkar.",

    # -------------------------------------------------------------------- ea-app
    ("ea-app", "Battlefield Serisi ve FPS"):
        "Geniş haritalarda araçlı ve büyük takımlı çatışmalara odaklanan nişancı "
        "yapımlarıdır. Takım oyunu bireysel nişandan daha belirleyicidir.",
    ("ea-app", "Star Wars Evreni"):
        "Lisanslı evrende geçen aksiyon ve macera yapımlarıdır. Tek oyunculu kampanya ve çok "
        "oyunculu modlar seriye göre değişir.",
    ("ea-app", "RPG ve Hikaye Odaklı"):
        "Karakter seçimlerinin anlatıyı değiştirdiği rol yapma yapımlarıdır. Oyun süresi "
        "uzundur, tek oturumda bitmez.",
    ("ea-app", "Yarış ve Spor"):
        "Arcade yarış ve lisanslı spor serilerini kapsar. Sezonluk içerik ve çevrimiçi "
        "modlar düzenli güncellenir.",
    ("ea-app", "Kooperatif ve İndie"):
        "Birlikte oynanan küçük ölçekli yapımlardır. Genellikle iki oyuncu için tasarlanır.",

    # ---------------------------------------------------------------- epic-games
    ("epic-games", "Aksiyon ve FPS Yapımları"):
        "Epic Games Store kütüphanesindeki çatışma odaklı yapımlardır. Hesap bağlandıktan "
        "sonra sahip olunan oyunlar bulutta listelenir.",
    ("epic-games", "RPG ve Macera"):
        "Karakter gelişimi ve keşif üzerine kurulu uzun soluklu yapımlardır.",
    ("epic-games", "Battle Royale ve Çok Oyunculu"):
        "Ücretsiz erişimli, sezonluk güncellenen rekabetçi yapımlardır. Giriş için oyun satın "
        "almak gerekmez.",
    ("epic-games", "Hayatta Kalma ve Açık Dünya"):
        "Kaynak toplama, üs kurma ve hava-yiyecek gibi ihtiyaçların yönetildiği yapımlardır. "
        "Oturumlar uzundur.",
    ("epic-games", "Sinematik Aksiyon-Macera"):
        "Sahne yönetimi güçlü, doğrusal ilerleyen yapımlardır. Hikâye tempoyu belirler.",

    # ----------------------------------------------------------------------- fps
    ("fps", "Rekabetçi ve Taktiksel FPS Oyunları"):
        "Hassas nişan, ekonomi yönetimi ve harita bilgisi üzerine kurulu, genellikle 5v5 "
        "oynanan alt türdür. Tek isabet ölümcül olabildiği için tempo diğer FPS türlerinden "
        "daha yavaştır.",
    ("fps", "Battle Royale FPS Oyunları"):
        "Büyük haritada daralan güvenli alanla son kalan olma yarışıdır. Ekipman her maçta "
        "sıfırdan toplanır.",
    ("fps", "Hikâye Odaklı Tek Oyunculu FPS"):
        "Çatışmayı senaryo ve sahne yönetimiyle birleştiren yapımlardır. Çevrimiçi rekabet "
        "yerine kampanya vardır.",
    ("fps", "Klasik Hızlı ve Eski FPS Oyunları"):
        "Mevzi kullanmak yerine sürekli hareket etmeyi zorunlu kılan, yüksek tempolu alt "
        "türdür. Sağlık paketi ve mühimmat harita üzerinden toplanır.",
    ("fps", "Co-op ve PvE FPS Oyunları"):
        "Rakibin oyuncu değil yapay zekâ olduğu, grup halinde görev tamamlanan yapımlardır. "
        "Zorluk koordinasyondan gelir.",
    ("fps", "Çok Oyunculu Online FPS Oyunları"):
        "Kısa maçlar, hızlı eşleşme ve sezonluk denge güncellemeleri üzerine kurulu "
        "yapımlardır. Her sezon meta değişir.",

    # -------------------------------------------------------------------- macera
    ("macera", "Açık Dünya Macera"):
        "Haritanın serbest gezildiği, görev sırasının oyuncuya bırakıldığı türdür. Keşif "
        "başlı başına bir ödül döngüsüdür.",
    ("macera", "Aksiyon-Macera"):
        "Çatışma, platform ve bulmacayı aynı yapımda dengeleyen türdür. Hiçbiri tek başına "
        "baskın değildir.",
    ("macera", "Hikaye Odaklı ve Sinematik Macera"):
        "Anlatının mekaniğin önünde olduğu, seçim ve diyalogla ilerleyen yapımlardır. Tekrar "
        "oynanışta farklı sonlar görülebilir.",
    ("macera", "Hayatta Kalma ve Survival-Macera"):
        "Kaynak kıtlığı ve çevresel tehdit altında ilerlenen türdür. Envanter yönetimi "
        "çatışma kadar belirleyicidir.",
    ("macera", "Bulmaca-Macera ve Kooperatif Macera"):
        "İlerlemenin çatışmayla değil bulmaca çözmeyle sağlandığı yapımlardır. Kooperatif "
        "sürümlerinde çözüm iki oyuncunun bilgisini birleştirmesini gerektirir.",
})

ALT_TUR_TANIM.update({

    # ----------------------------------------------------------------------- mmo
    ("mmo", "Themepark MMORPG"):
        "İçeriğin geliştirici tarafından belirli bir sırayla sunulduğu MMO türüdür. Görev "
        "zinciri, zindanlar ve baskınlar seviye ilerledikçe açılır.",
    ("mmo", "Açık Dünya MMORPG"):
        "Bölge geçişlerinin yükleme ekranı olmadan yapıldığı, keşfin ödüllendirildiği MMO "
        "türüdür. Oyuncu nereye gideceğine kendi karar verir.",
    ("mmo", "Sandbox MMO"):
        "Ekonominin ve çatışmanın büyük ölçüde oyuncular tarafından şekillendirildiği türdür. "
        "Kalıcı sonuçlar ve oyuncu politikası öne çıkar.",
    ("mmo", "MMOARPG ve Action MMO"):
        "Sekme tabanlı hedefleme yerine gerçek zamanlı nişan ve kaçınma kullanan MMO "
        "türüdür. Dövüş refleks gerektirir.",
    ("mmo", "MMOFPS ve Loot Shooter"):
        "Nişancı mekaniklerini kalıcı karakter gelişimi ve ekipman toplamayla birleştiren "
        "türdür. Görevler genellikle küçük gruplarla oynanır.",

    # ---------------------------------------------------------------------- moba
    ("moba", "Klasik 5v5 MOBA"):
        "İki takımın üç koridorlu haritada rakip üssü yıkmaya çalıştığı türdür. Maç içi "
        "ekonomi ve harita kontrolü sonucu belirler.",
    ("moba", "3. Şahıs MOBA"):
        "Aynı hedefi kuş bakışı yerine karakterin arkasından oynatan alt türdür. Yetenekler "
        "otomatik isabet yerine nişan alarak kullanılır.",
    ("moba", "Hero Shooter MOBA Hibrit"):
        "Karakter yeteneklerini nişancı mekanikleriyle birleştiren türdür. Rol dağılımı "
        "MOBA'dan, çatışma hissi FPS'ten gelir.",
    ("moba", "Battle Royale ve MOBA Hibrit"):
        "Daralan harita kuralını yetenek tabanlı karakterlerle birleştiren türdür. Hem "
        "toplama hem takım savaşı vardır.",

    # -------------------------------------------------------- oynamasi-ucretsiz
    ("oynamasi-ucretsiz", "Battle Royale Ücretsiz Oyunlar"):
        "Oyuna girmek için ücret istemeyen, gelirini kozmetik satışlarından sağlayan battle "
        "royale yapımlarıdır. Oynanışı etkileyen bir satın alma yoktur.",
    ("oynamasi-ucretsiz", "FPS ve Hero Shooter Ücretsiz Oyunlar"):
        "Ücretsiz erişimli nişancı yapımlarıdır. Karakter ve silahların bir kısmı oynayarak "
        "açılır.",
    ("oynamasi-ucretsiz", "MMO ve MMORPG Ücretsiz Oyunlar"):
        "Abonelik istemeyen kalıcı dünyalı yapımlardır. Genişleme paketleri ayrı satılabilir.",
    ("oynamasi-ucretsiz", "Açık Dünya ve RPG Ücretsiz Oyunlar"):
        "Ücretsiz başlayan, karakter toplama ya da sezonluk bölge güncellemeleriyle büyüyen "
        "yapımlardır.",
    ("oynamasi-ucretsiz", "MOBA ve Strateji Ücretsiz Oyunlar"):
        "Rekabetçi dengeyi bozmamak için tüm oynanış içeriğini ücretsiz tutan yapımlardır. "
        "Satın alınabilenler görseldir.",

    # ------------------------------------------------------------------- oyunlar
    ("oyunlar", "FPS ve Shooter Oyunları"):
        "Birinci ya da üçüncü şahıs nişan mekaniği üzerine kurulu yapımlardır. Rekabetçi ve "
        "hikâye odaklı alt kolları vardır.",
    ("oyunlar", "Aksiyon Oyunları"):
        "Refleks, zamanlama ve dövüş üzerine kurulu geniş bir türdür. Açık dünyadan "
        "soulslike'a kadar çok sayıda alt kolu barındırır.",
    ("oyunlar", "RPG ve Hikaye Odaklı Oyunlar"):
        "Karakter gelişimi, seçim ve anlatı üzerine kurulu yapımlardır. Oyun süreleri "
        "genellikle uzundur.",
    ("oyunlar", "MMO Oyunları"):
        "Kalıcı dünyada çok sayıda oyuncuyla birlikte ilerlenen yapımlardır. İçerik "
        "güncellemelerle genişler.",
    ("oyunlar", "Strateji Oyunları"):
        "Kaynak yönetimi ve planlamanın refleksin önünde olduğu yapımlardır. Gerçek zamanlı "
        "ve sıra tabanlı olmak üzere ikiye ayrılır.",
    ("oyunlar", "Yarış Oyunları"):
        "Araç kontrolü ve tur süresi üzerine kurulu yapımlardır. Arcade ve simülasyon uçları "
        "arasında geniş bir yelpaze vardır.",
    ("oyunlar", "Oynaması Ücretsiz Oyunlar"):
        "Girişte ücret istemeyen yapımlardır. Oynamak için mağaza hesabı yeterlidir, ayrıca "
        "lisans satın almak gerekmez.",
    ("oyunlar", "İndie Oyunlar"):
        "Küçük ekiplerin ürettiği, mekanik ya da anlatı açısından deneysel yapımlardır. "
        "Oyun süreleri kısadan uzuna değişir.",

    # ------------------------------------------------------------------ platform
    ("platform", "Metroidvania"):
        "Tek parça haritada, kazanılan yeteneklerle yeni bölgelerin açıldığı alt türdür. "
        "Geri dönüp önceki alanları yeniden gezmek tasarımın parçasıdır.",
    ("platform", "2D Platform"):
        "Yan görünümde zıplama ve zamanlama üzerine kurulu klasik türdür. Bölümler kısa ve "
        "tekrar denemeye açıktır.",
    ("platform", "3D Platform"):
        "Üç boyutlu alanda mesafe ve derinlik algısı gerektiren türdür. Kamera kontrolü "
        "oynanışın parçasıdır.",
    ("platform", "Roguelike Platformer"):
        "Platform mekaniğini her denemede değişen bölüm düzeniyle birleştiren türdür. Ölüm "
        "turu sıfırlar.",
    ("platform", "Hikaye Odaklı Platform"):
        "Zıplama mekaniğini anlatıyla birleştiren yapımlardır. Zorluk çoğu zaman erişilebilir "
        "tutulur.",

    # ----------------------------------------------------------- populer-oyunlar
    ("populer-oyunlar", "Açık Dünya ve Hikaye Odaklı RPG"):
        "Geniş haritada özgür keşfi güçlü bir anlatıyla birleştiren yapımlardır. En çok "
        "oynanan kategorilerin başında gelir.",
    ("populer-oyunlar", "Rekabetçi ve Çok Oyunculu"):
        "Sıralı maçlar ve sezonluk ilerleme üzerine kurulu yapımlardır. Oyuncu sayısı "
        "yoğunluğu eşleşme süresini kısaltır.",
    ("populer-oyunlar", "Strateji ve Sandbox"):
        "Uzun oturumlara ve planlamaya dayanan yapımlardır. Tek maç saatler sürebilir.",
    ("populer-oyunlar", "Simülasyon ve Hayatta Kalma"):
        "Sistem yönetimi ve kaynak dengesi üzerine kurulu yapımlardır. Kooperatif "
        "sürümlerinde iş bölümü öne çıkar.",

    # ---------------------------------------------------------------- simulasyon
    ("simulasyon", "Araç ve Yol Simülasyonu"):
        "Uzun mesafe sürüş, yük taşıma ve trafik kurallarını modelleyen türdür. Tempo "
        "kasıtlı olarak yavaştır; asıl ödül yolculuğun kendisidir.",
    ("simulasyon", "Uçuş Simülasyonu"):
        "Uçak sistemlerini kokpit düzeyinde modelleyen türdür. Kalkış ve iniş prosedürleri "
        "gerçek kontrol listelerine yakındır.",
    ("simulasyon", "Şehir İnşası ve Yönetim Simülasyonu"):
        "Altyapı, bütçe ve nüfus dengesini yöneten türdür. Hatalı planlama saatler sonra "
        "sonuç verir.",
    ("simulasyon", "Yaşam ve Çiftlik Simülasyonu"):
        "Günlük rutin, üretim ve ilişkiler üzerine kurulu, kaybetme koşulu olmayan türdür.",
    ("simulasyon", "Yarış Simülasyonu"):
        "Lastik, süspansiyon ve yakıt gibi değişkenleri modelleyen yarış türüdür. Direksiyon "
        "seti ile oynandığında fark belirginleşir.",
    ("simulasyon", "İşletme ve Park Yönetim Simülasyonu"):
        "Bir tesisin kurulması ve kârlı işletilmesi üzerine kurulu türdür. Ziyaretçi "
        "memnuniyeti ve gider dengesi ana metriklerdir.",
    ("simulasyon", "Koloni, Üretim ve Sandbox Simülasyonu"):
        "Üretim zinciri kurma ve otomasyon üzerine kurulu türdür. Oyun ilerledikçe sistem "
        "karmaşıklığı katlanarak artar.",

    # ---------------------------------------------------------------------- spor
    ("spor", "Arkade Spor"):
        "Gerçek kural setini sadeleştirip tempoyu öne çıkaran spor yapımlarıdır. Maçlar kısa "
        "ve yüksek skorludur.",
    ("spor", "Motor Sporları"):
        "Pist, ralli ve formula gibi disiplinleri kapsayan yapımlardır. Sürüş yardımları "
        "açılıp kapatılabilir.",
    ("spor", "Tenis"):
        "Vuruş zamanlaması ve kort konumlanması üzerine kurulu yapımlardır. Ralli uzunluğu "
        "zorluk ayarına göre değişir.",
    ("spor", "Kaykay ve Ekstrem Sporlar"):
        "Kombo zinciri ve puan üzerine kurulu yapımlardır. Bölümler serbest gezilir.",
    ("spor", "Güreş ve Dövüş Sporları"):
        "Kural setiyle birlikte modellenen temas sporlarıdır. Kariyer modu ve karakter "
        "düzenleme öne çıkar.",
    ("spor", "Avcılık ve Açık Hava"):
        "Sabır ve iz sürme üzerine kurulu, tempo bakımından diğer spor türlerinden ayrılan "
        "yapımlardır.",

    # --------------------------------------------------------------------- steam
    ("steam", "Aksiyon ve FPS Yapımları"):
        "Steam kütüphanesindeki çatışma odaklı yapımlardır. Hesap bağlandıktan sonra sahip "
        "olunan oyunlar bulutta listelenir.",
    ("steam", "Strateji ve 4X Yapımları"):
        "Uzun oturumlu, planlama ağırlıklı yapımlardır. Kaydetme ve devam etme bulutta da "
        "kaldığı yerden sürer.",
    ("steam", "RPG ve Hikaye Odaklı Oyunlar"):
        "Karakter gelişimi ve anlatı üzerine kurulu yapımlardır.",
    ("steam", "MMO ve Çevrimiçi Yapımlar"):
        "Kalıcı dünyalı, sürekli bağlantı gerektiren yapımlardır.",
    ("steam", "Bağımsız ve Indie Yapımlar"):
        "Küçük ekiplerin ürettiği yapımlardır; kütüphanenin en geniş ve en çeşitli bölümüdür.",

    # ------------------------------------------------------------------ strateji
    ("strateji", "Gerçek Zamanlı Strateji (RTS) Oyunları"):
        "Kaynak toplama, üs kurma ve ordu yönetiminin eş zamanlı yürüdüğü türdür. Karar "
        "hızı en az plan kadar belirleyicidir.",
    ("strateji", "4X Strateji Oyunları"):
        "Keşfet, genişle, işlet ve yok et döngüsü üzerine kurulu türdür. Tek oyun onlarca "
        "saat sürebilir.",
    ("strateji", "Sıra Tabanlı Strateji Oyunları"):
        "Her tarafın sırayla hamle yaptığı türdür. Süre baskısı olmadığı için derin planlamaya "
        "izin verir.",
    ("strateji", "Büyük Strateji (Grand Strategy) Oyunları"):
        "Diplomasi, ekonomi ve savaşı ülke ölçeğinde yöneten türdür. Öğrenme eğrisi diğer "
        "strateji türlerinden diktir.",
    ("strateji", "Şehir İnşası ve Yönetim Oyunları"):
        "Yerleşim planlama ve kaynak dengesi üzerine kurulu türdür. Rakip yerine sistemin "
        "kendisiyle uğraşılır.",

    # ----------------------------------------------------------- ubisoft-connect
    ("ubisoft-connect", "Assassin's Creed Serisi"):
        "Tarihî dönemlerde geçen, gizlilik ve parkur üzerine kurulu açık dünya serisidir. "
        "Her oyun farklı bir dönemde geçer, sıralı oynamak zorunlu değildir.",
    ("ubisoft-connect", "Açık Dünya Aksiyon ve FPS"):
        "Geniş haritalarda serbest yaklaşımlı görevler sunan yapımlardır.",
    ("ubisoft-connect", "Taktiksel ve Çok Oyunculu"):
        "Takım koordinasyonu ve hazırlık aşamasının belirleyici olduğu yapımlardır.",
    ("ubisoft-connect", "Yarış ve Motor Sporları"):
        "Açık dünya yarış ve motor sporu yapımlarıdır. Etkinlikler harita üzerinden açılır.",
    ("ubisoft-connect", "Strateji ve Yönetim"):
        "Planlama ve kaynak yönetimi üzerine kurulu yapımlardır.",

    # ---------------------------------------------------------------------- xbox
    ("xbox", "FPS ve Shooter"):
        "Xbox ve Game Pass kataloğundaki nişancı yapımlardır. Microsoft hesabı bağlandıktan "
        "sonra desteklenen oyunlar bulutta listelenir.",
    ("xbox", "Yarış ve Simülasyon"):
        "Açık dünya yarış ve simülasyon yapımlarıdır.",
    ("xbox", "RPG ve Macera"):
        "Uzun soluklu, karakter gelişimi olan yapımlardır.",
    ("xbox", "Kooperatif ve Survival"):
        "Grup halinde oynanan, kaynak yönetimi içeren yapımlardır.",
    ("xbox", "Strateji"):
        "Planlama ağırlıklı yapımlardır; konsol kökenli olanlarda kontrolcü desteği hazırdır.",

    # --------------------------------------------------------------------- yaris
    ("yaris", "Açık Dünya ve Arcade Yarış"):
        "Pist yerine serbest gezilebilen harita sunan, fizik modeli affedici yarış türüdür. "
        "Etkinlikler harita üzerinde dağıtılmıştır.",
    ("yaris", "Yarış Simülasyonu (Sim Racing)"):
        "Lastik sıcaklığı, yakıt ve süspansiyon gibi değişkenleri modelleyen türdür. "
        "Direksiyon seti ile oynandığında fark en çok burada hissedilir.",
    ("yaris", "Ralli ve Off-Road"):
        "Değişken zeminde, ko-pilot notlarıyla ilerlenen yarış türüdür. Pist ezberi yerine "
        "anlık tepki gerekir.",
    ("yaris", "Motosiklet ve MotoGP"):
        "İki tekerlekli araçların denge ve viraj çizgisi üzerine kurulu türdür. Hata payı "
        "otomobil yarışlarından düşüktür.",
    ("yaris", "Drift, Modifiye ve JDM Kültürü"):
        "Tur süresi yerine kontrollü kayma ve stil puanı üzerine kurulu türdür. Araç "
        "ayarları oynanışı doğrudan değiştirir.",
    ("yaris", "Kart, Demolition ve Aile Yarışı"):
        "Gerçekçilik iddiası olmayan, bölünmüş ekran ve grup oyununa uygun yarış türüdür.",
})


# =============================================================================
# 2) EK SSS  {slug: [(soru, cevap), ...]}
#    Alt tur ve arama niyeti odakli; mevcut SSS'lerin SONUNA eklenir ve FAQ
#    Schema'ya da girer. Cevaplar tur mekanigi duzeyinde kalir, belirli bir oyuna
#    dair dogrulanmamis iddia icermez.
# =============================================================================

EK_FAQ = {
 "aile-dostu": [
   ("Aile dostu oyunlarda bölünmüş ekran (split screen) var mı?",
    "Kooperatif aile yapımlarının bir bölümü aynı ekranda iki oyuncuyu destekler, bir bölümü ise "
    "yalnızca çevrimiçi kooperatif sunar. Bulutta oynarken bölünmüş ekran oyunun kendi desteğine "
    "bağlıdır; GeForce NOW oyunu olduğu gibi çalıştırır, ek bir kısıt getirmez."),
   ("Kooperatif aile oyunlarında ikinci oyuncunun da aboneliği gerekir mi?",
    "Aynı ekranda, tek cihazda oynanan bölünmüş ekran modlarında tek oturum yeterlidir. İki oyuncu "
    "ayrı cihazlardan çevrimiçi bağlanacaksa her iki tarafın da kendi oturumu ve oyunun lisansı "
    "olması gerekir."),
   ("Çocuklar için hangi aile dostu alt tür daha uygun?",
    "Kontrol şeması sade olduğu için LEGO ve lisanslı çocuk yapımları ile aile dostu platform "
    "oyunları giriş için en kolay alt türlerdir. Cozy yaşam simülasyonlarında kaybetme koşulu "
    "bulunmaz, bu da baskı hissetmeden oynamayı sağlar."),
 ],
 "aksiyon": [
   ("Soulslike ile hack-and-slash arasındaki fark nedir?",
    "Soulslike yapımlarda tempo yavaş, ceza yüksektir ve her düşman ayrı bir kalıp öğrenmeyi "
    "gerektirir. Hack-and-slash'te ise amaç kalabalık gruplara karşı kesintisiz kombo kurmaktır; "
    "hata cezası düşük, akıcılık ön plandadır."),
   ("Aksiyon oyunları için gamepad mi klavye-fare mi daha uygun?",
    "Yakın dövüş ve platform ağırlıklı aksiyon yapımlarında gamepad analog kontrol avantajı sunar. "
    "Nişan alma içeren FPS ve TPS alt türlerinde klavye-fare daha hassastır. GeForce NOW her iki "
    "kontrol yöntemini de destekler."),
   ("Açık dünya aksiyon oyunları bulutta ne kadar veri harcar?",
    "Bulut oyun tüketimi oyunun içeriğine değil çözünürlük ve kare hızına bağlıdır. 1080p 60 FPS "
    "yayında saatlik tüketim yaklaşık 7-10 GB bandında seyreder; 4K seçeneklerinde bu değer artar."),
 ],
 "arcade": [
   ("Arcade oyunları ile retro oyunlar aynı şey mi?",
    "Arcade, salon makineleri için tasarlanmış kısa oturumlu ve yüksek skor odaklı tasarımı "
    "anlatır. Retro ise yalnızca dönemi belirtir. Modern arcade yapımları güncel olabilir; buna "
    "karşılık her retro oyun arcade tasarımına sahip değildir."),
   ("Arcade oyunları kısa oturumlar için uygun mu?",
    "Evet. Bu türün tasarım hedefi tek turun birkaç dakikada bitmesidir. Bulutta kurulum ve güncelleme "
    "beklemesi olmadığı için kısa molalarda açıp kapatmaya uygundur."),
   ("Arcade dövüş oyunlarında çevrimiçi maç yapılabilir mi?",
    "Klasik derlemelerin çoğu çevrimiçi eşleşme desteğiyle yeniden yayımlandı. Rekabetçi oyunda "
    "gecikme belirleyici olduğu için Türkiye sunucusu üzerinden oynamak fark yaratır."),
 ],
 "bagimsiz": [
   ("Roguelike ile roguelite arasındaki fark nedir?",
    "İkisinde de bölümler her denemede yeniden üretilir. Fark kalıcılıkta: roguelite'ta denemeler "
    "arasında kalan yükseltmeler vardır ve oyuncu zamanla güçlenir, klasik roguelike'ta her tur "
    "sıfırdan başlar."),
   ("İndie oyunlar ne kadar sürer?",
    "Bağımsız yapımların süresi alt türe göre değişir. Atmosferik ve anlatı odaklı yapımlar çoğu "
    "zaman tek oturumda bitirilebilir; metroidvania ve roguelite yapımlarda oyun süresi onlarca "
    "saate çıkabilir."),
   ("Metroidvania oyunlarına nereden başlanmalı?",
    "Bu alt türde harita ezberi ve yetenek sırası önemlidir. Yeni başlayan bir oyuncu için ölüm "
    "cezası düşük, harita üzerinde işaret bırakmaya izin veren yapımlar daha uygundur."),
 ],
 "basit-eglence": [
   ("Casual oyun ile party oyunu arasındaki fark nedir?",
    "Casual, kuralları basit ve öğrenme süresi kısa her yapımı kapsar; tek başına da oynanabilir. "
    "Party oyunları ise özellikle grup halinde, kısa turlarla oynanmak üzere tasarlanır."),
   ("Casual oyunlar için güçlü bir bilgisayar gerekir mi?",
    "Bu türün donanım talebi genelde düşüktür, ancak bulutta oynarken işlem zaten sunucuda yapılır. "
    "Belirleyici olan cihazın gücü değil, bağlantının kararlılığıdır."),
   ("Kısa molalarda oynanabilecek alt türler hangileri?",
    "Roguelite casual yapımlar ve mini-oyun koleksiyonları birkaç dakikalık turlar hâlinde "
    "ilerler. Cozy yaşam simülasyonlarında da kaybetme koşulu olmadığı için oturum istenildiği "
    "an sonlandırılabilir."),
 ],
 "bulmaca": [
   ("Bulmaca oyunları ile zeka oyunları aynı şey mi?",
    "Bulmaca oyunları belirli bir çözümü olan bölümler sunar. Zeka oyunları ise daha çok pratik ve "
    "hız üzerine kuruludur. Fizik ve mühendislik bulmacalarında ise tek doğru çözüm bulunmaz, "
    "farklı verimlilikte pek çok yol vardır."),
   ("Bulmaca oyunları bulutta gecikmeden etkilenir mi?",
    "Bu tür refleks gerektirmediği için gecikmeye en az duyarlı kategorilerden biridir. Çözüm "
    "süresi düşünmeye bağlıdır, milisaniyelik farklar oynanışı etkilemez."),
   ("İki kişi birlikte oynanabilecek bulmaca oyunu var mı?",
    "Kooperatif bulmaca ve escape room yapımları tam olarak bunun için tasarlanır. Oyuncular farklı "
    "bilgi parçalarını görür ve çözüm ancak konuşarak bulunur; tek başına oynanamaz."),
 ],
 "canlandirma": [
   ("CRPG ile JRPG arasındaki fark nedir?",
    "CRPG'de karakteri oyuncu yaratır, kural tabanlı savaş ve diyalog seçimleri öndedir. JRPG'de "
    "kadro önceden belirlenmiştir ve anlatı çizgisi daha güçlüdür; savaş çoğunlukla sıra tabanlı "
    "ya da yarı gerçek zamanlıdır."),
   ("RPG oyunlarına yeni başlayanlar hangi alt türle başlamalı?",
    "Sinematik hikâye odaklı RPG'ler kural karmaşıklığı düşük olduğu için giriş noktası olarak "
    "daha uygundur. Klasik CRPG ve büyük strateji benzeri sistem yoğunluğu olan alt türler daha "
    "sonra denenebilir."),
   ("RPG oyunları ne kadar sürer?",
    "Alt türe göre değişir. Sinematik RPG'ler genellikle 20-40 saat bandındadır; açık dünya ve "
    "MMO RPG'lerde süre yan içerikle birlikte yüzlerce saate çıkabilir."),
 ],
 "demo": [
   ("Demo oyunlar ücretsiz mi?",
    "Evet, demo sürümleri ücretsizdir. Bulutta açmak için ilgili mağaza hesabının bağlı olması "
    "yeterlidir, ayrıca oyun lisansı gerekmez."),
   ("Demo ilerlemem tam sürüme aktarılır mı?",
    "Bu, oyunun kendi tercihine bağlıdır. Özellikle JRPG ve aksiyon-RPG demolarında ilerlemenin "
    "tam sürüme taşınması yaygındır; her demo bunu desteklemez."),
   ("Demo oynamak için ne kadar süre gerekir?",
    "Demolar çoğunlukla 30 dakika ile 2 saat arasında bir kesit sunar. Bulutta indirme beklemesi "
    "olmadığı için bu süre doğrudan oynamaya ayrılır."),
 ],
 "diger": [
   ("Battle.net hesabı GeForce NOW'a nasıl bağlanır?",
    "GeForce NOW uygulamasındaki hesap ayarlarından ilgili mağaza bağlanır ve oyun ilk açılışta "
    "giriş bilgilerini ister. Bağlantı bir kez kurulduktan sonra sonraki oturumlarda hatırlanır."),
   ("Bağımsız yayıncı oyunları için ayrı abonelik gerekir mi?",
    "GeForce NOW aboneliği oyunu çalıştırma hakkı verir. Oyunun kendi aboneliği varsa (bazı MMO ve "
    "sezonluk yapımlarda olduğu gibi) o ayrıca gereklidir."),
   ("Bu kategorideki oyunlar mobil cihazda oynanabilir mi?",
    "Desteklenen cihazlarda oynanabilir; belirleyici olan oyunun kontrol şemasıdır. Kontrolcü "
    "desteği olan yapımlar mobilde daha rahat oynanır."),
 ],
 "dovus-oyunu": [
   ("2D dövüş ile 3D arena dövüş arasındaki fark nedir?",
    "2D dövüşte hareket tek eksende olur, mesafe yönetimi ve giriş dizileri belirleyicidir. 3D "
    "arena dövüşte karakterler yana kaçabilir; bu, mesafe oyununa ek bir boyut katar."),
   ("Dövüş oyunlarında gecikme ne kadar önemli?",
    "Bu tür, gecikmeye en duyarlı kategorilerden biridir. Giriş zamanlaması kare düzeyinde "
    "çalıştığı için Türkiye sunucusu üzerinden oynamak rekabetçi maçlarda belirgin fark yaratır."),
   ("Dövüş oyunlarına yeni başlayanlar için hangi alt tür uygun?",
    "Platform brawler ve party fighter yapımları giriş dizisi ezberi gerektirmediği için en kolay "
    "başlangıçtır. Klasik 2D dövüş, rekabetçi sahnenin temeli olmakla birlikte daha dik bir "
    "öğrenme eğrisine sahiptir."),
 ],
 "ea-app": [
   ("EA App hesabı GeForce NOW'a nasıl bağlanır?",
    "Uygulamadaki hesap ayarlarından EA App bağlanır; oyun ilk açılışta giriş bilgilerini ister. "
    "Bağlantı bir kez kurulduktan sonra kütüphanedeki desteklenen oyunlar listelenir."),
   ("EA Play aboneliği GeForce NOW aboneliğine dahil mi?",
    "Hayır, ikisi ayrı hizmetlerdir. GeForce NOW oyunu bulutta çalıştırır; EA Play kataloğuna "
    "erişim için o aboneliğin ayrıca bulunması gerekir."),
   ("Battlefield gibi büyük haritalı FPS'ler bulutta akıcı çalışır mı?",
    "Bu yapımlarda belirleyici olan bilgisayarın gücü değil bağlantı kararlılığıdır. 1080p 60 FPS "
    "için önerilen bant genişliği sağlandığında büyük haritalı modlar sorunsuz oynanır."),
 ],
 "epic-games": [
   ("Epic Games hesabı GeForce NOW'a nasıl bağlanır?",
    "Uygulamadaki hesap ayarlarından Epic Games Store bağlanır. Bağlantı kurulduktan sonra "
    "kütüphanedeki desteklenen oyunlar bulutta listelenir."),
   ("Epic'in ücretsiz haftalık oyunları bulutta oynanabilir mi?",
    "Hesabına eklediğin ücretsiz oyunlar, GeForce NOW tarafından destekleniyorsa bulutta açılır. "
    "Desteklenmeyen yapımlar listede görünmez."),
   ("Epic Games kütüphanemdeki tüm oyunlar bulutta çalışır mı?",
    "Hayır. GeForce NOW yalnızca yayıncısının izin verdiği yapımları çalıştırır. Kütüphanendeki "
    "desteklenen oyunlar hesap bağlandıktan sonra otomatik olarak listelenir."),
 ],
 "fps": [
   ("Taktiksel FPS ile arena FPS arasındaki fark nedir?",
    "Taktiksel FPS'te tempo yavaştır, tek isabet ölümcül olabilir ve ekonomi yönetimi vardır. "
    "Klasik arena FPS'te ise sürekli hareket zorunludur; sağlık ve mühimhat harita üzerinden "
    "toplanır."),
   ("FPS oyunlarında bulut gecikmesi rekabeti etkiler mi?",
    "Rekabetçi modlarda gecikme doğrudan hissedilir. Türkiye sunucuları üzerinden oynandığında "
    "coğrafi yakınlık sayesinde gecikme düşük tutulur; sıralı maçlar için kablolu bağlantı "
    "önerilir."),
   ("FPS oyunlarında kaç FPS'e kadar çıkılabilir?",
    "Ulaşılabilecek kare hızı seçilen pakete ve oyunun kendi sınırına bağlıdır. Rekabetçi "
    "yapımlarda yüksek kare hızı nişan takibini kolaylaştırdığı için tercih edilir."),
 ],
 "gog": [
   ("GOG hesabı GeForce NOW'a nasıl bağlanır?",
    "Uygulamadaki hesap ayarlarından GOG bağlanır; desteklenen oyunlar bağlantı kurulduktan sonra "
    "kütüphanede listelenir."),
   ("GOG oyunları DRM'siz, bulutta da öyle mi çalışıyor?",
    "GOG kütüphanesi DRM'siz dağıtımıyla bilinir. Bulutta oynarken oyun yine senin hesabına bağlı "
    "olarak çalıştırılır; GeForce NOW oyunu satmaz, yalnızca uzaktan çalıştırır."),
   ("GOG kütüphanemdeki her oyun bulutta açılır mı?",
    "Hayır. Yalnızca yayıncısının bulut oyun izni verdiği yapımlar desteklenir; kalanlar listede "
    "görünmez."),
 ],
 "macera": [
   ("Macera oyunu ile aksiyon-macera arasındaki fark nedir?",
    "Saf macera yapımlarında ilerleme keşif ve bulmaca çözmeye dayanır. Aksiyon-macerada bunlara "
    "düzenli çatışma eklenir; tempo daha değişkendir."),
   ("Hikâye odaklı macera oyunları tekrar oynanır mı?",
    "Seçim tabanlı yapımlarda farklı kararlar farklı sonlara götürür, bu da ikinci oynanışı "
    "anlamlı kılar. Doğrusal sinematik yapımlarda tekrar değeri daha düşüktür."),
   ("Açık dünya macera oyunları ne kadar sürer?",
    "Ana hikâye çoğu yapımda 15-30 saat bandındadır; yan içerikle birlikte bu süre iki katına "
    "kadar çıkabilir."),
 ],
 "mmo": [
   ("MMO ile MMORPG arasındaki fark nedir?",
    "MMO, çok sayıda oyuncunun aynı dünyada bulunduğu her yapımı kapsar. MMORPG ise buna rol yapma "
    "sistemlerini, karakter sınıflarını ve seviye ilerlemesini ekler."),
   ("MMO oyunları uzun oturumlar için bulutta uygun mu?",
    "Uygundur; oturum süresi seçilen pakete bağlıdır ve oturum sonunda kaldığın yerden devam "
    "edilir. Baskın gibi uzun etkinliklerde kararlı bağlantı önemlidir."),
   ("Themepark ile sandbox MMO arasındaki fark nedir?",
    "Themepark MMO'da içerik belirli bir sırayla sunulur ve yol geliştirici tarafından çizilir. "
    "Sandbox MMO'da ekonomi ve çatışma büyük ölçüde oyuncular tarafından şekillendirilir."),
 ],
 "moba": [
   ("MOBA oyunlarında gecikme ne kadar kritik?",
    "Yetenek zamanlaması ve son vuruş milisaniye düzeyinde çalıştığı için MOBA, gecikmeye en "
    "duyarlı türlerden biridir. Türkiye sunucuları üzerinden oynamak bu farkı azaltır."),
   ("MOBA oyunları ücretsiz mi?",
    "Bu türün büyük çoğunluğu oynaması ücretsizdir. Rekabetçi dengeyi korumak için satın alınabilen "
    "içerik genellikle görsel öğelerle sınırlıdır."),
   ("Bir MOBA maçı ne kadar sürer?",
    "Klasik 5v5 maçlar çoğunlukla 25-40 dakika arasında sürer. Battle royale hibritlerinde tur "
    "süresi daha kısadır."),
 ],
 "oynamasi-ucretsiz": [
   ("Ücretsiz oyunlar için GeForce NOW aboneliği gerekir mi?",
    "Oyunun kendisi ücretsizdir; bulutta çalıştırmak için GeForce NOW oturumu gerekir. Ücretsiz "
    "yapımlarda ayrıca oyun lisansı satın alman gerekmez, mağaza hesabı yeterlidir."),
   ("Ücretsiz oyunlarda para harcamadan ilerlenebilir mi?",
    "Rekabetçi türlerde satın alınabilen içerik genellikle görseldir ve oynanışı etkilemez. "
    "İlerleme hızını etkileyen öğeler bulunan yapımlarda ise bu durum oyundan oyuna değişir."),
   ("Ücretsiz oyunlarda hangi alt tür en kalabalık?",
    "Battle royale ve hero shooter yapımları oyuncu yoğunluğu en yüksek alt türlerdir; bu da "
    "eşleşme sürelerini kısaltır."),
 ],
 "oyunlar": [
   ("GeForce NOW'da hangi oyunlar oynanabilir?",
    "Yalnızca yayıncısının bulut oyun izni verdiği yapımlar desteklenir. Mağaza hesabını "
    "bağladıktan sonra kütüphanendeki desteklenen oyunlar otomatik olarak listelenir."),
   ("Oyun kütüphanem hangi mağazalardan bağlanabilir?",
    "Steam, Epic Games Store, Xbox ve Game Pass, EA App, Ubisoft Connect, GOG ve Battle.net "
    "hesapları bağlanabilir. Her mağaza için desteklenen oyun listesi ayrıdır."),
   ("Bulutta oynamak için oyunu indirmem gerekir mi?",
    "Hayır. Oyun sunucuda çalışır, cihazına yalnızca görüntü akar. Güncelleme ve kurulum beklemesi "
    "olmaz."),
 ],
 "platform": [
   ("Metroidvania ile klasik 2D platform arasındaki fark nedir?",
    "Klasik 2D platformda bölümler sırayla geçilir. Metroidvania'da ise tek parça bir harita vardır "
    "ve yeni yetenek kazandıkça önceden geçilemeyen alanlar açılır; geri dönüş tasarımın "
    "parçasıdır."),
   ("Platform oyunları gamepad ile mi oynanmalı?",
    "Analog kontrol zıplama mesafesini ayarlamayı kolaylaştırdığı için gamepad yaygın tercihtir. "
    "Klavye de desteklenir; seçim oyuncunun alışkanlığına bağlıdır."),
   ("Platform oyunları bulutta gecikmeden etkilenir mi?",
    "Hassas zamanlama gerektiren bölümlerde gecikme hissedilebilir. Türkiye sunucuları üzerinden "
    "oynandığında bu fark düşük seviyede kalır."),
 ],
 "populer-oyunlar": [
   ("En çok oynanan oyunlar listesi ne sıklıkla değişir?",
    "Kütüphane sürekli güncellendiği için liste sabit değildir. Sezonluk güncellemeler ve yeni "
    "çıkışlar sıralamayı dönem dönem değiştirir."),
   ("Popüler oyunlar bulutta daha mı yavaş açılır?",
    "Hayır. Oyun sunucuda hazır çalıştığı için açılış süresi popülerlikten bağımsızdır; yoğun "
    "saatlerde oturum bekleme süresi seçilen pakete göre değişebilir."),
   ("Çok oyunculu popüler yapımlarda eşleşme süresi ne kadar?",
    "Oyuncu yoğunluğu yüksek olduğu için eşleşme genellikle hızlıdır. Süre, oyunun kendi "
    "sunucularına ve seçilen moda bağlıdır."),
 ],
 "simulasyon": [
   ("Simülasyon oyunları için direksiyon seti veya joystick şart mı?",
    "Şart değil, gamepad ve klavye ile de oynanır. Ancak yarış ve uçuş simülasyonlarında bu "
    "donanımlar kontrol hassasiyetini belirgin biçimde artırır."),
   ("Simülasyon oyunları yeni başlayanlar için zor mu?",
    "Alt türe göre değişir. Yaşam ve çiftlik simülasyonları giriş için en kolay olanlardır; uçuş "
    "ve koloni simülasyonlarında öğrenme eğrisi belirgin biçimde diktir."),
   ("Şehir inşası oyunları uzun oturum gerektirir mi?",
    "Bu alt türde kararların sonucu saatler içinde görülür, bu yüzden oturumlar uzun olma "
    "eğilimindedir. Bulutta kaldığın yerden devam edebildiğin için oturumu bölmek mümkündür."),
 ],
 "spor": [
   ("Spor oyunlarında arcade ile simülasyon farkı nedir?",
    "Arcade spor yapımları kuralları sadeleştirir ve tempoyu öne çıkarır. Simülasyon tarafında "
    "gerçek kural setleri, oyuncu istatistikleri ve fizik modeli ayrıntılı biçimde işlenir."),
   ("Spor oyunları iki kişi aynı ekranda oynanabilir mi?",
    "Birçok spor yapımı yerel çok oyunculu modu destekler. Bulutta bu, oyunun kendi desteğine "
    "bağlıdır; GeForce NOW ek bir kısıt getirmez."),
   ("Spor oyunlarında sezon güncellemeleri bulutta otomatik gelir mi?",
    "Evet. Oyun sunucu tarafında güncellendiği için indirme ya da yama bekleme olmaz, oturumu "
    "açtığında güncel sürümle başlarsın."),
 ],
 "steam": [
   ("Steam hesabı GeForce NOW'a nasıl bağlanır?",
    "Uygulamadaki hesap ayarlarından Steam bağlanır ve oyun ilk açılışta giriş bilgilerini ister. "
    "Bağlantı kurulduktan sonra desteklenen oyunlar kütüphanede listelenir."),
   ("Steam kütüphanemdeki her oyun bulutta çalışır mı?",
    "Hayır. Yalnızca yayıncısının bulut oyun izni verdiği yapımlar desteklenir. Desteklenmeyen "
    "oyunlar listede görünmez."),
   ("Steam bulut kayıtları (Steam Cloud) GeForce NOW ile senkron çalışır mı?",
    "Oyun Steam Cloud kullanıyorsa kayıtlar hesabına bağlı kalır ve cihaz değiştirdiğinde kaldığın "
    "yerden devam edebilirsin. Bu, oyunun kendi kayıt sistemine bağlıdır."),
 ],
 "strateji": [
   ("RTS ile sıra tabanlı strateji arasındaki fark nedir?",
    "RTS'te hamleler eş zamanlı yürür, karar hızı belirleyicidir. Sıra tabanlı stratejide her "
    "taraf sırayla oynar; süre baskısı olmadığı için daha derin planlamaya izin verir."),
   ("4X strateji oyunları ne kadar sürer?",
    "Tek bir oyun genellikle onlarca saat sürer. Bulutta kaldığın yerden devam edebildiğin için "
    "uzun kampanyaları birden çok oturuma bölmek mümkündür."),
   ("Strateji oyunları için yüksek kare hızı gerekir mi?",
    "Bu türde kare hızı refleksten çok okunabilirlik meselesidir. Kalabalık birim gruplarında "
    "yüksek kare hızı takibi kolaylaştırır, ancak rekabetçi FPS kadar belirleyici değildir."),
 ],
 "ubisoft-connect": [
   ("Ubisoft Connect hesabı GeForce NOW'a nasıl bağlanır?",
    "Uygulamadaki hesap ayarlarından Ubisoft Connect bağlanır. Bağlantı kurulduktan sonra "
    "kütüphanendeki desteklenen yapımlar listelenir."),
   ("Ubisoft+ aboneliği GeForce NOW aboneliğine dahil mi?",
    "Hayır, ikisi ayrı hizmetlerdir. GeForce NOW oyunu bulutta çalıştırır; Ubisoft+ kataloğuna "
    "erişim için o aboneliğin ayrıca bulunması gerekir."),
   ("Assassin's Creed serisi hangi sırayla oynanmalı?",
    "Her oyun kendi dönemi ve kahramanıyla bağımsız bir hikâye anlatır, bu yüzden çıkış sırasını "
    "takip etmek zorunlu değildir. Modern zaman anlatısını bütün hâlinde takip etmek isteyenler "
    "için çıkış sırası daha tutarlı bir deneyim sunar."),
 ],
 "xbox": [
   ("Game Pass aboneliği GeForce NOW aboneliğine dahil mi?",
    "Hayır, ikisi ayrı hizmetlerdir. GeForce NOW oyunu bulutta çalıştırır; Game Pass kataloğuna "
    "erişim için o aboneliğin ayrıca bulunması gerekir."),
   ("Xbox oyunları bulutta kontrolcü ile mi oynanmalı?",
    "Konsol kökenli yapımlarda kontrolcü şeması hazır geldiği için gamepad daha rahattır. Klavye "
    "ve fare de desteklenir."),
   ("Xbox kütüphanemdeki her oyun bulutta çalışır mı?",
    "Hayır. Yalnızca yayıncısının bulut oyun izni verdiği yapımlar desteklenir; desteklenenler "
    "hesap bağlandıktan sonra otomatik listelenir."),
 ],
 "yaris": [
   ("Arcade yarış ile yarış simülasyonu arasındaki fark nedir?",
    "Arcade yarışta fizik modeli affedicidir, sürüş yardımları açıktır ve tempo öne çıkar. "
    "Simülasyonda lastik sıcaklığı, yakıt ve süspansiyon gibi değişkenler modellenir; hata payı "
    "belirgin biçimde düşüktür."),
   ("Yarış oyunlarında direksiyon seti farkı ne kadar hissedilir?",
    "Arcade yapımlarda fark sınırlı kalır. Yarış simülasyonlarında ise güç geri beslemesi lastik "
    "tutuşunu doğrudan aktardığı için fark en çok bu alt türde hissedilir."),
   ("Ralli oyunları pist yarışlarından neden daha zor?",
    "Ralli parkurları ezberlenmek yerine ko-pilot notlarıyla anlık okunur ve zemin sürekli değişir. "
    "Bu, pist yarışındaki tur ezberine göre daha yüksek tepki hızı gerektirir."),
 ],
}


# =============================================================================
# 3) KATEGORI TANIMI - H2'nin hemen altina, ilk 100 kelime icinde
#    Iki isi birden yapar: (a) AI Overview icin kategori duzeyinde tanim-once
#    cumlesi, (b) slug terimi ile piyasa terimini ayni cumlede bulusturur.
#    Denetimde 5 kategoride slug terimi metinde HIC gecmiyordu (canlandirma,
#    basit-eglence, diger, bagimsiz, ea-app); bu blok o acigi kapatir.
# =============================================================================

KATEGORI_TANIM = {
 "aile-dostu": ("Aile dostu oyunlar nedir?",
   "Şiddet içeriği düşük tutulan, çocuklarla birlikte oynanabilen ve çoğunlukla kooperatif "
   "mod sunan yapımlardır. GeForce NOW'da bu kategori LEGO ve lisanslı çocuk yapımlarından "
   "cozy yaşam simülasyonlarına kadar uzanır."),
 "aksiyon": ("Aksiyon oyunları nedir?",
   "Refleks, zamanlama ve dövüşün merkezde olduğu geniş bir türdür. Battle royale, soulslike, "
   "hack-and-slash ve açık dünya aksiyon gibi birbirinden belirgin biçimde ayrışan alt türleri "
   "vardır."),
 "arcade": ("Arcade oyunları nedir?",
   "Salon makineleri için tasarlanmış kısa oturumlu, yüksek skor odaklı tasarımı sürdüren "
   "yapımlardır. Retro derlemeler kadar aynı tasarım anlayışını taşıyan güncel yapımları da "
   "kapsar."),
 "bagimsiz": ("Bağımsız (indie) oyunlar nedir?",
   "Büyük yayıncı desteği olmadan, küçük ekipler tarafından geliştirilen yapımlardır. Bağımsız "
   "oyunlar bütçe yerine mekanik ya da anlatı özgünlüğüyle öne çıkar; metroidvania, roguelite ve "
   "yaşam simülasyonu bu kategorinin en yoğun alt türleridir."),
 "basit-eglence": ("Basit eğlence (casual) oyunları nedir?",
   "Kuralları kısa sürede öğrenilen, tek oturumu birkaç dakikayla sınırlı tutulabilen "
   "yapımlardır. Basit eğlence kategorisi party oyunlarından cozy yaşam simülasyonlarına kadar "
   "geniş bir yelpazeyi kapsar."),
 "bulmaca": ("Bulmaca oyunları nedir?",
   "Çözümü düşünmeye ve sistemi anlamaya dayanan, refleks gerektirmeyen yapımlardır. Fizik "
   "bulmacalarından programlama bulmacalarına kadar birbirinden farklı zorluk türleri barındırır."),
 "canlandirma": ("Canlandırma (RPG) oyunları nedir?",
   "Karakter gelişimi, seçim ve anlatı üzerine kurulu rol yapma yapımlarıdır. GeForce NOW'da "
   "canlandırma kategorisi klasik CRPG'den JRPG'ye, aksiyon RPG'den MMORPG'ye kadar tüm rol "
   "yapma alt türlerini kapsar."),
 "demo": ("Demo oyunlar nedir?",
   "Tam sürümün ücretsiz oynanabilen bir kesitidir. Satın almadan önce dövüş hissini, tempoyu ve "
   "performansı denemeye yarar; bulutta indirme beklemesi olmadığı için süre doğrudan oynamaya "
   "ayrılır."),
 "diger": ("Diğer yayıncı oyunları nedir?",
   "Steam, Epic Games ve Xbox dışındaki mağaza ve başlatıcılara bağlı yapımlardır. Bu kategoride "
   "Battle.net, HoYoverse ve kendi başlatıcısını kullanan diğer yayıncıların oyunları toplanır."),
 "dovus-oyunu": ("Dövüş oyunları nedir?",
   "İki oyuncunun karşılıklı mücadele ettiği, giriş zamanlaması ve mesafe yönetimi üzerine kurulu "
   "türdür. 2D, 3D arena, platform brawler ve beat 'em up olmak üzere dört ana kolu vardır."),
 "ea-app": ("EA App oyunları nedir?",
   "Electronic Arts'ın kendi mağazası EA App üzerinden dağıtılan yapımlardır. EA App hesabı "
   "GeForce NOW'a bağlandığında kütüphanedeki desteklenen oyunlar bulutta listelenir."),
 "epic-games": ("Epic Games oyunları nedir?",
   "Epic Games Store üzerinden edinilen yapımlardır. Hesap GeForce NOW'a bağlandığında "
   "kütüphanedeki desteklenen oyunlar, ücretsiz haftalık yapımlar dahil, bulutta listelenir."),
 "fps": ("FPS oyunları nedir?",
   "FPS, \"First Person Shooter\" yani birinci şahıs nişancı türünün kısaltmasıdır. Rekabetçi "
   "taktiksel yapımlardan hikâye odaklı kampanyalara kadar birbirinden ayrışan alt türleri "
   "bulunur."),
 "gog": ("GOG oyunları nedir?",
   "GOG, DRM'siz dağıtımıyla bilinen bir oyun mağazasıdır ve CD Projekt RED kataloğunun ana "
   "dağıtım kanalıdır. GOG hesabı bağlandığında desteklenen yapımlar GeForce NOW kütüphanesinde "
   "görünür."),
 "macera": ("Macera oyunları nedir?",
   "İlerlemenin keşif, bulmaca ve hikâye üzerinden kurulduğu türdür. Açık dünya macera, "
   "aksiyon-macera ve sinematik macera olmak üzere tempo bakımından belirgin biçimde ayrışan "
   "alt kolları vardır."),
 "mmo": ("MMO oyunlar nedir?",
   "MMO, çok sayıda oyuncunun aynı kalıcı dünyada bulunduğu yapımları anlatır. MMORPG ise buna "
   "karakter sınıfları ve seviye ilerlemesi ekleyen alt türdür."),
 "moba": ("MOBA oyunlar nedir?",
   "MOBA, \"Multiplayer Online Battle Arena\" kısaltmasıdır; iki takımın koridorlu bir haritada "
   "rakip üssü yıkmaya çalıştığı türü anlatır. Maç içi ekonomi ve harita kontrolü sonucu "
   "belirler."),
 "oynamasi-ucretsiz": ("Ücretsiz oyunlar nedir?",
   "Oynamak için satın alma gerektirmeyen, gelirini çoğunlukla kozmetik içerikten sağlayan "
   "yapımlardır. Ücretsiz oyunlar için ayrıca lisans almana gerek yoktur, mağaza hesabı "
   "yeterlidir."),
 "oyunlar": ("GeForce NOW oyunları nedir?",
   "GeForce NOW, sahip olduğun oyunları NVIDIA'nın bulut sunucularında çalıştırıp cihazına "
   "aktaran bir bulut oyun servisidir. Kütüphanede yalnızca yayıncısının bulut izni verdiği "
   "yapımlar bulunur."),
 "platform": ("Platform oyunları nedir?",
   "Zıplama, tırmanma ve zamanlama üzerine kurulu türdür. 2D ve 3D platform yapımlarının yanında "
   "tek parça haritada ilerleyen metroidvania alt türünü de kapsar."),
 "populer-oyunlar": ("Popüler oyunlar nedir?",
   "GeForce NOW kütüphanesinde en çok oynanan ve en çok aranan yapımlardır. Liste sabit değildir; "
   "sezonluk güncellemeler ve yeni çıkışlarla dönem dönem değişir."),
 "simulasyon": ("Simülasyon oyunları nedir?",
   "Gerçek bir sistemi ya da mesleği kurallarıyla birlikte modelleyen türdür. Araç ve uçuş "
   "simülasyonlarından şehir inşasına ve üretim otomasyonuna kadar uzanır."),
 "spor": ("Spor oyunları nedir?",
   "Gerçek spor dallarını kural setiyle birlikte oyunlaştıran türdür. Arcade uçta tempo, "
   "simülasyon uçta istatistik ve fizik modeli öne çıkar."),
 "steam": ("Steam oyunları nedir?",
   "Steam üzerinden edinilen yapımlardır. Steam hesabı GeForce NOW'a bağlandığında kütüphanendeki "
   "desteklenen oyunlar bulutta listelenir; kütüphanenin tamamı değil, yalnız izin verilenler "
   "görünür."),
 "strateji": ("Strateji oyunları nedir?",
   "Kaynak yönetimi ve planlamanın refleksin önünde olduğu türdür. Gerçek zamanlı (RTS), sıra "
   "tabanlı, 4X ve büyük strateji olmak üzere dört ana kolu vardır."),
 "ubisoft-connect": ("Ubisoft Connect oyunları nedir?",
   "Ubisoft'un kendi başlatıcısı Ubisoft Connect üzerinden çalışan yapımlardır. Hesap "
   "bağlandığında Assassin's Creed serisi başta olmak üzere desteklenen oyunlar bulutta "
   "listelenir."),
 "xbox": ("Xbox oyunları nedir?",
   "Xbox ve Game Pass kataloğundaki, PC sürümü desteklenen yapımlardır. Microsoft hesabı "
   "bağlandığında kütüphanendeki desteklenen oyunlar bulutta görünür."),
 "yaris": ("Yarış oyunları nedir?",
   "Araç kontrolü ve tur süresi üzerine kurulu türdür. Affedici fizikli arcade yarıştan lastik ve "
   "yakıtın modellendiği yarış simülasyonuna kadar geniş bir yelpazeyi kapsar."),
}


# Slug terimi metinde hala seyrek kalan 6 kategori icin, terimi DOGAL kullanan
# birer soru daha. Amac yogunlugu zorla yukseltmek degil; terimi bir sorgu
# kaliniba oturtmak. (Denetim: exact-phrase yogunlugu %0.3 altindaydi.)
EK_FAQ["bagimsiz"].append(
  ("Bağımsız oyunlar ile büyük yapımlar arasındaki fark nedir?",
   "Bağımsız oyunlar küçük ekiplerce, büyük yayıncı bütçesi olmadan geliştirilir. Bu yüzden "
   "üretim ölçeği daha küçüktür; buna karşılık mekanik ve anlatı tarafında daha çok deneme "
   "yapılır. GeForce NOW kütüphanesinde bağımsız oyunlar en geniş kategorilerden biridir."))
EK_FAQ["canlandirma"].append(
  ("Canlandırma kategorisi hangi oyunları kapsıyor?",
   "Canlandırma, GeForce NOW kütüphanesinde rol yapma (RPG) yapımlarının toplandığı kategoridir. "
   "Klasik CRPG, JRPG, aksiyon RPG, soulslike hibritler ve MMORPG bu başlık altında yer alır."))
EK_FAQ["basit-eglence"].append(
  ("Basit eğlence kategorisi hangi oyunları kapsıyor?",
   "Basit eğlence, kuralları kısa sürede öğrenilen ve kısa oturumlara uygun casual yapımların "
   "toplandığı kategoridir. Party oyunları, cozy yaşam simülasyonları, iş simülasyonları ve "
   "mini-oyun koleksiyonları bu başlık altındadır."))
EK_FAQ["diger"].append(
  ("Diğer yayıncı oyunları kategorisinde neler var?",
   "Bu kategoride Steam, Epic Games ve Xbox dışındaki mağaza ve başlatıcılara bağlı yapımlar "
   "toplanır. Battle.net kataloğu, HoYoverse evreni ve kendi başlatıcısını kullanan diğer "
   "yayıncıların oyunları buraya girer."))
EK_FAQ["epic-games"].append(
  ("Epic Games oyunları GeForce NOW'da nasıl açılır?",
   "Epic Games hesabını GeForce NOW'a bağladıktan sonra kütüphanendeki desteklenen Epic Games "
   "oyunları listede görünür. Oyunu seçtiğinde bulut sunucusunda başlar, cihazına indirme "
   "yapılmaz."))
EK_FAQ["oyunlar"].append(
  ("GeForce NOW oyunları listesi ne sıklıkla güncelleniyor?",
   "Kütüphaneye her hafta yeni yapımlar ekleniyor. GeForce NOW oyunları listesi yayıncı "
   "izinlerine bağlı olduğu için bazı oyunlar listeden çıkabilir; güncel durum kategori "
   "sayfalarındaki grid üzerinden görülebilir."))

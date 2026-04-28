SORU-1 KISA bir Python hatırlatması

-------------------------------------------------------------------
-------------------------------------------------------------------
SORU-1  "AI–ML–DL farkları, kullanım senaryoları nelerdir"

AI, ML ve DL kavramlarını birbirinden net biçimde ayıracağım; sonra aralarındaki ilişkiyi, temel farkları, hangi durumda hangisinin kullanıldığını, gerçek hayat senaryolarını, avantaj–dezavantajlarını ve sık yapılan kavram hatalar:

# AI – ML – DL farkları ve kullanım senaryoları

Bu üç kavram çoğu zaman birbirine karıştırılıyor. Halbuki aralarında **kapsam ilişkisi** var.

En kısa mantık şu:

* **AI (Artificial Intelligence / Yapay Zekâ)** en geniş kümedir.
* **ML (Machine Learning / Makine Öğrenmesi)**, AI’nin alt dalıdır.
* **DL (Deep Learning / Derin Öğrenme)** ise ML’nin alt dalıdır.

Yani matematiksel olarak düşünürsek:

**DL ⊂ ML ⊂ AI**

Başka bir ifadeyle:

* Her DL sistemi aynı zamanda ML’dir.
* Her ML sistemi aynı zamanda AI yaklaşımıdır.
* Ama her AI sistemi ML veya DL olmak zorunda değildir.

Buradaki kafa karışıklığı genelde şuradan çıkar:
İnsanlar “akıllı çalışan her şey = deep learning” sanıyor. Yok öyle sihirli değnek. Bazen basit bir kural tabanlı sistem, bazen klasik makine öğrenmesi, bazen de derin öğrenme yeterlidir.

---

## 1) AI nedir?

**Yapay zekâ**, bilgisayarların insan benzeri karar verme, problem çözme, tahmin yapma, planlama, dil anlama, algılama gibi görevleri yerine getirmesini amaçlayan geniş alandır.

AI bir teknoloji değil, daha çok bir **üst şemsiye kavramdır**.

AI içinde şu tür yaklaşımlar olabilir:

* Kural tabanlı sistemler
* Uzman sistemler
* Arama algoritmaları
* Planlama sistemleri
* Bulanık mantık
* Makine öğrenmesi
* Derin öğrenme
* Takviyeli öğrenme

### AI’nin temel amacı

Makinenin:

* çevreyi algılaması,
* veriyi işlemesi,
* karar üretmesi,
* belli hedefe göre davranmasıdır.

### AI örnekleri

* Satranç oynayan sistem
* Müşteri destek chatbotu
* Rota planlayan navigasyon
* Dolandırıcılık alarm sistemi
* Oyun oynayan ajan
* Otonom araç karar modülü
* Akıllı öneri sistemi

Burada önemli nokta şu:
Bir sistemin AI olması için illa sinir ağı kullanması gerekmez.
Örneğin:

* “Eğer müşteri son 24 saatte 10 başarısız giriş yaptıysa hesabı kilitle”
  bu da belli ölçüde zekâ davranışı içeren otomasyon olabilir ama bu **ML değildir**, daha çok **kural tabanlı AI** yaklaşımıdır.

---

## 2) ML nedir?

**Makine öğrenmesi**, bilgisayara bütün kuralları tek tek yazmak yerine, veriden örüntü öğrenmesini sağlayan yaklaşımdır.

Klasik programlamada mantık şöyledir:

**Kurallar + Veri → Sonuç**

Makine öğrenmesinde ise:

**Veri + Sonuç örnekleri → Model öğrenir → Yeni sonuç üretir**

Yani geliştirici bütün kuralları açık açık tanımlamaz.
Model, geçmiş örnekleri inceleyerek bir fonksiyon öğrenir.

### ML’nin amacı

Veriden şunları öğrenmektir:

* sınıflandırma
* tahmin
* kümeleme
* anomali tespiti
* öneri
* skor üretme
* karar destek

### ML örnekleri

* Bir mail spam mi değil mi?
* Kredi başvurusu riskli mi?
* Müşteri ürünü satın alır mı?
* Bu evin tahmini fiyatı nedir?
* Hangi müşteri segmentte yer alıyor?
* Hangi işlem sahtekârlık olabilir?

### ML nasıl çalışır?

Genel akış şöyledir:

1. Veri toplanır
2. Veri temizlenir
3. Özellikler (features) çıkarılır
4. Model eğitilir
5. Model test edilir
6. Gerçek ortamda tahmin üretir

### ML türleri

Makine öğrenmesi genelde 4 başlıkta düşünülür:

#### a) Supervised Learning (Denetimli Öğrenme)

Etiketli veri vardır.

Örnek:

* Girdi: müşteri bilgileri
* Çıktı: krediyi ödedi / ödemedi

Amaç, girişten çıkışı öğrenmektir.

Kullanım:

* sınıflandırma
* regresyon

Örnek algoritmalar:

* Linear Regression
* Logistic Regression
* Decision Tree
* Random Forest
* SVM
* KNN
* XGBoost

#### b) Unsupervised Learning (Denetimsiz Öğrenme)

Etiket yoktur. Model verideki yapıyı keşfetmeye çalışır.

Kullanım:

* müşteri segmentasyonu
* benzer grupları bulma
* anomali sezme
* boyut indirgeme

Örnek algoritmalar:

* K-Means
* DBSCAN
* Hierarchical Clustering
* PCA

#### c) Semi-Supervised Learning

Az etiketli, çok etiketsiz veri vardır.

Kullanım:

* etiketlemenin pahalı olduğu durumlar
* tıbbi görüntüler
* belge sınıflandırma

#### d) Reinforcement Learning

Ajan, çevreyle etkileşir; ödül-ceza alarak öğrenir.

Kullanım:

* oyun
* robotik
* stratejik karar sistemleri
* otonom kontrol

---

## 3) DL nedir?

**Derin öğrenme**, çok katmanlı yapay sinir ağları kullanarak veriden otomatik olarak karmaşık temsiller öğrenen bir makine öğrenmesi alt alanıdır.

Buradaki “deep” kelimesi, ağın çok katmanlı olmasını ifade eder.

### DL neden farklı?

Klasik ML’de çoğu zaman insan şu işi yapar:

* “Hangi özellikler önemli?”
* “Bu veriden hangi sütunlar çıkmalı?”
* “Hangi istatistiksel dönüşüm yapılmalı?”

DL’de ise sistem birçok durumda özellikleri kendi öğrenebilir.

Özellikle şu alanlarda çok güçlüdür:

* görüntü işleme
* konuşma tanıma
* doğal dil işleme
* video analizi
* büyük ve karmaşık veri

### DL örnekleri

* Fotoğrafta kedi var mı?
* Ses kaydında hangi kelime söylendi?
* Metin özetleme
* Otomatik çeviri
* yüz tanıma
* nesne tespiti
* büyük dil modelleri

### DL’nin temel yapıları

Başlıca derin öğrenme mimarileri:

* **ANN / MLP**: temel tam bağlı ağlar
* **CNN**: görüntü verileri için çok güçlü
* **RNN / LSTM / GRU**: zaman serisi ve sıralı veriler için
* **Transformer**: NLP ve artık birçok alanda baskın yapı
* **Autoencoder**: sıkıştırma, gürültü temizleme, temsil öğrenme
* **GAN**: veri üretme, görüntü sentezi
* **Diffusion Models**: modern görüntü üretim sistemleri

---

# AI, ML, DL arasındaki temel fark

## 1. Kapsam farkı

* AI en geniş alan
* ML AI’nin öğrenme yapan kısmı
* DL ML’nin sinir ağlarına dayalı daha gelişmiş kısmı

## 2. Kural yazımı vs öğrenme

* AI: bazen kural tabanlı olabilir
* ML: veriden öğrenir
* DL: çok büyük veriden çok katmanlı ağlarla öğrenir

## 3. Veri ihtiyacı

* Basit AI sistemleri az veriyle çalışabilir
* ML orta miktarda veriyle iyi çalışabilir
* DL genelde çok daha fazla veri ister

## 4. Donanım ihtiyacı

* Kural tabanlı AI: düşük
* Klasik ML: orta
* DL: yüksek, çoğu zaman GPU gerekir

## 5. Açıklanabilirlik

* Kural tabanlı AI: çok açıklanabilir
* Klasik ML: nispeten açıklanabilir
* DL: çoğu zaman kara kutuya daha yakın

## 6. Problem karmaşıklığı

* Basit karar mantıkları için AI/kural tabanı yeterli olabilir
* Yapısal tablo verilerinde ML çok güçlüdür
* Görüntü, ses, metin gibi karmaşık verilerde DL öne çıkar

---

# Kısa karşılaştırma tablosu

| Kriter           | AI                                     | ML                     | DL                                    |
| ---------------- | -------------------------------------- | ---------------------- | ------------------------------------- |
| Kapsam           | En geniş alan                          | AI’nin alt dalı        | ML’nin alt dalı                       |
| Çalışma mantığı  | Kural, mantık, arama, öğrenme olabilir | Veriden örüntü öğrenir | Çok katmanlı sinir ağları ile öğrenir |
| Veri ihtiyacı    | Düşük/orta olabilir                    | Orta                   | Genelde yüksek                        |
| Donanım ihtiyacı | Düşük/orta                             | Orta                   | Yüksek                                |
| Özellik çıkarımı | Çoğu zaman insan tanımlar              | İnsan + model          | Büyük oranda model öğrenebilir        |
| Açıklanabilirlik | Yüksek olabilir                        | Orta                   | Düşük/orta                            |
| Uygun veri tipi  | Kurallar, mantık, yapılandırılmış veri | Özellikle tablo verisi | Görüntü, ses, metin, büyük veri       |
| Eğitim süresi    | Düşük olabilir                         | Orta                   | Uzun olabilir                         |

---

# Basit örnekle farkı anlatayım

Bir e-ticaret projesi düşün.

## AI yaklaşımı

“Sepet tutarı 1000 TL üzerindeyse ve kullanıcı son 7 günde aktifse indirim kuponu göster.”

Bu kural tabanlıdır. İnsan kuralları yazmıştır.

## ML yaklaşımı

Geçmiş müşteri verilerine bakıp model eğitirsin:

* yaş
* il
* cihaz tipi
* son ziyaret sayısı
* sepet değeri
* önceki satın alma geçmişi

Model der ki:
“Bu kullanıcının satın alma ihtimali %78.”

Burada sistem kuralları veriden öğrenmiştir.

## DL yaklaşımı

Kullanıcının:

* metin yorumlarını,
* site içi davranış akışını,
* görsel etkileşimlerini,
* ürün açıklamalarını

aynı anda çok büyük veriyle işleyip daha karmaşık örüntüler öğrenen bir sinir ağı kurarsın.

Bu artık daha ağır, daha karmaşık, ama bazı durumlarda daha güçlü bir çözümdür.

---

# Kullanım senaryoları nelerdir?

Şimdi asıl pratik taraf.
“Hangi durumda hangisini seçmeliyim?”

---

## A) AI kullanım senaryoları

AI’nin ML içermeyen ya da hafif öğrenme içeren kullanım alanları da vardır.

### 1. Kural tabanlı uzman sistemler

Örnek:

* vergi hesaplama
* iş akışı otomasyonu
* uygunluk kontrolü
* belge onay süreçleri

Neden uygun?
Çünkü kurallar nettir. Öğrenmeye gerek yoktur.

### 2. Karar motorları

Örnek:

* sigorta ön değerlendirme
* kampanya tetikleme
* fraud risk eşiği bazlı alarm
* workflow routing

### 3. Oyun yapay zekâsı

Örnek:

* NPC davranışları
* pathfinding
* minimax tabanlı strateji

### 4. Planlama ve optimizasyon

Örnek:

* teslimat rotası planlama
* vardiya çizelgeleme
* kaynak planlama

### 5. Chatbot akışları

Örnek:

* sabit senaryolu müşteri hizmetleri botu
* menü tabanlı yanıt sistemi

Bunların hepsi illa deep learning gerektirmez.

---

## B) ML kullanım senaryoları

ML özellikle **tablo verisi** olan iş problemlerinde çok güçlüdür.

### 1. Tahminleme

Örnek:

* satış tahmini
* fiyat tahmini
* talep tahmini
* stok ihtiyacı tahmini

Sektörler:

* perakende
* finans
* üretim
* lojistik

### 2. Sınıflandırma

Örnek:

* spam tespiti
* kredi risk sınıflandırma
* müşteri churn tahmini
* hastalık riski skoru
* belge kategorilendirme

### 3. Anomali tespiti

Örnek:

* sahtekârlık tespiti
* ağ trafiğinde anormal davranış
* sensör verisinde arıza sinyali
* olağandışı kullanıcı hareketleri

### 4. Segmentasyon

Örnek:

* müşteri kümeleri
* davranış bazlı pazarlama segmentleri
* kullanıcı persona çıkarımı

### 5. Öneri sistemleri

Örnek:

* kullanıcıya ürün öner
* benzer içerik öner
* izleme geçmişine göre film öner

### 6. Bakım tahmini

Örnek:

* makine ne zaman arızalanır?
* hangi bileşen risk altında?

Bu tarz alanlarda klasik ML çoğu zaman DL’den daha mantıklıdır.
Çünkü veri çoğunlukla tablo formatındadır ve açıklanabilirlik istenir.

---

## C) DL kullanım senaryoları

DL, özellikle insanın algı sistemine benzeyen zor görevlerde parlar.

### 1. Görüntü işleme

Örnek:

* yüz tanıma
* nesne tespiti
* kalite kontrol
* tıbbi görüntü analizi
* plaka okuma

Gerçek kullanım:

* fabrikada hatalı ürün bulma
* MR / tomografi yorum destek sistemleri
* güvenlik kameralarında insan/araç tespiti

### 2. Doğal dil işleme (NLP)

Örnek:

* metin sınıflandırma
* duygu analizi
* soru-cevap
* çeviri
* özetleme
* belge üretme
* büyük dil modelleri

Gerçek kullanım:

* çağrı merkezi asistanı
* hukuki belge analizi
* otomatik rapor üretimi
* müşteri mesajı sınıflandırma

### 3. Ses ve konuşma

Örnek:

* speech-to-text
* text-to-speech
* sesli asistan
* konuşmacı tanıma

### 4. Video analizi

Örnek:

* davranış tespiti
* trafik yoğunluğu analizi
* güvenlik ihlali tespiti

### 5. Otonom sistemler

Örnek:

* araç algılama
* şerit takibi
* çevre analizi
* robotik görme

### 6. Üretici yapay zekâ

Örnek:

* metin üretimi
* resim üretimi
* müzik üretimi
* kod üretimi

Bu alanlar DL’nin doğal oyun alanıdır.

---

# Hangi durumda AI, ML, DL seçilmeli?

## AI seç

Şu durumda:

* problem kurallarla açıkça tanımlanabiliyorsa
* açıklanabilirlik çok önemliyse
* veri azsa
* hızlı prototip gerekiyorsa
* bakım kolaylığı isteniyorsa

Örnek:

* muhasebe onay akışı
* kampanya kural motoru
* izin onay sistemi
* erişim kontrol sistemi

## ML seç

Şu durumda:

* elinde tarihsel veri varsa
* problem tahmin/sınıflandırma ise
* veri çoğunlukla tablo şeklindeyse
* açıklanabilirlik isteniyorsa
* eğitim maliyeti kontrollü olsun istiyorsan

Örnek:

* kredi skorlama
* satış tahmini
* churn tahmini
* müşteri segmentasyonu
* anomali tespiti

## DL seç

Şu durumda:

* veri tipi görüntü, ses, metin veya büyük ölçekli karmaşık veri ise
* çok yüksek doğruluk gerekiyorsa
* yeterli veri ve donanım varsa
* problem klasik feature engineering ile zor çözülüyorsa

Örnek:

* yüz tanıma
* belge OCR sonrası anlamlandırma
* chatbot / LLM sistemi
* görüntüden arıza tespiti
* konuşma tanıma

---

# Sık yapılan yanlışlar

## Yanlış 1: AI = robot

Hayır. AI robot olmak zorunda değil.
Bir banka fraud sistemi de AI olabilir, fiziksel robot olmak zorunda değil.

## Yanlış 2: ML olmadan AI olmaz

Olur.
Uzman sistemler, arama algoritmaları, mantıksal çıkarım sistemleri ML’siz AI örnekleri olabilir.

## Yanlış 3: DL her zaman daha iyidir

Hayır.
DL daha ağırdır, daha çok veri ister, daha çok kaynak ister.
Tablo verisinde XGBoost gibi klasik ML yöntemleri çoğu zaman DL’den daha iyi veya daha verimli olabilir.

## Yanlış 4: Çok veri varsa otomatik başarı gelir

Yok öyle otomatik cennet.
Veri kalitesizse model de çöpten taç yapar.
Eksik, yanlı, bozuk veriyle harika model çıkmaz.

## Yanlış 5: Büyük model = akıllı model

Her zaman değil.
İş problemine göre en uygun çözüm önemlidir.
Basit problemde devasa model kullanmak, karınca için tank göndermeye benzer.

---

# Gerçek hayattan sektör bazlı örnekler

## 1. Sağlık

### AI

* klinik karar destek kural motoru
* randevu önceliklendirme

### ML

* hastalık risk skoru
* hastane yatış tahmini
* ilaç uyum tahmini

### DL

* MR, CT, röntgen görüntüsü analizi
* patoloji görüntü sınıflandırma
* medikal rapor özetleme

---

## 2. Finans

### AI

* kural tabanlı işlem alarmı
* limit kontrol sistemi

### ML

* kredi skorlama
* fraud detection
* müşteri terk etme tahmini

### DL

* sesli müşteri doğrulama
* karmaşık işlem örüntü analizi
* belge okuma ve anlamlandırma

---

## 3. E-ticaret

### AI

* kampanya motoru
* chatbot akış yönetimi

### ML

* ürün öneri modeli
* satın alma ihtimali tahmini
* stok tahmini

### DL

* görsel arama
* yorum analizi
* metin üretimi
* ürün açıklaması oluşturma

---

## 4. Üretim / Sanayi

### AI

* iş akışı ve bakım kuralları
* alarm eşik motorları

### ML

* kestirimci bakım
* enerji tüketim tahmini
* kalite skor tahmini

### DL

* kamera ile kalite kontrol
* kusur tespiti
* üretim hattı görüntü analizi

---

## 5. Eğitim teknolojileri

Senin alanına daha yakın örnek vereyim.

### AI

* öğrencinin seviyesine göre sabit kurallı içerik yönlendirme
* sınav akış kuralları
* otomatik içerik sıralama

### ML

* öğrencinin başarı tahmini
* terk etme ihtimali
* en uygun ders önerisi
* öğrenme analitiği

### DL

* öğrencinin yazılı cevabını anlamsal analiz etme
* konuşma tabanlı dil pratiği
* kişiselleştirilmiş chatbot eğitmeni
* doküman özetleme ve soru üretimi

---

# Teknik farkları biraz daha derin anlatalım

## Feature Engineering farkı

### Klasik ML

Veriden anlamlı özellikleri çoğu zaman insan çıkarır.

Örnek:
Ev fiyat tahmini için:

* oda sayısı
* metrekare
* bina yaşı
* mahalle
* kat bilgisi

Bunları sütun olarak modele verirsin.

### DL

Ham veriden temsil öğrenebilir.

Örnek:
Bir fotoğrafı doğrudan verirsin; sistem kenar, şekil, parça, nesne gibi katmanlı temsilleri kendi öğrenir.

---

## Veri tipi farkı

### ML

En iyi olduğu alan:

* CSV
* Excel
* SQL tablo verisi
* sayısal/kategorik yapılandırılmış veri

### DL

En iyi olduğu alan:

* resim
* ses
* video
* serbest metin
* büyük ölçekli çok boyutlu veri

---

## Hesaplama maliyeti farkı

### ML

* CPU ile çoğu zaman yeterli olabilir
* eğitim süresi daha kısa olabilir
* deploy etmesi daha kolay olabilir

### DL

* GPU/TPU avantaj sağlar
* eğitim daha pahalı olabilir
* model boyutu büyük olabilir
* inference maliyeti artabilir

---

## Açıklanabilirlik farkı

Kurumsal sistemlerde kritik konu budur.

### AI / Kural tabanlı sistem

“Bu karar neden çıktı?”
Cevap net:
“Çünkü kural 17 çalıştı.”

### ML

Açıklama mümkündür:

* feature importance
* SHAP
* coefficients
* tree paths

### DL

Açıklamak daha zordur:

* attention map
* saliency map
* LIME / SHAP benzeri yaklaşımlar
  ama yine de klasik ML kadar şeffaf değildir.

Finans, sağlık, kamu gibi alanlarda bu fark çok önemlidir.

---

# Avantaj ve dezavantajlar

## AI avantajları

* hızlı uygulanabilir
* kurallar nettir
* açıklanması kolaydır
* bakım yönetimi kolay olabilir

## AI dezavantajları

* kurallar arttıkça karmaşa büyür
* istisnalar çoğalır
* esneklik azalır
* öğrenme yeteneği sınırlıdır

---

## ML avantajları

* veriden öğrenir
* tahmin kabiliyeti yüksektir
* yapılandırılmış veride çok başarılıdır
* DL’ye göre daha az kaynak isteyebilir

## ML dezavantajları

* veri kalitesine bağımlıdır
* feature engineering gerekebilir
* dağılım değişirse performans düşer
* yanlış yorumlanırsa risklidir

---

## DL avantajları

* karmaşık örüntüleri öğrenir
* görüntü/ses/metinde çok güçlüdür
* otomatik özellik öğrenme avantajı vardır
* büyük ölçekli problemlerde çok başarılıdır

## DL dezavantajları

* çok veri ister
* eğitim pahalıdır
* açıklanması zordur
* tuning süreci daha zahmetlidir
* küçük veri setlerinde gereksiz olabilir

---

# Çok net karar rehberi

Şunu cebine koy:

## Problem kurallarla çözülüyorsa

**AI / Rule-based** düşün.

## Problem tablo verisiyle tahmin işi ise

**ML** düşün.

## Problem görüntü, ses, dil, video ise

**DL** düşün.

## Regülasyon ve açıklanabilirlik çok önemliyse

Önce **Rule-based + ML** düşün, DL’yi hemen kutsallaştırma.

## Veri azsa

DL’ye balıklama atlama.
Klasik ML veya hibrit yaklaşım daha mantıklı olabilir.

---

# Hibrit kullanım da vardır

Gerçek sistemlerde bunlar tek başına değil birlikte kullanılır.

Örnek: Akıllı eğitim platformu

* **AI**: öğrenciyi seviyeye göre ders akışına yönlendirir
* **ML**: başarı riskini tahmin eder
* **DL**: öğrencinin açık uçlu cevabını anlamsal olarak analiz eder
* **Rule Engine**: not politikasını uygular
* **LLM**: açıklama ve geri bildirim üretir

Yani gerçek dünyada mimari çoğu zaman şöyledir:
**Sadece DL değil, katmanlı bir akıllı sistem mimarisi.**

---

# Bir cümlede özet

* **AI**: Makinenin akıllı davranış göstermesini amaçlayan en geniş alan.
* **ML**: Makinenin veriden öğrenmesini sağlayan AI alt dalı.
* **DL**: Çok katmanlı sinir ağlarıyla karmaşık veriden öğrenen ML alt dalı.

---

# Son söz: hangisi daha önemli?

Bu soru biraz “çekiç mi daha önemli tornavida mı?” sorusu gibi.
İşe göre değişir.

Doğru soru şudur:

**Elimdeki problem ne, verim ne, kaynaklarım ne, açıklanabilirlik ihtiyacım ne?**

Teknik olgun yaklaşım budur.
Her yere deep learning sürmek, menemene beton dökmek gibi bir şey olur.

Sonraki adımda bunu senin için şu formatlardan biriyle de hazırlayabilirim:
**ders notu**, **sunumluk madde madde içerik**, **öğrenciye anlatılacak sade versiyon**, **kurumsal eğitim dokümanı**, **tablo karşılaştırmalı PDF taslağı**.

------------------------------------------------
------------------------------------------------

SORU-XX AI-ML-DL öğrenirken yol haritamız nasıl olmalııdır ?

Önce ne yapacağımı söyleyeyim:
AI–ML–DL öğrenme yol haritasını **sıfırdan başlayıp üretim seviyesine kadar** aşama aşama kuracağım. Sadece konu listesi vermeyeceğim; **hangi sırayla**, **neden o sırayla**, **hangi araçlarla**, **hangi projelerle** ilerlenmesi gerektiğini net yazacağım.

# AI–ML–DL öğrenirken yol haritası nasıl olmalı?

En büyük hata şudur:
İnsanlar direkt “LLM, transformer, agent, RAG” diye atlıyor. Temel yoksa bu iş makyajlı ezber olur. İlk rüzgârda dağılır.

Doğru sıra şudur:

**Programlama temeli → matematik ve veri mantığı → klasik ML → model değerlendirme → derin öğrenme → uzmanlaşma alanı → MLOps / üretim**

Yani bina kuruyorsan önce temel, sonra kolon, sonra kat. Tavana avizeyi önce asmaya çalışırsan aşağı inersin.

---

# 1) Önce zihinsel çerçeveyi doğru kur

İlk bilmen gereken şey:

* **AI** en geniş alan
* **ML** AI’nin alt dalı
* **DL** ML’nin alt dalı

Bunu anlamadan öğrenme dağınık olur.

Ayrıca şu ayrımı da baştan oturt:

* Bu bir **matematik + yazılım + veri** alanıdır
* Sadece Python bilmek yetmez
* Sadece algoritma ezberlemek de yetmez
* Sadece model eğitmek hiç yetmez

Bir AI mühendisi aslında şu üç şeyi birlikte yapar:

* veriyi anlar
* modeli kurar
* sistemi çalışır hale getirir

---

# 2) Aşama 1 — Python ve programlama temeli

Burası pazarlık kaldırmaz.
Python zayıfsa AI öğrenimi sürekli tökezler.

## Öğrenmen gerekenler

### Python temel

* değişkenler
* veri tipleri
* if / else
* for / while
* fonksiyonlar
* list, tuple, set, dict
* string işlemleri

### Orta seviye Python

* list comprehension
* lambda
* exception handling
* file işlemleri
* modül mantığı
* class / OOP temeli
* package yapısı

### Veriyle ilgili Python alışkanlıkları

* temiz fonksiyon yazma
* notebook ve script farkı
* virtual environment
* pip kullanımı
* requirements.txt

## Hedef

Şunu rahat yapabilmelisin:

* CSV oku
* filtrele
* veri temizle
* fonksiyon yaz
* sonucu dosyaya kaydet

## Ne kadar sürer?

Düzenli çalışmayla:

* sağlam temel: **2–4 hafta**
* rahat kullanım: **4–6 hafta**

## Mini proje

* öğrenci not analizi
* satış raporu
* log dosyası analizi
* CSV temizleme scripti

---

# 3) Aşama 2 — Matematik temeli

Burada insanları korkutan gereksiz mistik hava var.
Yok efendim önce doktora düzeyi matematik. Gerek yok.
Ama matematiksiz de AI öğreniyorum demek biraz freni olmayan araba sürmek gibi.

## Bilmen gereken matematik alanları

### Lineer cebir

Çünkü veri çoğu zaman vektör ve matristir.

Öğren:

* vektör
* matris
* boyut (shape)
* transpose
* dot product
* matrix multiplication
* identity matrix
* eigenvalue / eigenvector mantığı
* projection temel fikri

### İstatistik ve olasılık

Çünkü model performansı, dağılım, belirsizlik burada yaşar.

Öğren:

* mean, median, mode
* variance, std
* distribution
* normal distribution
* probability basics
* conditional probability
* Bayes mantığı
* sampling
* hypothesis testing temel fikir

### Türev ve optimizasyon

Çünkü model eğitiminde kayıp azaltılır.

Öğren:

* fonksiyon mantığı
* türev nedir
* kısmi türev
* gradient
* chain rule
* minimum / maximum
* gradient descent mantığı

## Hedef

Şunları anlayabil:

* loss neden azalıyor?
* gradient ne işe yarıyor?
* PCA neden boyut indiriyor?
* logistic regression neden olasılık üretiyor?

## Ne kadar sürer?

* uygulamalı temel: **4–6 hafta**
* rahat kavrama: **6–8 hafta**

## Not

Burada amaç ispat ezberi değil.
Ama “bu formül ne anlatıyor?” seviyesine gelmelisin.

---

# 4) Aşama 3 — Veri analizi ve veri işleme

Modelden önce veri gelir.
Gerçek projelerde zamanın büyük kısmı burada geçer.

## Öğrenmen gereken kütüphaneler

* NumPy
* Pandas
* Matplotlib
* Seaborn

## Bilmen gerekenler

* DataFrame mantığı
* eksik veri analizi
* aykırı değer analizi
* sütun türleri
* kategorik veri
* sayısal veri
* encoding
* scaling
* normalization
* standardization
* correlation
* target-feature ilişkisi
* veri sızıntısı

## Hedef

Bir veri seti geldiğinde şu akışı yapabil:

* `head()`
* `info()`
* `describe()`
* missing value analizi
* dağılım grafikleri
* korelasyon
* hedef değişken inceleme
* train/test’e uygun hazırlık

## Mini projeler

* Titanic analizi
* ev fiyat veri seti analizi
* müşteri segment verisi analizi
* satış verisi temizleme ve görselleştirme

## Kritik kazanım

Şunu öğren:
**Çöp veri + iyi model = yine çöp sonuç**

---

# 5) Aşama 4 — Makine öğrenmesinin temeli

Burası asıl omurga.

Önce klasik ML öğren.
Derin öğrenmeye atlamadan önce bunu bilmek zorundasın. Çünkü burada model kurma mantığı oturur.

## Önce öğrenilecek kavramlar

* supervised learning
* unsupervised learning
* classification
* regression
* clustering
* train / validation / test
* overfitting
* underfitting
* bias / variance
* feature engineering
* data leakage
* cross validation

## Öğrenilecek temel algoritmalar

### Classification

* Logistic Regression
* KNN
* Decision Tree
* Random Forest
* SVM
* Naive Bayes

### Regression

* Linear Regression
* Ridge / Lasso
* Decision Tree Regressor
* Random Forest Regressor

### Clustering

* K-Means
* Hierarchical Clustering
* DBSCAN

## Öğrenilecek değerlendirme metrikleri

### Classification için

* accuracy
* precision
* recall
* F1-score
* confusion matrix
* ROC-AUC

### Regression için

* MAE
* MSE
* RMSE
* R²

### Clustering için

* silhouette score
* inertia mantığı

## Kullanılacak ana araç

* **scikit-learn**

## Hedef

Bir veri setinde:

* problemi tanımla
* feature / target ayır
* train/test split yap
* model eğit
* metrik hesapla
* modeli karşılaştır
* overfitting var mı bak

## Ne kadar sürer?

* temel kavrama: **6–8 hafta**
* rahat proje geliştirme: **2–3 ay**

---

# 6) Aşama 5 — Gerçek mini proje dönemi

Bu aşama atlanmamalı.
Çünkü konu bitirmekle öğrenme olmaz. Proje yapmadan bilgi, rafta duran tornavida gibi kalır.

## Yapman gereken proje tipleri

### Proje 1 — Classification

Örnek:

* spam tespiti
* müşteri churn tahmini
* kredi onayı
* hastalık sınıflandırma

### Proje 2 — Regression

Örnek:

* ev fiyat tahmini
* satış tahmini
* enerji tüketimi tahmini

### Proje 3 — Clustering

Örnek:

* müşteri segmentasyonu
* ürün gruplama

### Proje 4 — End-to-End tabular ML

İçermeli:

* veri temizleme
* preprocessing
* model seçimi
* tuning
* evaluation
* model kaydetme

## Bu aşamada öğreneceğin şey

“Algoritma bilmek” ile “iş çözmek” arasındaki fark.

---

# 7) Aşama 6 — İleri klasik ML

Burada artık işin daha güçlü tarafına geçersin.

## Öğren

* ensemble methods
* bagging
* boosting
* stacking
* feature selection
* hyperparameter tuning
* pipeline
* model explainability

## Özellikle öğrenilecekler

* Random Forest
* XGBoost
* LightGBM
* CatBoost
* Grid Search
* Random Search
* Optuna mantığı
* SHAP / feature importance

## Neden önemli?

Gerçek tablo verisinde çoğu zaman derin öğrenmeden önce bunlar kazanır.

## Mini proje

* bankacılık fraud detection
* e-ticaret satın alma tahmini
* müşteri yaşam boyu değer tahmini

---

# 8) Aşama 7 — Derin öğrenmeye giriş

Klasik ML temeli oturduktan sonra DL öğrenmek mantıklı olur.

## Önce öğrenilecek kavramlar

* neuron
* layer
* weight
* bias
* activation function
* forward propagation
* backpropagation
* loss function
* optimizer
* epoch
* batch
* learning rate

## Öğrenilecek araç

* PyTorch veya TensorFlow

Ben pratik sıra için çoğu kişiye şunu öneririm:

* **PyTorch** ile başla
  çünkü daha esnek ve modern ekosistemde çok güçlü

## Öğrenilecek yapılar

* MLP
* CNN
* RNN
* LSTM
* GRU
* Transformer mantığı

## Öğrenilecek optimizasyon kavramları

* SGD
* Adam
* regularization
* dropout
* batch normalization
* early stopping

## Hedef

Küçük bir sinir ağı kurup:

* veri yükle
* model tanımla
* loss hesapla
* eğitim döngüsü yaz
* validasyon yap
* test et

## Mini proje

* MNIST rakam tanıma
* fashion image classification
* temel sentiment analysis
* basit time series forecasting

---

# 9) Aşama 8 — Uzmanlaşma alanı seç

Buradan sonra herkesin yolu biraz ayrılır.
Her şeyi aynı anda uzman seviyede öğrenmeye çalışma. O noktada beyin RAM’i kızarır.

Ana uzmanlık yolları:

## A) Tabular ML / Decision Intelligence

Uygun alanlar:

* finans
* CRM
* churn
* fraud
* satış tahmini
* risk skorlama

Öğren:

* XGBoost
* LightGBM
* CatBoost
* explainability
* feature store mantığı

## B) NLP

Uygun alanlar:

* chatbot
* metin sınıflandırma
* özetleme
* çeviri
* duygu analizi
* doküman işleme

Öğren:

* tokenization
* embeddings
* RNN’den transformer’a geçiş
* BERT
* sentence transformers
* Hugging Face

## C) Computer Vision

Uygun alanlar:

* yüz tanıma
* kalite kontrol
* object detection
* segmentation
* OCR

Öğren:

* CNN
* OpenCV
* transfer learning
* ResNet
* YOLO
* U-Net

## D) Time Series

Uygun alanlar:

* finansal tahmin
* talep tahmini
* IoT
* sensör verisi
* enerji analizi

Öğren:

* ARIMA
* Prophet
* LSTM
* temporal validation

## E) Generative AI / LLM

Uygun alanlar:

* RAG
* agent
* doküman soru-cevap
* içerik üretimi
* enterprise AI assistant

Öğren:

* transformer
* embeddings
* vector database mantığı
* fine-tuning temel
* PEFT / LoRA
* inference
* prompt engineering
* evaluation

---

# 10) Aşama 9 — MLOps ve üretim mantığı

Burayı bilmeyen kişi model geliştirir ama sistem kuramaz.
Sektörde fark yaratan kısım burasıdır.

## Öğrenilecekler

* model serialization
* API ile servis etme
* FastAPI
* Docker
* experiment tracking
* MLflow
* veri versiyonlama
* model monitoring
* drift detection
* retraining mantığı
* CI/CD temel yaklaşım

## Neden önemli?

Notebook’ta çalışan model başka şeydir.
Üretimde sürdürülebilir çalışan sistem başka şeydir.

## Mini proje

Bir modeli:

* eğit
* `.pkl` / `.pt` olarak kaydet
* FastAPI ile endpoint aç
* Docker ile paketle
* basit frontend veya Swagger ile test et

İşte burada mühendislik başlar.

---

# 11) Aşama 10 — Portföy ve gerçek proje disiplini

Öğrenmenin ispatı konu bitirmek değil, proje çıkarmaktır.

## Portföyde olması gereken proje tipleri

### 1. Tabular ML projesi

* classification veya regression
* EDA + model karşılaştırma + tuning

### 2. Deep learning projesi

* image veya text

### 3. NLP/LLM mini proje

* semantic search
* doküman soru-cevap
* chatbot

### 4. Deployment projesi

* model API
* Docker
* basit UI

### 5. Açıklanabilirlik projesi

* SHAP
* feature importance
* business interpretation

## GitHub’da dikkat edilecekler

* README düzgün olmalı
* veri akışı net olmalı
* requirements.txt olmalı
* notebook yanında temiz Python script de olmalı
* sonuçlar yorumlanmalı

---

# 12) Öğrenme sırası tam olarak nasıl olmalı?

Şimdi bunu net sıraya koyuyorum.

## 1. Python

## 2. NumPy + Pandas

## 3. Matplotlib + Seaborn

## 4. İstatistik + lineer cebir + türev mantığı

## 5. Veri analizi + preprocessing

## 6. scikit-learn ile klasik ML

## 7. Model evaluation + overfitting + cross validation

## 8. Ensemble methods + boosting

## 9. Proje geliştirme

## 10. PyTorch / TensorFlow ile DL

## 11. CNN / RNN / Transformer temeli

## 12. Uzmanlık alanı seçimi

## 13. MLOps + deployment

## 14. Portföy ve gerçek ürün mantığı

Bu sıra bence en sağlıklı, en az saç-baş yolduran sıradır.

---

# 13) Haftalık örnek yol haritası

Daha somut yapalım.

## İlk 1–2 ay

* Python
* NumPy
* Pandas
* veri analizi
* temel istatistik

## 3–4. ay

* scikit-learn
* classification / regression / clustering
* metrikler
* mini projeler

## 5–6. ay

* ensemble
* tuning
* gerçek veri setleri
* portföy projeleri

## 7–8. ay

* PyTorch / TensorFlow
* MLP / CNN / RNN
* temel DL projeleri

## 9–10. ay

* NLP veya CV veya tabular uzmanlaşma
* ileri projeler

## 11–12. ay

* deployment
* FastAPI
* Docker
* MLflow
* üretim mantığı

Düzenli çalışan biri 1 yılda ciddi seviyeye gelir.
Ama burada “günde 20 video izledim” değil, gerçekten kod yazmak belirleyicidir.

---

# 14) Hangi kaynak türleriyle öğrenilmeli?

En iyi kombinasyon şu:

## Teori

* ders notu
* kitap
* temiz eğitim videoları

## Uygulama

* notebook
* küçük veri setleri
* Kaggle tarzı denemeler

## Pekiştirme

* aynı konuyu sıfırdan kodlama
* başkasının kodunu kopyalamadan yeniden yazma

## Derinleştirme

* makale / dokümantasyon okuma
* resmi dokümanlar
* açık kaynak repo inceleme

Sadece video izleyerek öğrenme çok aldatıcıdır.
Zihin “anladım” sanır, el ise hiçbir şey yapamaz.

---

# 15) Öğrenirken yapılan büyük hatalar

## Hata 1

Direkt DL veya LLM’e atlamak

## Hata 2

Matematiği tamamen yok saymak

## Hata 3

Sürekli konu tüketip proje yapmamak

## Hata 4

Sadece notebook kullanıp temiz proje yapısı öğrenmemek

## Hata 5

Model metriklerini anlamadan “accuracy iyi” deyip geçmek

## Hata 6

Data leakage, overfitting, train/valid/test mantığını hafife almak

## Hata 7

Deployment tarafını hiç öğrenmemek

---

# 16) Her aşamada ne üretmelisin?

## Python aşaması

* 5 küçük script

## Veri analizi aşaması

* 3 EDA notebook

## Klasik ML aşaması

* 5 modelleme projesi

## DL aşaması

* 3 derin öğrenme projesi

## Uzmanlaşma aşaması

* 2 ciddi domain projesi

## MLOps aşaması

* 1 deploy edilmiş model

Bu üretim sayıları seni tüketmez ama gelişimini gerçek yapar.

---

# 17) Eğer hedefin iş dünyasıysa

Akademik taraftan biraz farklı çalışman gerekir.

Öncelik ver:

* Python
* SQL
* Pandas
* scikit-learn
* XGBoost / LightGBM
* FastAPI
* Docker
* MLflow
* temel cloud mantığı

Çünkü şirketlerde ilk iş çoğu zaman “sıfırdan AGI yaz” olmaz.
Daha çok:

* tahmin modeli
* risk modeli
* öneri sistemi
* chatbot entegrasyonu
* veri pipeline
* model servisi
  gibi işler gelir.

---

# 18) Eğer hedefin araştırma / akademi ise

Daha çok şunlara yüklen:

* lineer cebir
* olasılık
* optimizasyon
* paper reading
* PyTorch
* transformer mimarileri
* distributed training
* deney tasarımı

---

# 19) Kısacık karar özeti

## Sıfırdan başlıyorsan:

Python + veri analizi + klasik ML

## Orta seviyedeysen:

ensemble + tuning + evaluation + proje

## İleri gitmek istiyorsan:

DL + uzmanlaşma + MLOps + deployment

---

# 20) Tek cümlelik doğru rota

**Önce veriyi anla, sonra modeli öğren, sonra sistemi kur.**

Bu sıra bozulursa bilgi parçalı kalır.

---

# Sana önerdiğim net öğrenme planı

Senin gibi teknik arka planı güçlü birisi için en verimli rota şu olur:

### Faz 1

* Python tekrar
* NumPy
* Pandas
* veri görselleştirme
* istatistik temeli

### Faz 2

* scikit-learn
* classification / regression / clustering
* evaluation
* overfitting / leakage / CV

### Faz 3

* XGBoost / LightGBM / CatBoost
* feature engineering
* explainability
* gerçek iş verisi mantığı

### Faz 4

* PyTorch
* ANN / CNN / RNN / Transformer
* NLP veya CV uzmanlaşma

### Faz 5

* FastAPI
* Docker
* MLflow
* production pipeline

Bu rota hem öğretilebilir, hem sektörel, hem de dağılmadan ilerler.

------------------------------------------------
------------------------------------------------

SORU-XX DL mimarisi nedir ? detaylıca açıklayınız ?

Önce ne yapacağımı söyleyeyim.
**Derin öğrenme (Deep Learning) mimarisinin ne olduğunu**, neden mimari kavramının ortaya çıktığını, bir DL modelinin temel yapı taşlarını, en önemli mimari türlerini (MLP, CNN, RNN, Transformer vb.) ve gerçek uygulamalarda nasıl kullanıldıklarını **temelden başlayarak detaylı şekilde** açıklayacağım.

---

# Deep Learning (DL) Mimarisı Nedir?

**DL mimarisi**, bir derin öğrenme modelinin **katmanlarının (layers), bağlantılarının ve veri akışının nasıl organize edildiğini belirleyen yapısal tasarımdır.**

Başka bir ifadeyle:

DL mimarisi, sinir ağının şu sorulara verdiği cevaptır:

* Kaç katman var?
* Katmanlar nasıl bağlanıyor?
* Veri hangi sırayla akıyor?
* Hangi hesaplama birimleri kullanılıyor?
* Hangi aktivasyon fonksiyonları kullanılıyor?

Bu nedenle mimari, modelin **yapısal planıdır.**

Bir bina düşün:

* tuğlalar → neuron
* katlar → layer
* bina planı → mimari

Derin öğrenme mimarisi de aynen bu mantıkla çalışır.

---

# Derin Öğrenme Neden “Derin”?

Klasik makine öğrenmesi çoğu zaman tek bir model kullanır.

Örnek:

```
input → logistic regression → output
```

Derin öğrenmede ise çok sayıda katman vardır.

```
input
↓
hidden layer
↓
hidden layer
↓
hidden layer
↓
output
```

Bu katmanlar verinin **giderek daha soyut temsilini öğrenir.**

Örneğin görüntü işleme:

1. katman → kenarlar
2. katman → şekiller
3. katman → parçalar
4. katman → nesneler

---

# Bir DL Mimarisinin Temel Bileşenleri

## 1) Input Layer

Verinin modele girdiği katmandır.

Örnek:

Bir görüntü:

```
224 × 224 × 3
```

Bir metin:

```
token dizisi
```

Bir tablo verisi:

```
feature vector
```

Input layer genelde hesaplama yapmaz, sadece veriyi aktarır.

---

## 2) Hidden Layers

Modelin öğrenme yaptığı katmanlardır.

Her hidden layer şu işlemi yapar:

```
z = Wx + b
a = activation(z)
```

Burada:

* W → ağırlık matrisi
* b → bias
* activation → aktivasyon fonksiyonu

Bu katmanlar veriyi dönüştürür.

---

## 3) Output Layer

Modelin son tahmini ürettiği katmandır.

Örnek:

Classification:

```
softmax
```

Binary classification:

```
sigmoid
```

Regression:

```
linear output
```

---

# Sinir Ağındaki Temel Hesaplama

Bir neuron şu işlemi yapar:

```
y = activation( w1x1 + w2x2 + ... + wnxn + b )
```

Bu işlem aslında **lineer dönüşüm + nonlinearity** kombinasyonudur.

Bu yüzden sinir ağları güçlüdür.

---

# Aktivasyon Fonksiyonları

Aktivasyon fonksiyonları modele doğrusal olmayan davranış kazandırır.

En yaygın olanlar:

### ReLU

```
f(x) = max(0, x)
```

Çok hızlıdır ve DL’de en çok kullanılır.

---

### Sigmoid

Çıktıyı 0 ile 1 arasına sıkıştırır.

Binary classification için kullanılır.

---

### Tanh

-1 ile 1 arasında çıktı üretir.

---

### Softmax

Çok sınıflı sınıflandırmada olasılık üretir.

---

# Derin Öğrenme Eğitim Süreci

Bir DL modeli şu şekilde öğrenir:

1. Forward propagation
2. Loss hesaplama
3. Backpropagation
4. Weight update

---

## Forward Propagation

Veri katmanlardan geçer ve tahmin üretilir.

---

## Loss Function

Model hatasını ölçer.

Örnek:

* Cross entropy
* MSE

---

## Backpropagation

Hata geriye doğru yayılır ve ağırlıkların nasıl değişmesi gerektiği hesaplanır.

---

## Optimizer

Ağırlıkları günceller.

Örnek:

* SGD
* Adam
* RMSProp

---

# DL Mimari Türleri

Şimdi en önemli mimari ailelerine bakalım.

---

# 1) MLP (Multi Layer Perceptron)

En temel sinir ağıdır.

Yapı:

```
input → fully connected → fully connected → output
```

Özellikleri:

* her neuron diğerine bağlıdır
* tabular veri için uygundur

Kullanım alanları:

* kredi riski
* müşteri churn tahmini
* genel classification problemleri

---

# 2) CNN (Convolutional Neural Network)

Görüntü işleme için tasarlanmıştır.

Temel katmanlar:

* convolution
* pooling
* fully connected

---

## Convolution

Görüntü üzerinde filtre uygulayarak özellik çıkarır.

Örnek:

```
kenar
köşe
doku
```

---

## Pooling

Görüntü boyutunu küçültür.

En yaygın:

* max pooling

---

CNN mimarileri:

* LeNet
* AlexNet
* VGG
* ResNet
* EfficientNet

---

# 3) RNN (Recurrent Neural Network)

Sıralı veriler için tasarlanmıştır.

Örnek veri:

* metin
* zaman serisi
* konuşma

RNN’de geçmiş bilgi saklanır.

```
ht = f(xt , ht-1)
```

Sorunu:

* long-term dependency problemi

---

# 4) LSTM

RNN’in gelişmiş versiyonudur.

Memory cell kullanır.

Gate mekanizması:

* forget gate
* input gate
* output gate

Bu sayede uzun bağımlılıkları öğrenebilir.

Kullanım alanları:

* speech recognition
* language modeling
* time series

---

# 5) GRU

LSTM’in daha sade versiyonudur.

Daha az parametre içerir.

---

# 6) Transformer

Modern NLP'nin ana mimarisidir.

Özelliği:

```
attention mechanism
```

Transformer şu katmanlardan oluşur:

* embedding
* positional encoding
* multi-head attention
* feedforward layers

---

## Self Attention

Bir kelimenin diğer kelimelerle ilişkisini hesaplar.

Bu sayede model:

* bağlamı anlar
* uzun cümleleri işler

---

Transformer tabanlı modeller:

* BERT
* GPT
* T5
* LLaMA

---

# 7) GAN (Generative Adversarial Network)

İki model içerir:

```
Generator
Discriminator
```

Generator veri üretir.

Discriminator gerçek mi sahte mi karar verir.

Bu rekabet modelin öğrenmesini sağlar.

Kullanım alanları:

* görüntü üretimi
* deepfake
* veri artırma

---

# 8) Diffusion Models

Son yılların en güçlü generative mimarisidir.

Mantık:

1. veriye gürültü ekle
2. sonra gürültüyü kaldırmayı öğren

Örnek:

* Stable Diffusion
* DALL-E

---

# DL Mimari Tasarımında Dikkat Edilen Şeyler

Bir mimari tasarlanırken şu sorular sorulur.

### Veri tipi nedir?

* görüntü
* metin
* ses
* tablo

### Veri boyutu nedir?

### Model karmaşıklığı ne olmalı?

### Overfitting riski var mı?

### Eğitim maliyeti nedir?

---

# DL Mimarisinin Avantajları

* karmaşık örüntüleri öğrenebilir
* feature engineering ihtiyacı azalır
* büyük veri ile çok güçlüdür

---

# DL Mimarisinin Dezavantajları

* çok veri ister
* eğitim pahalıdır
* yorumlanması zor
* hyperparameter tuning zor olabilir

---

# Basit Bir DL Mimari Örneği

Bir görüntü sınıflandırma modeli:

```
input image
↓
convolution layer
↓
relu
↓
max pooling
↓
convolution
↓
relu
↓
fully connected
↓
softmax
↓
class prediction
```

---

# DL Mimarisinin Özeti

Bir derin öğrenme mimarisi şu üç şeyi tanımlar:

1. katman yapısı
2. veri akışı
3. hesaplama türü

En yaygın mimari aileleri:

* MLP
* CNN
* RNN
* LSTM
* Transformer
* GAN
* Diffusion

---

# Çok önemli bir gerçek

Her problem için aynı mimari kullanılmaz.

Veri tipi mimariyi belirler:

| Veri         | Mimari             |
| ------------ | ------------------ |
| tablo        | MLP                |
| görüntü      | CNN                |
| metin        | Transformer        |
| zaman serisi | LSTM / Transformer |
| veri üretimi | GAN / Diffusion    |

---




------------------------------------------------
------------------------------------------------

SORU-XX ML mimarisi nedir ? detaylıca açıklayınız ?

Önce ne yapacağımı söyleyeyim:
**ML mimarisi (Machine Learning architecture)** kavramını karıştırılmayacak şekilde açıklayacağım. Önce “algoritma” ile “mimari” farkını netleştireceğim; sonra bir ML sisteminin katmanlarını, veri akışını, bileşenlerini, geliştirme ve üretim mimarisini, gerçek proje örneklerini ve sık yapılan mimari hataları detaylı şekilde anlatacağım.

# ML mimarisi nedir?

**ML mimarisi**, bir makine öğrenmesi sisteminin **uçtan uca nasıl tasarlandığını** anlatan yapıdır.

Yani sadece model değildir.
Sadece algoritma da değildir.
Sadece Python kodu hiç değildir.

ML mimarisi şunu tanımlar:

* veri nereden gelir?
* nasıl temizlenir?
* hangi özellikler çıkarılır?
* model nasıl eğitilir?
* nasıl doğrulanır?
* nasıl servis edilir?
* nasıl izlenir?
* ne zaman yeniden eğitilir?

Başka bir ifadeyle:

**ML mimarisi = veri + özellik + model + değerlendirme + dağıtım + izleme + bakım**

Bu yüzden mimari, “modelin etrafındaki bütün sistem” demektir.

---

# En temel ayrım: algoritma ≠ mimari

Bu ayrım net olmazsa konu çorba olur.

## Algoritma nedir?

Belirli bir öğrenme yöntemidir.

Örnek:

* Linear Regression
* Logistic Regression
* Decision Tree
* Random Forest
* XGBoost
* SVM
* K-Means

## Mimari nedir?

Bu algoritmaların yer aldığı **sistemin genel tasarımıdır.**

Örnek:
Bir churn tahmin sistemi düşün:

* müşteri verisi SQL’den gelir
* veri temizlenir
* feature engineering yapılır
* model eğitilir
* API olarak yayınlanır
* günlük olarak izlenir
* drift olursa yeniden eğitilir

İşte buna **ML mimarisi** denir.

Yani:

* **algoritma** = motor
* **mimari** = aracın tamamı

---

# ML mimarisi neden gerekir?

Çünkü gerçek hayatta mesele sadece model eğitmek değildir.

Notebook’ta çalışan bir model, gerçek sistem demek değildir.
Gerçek hayatta şu sorunlar vardır:

* veri eksik gelir
* veri formatı değişir
* kategoriler değişir
* train ve production verisi farklılaşır
* model zamanla bozulur
* API gecikir
* tahmin log’lanmaz
* yeniden eğitim unutulur

ML mimarisi, bu kaosu düzenlemek için kurulur.

---

# ML mimarisinin temel bileşenleri

Bir makine öğrenmesi mimarisi genelde şu ana katmanlardan oluşur:

1. Veri kaynakları
2. Veri toplama katmanı
3. Veri işleme / hazırlama katmanı
4. Feature engineering katmanı
5. Train / validation / test katmanı
6. Model eğitim katmanı
7. Model değerlendirme katmanı
8. Model kayıt / versiyonlama katmanı
9. Model deployment katmanı
10. İzleme / yeniden eğitim katmanı

Şimdi bunları tek tek açalım.

---

# 1) Veri kaynakları katmanı

ML mimarisinin başlangıç noktası veridir.

Veri kaynakları şunlar olabilir:

* SQL / PostgreSQL / MySQL
* NoSQL / MongoDB
* CSV / Excel / JSON
* log dosyaları
* API verileri
* sensör verileri
* görüntü / metin / ses verileri
* kullanıcı davranış verileri
* üçüncü taraf veri servisleri

Buradaki kritik soru şudur:

**Model hangi veriye dayanarak karar verecek?**

Yanlış veri kaynağıyla kurulan mimari, baştan topaldır.

---

# 2) Veri toplama katmanı

Bu katmanda veri sisteme alınır.

İşlemler:

* veri çekme
* veri birleştirme
* ETL / ELT
* batch veya streaming akışı
* veri doğrulama

## Batch veri toplama

Belirli aralıklarla veri çekilir.

Örnek:

* her gece müşteri işlemleri alınır
* günlük satışlar sisteme işlenir

## Streaming veri toplama

Veri anlık akar.

Örnek:

* fraud detection
* canlı öneri sistemi
* IoT sensör verileri

Bu seçim mimariyi ciddi etkiler.

---

# 3) Veri hazırlama / preprocessing katmanı

Ham veri çoğu zaman model için uygun değildir.
Burada veri temizlenir ve dönüştürülür.

Tipik işlemler:

* eksik veri analizi
* aykırı değer kontrolü
* veri tipi düzeltme
* tarih alanı dönüştürme
* kategorik veri encoding
* ölçekleme
* normalizasyon
* duplicate kayıt temizleme

Örnek:
Bir müşteri veri setinde şu sorunlar olabilir:

* yaş alanı boş
* gelir string gelmiş
* şehir isimleri tutarsız
* tarih formatı karışık

Model bunları ham haliyle yiyemez.
Burası mutfaktır. Çiğ malzemeyi servise çıkarmazsın.

---

# 4) Feature engineering katmanı

Makine öğrenmesinin çok kritik kısmıdır.

Ham veriden anlamlı özellikler çıkarılır.

Örnek:
Ham sütunlar:

* doğum tarihi
* son satın alma tarihi
* işlem listesi

Feature’lar:

* yaş
* son alışverişten geçen gün sayısı
* son 30 gün işlem adedi
* ortalama sepet tutarı
* churn riski ile ilişkili davranış skorları

Feature engineering, özellikle klasik ML’de çok değerlidir.

Bu katmanda şunlar olabilir:

* tarih parçalama
* oran üretme
* log dönüşümü
* target encoding
* text vectorization
* interaction feature üretimi

## Çok kritik kural

Feature üretirken şu soru sorulur:

**Bu bilgi tahmin anında gerçekten var mı?**

Yoksa leakage olur ve sistem kendini kandırır.

---

# 5) Veri bölme katmanı: train / validation / test

ML mimarisinde veri tek parça kullanılmaz.

## Train

Model öğrenir.

## Validation

Model ayarlanır.

## Test

Gerçek performans en son ölçülür.

Bu ayrım mimarinin temel güvenlik duvarıdır.
Yoksa model başarı numarası yapar.

Zaman serilerinde bu katman daha da önemlidir.
Geleceği geçmişe karıştırırsan iş biter.

---

# 6) Model eğitim katmanı

Burada algoritma seçilir ve model eğitilir.

Örnek algoritmalar:

* Linear Regression
* Logistic Regression
* Decision Tree
* Random Forest
* XGBoost
* LightGBM
* CatBoost
* SVM
* K-Means

Bu katmanda tipik işlemler:

* model seçimi
* hyperparameter tuning
* cross validation
* eğitim süresi ölçümü
* feature importance analizi

Burada mimari şunu tanımlar:

* tek model mi var?
* birden çok model karşılaştırılıyor mu?
* tuning otomatik mi?
* pipeline mı kullanılıyor?

---

# 7) Model değerlendirme katmanı

Her model iyi değildir; bazısı sadece güzel görünür.

Değerlendirme katmanı modelin gerçekten işe yarayıp yaramadığını test eder.

## Classification metrikleri

* accuracy
* precision
* recall
* F1
* ROC-AUC
* confusion matrix

## Regression metrikleri

* MAE
* MSE
* RMSE
* R²

## Clustering metrikleri

* silhouette score
* inertia
* Davies-Bouldin

Burada ayrıca şu kontroller yapılır:

* overfitting var mı?
* underfitting var mı?
* leakage olabilir mi?
* sınıf dengesizliği etkiliyor mu?
* business metric ile uyumlu mu?

Çünkü bazen akademik metrik iyi olur ama iş sonucu kötü olur.

Örnek:
Fraud modelinde accuracy %99 olabilir ama fraud’ları kaçırıyorsa model faydasızdır.

---

# 8) Model artifact ve versiyonlama katmanı

Eğitilen model kaydedilir.

Örnek:

* `.pkl`
* `.joblib`
* `.onnx`
* framework’e göre özel formatlar

Sadece model değil, şunlar da saklanmalıdır:

* scaler
* encoder
* feature sırası
* config
* eğitim tarihi
* metrikler
* veri versiyonu
* model versiyonu

Çünkü production’da şu rezalet çok yaşanır:
Model kaydedilir ama preprocessing unutulur.
Sonra API farklı sütun sırasıyla tahmin yapar ve saçmalar.

Bu yüzden mimaride **model + preprocessing birlikte** ele alınmalıdır.

---

# 9) Deployment katmanı

Burada model canlı ortama alınır.

Temel servis modelleri:

## A) Batch inference

Tahminler toplu üretilir.

Örnek:

* günlük churn skoru
* haftalık talep tahmini
* aylık kredi risk raporu

## B) Online inference

Kullanıcı isteği geldiğinde anlık tahmin yapılır.

Örnek:

* kredi başvurusunda anlık skor
* e-ticarette ürün öneri skoru
* fraud işlemi anında alarm

## C) Streaming inference

Sürekli akan veri üzerinde gerçek zamanlı tahmin

Örnek:

* sensör arıza tahmini
* anlık fraud
* trafik analizi

Deployment genelde şu araçlarla olur:

* FastAPI / Flask
* Docker
* Kubernetes
* model serving altyapıları

---

# 10) Monitoring ve bakım katmanı

Birçok kişinin unuttuğu ama en önemli katmandır.

Model canlıya çıktıktan sonra iş bitmez, başlar.

İzlenmesi gerekenler:

* tahmin gecikmesi
* hata oranı
* giriş veri dağılımı
* çıktı dağılımı
* business KPI etkisi
* veri drift
* concept drift

## Data drift

Giriş verisi değişir.

Örnek:
Eğitimde müşteri yaş ortalaması 35, production’da 49 olmuş.

## Concept drift

Girdi-hedef ilişkisi değişir.

Örnek:
Geçen yıl churn davranışı farklıydı, bu yıl ekonomi değişti ve örüntü bozuldu.

Bu durumda yeniden eğitim gerekir.

---

# ML mimarisi tipleri

Makine öğrenmesi sistemleri farklı mimarilerle kurulabilir.

---

# 1) Basit offline ML mimarisi

En temel yapı budur.

Akış:

```text
Veri Kaynağı
   ↓
CSV / DB
   ↓
Preprocessing
   ↓
Feature Engineering
   ↓
Train / Test Split
   ↓
Model Training
   ↓
Evaluation
   ↓
Model Save
```

Ne için uygundur?

* eğitim
* POC
* küçük projeler
* akademik çalışmalar

Eksisi:

* canlı sistem değildir
* otomasyon azdır
* izleme yoktur

---

# 2) Batch prediction mimarisi

Akış:

```text
DB / Data Warehouse
   ↓
Nightly ETL
   ↓
Preprocessing
   ↓
Model Inference
   ↓
Prediction Table
   ↓
Dashboard / CRM / Reporting
```

Kullanım:

* müşteri churn listesi
* kampanya hedefleme
* günlük risk raporu

Avantaj:

* daha basit
* düşük maliyetli
* kurumsal işlerde çok yaygın

---

# 3) Online inference mimarisi

Akış:

```text
Client Request
   ↓
API Gateway
   ↓
Feature Preparation
   ↓
Model Service
   ↓
Prediction Response
```

Kullanım:

* kredi skoru
* fraud kararı
* öneri motoru
* canlı fiyat tahmini

Burada önemli konular:

* latency
* ölçeklenebilirlik
* hata yönetimi
* fallback mekanizması

---

# 4) Real-time streaming ML mimarisi

Akış:

```text
Event Stream
   ↓
Streaming Processor
   ↓
Online Feature Computation
   ↓
Real-Time Model Inference
   ↓
Alert / Action
```

Kullanım:

* fraud
* IoT arıza tahmini
* log anomaly detection
* gerçek zamanlı reklam optimizasyonu

Bu mimari daha zor ama güçlüdür.

---

# 5) End-to-end production ML mimarisi

Bu daha kurumsal yapı olur.

```text
Data Sources
   ↓
Ingestion Layer
   ↓
Raw Storage
   ↓
Preprocessing Pipeline
   ↓
Feature Store
   ↓
Training Pipeline
   ↓
Validation / Evaluation
   ↓
Model Registry
   ↓
Deployment Service
   ↓
Monitoring / Drift Detection
   ↓
Retraining Pipeline
```

Bu artık oyuncak değil, ciddi üretim hattıdır.

---

# ML mimarisinde pipeline nedir?

Pipeline, veri işleme ve modelleme adımlarının sıralı ve tekrar edilebilir hale getirilmesidir.

Örnek pipeline:

* eksik veri doldurma
* encoding
* scaling
* model eğitimi

Neden önemlidir?

* train ile test aynı işlemden geçer
* leakage azalır
* tekrarlanabilirlik artar
* deployment kolaylaşır

Pipeline olmadan proje çoğu zaman “notebook sihri” olarak kalır.

---

# ML mimarisinde feature store nedir?

Feature store, modelin kullandığı özelliklerin merkezi ve tutarlı biçimde saklandığı yapıdır.

Neden önemlidir?

* training’de kullanılan feature ile serving’de kullanılan feature aynı olur
* tekrar üretim kolaylaşır
* ekipler ortak kullanır
* tutarsızlık azalır

Örnek:
“Son 30 günlük işlem sayısı” özelliği training’de başka, production’da başka hesaplanırsa model saçmalar.

Feature store bu saçmalığı önlemeye yarar.

---

# ML mimarisi ile DL mimarisi farkı

Bu karışıyor, net ayıralım.

## ML mimarisi

Daha çok **sistemin tamamını** ifade eder.

* veri akışı
* preprocessing
* feature engineering
* model lifecycle
* deployment
* monitoring

## DL mimarisi

Daha çok **sinir ağının iç yapısını** ifade eder.

* layer sayısı
* neuron düzeni
* CNN / RNN / Transformer
* activation
* attention

Yani:

* **ML mimarisi** = fabrikanın tamamı
* **DL mimarisi** = fabrikanın içindeki özel makinenin tasarımı

---

# Gerçek proje örneği 1: churn prediction ML mimarisi

Bir telekom şirketi müşterinin ayrılma riskini tahmin etmek istiyor.

## Veri kaynakları

* müşteri bilgisi
* fatura geçmişi
* çağrı merkezi kayıtları
* kullanım miktarı

## Preprocessing

* eksik veri doldurma
* kategorik encoding
* tarih dönüşümü

## Feature engineering

* son ödeme gecikme günleri
* son 90 gün destek talebi sayısı
* ortalama aylık kullanım

## Model

* XGBoost
* LightGBM
* Logistic Regression karşılaştırması

## Deployment

* haftalık batch skor üretimi

## Monitoring

* churn oranı değişimi
* feature drift
* model precision takibi

İşte bu bütün yapı bir **ML mimarisidir**.

---

# Gerçek proje örneği 2: fraud detection mimarisi

Banka kart işlemlerinde sahtekârlık tespiti.

## Veri kaynakları

* işlem bilgisi
* kullanıcı lokasyonu
* cihaz bilgisi
* geçmiş işlem davranışı

## Mimari tipi

* gerçek zamanlı online inference

## Pipeline

* işlem geldi
* son 1 saat işlem sayısı hesaplandı
* anlık feature üretildi
* model skoru döndü
* eşik üstüyse alarm

## Model

* XGBoost veya online anomaly model

## Monitoring

* false positive oranı
* fraud yakalama oranı
* inference latency

Bu mimari batch değildir; online’dır. Mimari seçimi tamamen iş problemine göre değişir.

---

# ML mimarisinde en önemli tasarım soruları

Bir sistem kurarken şu sorular sorulur:

1. Problem tipi ne?

    * classification mı?
    * regression mı?
    * clustering mi?

2. Veri tipi ne?

    * tablo mu?
    * metin mi?
    * görüntü mü?
    * zaman serisi mi?

3. Tahmin ne zaman gerekiyor?

    * anlık mı?
    * günlük mü?
    * haftalık mı?

4. Gecikme toleransı ne?

    * 20 ms mi?
    * 5 dakika mı?
    * gece batch mi?

5. Açıklanabilirlik gerekiyor mu?

    * finans ve sağlıkta kritik olabilir

6. Veri sıklıkla değişiyor mu?

    * drift yüksek mi?

7. Model ne sıklıkla güncellenecek?

Bu sorular mimariyi belirler.
Algoritmadan önce bunlar düşünülmelidir.

---

# Sık yapılan mimari hatalar

## 1) Notebook’u sistem sanmak

Notebook demo içindir; üretim sistemi değildir.

## 2) Preprocessing’i modele dahil etmemek

Train’de yapılan dönüşüm serving’de unutulur.

## 3) Test verisini erken kullanmak

Sahte başarı üretir.

## 4) Feature leakage

Gelecek bilgisi modele sızar.

## 5) Monitoring koymamak

Canlı sistem bozulur, kimse fark etmez.

## 6) Retraining stratejisi olmamak

Model eskir.

## 7) Business metric’i göz ardı etmek

Accuracy iyi diye sevinilir, iş sonucu kötü olur.

---

# Basit bir ML mimarisi şeması

```text
[Veri Kaynakları]
      ↓
[Veri Toplama]
      ↓
[Veri Temizleme / Preprocessing]
      ↓
[Feature Engineering]
      ↓
[Train / Validation / Test]
      ↓
[Model Training]
      ↓
[Evaluation]
      ↓
[Model Registry / Save]
      ↓
[Deployment]
      ↓
[Monitoring]
      ↓
[Retraining]
```

Bu akış ML mimarisinin omurgasıdır.

---

# Kısa özet

**ML mimarisi**, makine öğrenmesi modelinin yalnızca algoritmasını değil, **verinin alınmasından canlıda izlenmesine kadar tüm yaşam döngüsünü kapsayan sistem tasarımıdır.**

İçerdiği ana parçalar:

* veri kaynakları
* preprocessing
* feature engineering
* model training
* evaluation
* deployment
* monitoring
* retraining

Yani ML mimarisi:
**“Modeli nasıl kurduk?”** sorusundan daha büyük bir şeydir.
Asıl soru şudur:

**“Bu modeli veriyle birlikte, güvenilir, tekrar üretilebilir ve sürdürülebilir biçimde nasıl çalıştıracağız?”**

İşte mimari bunun cevabıdır.




------------------------------------------------
------------------------------------------------

SORU-XX AI mimarisi nedir ? detaylıca açıklayınız ?

Önce ne yapacağımı söyleyeyim.
“**AI mimarisi nedir**” sorusunu sadece yüzeysel değil, mühendislik bakışıyla anlatacağım. Önce kavramı netleştireceğim, sonra bir yapay zekâ sisteminin **katmanlarını**, **bileşenlerini**, **veri akışını**, **mimari tiplerini**, **gerçek sistem örneklerini** ve **ML / DL mimarilerinden farkını** ayrıntılı şekilde açıklayacağım.

---

# AI mimarisi nedir?

**AI mimarisi**, bir yapay zekâ sisteminin **veri, model, karar mekanizması ve servis katmanlarının nasıl organize edildiğini belirleyen sistem tasarımıdır.**

Başka bir ifadeyle:

AI mimarisi şu soruların cevabıdır:

* sistem hangi veriyi kullanıyor?
* veri nasıl işleniyor?
* hangi model öğreniyor?
* karar nasıl veriliyor?
* sonuç nasıl sunuluyor?
* sistem nasıl güncelleniyor?

Yani AI mimarisi sadece model değildir.
**AI mimarisi = tüm yapay zekâ sisteminin tasarımıdır.**

Bir benzetme yapalım:

* **algoritma** → motor
* **ML modeli** → aracın motoru
* **AI mimarisi** → aracın tamamı

---

# AI mimarisi neden gereklidir?

Çünkü gerçek dünyada AI sadece model değildir.

Bir AI sistemi şu problemlerle uğraşır:

* veri farklı kaynaklardan gelir
* veri sürekli değişir
* model güncellenir
* kullanıcı sorgu gönderir
* sonuç hızlı dönmelidir
* sistem izlenmelidir
* model zamanla bozulur

AI mimarisi bu karmaşıklığı yönetir.

---

# AI mimarisinin temel bileşenleri

Bir AI sisteminin mimarisi genellikle şu katmanlardan oluşur:

1️⃣ Veri katmanı
2️⃣ Veri işleme katmanı
3️⃣ Feature engineering katmanı
4️⃣ Model eğitim katmanı
5️⃣ Model değerlendirme katmanı
6️⃣ Model servis katmanı
7️⃣ Karar katmanı
8️⃣ İzleme ve yeniden eğitim katmanı

Şimdi bunları tek tek inceleyelim.

---

# 1) Veri katmanı

AI sistemlerinin yakıtı veridir.

Veri kaynakları şunlar olabilir:

* veritabanları
* API servisleri
* log kayıtları
* sensör verileri
* kullanıcı davranışı
* görüntü verisi
* metin verisi
* ses verisi
* IoT verileri

Örnek:

Bir e-ticaret AI sistemi şu verileri kullanabilir:

* müşteri davranışı
* ürün görüntüleri
* satın alma geçmişi
* arama kayıtları
* tıklama verileri

Bu veriler AI sisteminin girişini oluşturur.

---

# 2) Veri toplama ve veri akışı

Veri sistem içine iki şekilde alınabilir.

### Batch veri akışı

Veri belirli aralıklarla alınır.

Örnek:

* günlük satış raporu
* haftalık müşteri analizi

### Streaming veri akışı

Veri sürekli akar.

Örnek:

* kredi kartı işlemleri
* sensör verisi
* gerçek zamanlı trafik

Streaming mimariler genellikle şu sistemleri kullanır:

* Kafka
* Kinesis
* Pub/Sub

---

# 3) Veri işleme ve veri hazırlama

Ham veri genellikle model için uygun değildir.

Bu aşamada yapılan işlemler:

* veri temizleme
* eksik veri doldurma
* aykırı değer temizleme
* veri tipi dönüşümü
* kategorik veri encoding
* veri ölçekleme

Örnek:

Bir müşteri veri seti düşün:

ham veri:

```
isim
şehir
alışveriş tarihi
fatura tutarı
```

model için dönüştürülmüş veri:

```
şehir_encoded
son alışveriş gün sayısı
ortalama harcama
alışveriş sıklığı
```

---

# 4) Feature engineering katmanı

Bu aşamada veriden anlamlı özellikler üretilir.

Örnek:

Ham veri:

```
doğum tarihi
alışveriş tarihleri
```

Feature üretimi:

```
yaş
son alışverişten geçen gün
son 30 gün alışveriş sayısı
```

Feature engineering AI sistemlerinde çok önemlidir.

Çünkü model veriyi olduğu gibi değil, **özellikler üzerinden öğrenir.**

---

# 5) Model eğitim katmanı

Bu aşamada AI modeli eğitilir.

Kullanılan yöntemler:

### Machine Learning

* Logistic Regression
* Random Forest
* XGBoost
* SVM

### Deep Learning

* CNN
* RNN
* Transformer

### Generative AI

* GPT
* Diffusion
* GAN

Model bu aşamada veri üzerinden öğrenir.

---

# 6) Model değerlendirme katmanı

Model eğitildikten sonra performansı ölçülür.

### Classification metrikleri

* accuracy
* precision
* recall
* F1
* ROC-AUC

### Regression metrikleri

* MAE
* MSE
* RMSE
* R²

Ama sadece metrik yeterli değildir.

Şu sorular da sorulur:

* overfitting var mı?
* model adil mi?
* model açıklanabilir mi?
* veri sızıntısı var mı?

---

# 7) Model servis katmanı

Model eğitildikten sonra **kullanıcıların erişebileceği şekilde servis edilir.**

Bu genelde API ile yapılır.

Örnek mimari:

```
Client
   ↓
API
   ↓
Model Service
   ↓
Prediction
```

Kullanılan araçlar:

* FastAPI
* Flask
* TensorFlow Serving
* TorchServe
* Docker
* Kubernetes

---

# 8) Karar katmanı

AI sistemleri çoğu zaman sadece tahmin üretmez, karar üretir.

Örnek:

Fraud detection sistemi.

Model:

```
fraud probability = 0.87
```

Karar sistemi:

```
> 0.8 ise işlem blokla
```

Yani model çıktı üretir, karar katmanı bu çıktıyı yorumlar.

---

# 9) İzleme ve bakım katmanı

AI sistemlerinde model zamanla bozulabilir.

Buna **model drift** denir.

İzlenmesi gereken şeyler:

* veri dağılımı
* tahmin dağılımı
* hata oranı
* gecikme süresi

Örnek:

Eğitim verisinde müşteri yaş ortalaması:

```
35
```

Canlı sistemde:

```
47
```

Bu **data drift** olabilir.

Bu durumda model yeniden eğitilmelidir.

---

# AI mimari türleri

AI sistemleri farklı mimari modellerle kurulabilir.

---

# 1) Basit AI mimarisi

Küçük projelerde kullanılır.

Akış:

```
Veri
↓
Preprocessing
↓
Model
↓
Prediction
```

Bu mimari eğitim ve prototip için uygundur.

---

# 2) Batch AI mimarisi

Tahminler toplu yapılır.

Örnek:

* günlük satış tahmini
* haftalık müşteri segmentasyonu

Akış:

```
DB
↓
ETL
↓
Model
↓
Prediction Table
↓
Dashboard
```

---

# 3) Online AI mimarisi

Tahminler anlık yapılır.

Örnek:

* kredi skoru
* öneri sistemi
* fraud detection

Akış:

```
User Request
↓
API
↓
Feature Processing
↓
Model
↓
Prediction
```

---

# 4) Streaming AI mimarisi

Gerçek zamanlı veri akışı üzerinde çalışır.

Örnek:

* IoT
* anlık fraud
* trafik analizi

Akış:

```
Event Stream
↓
Stream Processing
↓
Model
↓
Alert
```

---

# 5) Generative AI mimarisi

Modern AI sistemlerinde kullanılan mimaridir.

Bileşenler:

* LLM
* embedding modeli
* vector database
* retrieval sistemi
* inference servisi

Örnek:

RAG mimarisi.

```
User Question
↓
Embedding
↓
Vector Search
↓
LLM
↓
Answer
```

---

# AI mimarisi ile ML mimarisi farkı

Bu iki kavram sık karıştırılır.

### ML mimarisi

Makine öğrenmesi modellerinin veri pipeline’ı.

Odak:

* veri
* model
* training
* evaluation

### AI mimarisi

Daha geniştir.

Şunları kapsar:

* ML
* DL
* NLP
* bilgisayarla görme
* karar sistemleri
* bilgi tabanı
* kural motoru

Yani:

**AI mimarisi = ML mimarisi + karar sistemleri + uygulama sistemi**

---

# AI mimarisinin gerçek dünya örnekleri

## 1) Netflix öneri sistemi

Veri:

* izleme geçmişi
* kullanıcı davranışı
* film özellikleri

AI mimarisi:

```
User Data
↓
Feature Store
↓
Recommendation Model
↓
Ranking System
↓
Personalized Feed
```

---

## 2) Fraud detection sistemi

```
Transaction
↓
Feature Computation
↓
Fraud Model
↓
Risk Score
↓
Decision Engine
```

---

## 3) ChatGPT benzeri sistem

```
User Prompt
↓
Embedding
↓
Context Retrieval
↓
LLM
↓
Generated Response
```

---

# AI mimarisi tasarlanırken sorulan kritik sorular

Bir AI sistemi kurulurken şu sorular sorulur:

* veri nereden geliyor?
* veri ne sıklıkla güncelleniyor?
* model ne kadar hızlı cevap vermeli?
* tahmin anlık mı batch mi?
* model açıklanabilir mi?
* model ne sıklıkla güncellenecek?
* sistem kaç kullanıcıya hizmet verecek?

Bu sorular mimariyi belirler.

---

# AI mimarisinin avantajları

* büyük veri ile çalışabilir
* karmaşık problemleri çözebilir
* otomatik karar üretir
* ölçeklenebilir sistem kurar

---

# AI mimarisinin zorlukları

* veri yönetimi zor olabilir
* model drift oluşabilir
* maliyet yüksek olabilir
* açıklanabilirlik zor olabilir

---

# Kısa özet

**AI mimarisi**, yapay zekâ sisteminin uçtan uca tasarımını ifade eder.

İçerdiği temel bileşenler:

* veri kaynakları
* veri işleme
* feature engineering
* model eğitimi
* model servis etme
* karar mekanizması
* izleme ve yeniden eğitim

Yani AI mimarisi şunu anlatır:

**“Bir yapay zekâ sistemi veriyi alıp nasıl öğrenir, karar verir ve canlı ortamda nasıl çalışır?”**

---



------------------------------------------------
------------------------------------------------

SORU-XX AI,ML,DL ile ilgii en çok kullanılan sözlük kelimeler ve açıklamaları yaz çok detaylı olaraka
Önce ne yapacağımı söyleyeyim.

AI, ML ve DL alanında **en çok kullanılan teknik terimleri** bir sözlük mantığında anlatacağım. Kavramları **temel kavramlar → veri kavramları → model kavramları → eğitim kavramları → değerlendirme kavramları → derin öğrenme kavramları** şeklinde düzenleyeceğim. Her terimin kısa tanımını, ne işe yaradığını ve nerede kullanıldığını açıklayalım.

---

# AI – ML – DL Sözlüğü (Temel Kavramlar)

## Artificial Intelligence (AI)

Bilgisayarların insan benzeri görevleri yerine getirmesini amaçlayan geniş bilim alanıdır.
Amaç:

* problem çözme
* karar verme
* öğrenme
* algılama
* dil anlama

AI; makine öğrenmesi, uzman sistemler, planlama algoritmaları gibi birçok yaklaşımı kapsayan **üst şemsiye alandır**.

---

## Machine Learning (ML)

Makine öğrenmesi, bilgisayarların veriden örüntüler öğrenmesini sağlayan yapay zekâ alt alanıdır.

Klasik programlama:

```
kurallar + veri → sonuç
```

Makine öğrenmesi:

```
veri + sonuç örnekleri → model öğrenir → yeni sonuç üretir
```

Model, verideki ilişkileri öğrenir ve yeni veriler için tahmin üretir.

---

## Deep Learning (DL)

Derin öğrenme, çok katmanlı yapay sinir ağları kullanarak veriden karmaşık temsiller öğrenen makine öğrenmesi alt dalıdır.

Özellikle güçlü olduğu alanlar:

* görüntü tanıma
* konuşma tanıma
* doğal dil işleme
* video analizi
* üretici yapay zekâ

---

## Model

Veriden öğrenilen matematiksel yapıdır.

Model aslında şu fonksiyonu temsil eder:

```
f(x) → y
```

x = giriş verisi
y = tahmin edilen çıktı

Örnek model:

* logistic regression
* decision tree
* neural network

---

## Algorithm

Modeli eğitmek için kullanılan matematiksel yöntemdir.

Örnek algoritmalar:

* gradient descent
* random forest
* support vector machine
* k-means

Algoritma = öğrenme yöntemi
Model = öğrenilen yapı

---

# Veri ile ilgili terimler

## Dataset

Makine öğrenmesi için kullanılan veri kümesidir.

Genellikle tablo formatındadır.

```
rows → örnekler
columns → özellikler
```

---

## Sample (Observation)

Veri setindeki tek bir kayıt.

Örnek:

Bir müşteri

```
yaş = 35
gelir = 20000
şehir = Ankara
```

---

## Feature

Modelin kullandığı giriş değişkenleridir.

Örnek:

Ev fiyatı tahmini modeli

Feature’lar:

* metrekare
* oda sayısı
* konum
* bina yaşı

---

## Feature Vector

Bir gözleme ait bütün özelliklerin sayısal temsilidir.

```
[120 m², 3 oda, 5 yaş, şehir = İstanbul]
```

Bu vektör modele giriş olur.

---

## Target (Label)

Modelin tahmin etmeye çalıştığı değişkendir.

Örnek:

```
ev fiyatı
spam / değil
hastalık var / yok
```

---

## Structured Data

Tablo formatında düzenlenmiş verilerdir.

Örnek:

* SQL verileri
* Excel tabloları
* müşteri kayıtları

---

## Unstructured Data

Tablo formatında olmayan veridir.

Örnek:

* görüntüler
* metinler
* ses kayıtları
* videolar

---

# Öğrenme türleri

## Supervised Learning

Model, etiketli veri ile eğitilir.

Veri:

```
X → özellikler
y → hedef
```

Amaç:

```
X → y ilişkisini öğrenmek
```

Örnek:

* spam tespiti
* kredi riski
* fiyat tahmini

---

## Unsupervised Learning

Veride etiket yoktur.

Model verideki yapıyı keşfeder.

Örnek:

* müşteri segmentasyonu
* veri kümeleri

---

## Reinforcement Learning

Ajan, çevreyle etkileşerek ödül-ceza mekanizması ile öğrenir.

Kullanım alanları:

* oyun AI
* robotik
* otonom araç

---

# Problem türleri

## Classification

Amaç veriyi kategorilere ayırmaktır.

Örnek:

```
spam / değil
kanser / değil
kedi / köpek
```

---

## Regression

Amaç sayısal bir değer tahmin etmektir.

Örnek:

```
ev fiyatı
satış tahmini
sıcaklık tahmini
```

---

## Clustering

Veriyi benzer gruplara ayırmaktır.

Model etiketleri bilmez.

Örnek:

* müşteri segmentasyonu

---

# Model eğitim terimleri

## Training

Modelin veriden öğrenme sürecidir.

Model parametreleri eğitim verisi üzerinden güncellenir.

---

## Epoch

Modelin tüm veri setini bir kez görmesi.

Örnek:

```
10 epoch → model veri setini 10 kez görür
```

---

## Batch

Eğitim sırasında verinin küçük parçalara bölünmesidir.

Örnek:

```
batch size = 32
```

Model her adımda 32 örnek görür.

---

## Iteration

Bir batch'in modelden geçirilmesidir.

---

## Hyperparameter

Model eğitiminden önce belirlenen parametrelerdir.

Örnek:

* learning rate
* tree depth
* batch size
* epoch sayısı

---

## Parameter

Modelin öğrenme sırasında optimize ettiği değerlerdir.

Örnek:

* neural network ağırlıkları
* regression katsayıları

---

# Model performans kavramları

## Accuracy

Doğru tahmin oranıdır.

```
accuracy = doğru tahmin / toplam tahmin
```

---

## Precision

Pozitif tahminlerin doğruluk oranıdır.

---

## Recall

Gerçek pozitifleri yakalama oranıdır.

---

## F1 Score

Precision ve recall'un dengeli ortalamasıdır.

---

## Confusion Matrix

Model tahminlerinin dağılımını gösteren tablodur.

```
True Positive
True Negative
False Positive
False Negative
```

---

# Model hataları

## Overfitting

Model eğitim verisini ezberler.

Belirtiler:

```
train accuracy yüksek
test accuracy düşük
```

---

## Underfitting

Model veriyi yeterince öğrenemez.

Belirtiler:

```
train düşük
test düşük
```

---

# Veri kavramları

## Data Leakage

Modelin tahmin sırasında erişememesi gereken bilgiyi kullanmasıdır.

Bu durum model performansını sahte şekilde yükseltir.

---

## Missing Data

Eksik veri değerleridir.

Çözüm yöntemleri:

* silme
* ortalama doldurma
* model ile tahmin

---

## Outlier

Normal veri dağılımından aşırı uzak değerlerdir.

Örnek:

```
normal maaş = 10000
outlier = 1.000.000
```

---

# Derin öğrenme terimleri

## Neural Network

İnsan beyninden esinlenen matematiksel modeldir.

Katmanlardan oluşur.

---

## Neuron

Sinir ağındaki temel hesaplama birimidir.

---

## Layer

Ağın katmanlarıdır.

Türleri:

* input layer
* hidden layer
* output layer

---

## Activation Function

Neuron çıktısını dönüştüren fonksiyondur.

Örnek:

* ReLU
* Sigmoid
* Tanh
* Softmax

---

## Backpropagation

Sinir ağında hatayı geriye doğru yayarak ağırlıkları güncelleme algoritmasıdır.

---

## Gradient Descent

Hata fonksiyonunu minimize etmek için kullanılan optimizasyon algoritmasıdır.

---

## Loss Function

Modelin hatasını ölçen fonksiyondur.

Örnek:

* MSE
* Cross entropy

---

# NLP terimleri

## Token

Metnin parçalanmış halidir.

Örnek:

```
"Machine learning is powerful"

tokenler:

machine
learning
is
powerful
```

---

## Embedding

Kelimenin sayısal vektör temsili.

---

## Transformer

Modern NLP modellerinin temel mimarisidir.

ChatGPT, BERT gibi modeller transformer kullanır.

---

# Üretici yapay zekâ terimleri

## Generative AI

Yeni veri üretebilen yapay zekâ modelleridir.

Örnek:

* metin üretimi
* resim üretimi
* müzik üretimi

---

## Large Language Model (LLM)

Büyük metin veri setleri üzerinde eğitilmiş dil modelleridir.

Örnek:

* GPT
* LLaMA
* Claude

---

# Sonuç

AI-ML-DL alanındaki kavramlar temel olarak şu kategorilere ayrılır:

```
AI temel kavramlar
veri kavramları
öğrenme türleri
problem tipleri
model eğitim kavramları
model değerlendirme
derin öğrenme kavramları
```

Bu kavramları anlamak, yapay zekâ sistemlerini doğru kurabilmenin temelidir.

---

------------------------------------------------
------------------------------------------------

SORU-XX Hazırla AI-ML-DL için 300+ teknik terimden oluşan geniş sözlük

Önce ne yapacağımı söyleyeyim.
AI-ML-DL alanında **300+ teknik terimi** bir sözlük formatında hazırlayacağım. Kavramları mantıklı bir düzenlemesi:

1️⃣ Temel AI kavramları
2️⃣ Veri ve veri bilimi kavramları
3️⃣ Makine öğrenmesi kavramları
4️⃣ Model eğitimi kavramları
5️⃣ Model değerlendirme kavramları
6️⃣ Derin öğrenme kavramları
7️⃣ NLP kavramları
8️⃣ Computer Vision kavramları
9️⃣ Generative AI kavramları
10️⃣ MLOps kavramları

Her terimin kısa ama teknik açıklaması olacak. Bu bir **referans sözlük** gibi kullanılabilir.

Uzun olduğu için parça parça ilerleyeceğim.

---

# AI – ML – DL TEKNİK SÖZLÜK (300+ Terim)

---

# 1. TEMEL AI KAVRAMLARI

### Artificial Intelligence

Bilgisayarların insan benzeri karar verme, öğrenme ve problem çözme yeteneklerini taklit etmesini amaçlayan bilim alanıdır.

### Narrow AI

Belirli bir görevi yerine getiren yapay zekâ sistemidir.
Örnek: spam filtreleri.

### General AI

İnsan seviyesinde genel zekâya sahip teorik yapay zekâdır.

### Super AI

İnsan zekasını aşan hipotetik yapay zekâ sistemidir.

### Intelligent Agent

Çevreyi algılayıp hedefe göre hareket eden sistemdir.

### Environment

Ajanın etkileşimde bulunduğu ortamdır.

### State

Sistemin belirli bir andaki durumunu temsil eder.

### Action

Ajanın gerçekleştirdiği davranıştır.

### Policy

Ajanın hangi durumda hangi aksiyonu alacağını belirleyen stratejidir.

### Reward

Reinforcement learning’de ajanı yönlendiren ödül sinyalidir.

### Planning

AI sistemlerinin hedefe ulaşmak için adımlar planlamasıdır.

### Search Algorithm

Problem çözmek için durum uzayında arama yapan algoritmalardır.

### Heuristic

Problemi çözmek için kullanılan yaklaşık yöntemdir.

### Knowledge Representation

Bilginin bilgisayar tarafından anlaşılabilir şekilde modellenmesidir.

### Expert System

Uzman bilgisi içeren kural tabanlı AI sistemidir.

### Inference Engine

Uzman sistemlerde karar çıkarımı yapan modüldür.

### Symbolic AI

Mantık ve sembolik kurallarla çalışan yapay zekâ yaklaşımıdır.

### Connectionism

Sinir ağlarına dayalı AI yaklaşımıdır.

### Cognitive Computing

İnsan düşünce süreçlerini modelleyen AI sistemleridir.

### Autonomous System

İnsan müdahalesi olmadan çalışan sistemdir.

---

# 2. VERİ VE VERİ BİLİMİ KAVRAMLARI

### Dataset

Makine öğrenmesi için kullanılan veri kümesidir.

### Data Point

Veri setindeki tek bir gözlemdir.

### Feature

Modelin kullandığı giriş değişkenidir.

### Feature Vector

Bir örneğe ait tüm özelliklerin sayısal temsili.

### Label

Modelin tahmin etmeye çalıştığı hedef değişken.

### Structured Data

Tablo şeklinde organize edilmiş veridir.

### Unstructured Data

Metin, görüntü veya ses gibi yapılandırılmamış veridir.

### Semi-Structured Data

JSON veya XML gibi yarı yapılandırılmış veridir.

### Data Preprocessing

Verinin model için hazırlanması sürecidir.

### Data Cleaning

Eksik veya hatalı verilerin düzeltilmesidir.

### Data Transformation

Verinin farklı formatlara dönüştürülmesidir.

### Data Normalization

Verilerin aynı ölçeğe getirilmesidir.

### Standardization

Verinin ortalaması 0 ve varyansı 1 olacak şekilde ölçeklenmesidir.

### Encoding

Kategorik verinin sayısal forma dönüştürülmesidir.

### One-Hot Encoding

Her kategori için ayrı binary sütun oluşturma yöntemidir.

### Label Encoding

Kategorileri sayısal değerlere dönüştürme yöntemidir.

### Data Augmentation

Veri setini artırmak için yapılan dönüşümlerdir.

### Sampling

Veri setinden örnek seçme işlemidir.

### Stratified Sampling

Sınıf dağılımını koruyarak örnekleme yapmaktır.

### Data Imbalance

Veri setinde sınıfların eşit dağılmaması durumudur.

### Outlier

Veri dağılımından aşırı uzak gözlemdir.

### Missing Data

Eksik veri değeridir.

### Data Pipeline

Veri işleme adımlarının otomatik akışıdır.

### Data Drift

Zamanla veri dağılımının değişmesidir.

### Concept Drift

Hedef değişken ile özellikler arasındaki ilişkinin değişmesidir.

---

# 3. MAKİNE ÖĞRENMESİ KAVRAMLARI

### Machine Learning

Veriden öğrenen algoritmalar geliştiren AI alanıdır.

### Supervised Learning

Etiketli veri ile öğrenme yöntemidir.

### Unsupervised Learning

Etiketsiz veri ile öğrenme yöntemidir.

### Reinforcement Learning

Ödül-ceza sistemi ile öğrenme yöntemidir.

### Semi-Supervised Learning

Az etiketli veri ile öğrenme yöntemidir.

### Self-Supervised Learning

Verinin kendisinden etiket üreterek öğrenme yöntemidir.

### Classification

Verileri kategorilere ayırma problemidir.

### Regression

Sürekli değer tahmini problemidir.

### Clustering

Benzer verileri kümelere ayırma problemidir.

### Dimensionality Reduction

Veri boyutunu azaltma yöntemidir.

### Feature Engineering

Yeni özellikler oluşturma sürecidir.

### Feature Selection

En önemli özellikleri seçme işlemidir.

### Feature Importance

Model için en etkili özelliklerin ölçülmesidir.

### Model

Veriden öğrenilen matematiksel yapı.

### Algorithm

Modeli eğiten yöntem.

### Hyperparameter

Model eğitimi öncesi belirlenen parametre.

### Parameter

Modelin öğrenme sırasında optimize ettiği değer.

### Decision Boundary

Sınıfları ayıran matematiksel sınır.

### Bias

Modelin sistematik hatası.

### Variance

Modelin veriye aşırı duyarlılığı.

### Bias-Variance Tradeoff

Model karmaşıklığı ile hata arasındaki denge.

---

# 4. MODEL EĞİTİMİ KAVRAMLARI

### Training

Modelin öğrenme sürecidir.

### Epoch

Modelin tüm veri setini bir kez görmesidir.

### Batch

Eğitim sırasında kullanılan veri parçası.

### Batch Size

Bir iterasyonda kullanılan örnek sayısı.

### Iteration

Bir batch’in işlenmesidir.

### Learning Rate

Model ağırlıklarının güncellenme hızıdır.

### Gradient

Hata fonksiyonunun türevidir.

### Gradient Descent

Hata fonksiyonunu minimize eden optimizasyon algoritmasıdır.

### Stochastic Gradient Descent

Rastgele örneklerle yapılan gradient descent yöntemidir.

### Mini Batch Gradient Descent

Batch ve stochastic yönteminin birleşimidir.

### Loss Function

Model hatasını ölçen fonksiyondur.

### Cost Function

Tüm veri için hesaplanan toplam hatadır.

### Optimization

Model parametrelerini iyileştirme sürecidir.

### Convergence

Modelin stabil hale gelmesidir.

### Initialization

Model ağırlıklarının başlangıç değeridir.

---

# 5. MODEL DEĞERLENDİRME KAVRAMLARI

### Train Set

Modelin öğrenmesi için kullanılan veri.

### Validation Set

Model ayarlamaları için kullanılan veri.

### Test Set

Model performansını ölçmek için kullanılan veri.

### Cross Validation

Veriyi birden fazla parçaya bölerek model test etme yöntemidir.

### K-Fold Cross Validation

Veriyi k parçaya bölerek eğitim ve test yapma yöntemidir.

### Accuracy

Doğru tahmin oranı.

### Precision

Pozitif tahminlerin doğruluk oranı.

### Recall

Gerçek pozitifleri yakalama oranı.

### F1 Score

Precision ve recall’un harmonik ortalaması.

### ROC Curve

Model performansını gösteren grafik.

### AUC

ROC eğrisinin altındaki alan.

### Confusion Matrix

Tahmin sonuçlarının tablo gösterimi.

### MAE

Ortalama mutlak hata.

### MSE

Ortalama kare hata.

### RMSE

Karekök ortalama hata.

### R² Score

Regresyon performans ölçüsüdür.

---

# 6. DERİN ÖĞRENME KAVRAMLARI

### Neural Network

İnsan beyninden esinlenen matematiksel modeldir.

### Neuron

Sinir ağındaki hesaplama birimidir.

### Layer

Sinir ağındaki katman.

### Input Layer

Verinin girdiği katman.

### Hidden Layer

Ara katmanlar.

### Output Layer

Model çıktısını üreten katman.

### Activation Function

Neuron çıktısını dönüştüren fonksiyon.

### ReLU

Rectified Linear Unit aktivasyon fonksiyonu.

### Sigmoid

0-1 arasında çıktı veren fonksiyon.

### Tanh

-1 ile 1 arasında çıktı veren fonksiyon.

### Softmax

Çok sınıflı sınıflandırma fonksiyonu.

### Backpropagation

Hatanın geriye yayılması algoritması.

### Vanishing Gradient

Gradient değerlerinin çok küçülmesi sorunu.

### Exploding Gradient

Gradient değerlerinin aşırı büyümesi sorunu.

### Dropout

Overfitting’i azaltan düzenleme yöntemi.

### Batch Normalization

Katman girişlerini normalize eden yöntem.

### Convolution

Görüntü işlemede kullanılan filtreleme işlemi.

### Kernel

Convolution filtresidir.

### Stride

Filtrenin kayma adımıdır.

### Padding

Görüntü boyutunu korumak için yapılan dolgu.

### Pooling

Özellik haritasını küçültme işlemi.

### Max Pooling

En büyük değeri seçen pooling yöntemi.

### Average Pooling

Ortalama değer alan pooling yöntemi.

---

# 7. NLP TERİMLERİ

### Natural Language Processing

Bilgisayarların insan dilini anlamasını sağlayan AI alanıdır.

### Token

Metnin parçalanmış birimidir.

### Tokenization

Metni tokenlara ayırma işlemidir.

### Stop Words

Anlam taşımayan yaygın kelimelerdir.

### Stemming

Kelime kökünü bulma yöntemidir.

### Lemmatization

Kelimenin sözlük formunu bulma işlemidir.

### N-Gram

Kelime grupları.

### Bag of Words

Metni kelime frekansları ile temsil etme yöntemidir.

### TF-IDF

Kelime önemini ölçen istatistiksel yöntem.

### Word Embedding

Kelimenin vektör temsili.

### Word2Vec

Kelime embedding algoritması.

### GloVe

Kelime vektör modeli.

### Transformer

Modern NLP mimarisi.

### Attention

Modelin önemli kelimelere odaklanmasını sağlayan mekanizma.

### Self Attention

Kelimenin diğer kelimelerle ilişkisini hesaplayan yöntem.

---

# 8. COMPUTER VISION TERİMLERİ

### Computer Vision

Görüntüleri analiz eden AI alanıdır.

### Image Classification

Görüntüyü kategorize etme problemidir.

### Object Detection

Görüntüdeki nesneleri bulma işlemidir.

### Bounding Box

Nesne etrafındaki dikdörtgen kutu.

### Semantic Segmentation

Her pikseli sınıflandırma işlemidir.

### Instance Segmentation

Her nesneyi ayrı ayrı segment etme yöntemidir.

### Feature Map

CNN katmanlarında oluşan özellik haritasıdır.

---

# 9. GENERATIVE AI TERİMLERİ

### Generative AI

Yeni veri üretebilen yapay zekâ modelleridir.

### Large Language Model

Büyük metin veri setleri ile eğitilmiş dil modelidir.

### Prompt

Modelin giriş metni.

### Prompt Engineering

Modelden doğru çıktı almak için prompt tasarlama yöntemidir.

### Fine Tuning

Önceden eğitilmiş modeli yeniden eğitme işlemidir.

### Diffusion Model

Görüntü üretimi için kullanılan model türüdür.

### GAN

Generative Adversarial Network.

---

# 10. MLOPS TERİMLERİ

### MLOps

Makine öğrenmesi sistemlerinin üretime alınması ve yönetilmesidir.

### Model Deployment

Modelin üretim ortamına taşınması.

### Model Monitoring

Model performansını izleme.

### Model Retraining

Modeli yeniden eğitme.

### CI/CD

Sürekli entegrasyon ve dağıtım süreci.

### Feature Store

Model özelliklerinin saklandığı sistem.

### Experiment Tracking

Model deneylerinin kaydedilmesi.

---



------------------------------------------------
------------------------------------------------

SORU-XX Hazırla AI / ML projelerinde kullanılan Python kütüphaneleri sözlüğü

AI / ML projelerinde kullanılan **Python kütüphanelerini sözlük formatında** düzenleyeceğim. Sadece isim vermeyeceğim; her kütüphane için **ne işe yarar, hangi problemde kullanılır, güçlü tarafı nedir, tipik kullanım senaryosu nedir** bunları yazacağım.
Düzeni şu şekilde kuracağım:

* Temel veri işleme
* Görselleştirme
* Klasik ML
* İstatistik ve bilimsel hesaplama
* Deep Learning
* NLP
* Computer Vision
* Generative AI / LLM
* MLOps / deployment / tracking
* Büyük veri ve yardımcı araçlar

Bu konu geniş. İlk parçada sağlam bir sözlük vereceğim. Sonra istersen **2. parçada ileri seviye ve niş kütüphaneleri** de eklerim.

---

# AI / ML Projelerinde Kullanılan Python Kütüphaneleri Sözlüğü

## 1) Temel Veri İşleme Kütüphaneleri

### NumPy

Python’da sayısal hesaplama için temel kütüphanedir.
Çok boyutlu diziler (`ndarray`) üzerinde hızlı işlem yapmayı sağlar.

**Ne için kullanılır?**

* vektör/matris işlemleri
* lineer cebir
* istatistiksel hesaplamalar
* ML modellerine veri hazırlama

**Neden önemli?**
AI/ML ekosisteminin temel taşıdır. Birçok kütüphane içerde NumPy kullanır.

**Tipik kullanım:**

* dizi oluşturma
* reshape
* broadcasting
* toplama, çarpma, matris işlemleri

---

### Pandas

Tablo verisiyle çalışmak için en çok kullanılan kütüphanedir.

**Temel yapıları:**

* `Series`
* `DataFrame`

**Ne için kullanılır?**

* CSV / Excel / SQL veri okuma
* veri temizleme
* sütun bazlı işlem
* eksik veri analizi
* gruplama ve özetleme
* feature engineering

**Neden önemli?**
Makine öğrenmesi projelerinde modelden önce en çok zaman burada harcanır.

**Tipik kullanım:**

* `read_csv`
* filtreleme
* `groupby`
* `merge`
* `fillna`
* `dropna`

---

### Polars

Pandas’a alternatif, daha hızlı ve modern veri işleme kütüphanesidir.

**Ne için kullanılır?**

* büyük tablo verilerinde hızlı işlem
* lazy execution
* yüksek performanslı veri dönüşümleri

**Neden önemli?**
Özellikle büyük veri setlerinde Pandas’tan daha hızlı olabilir.

**Tipik kullanım:**

* büyük CSV işleme
* kolon bazlı analitik
* performans odaklı ETL

---

### PyArrow

Bellek verimliliği yüksek kolon bazlı veri yapıları ve formatları için kullanılır.

**Ne için kullanılır?**

* Parquet
* Arrow formatı
* hızlı veri paylaşımı
* büyük veri araçlarıyla entegrasyon

**Neden önemli?**
Modern veri mühendisliği ve ML pipeline’larında çok görülür.

---

### OpenPyXL

Excel dosyalarıyla çalışmak için kullanılır.

**Ne için kullanılır?**

* `.xlsx` okuma/yazma
* Excel raporu oluşturma
* hücre stilleri
* tablo üretme

**Tipik kullanım:**

* iş dünyası raporlama
* model sonuçlarını Excel’e aktarma

---

## 2) Bilimsel Hesaplama ve İstatistik Kütüphaneleri

### SciPy

Bilimsel hesaplama için geniş kapsamlı kütüphanedir.

**Ne için kullanılır?**

* optimizasyon
* istatistik
* sinyal işleme
* lineer cebir
* sayısal integrasyon

**Neden önemli?**
ML’nin matematik motorlarından biridir.

---

### Statsmodels

İstatistiksel modelleme ve ekonometrik analiz için kullanılır.

**Ne için kullanılır?**

* regresyon analizleri
* istatistiksel testler
* zaman serisi
* p-value, confidence interval gibi klasik istatistik çıktıları

**Neden önemli?**
Scikit-learn tahmin odaklıdır; Statsmodels daha çok açıklama ve istatistik odaklıdır.

**Tipik kullanım:**

* OLS regression
* ARIMA
* hypothesis testing

---

### SymPy

Sembolik matematik kütüphanesidir.

**Ne için kullanılır?**

* cebirsel ifade çözümü
* türev/integral
* sembolik denklem işleme

**AI/ML’de nerede işe yarar?**

* eğitim amaçlı anlatım
* matematiksel prototipleme

---

## 3) Görselleştirme Kütüphaneleri

### Matplotlib

Python’un temel grafik çizim kütüphanesidir.

**Ne için kullanılır?**

* çizgi grafik
* histogram
* scatter plot
* bar chart
* eğitim/raporlama grafikleri

**Neden önemli?**
Birçok görselleştirme kütüphanesinin temelinde bu vardır.

---

### Seaborn

Matplotlib üzerine kurulmuş daha estetik ve istatistiksel görselleştirme kütüphanesidir.

**Ne için kullanılır?**

* korelasyon heatmap
* boxplot
* violin plot
* pairplot
* class distribution analizi

**Neden önemli?**
EDA yani keşifsel veri analizi için çok pratiktir.

---

### Plotly

İnteraktif grafikler üretmek için kullanılır.

**Ne için kullanılır?**

* dashboard
* zoom yapılabilen grafikler
* web tabanlı veri görselleştirme

**Tipik kullanım:**

* model performans panelleri
* iş zekâsı sunumları

---

### Bokeh

Tarayıcı üzerinde çalışan interaktif görselleştirme kütüphanesidir.

**Ne için kullanılır?**

* interaktif veri uygulamaları
* analitik dashboardlar

---

### Altair

Deklaratif, temiz sözdizimine sahip görselleştirme kütüphanesidir.

**Ne için kullanılır?**

* veri analizi
* hızlı prototipleme
* sade ve okunabilir grafik tanımları

---

## 4) Klasik Makine Öğrenmesi Kütüphaneleri

### Scikit-learn

Klasik makine öğrenmesinin en popüler Python kütüphanesidir.

**Ne için kullanılır?**

* classification
* regression
* clustering
* preprocessing
* feature selection
* model evaluation
* pipeline

**Desteklediği modeller:**

* logistic regression
* decision tree
* random forest
* SVM
* KNN
* naive bayes
* PCA
* k-means

**Neden önemli?**
Klasik ML öğrenmek isteyen herkesin ana aracıdır.

**Tipik kullanım:**

* train/test split
* scaler
* model fit/predict
* cross validation

---

### XGBoost

Gradient boosting tabanlı çok güçlü bir ML kütüphanesidir.

**Ne için kullanılır?**

* tablo verilerinde yüksek performanslı classification/regression
* Kaggle yarışmaları
* kredi skorlama
* churn tahmini
* fraud detection

**Neden önemli?**
Tablo verilerinde çoğu zaman çok güçlü sonuç verir.

---

### LightGBM

Microsoft tarafından geliştirilen, hızlı gradient boosting kütüphanesidir.

**Ne için kullanılır?**

* büyük veri setleri
* yüksek hızlı eğitim
* classification/regression/ranking

**Neden önemli?**
Özellikle büyük ölçekli tablo verilerinde verimli çalışır.

---

### CatBoost

Özellikle kategorik verilerde güçlü çalışan boosting kütüphanesidir.

**Ne için kullanılır?**

* kategorik feature’ların yoğun olduğu veri setleri
* sınıflandırma ve regresyon

**Neden önemli?**
Kategorik verileri daha az manuel encoding ile iyi işleyebilir.

---

### Imbalanced-learn

Dengesiz veri setleri için yardımcı araçlar sağlar.

**Ne için kullanılır?**

* SMOTE
* undersampling
* oversampling
* class imbalance problemleri

**Neden önemli?**
Gerçek hayatta veri çoğu zaman dengeli değildir. Spam, fraud, hastalık verileri buna klasik örnektir.

---

### Yellowbrick

Scikit-learn modellerini görselleştirmek için kullanılır.

**Ne için kullanılır?**

* confusion matrix görselleştirme
* ROC curve
* feature importance
* elbow plot

**Neden önemli?**
Model yorumlamayı kolaylaştırır.

---

## 5) Deep Learning Kütüphaneleri

### TensorFlow

Google destekli derin öğrenme framework’üdür.

**Ne için kullanılır?**

* neural network
* CNN
* RNN
* transformer
* production-grade DL sistemleri

**Neden önemli?**
Uzun yıllardır endüstride yaygın kullanılan büyük ekosistemdir.

---

### Keras

TensorFlow üzerinde çalışan, daha kullanıcı dostu yüksek seviye deep learning API’sidir.

**Ne için kullanılır?**

* hızlı model geliştirme
* eğitim amaçlı derin öğrenme
* prototipleme

**Neden önemli?**
Derin öğrenmeye giriş için çok kullanışlıdır.

---

### PyTorch

Meta tarafından geliştirilen popüler deep learning framework’üdür.

**Ne için kullanılır?**

* araştırma
* üretim
* NLP
* computer vision
* generative AI
* LLM eğitimi/inference

**Neden önemli?**
Bugün araştırma dünyasında ve modern AI ekosisteminde aşırı yaygındır.

**Güçlü tarafı:**

* esnek yapı
* pythonic yaklaşım
* dinamik computation graph

---

### PyTorch Lightning

PyTorch kodunu daha düzenli ve modüler hale getiren üst seviye yapıdır.

**Ne için kullanılır?**

* eğitim döngülerini sadeleştirme
* deney yönetimi
* daha temiz proje yapısı

---

### JAX

Yüksek performanslı sayısal hesaplama ve otomatik türev için kullanılan modern kütüphanedir.

**Ne için kullanılır?**

* araştırma
* hız odaklı modelleme
* TPU/GPU hızlandırmalı matematik

**Neden önemli?**
Özellikle ileri seviye araştırma ve optimizasyon işlerinde parlıyor.

---

### Flax

JAX tabanlı neural network kütüphanesidir.

**Ne için kullanılır?**

* modern araştırma projeleri
* JAX ekosisteminde model geliştirme

---

## 6) NLP (Doğal Dil İşleme) Kütüphaneleri

### NLTK

Doğal dil işleme eğitimi ve temel metin işleme için klasik kütüphanedir.

**Ne için kullanılır?**

* tokenization
* stopword temizleme
* stemming
* lemmatization
* temel corpus işlemleri

**Neden önemli?**
NLP öğrenmeye başlamak için klasik araçtır.

---

### spaCy

Endüstri odaklı, hızlı ve güçlü NLP kütüphanesidir.

**Ne için kullanılır?**

* named entity recognition
* part-of-speech tagging
* dependency parsing
* metin işleme pipeline’ları

**Neden önemli?**
Gerçek uygulamalarda NLTK’den daha pratik ve hızlıdır.

---

### Gensim

Topic modeling ve word embedding için kullanılır.

**Ne için kullanılır?**

* Word2Vec
* Doc2Vec
* LDA topic modeling

---

### Transformers

Hugging Face tarafından sunulan, transformer tabanlı modeller için ana kütüphanedir.

**Ne için kullanılır?**

* BERT
* GPT benzeri modeller
* text classification
* summarization
* translation
* question answering
* text generation

**Neden önemli?**
Modern NLP’nin ana damarlarından biridir.

---

### Tokenizers

Hızlı tokenizer işlemleri için kullanılır.

**Ne için kullanılır?**

* BPE
* WordPiece
* modern alt-kelime tokenization süreçleri

---

### Sentence Transformers

Cümle embedding üretmek için çok kullanılan kütüphanedir.

**Ne için kullanılır?**

* semantic search
* benzerlik analizi
* RAG sistemleri
* embedding tabanlı eşleştirme

---

## 7) Computer Vision Kütüphaneleri

### OpenCV

Görüntü işleme ve computer vision için en yaygın kütüphanelerden biridir.

**Ne için kullanılır?**

* görüntü okuma/yazma
* filtreleme
* kenar bulma
* yüz tespiti
* video işleme
* kamera işlemleri

**Neden önemli?**
CV dünyasının tornavidası, çekici, pense seti gibi bir şeydir.

---

### Pillow (PIL)

Temel görüntü işleme kütüphanesidir.

**Ne için kullanılır?**

* resize
* crop
* format dönüştürme
* basit image manipulation

---

### torchvision

PyTorch ekosisteminde vision veri setleri, modeller ve dönüşümler sunar.

**Ne için kullanılır?**

* pretrained CNN modelleri
* image transforms
* dataset loaders

---

### Albumentations

Görüntü veri artırma için çok güçlü kütüphanedir.

**Ne için kullanılır?**

* rotate
* flip
* crop
* blur
* noise
* augmentation pipeline

**Neden önemli?**
Computer vision projelerinde veri artırma için çok sevilir.

---

### Ultralytics

YOLO tabanlı object detection modelleri için popüler ekosistemdir.

**Ne için kullanılır?**

* object detection
* segmentation
* tracking

---

## 8) Generative AI / LLM Kütüphaneleri

### Hugging Face Hub

Hazır model ve dataset paylaşımı için kullanılan merkezdir.

**Ne için kullanılır?**

* model indirme
* fine-tuned model paylaşımı
* dataset erişimi

---

### Datasets

Hugging Face’in dataset yönetim kütüphanesidir.

**Ne için kullanılır?**

* NLP / CV veri setlerini kolay yükleme
* split yönetimi
* preprocessing

---

### PEFT

Parameter-Efficient Fine-Tuning için kullanılır.

**Ne için kullanılır?**

* LoRA
* adapter tabanlı fine-tuning
* daha düşük maliyetli model uyarlama

---

### Accelerate

Büyük modellerin çoklu cihazlarda çalıştırılması ve eğitimini kolaylaştırır.

**Ne için kullanılır?**

* distributed training
* mixed precision
* GPU yönetimi

---

### Diffusers

Diffusion tabanlı generative modeller için kullanılır.

**Ne için kullanılır?**

* image generation
* text-to-image
* stable diffusion tabanlı işler

---

### LangChain

LLM tabanlı uygulamalar kurmak için kullanılan framework’tür.

**Ne için kullanılır?**

* RAG
* agent sistemleri
* tool calling
* prompt workflow

**Neden önemli?**
LLM uygulama katmanında çok görülür, ama her derde deva değildir. Bazen fazla şatafatlı olabilir.

---

### LlamaIndex

Özellikle veri kaynaklarını LLM ile bağlamak için kullanılan framework’tür.

**Ne için kullanılır?**

* doküman indeksleme
* retrieval
* RAG uygulamaları

---

### vLLM

Büyük dil modelleri için yüksek performanslı inference altyapısı sağlar.

**Ne için kullanılır?**

* hızlı text generation
* ölçekli LLM serving

---

### Ollama

Yerelde LLM çalıştırmayı kolaylaştıran araçtır.

**Ne için kullanılır?**

* local model serving
* küçük/orta ölçekli LLM denemeleri

---

## 9) Model Açıklanabilirliği ve Yorumlama Kütüphaneleri

### SHAP

Modelin tahminlerini açıklamak için kullanılan çok güçlü kütüphanedir.

**Ne için kullanılır?**

* feature importance
* bireysel tahmin açıklama
* global/local interpretability

**Neden önemli?**
Finans, sağlık, kurumsal karar sistemlerinde çok değerlidir.

---

### LIME

Yerel tahmin açıklaması için kullanılır.

**Ne için kullanılır?**

* bir örnek bazında model neden böyle karar verdi sorusuna yanıt üretmek

---

### ELI5

Model açıklamaları ve feature ağırlıkları için kullanılan yardımcı kütüphanedir.

---

## 10) MLOps, Tracking ve Deployment Kütüphaneleri

### MLflow

ML deney takibi, model kayıt ve yaşam döngüsü yönetimi için kullanılır.

**Ne için kullanılır?**

* experiment tracking
* parameter logging
* metric logging
* model registry

**Neden önemli?**
“Bu modeli nasıl eğitmiştik?” sorusunun panik butonudur.

---

### Weights & Biases (wandb)

Deney takibi ve görsel training dashboard için kullanılır.

**Ne için kullanılır?**

* metric izleme
* hyperparameter takibi
* model karşılaştırma

---

### DVC

Data Version Control anlamına gelir.

**Ne için kullanılır?**

* veri versiyonlama
* model artifact yönetimi
* pipeline takibi

---

### BentoML

ML modellerini servis haline getirmek için kullanılır.

**Ne için kullanılır?**

* model API deployment
* production serving

---

### FastAPI

Doğrudan ML kütüphanesi değildir ama ML deployment’ta çok kullanılır.

**Ne için kullanılır?**

* model inference API
* REST servisleri
* prediction endpoint’leri

---

### Uvicorn

FastAPI gibi ASGI uygulamalarını çalıştırmak için sunucudur.

---

### Gradio

ML model demo arayüzleri yapmak için kullanılır.

**Ne için kullanılır?**

* hızlı prototip UI
* model demosu
* kullanıcı testleri

---

### Streamlit

Veri bilimi ve ML uygulamaları için hızlı web arayüzü geliştirir.

**Ne için kullanılır?**

* dashboard
* model demo
* analitik uygulama

---

## 11) Zaman Serisi Kütüphaneleri

### Prophet

Zaman serisi tahmini için kullanılır.

**Ne için kullanılır?**

* satış tahmini
* trend/sezonsallık analizi
* iş metrikleri forecast

---

### pmdarima

ARIMA benzeri klasik zaman serisi modelleri için kullanılır.

---

### Darts

Modern zaman serisi kütüphanesidir.

**Ne için kullanılır?**

* çoklu forecast modelleri
* deep learning + classical forecasting

---

### sktime

Scikit-learn benzeri yapı ile zaman serisi modelleme sunar.

---

## 12) Büyük Veri ve Dağıtık İşleme Kütüphaneleri

### PySpark

Apache Spark’ın Python arayüzüdür.

**Ne için kullanılır?**

* büyük veri işleme
* dağıtık ETL
* büyük ölçekli ML

---

### Dask

Pandas / NumPy benzeri yapıları dağıtık şekilde çalıştırır.

**Ne için kullanılır?**

* büyük veri paralel işleme
* memory sınırını aşan veri setleri

---

### Ray

Dağıtık hesaplama ve ölçekli AI iş akışları için kullanılır.

**Ne için kullanılır?**

* paralel eğitim
* hyperparameter tuning
* distributed inference

---

## 13) Hyperparameter Tuning Kütüphaneleri

### Optuna

Hyperparameter optimizasyonu için modern ve güçlü kütüphanedir.

**Ne için kullanılır?**

* learning rate
* max depth
* batch size
* model tuning

**Neden önemli?**
Grid search’in öküz gibi brute force yaptığı işleri daha akıllıca yapabilir.

---

### Hyperopt

Bayesian optimization tabanlı tuning kütüphanesidir.

---

### Ray Tune

Dağıtık hyperparameter tuning için kullanılır.

---

## 14) Yardımcı ve Altyapı Kütüphaneleri

### Joblib

Model veya büyük Python objelerini serileştirmek için kullanılır.

**Ne için kullanılır?**

* model kaydetme
* pipeline saklama

---

### Pickle

Python objelerini dosyaya yazmak için kullanılan yerleşik modüldür.

**Dikkat:**
Güvenlik açısından bilinmeyen pickle dosyaları risklidir.

---

### tqdm

Uzun işlemlerde ilerleme çubuğu gösterir.

**Ne için kullanılır?**

* veri işleme pipeline’ları
* eğitim sırasında progress göstermek

---

### Loguru

Loglama işlemlerini kolaylaştırır.

---

### Rich

Terminal çıktısını daha okunabilir hale getirir.

---

### PyYAML

YAML konfigürasyon dosyaları için kullanılır.

**Ne için kullanılır?**

* model config
* experiment config
* deployment ayarları

---

## 15) Hangi kütüphane hangi iş için?

### Klasik tablo verisi ML projesi

En tipik set:

* NumPy
* Pandas
* Matplotlib / Seaborn
* Scikit-learn
* XGBoost / LightGBM / CatBoost
* SHAP
* MLflow

---

### Deep Learning projesi

En tipik set:

* NumPy
* Pandas
* PyTorch veya TensorFlow
* Matplotlib
* torchvision / albumentations
* wandb veya MLflow

---

### NLP projesi

En tipik set:

* Pandas
* spaCy / NLTK
* Transformers
* Sentence Transformers
* Datasets
* PEFT

---

### Computer Vision projesi

En tipik set:

* OpenCV
* Pillow
* PyTorch
* torchvision
* albumentations
* ultralytics

---

### LLM / RAG projesi

En tipik set:

* Transformers
* Sentence Transformers
* LangChain veya LlamaIndex
* FAISS benzeri vektör altyapıları
* FastAPI
* Gradio / Streamlit
* vLLM / Ollama

---

## 16) En kritik gerçek

Her projede 40 kütüphane kullanman gerekmez.
Çoğu iş için çekirdek set şudur:

* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* PyTorch veya TensorFlow
* Transformers
* FastAPI
* MLflow

Geri kalanı proje tipine göre gelir.

---

## 17) Başlangıç için öğrenme sırası

Mantıklı sıra şudur:

1. NumPy
2. Pandas
3. Matplotlib / Seaborn
4. Scikit-learn
5. XGBoost / LightGBM
6. PyTorch
7. Transformers
8. FastAPI
9. MLflow

Bu sıra gayet ayıklanmış, gereksiz şişkinlikten uzak bir rotadır.

---
------------------------------------------------
------------------------------------------------

SORU-2 Problem tipleri: sınıflandırma / regresyon / kümeleme
Önce ne yapacağımı söyleyeyim:
Makine öğrenmesindeki **problem tiplerini (classification, regression, clustering)** temelden başlayarak anlatacağım. Her birinin mantığını, matematiksel düşüncesini, hangi algoritmaların kullanıldığını, gerçek hayat senaryolarını, veri tiplerini, avantaj–dezavantajlarını ve yanlış kullanım durumları:

---

# Makine Öğrenmesinde Problem Tipleri

Makine öğrenmesi dünyasında çoğu problem aslında üç ana kategoriye düşer:

1️⃣ **Classification (Sınıflandırma)**
2️⃣ **Regression (Regresyon)**
3️⃣ **Clustering (Kümeleme)**

Bu üçü öğrenme paradigmasının temelini oluşturur.

Daha üst seviyede düşünürsek:

| Problem tipi   | Öğrenme türü          |
| -------------- | --------------------- |
| Classification | Supervised Learning   |
| Regression     | Supervised Learning   |
| Clustering     | Unsupervised Learning |

Yani:

* **Classification ve Regression → etiketli veri**
* **Clustering → etiketsiz veri**

---

# 1) Classification (Sınıflandırma)

## Tanım

Sınıflandırma, bir veriyi **önceden tanımlanmış kategorilerden birine atama problemidir.**

Başka bir ifadeyle:

Modelin çıktısı **sınıf etiketi** olur.

Örnek çıktı:

* spam / değil
* hasta / sağlıklı
* sahtekarlık / normal
* kabul / reddedildi
* kedi / köpek / kuş

Yani çıktı **kesikli (discrete)** değerlerdir.

---

## Matematiksel bakış

Model şu fonksiyonu öğrenir:

[
f(x) \rightarrow y
]

Burada

x → giriş özellikleri
y → sınıf etiketi

Örnek:

```
x = [yaş, gelir, kredi geçmişi]

y = kredi_onayı
```

---

## Basit örnek

Bir email sistemi düşün.

Girdi:

* mesaj uzunluğu
* link sayısı
* büyük harf oranı
* anahtar kelimeler

Model öğrenir ve karar verir:

```
Spam mı?
Spam değil mi?
```

---

## Classification türleri

### Binary Classification

İki sınıf vardır.

Örnek:

* hastalık var / yok
* spam / normal
* kredi riskli / risksiz

Algoritmalar:

* Logistic Regression
* SVM
* Decision Tree
* Random Forest
* Naive Bayes
* XGBoost

---

### Multi-class Classification

İkiden fazla sınıf vardır.

Örnek:

* kedi
* köpek
* kuş

veya

* ürün kategorisi
* haber kategorisi

Algoritmalar:

* Softmax Regression
* Decision Tree
* Random Forest
* Neural Network

---

### Multi-label Classification

Bir veri birden fazla etikete sahip olabilir.

Örnek:

Bir film:

* aksiyon
* bilim kurgu
* dram

---

## Gerçek hayat senaryoları

### Finans

* kredi onayı
* dolandırıcılık tespiti
* risk kategorisi

### Sağlık

* hastalık teşhisi
* kanser sınıflandırması

### E-ticaret

* müşteri churn tahmini
* ürün kategori tahmini

### NLP

* spam tespiti
* duygu analizi
* metin sınıflandırma

---

## Classification değerlendirme metrikleri

Model başarısı şu metriklerle ölçülür:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

Özellikle dengesiz veri setlerinde accuracy tek başına yeterli değildir.

---

## Avantajlar

* yorumlanabilir
* birçok algoritma var
* geniş kullanım alanı

## Dezavantajlar

* dengesiz veri problemi
* yanlış etiket problemi
* sınıf sayısı arttıkça zorluk

---

# 2) Regression (Regresyon)

## Tanım

Regresyon, **sürekli (continuous) bir sayıyı tahmin etme problemidir.**

Yani model bir kategori değil **sayısal değer** üretir.

---

## Örnek

Bir ev fiyat tahmini modeli.

Girdi:

* metrekare
* oda sayısı
* bina yaşı
* lokasyon

Çıktı:

```
Ev fiyatı = 2.750.000 TL
```

---

## Matematiksel düşünce

Regresyon modeli bir fonksiyon öğrenir:

[
y = f(x) + \epsilon
]

Burada:

x → özellikler
y → hedef değişken
ε → hata

---

## Regression türleri

### Linear Regression

En basit modeldir.

[
y = ax + b
]

veya çok değişkenli:

[
y = w_1x_1 + w_2x_2 + ... + b
]

---

### Polynomial Regression

Doğrusal olmayan ilişkiler için kullanılır.

[
y = ax^2 + bx + c
]

---

### Regularized Regression

Aşırı öğrenmeyi azaltmak için kullanılır.

* Ridge
* Lasso
* ElasticNet

---

### Tree-based Regression

Daha güçlü modeller:

* Random Forest Regression
* Gradient Boosting
* XGBoost
* LightGBM

---

## Gerçek hayat senaryoları

### Ekonomi

* enflasyon tahmini
* döviz tahmini
* satış tahmini

### E-ticaret

* talep tahmini
* stok tahmini

### Sağlık

* hasta kalış süresi
* ilaç doz tahmini

### Enerji

* elektrik tüketimi tahmini
* enerji üretimi tahmini

---

## Regression metrikleri

Başarı ölçümü:

* MAE (Mean Absolute Error)
* MSE (Mean Squared Error)
* RMSE
* R² Score

---

## Avantajlar

* sayısal tahmin problemleri için ideal
* ekonometrik uygulamalar için güçlü

## Dezavantajlar

* outlier problemi
* doğrusal varsayım hataları

---

# 3) Clustering (Kümeleme)

Şimdi iş biraz dedektiflik moduna geçiyor.

Çünkü burada **etiket yok.**

Model verideki **doğal grupları keşfetmeye çalışır.**

---

## Tanım

Clustering, benzer verileri **aynı grupta toplama problemidir.**

Model:

“Bu veriler birbirine benziyor” diyerek kümeler oluşturur.

---

## Basit örnek

Bir e-ticaret şirketi müşterileri segmentlere ayırmak istiyor.

Veriler:

* yaş
* gelir
* harcama miktarı

Model şunu bulur:

```
Küme 1 → genç düşük gelir
Küme 2 → orta yaş yüksek harcama
Küme 3 → sadık müşteriler
```

---

## Clustering algoritmaları

### K-Means

En popüler yöntem.

Mantık:

* K adet merkez seçilir
* noktalar en yakın merkeze atanır
* merkezler güncellenir

---

### Hierarchical Clustering

Ağaç yapısı oluşturur.

Küçük kümeler birleşerek büyür.

---

### DBSCAN

Yoğunluk tabanlı algoritma.

Avantaj:

* outlier tespiti
* düzensiz kümeler

---

### Gaussian Mixture Models

Olasılıksal kümeleme yöntemidir.

---

## Gerçek kullanım senaryoları

### Pazarlama

* müşteri segmentasyonu
* kampanya hedefleme

### Biyoloji

* gen kümeleri

### Sosyal medya

* kullanıcı davranış analizi

### Anomali tespiti

* olağandışı veri noktaları

---

## Clustering değerlendirme metrikleri

Çünkü doğru etiket yok.

Bu yüzden farklı metrikler kullanılır:

* Silhouette score
* Davies–Bouldin index
* Calinski–Harabasz

---

# Üç problem tipinin karşılaştırması

| Özellik      | Classification   | Regression    | Clustering            |
| ------------ | ---------------- | ------------- | --------------------- |
| Öğrenme türü | Supervised       | Supervised    | Unsupervised          |
| Çıktı        | sınıf etiketi    | sayısal değer | grup etiketi          |
| Etiket       | var              | var           | yok                   |
| Amaç         | kategorize etmek | değer tahmini | benzer gruplar bulmak |
| Örnek        | spam tespiti     | fiyat tahmini | müşteri segmentasyonu |

---

# Çok kritik kavram farkı

Şuna dikkat etmek gerekir.

### Classification

Çıktı:

```
0
1
2
```

ama bu sayılar **kategori** anlamındadır.

---

### Regression

Çıktı:

```
3.54
21.88
108.1
```

gerçek **sürekli sayıdır.**

---

### Clustering

Çıktı:

```
Cluster 1
Cluster 2
Cluster 3
```

ama bu kümeler **önceden bilinmez.**

---

# Gerçek projede nasıl kullanılır?

Örnek: bir e-ticaret platformu.

### Clustering

Müşterileri segmente ayır.

---

### Classification

Hangi müşteri ürünü satın alır?

---

### Regression

Müşteri ne kadar harcar?

---

Yani bu üç problem tipi genelde **birlikte kullanılır.**

---

# En yaygın hata

Yeni başlayanlar genelde şu hatayı yapar:

Her problemi classification sanırlar.

Oysa önce şu soruyu sormak gerekir:

**Çıktım kategori mi, sayı mı, yoksa etiket yok mu?**

Buna göre problem tipi seçilir.

---

# Kısa akıl kuralı

Çıktı türüne bak:

```
kategori → classification

sayı → regression

etiket yok → clustering
```

---


--------------------------------------------------------------
--------------------------------------------------------------

SORU-3 Veri sızıntısı (data leakage) nedir, neden yakar?
Önce ne yapacağımı söyleyeyim:
**Data leakage (veri sızıntısı)** kavramını temelden açıklayacağım; neden tehlikeli olduğunu, makine öğrenmesi projelerinde nasıl ortaya çıktığını, gerçek hayatta nasıl modeli “yanlış başarıya” götürdüğünü ve nasıl önlenmesi gerektiğini detaylı şekilde anlatacağım.

---

# Veri Sızıntısı (Data Leakage) Nedir?

Makine öğrenmesinde **data leakage**, modelin eğitim sırasında **gerçek hayatta erişememesi gereken bilgileri kullanarak öğrenmesi** durumudur.

Başka bir ifadeyle:

Model, tahmin yaparken **gelecekten veya hedef değişkenden bilgi sızması** sayesinde “hileli şekilde” yüksek doğruluk elde eder.

Bu durum şu anlama gelir:

Model testte çok iyi görünür ama **gerçek dünyada çöker.**

---

# Basit bir örnekle düşün

Bir model yapıyorsun:

Amaç:

```
Bir müşterinin krediyi ödeyip ödemeyeceğini tahmin etmek
```

Veriler:

* yaş
* gelir
* kredi geçmişi
* borç miktarı
* kredi sonucu

Ama veri setinde şu sütun da var:

```
“borç kapatıldı mı”
```

Bu bilgi aslında **gelecek bilgisi**.

Model bunu kullanırsa:

Modelin doğruluğu %99 olur.

Ama gerçek dünyada:

Bu bilgi **tahmin anında yoktur.**

Dolayısıyla model aslında **hile yapmıştır.**

İşte bu **data leakage**.

---

# Veri sızıntısı neden yakar?

Bilimde bazen şeytan küçük ayrıntılarda gizlidir.
Veri sızıntısı da tam olarak böyle bir tuzaktır.

Bir modelin performansı şu şekilde görünür:

```
Accuracy = %98
```

Ama gerçek hayatta:

```
Accuracy = %55
```

Sebep?

Model eğitim sırasında **geleceği görmüştür.**

---

# Data leakage neden çok tehlikeli?

Çünkü şu 3 şeyi bozar:

### 1️⃣ Model değerlendirmesi

Model test verisini bilmeden tahmin yapmalı.

Ama leakage varsa model:

```
test verisini dolaylı şekilde öğrenmiş olur
```

Bu da performansı **sahte şekilde yükseltir.**

---

### 2️⃣ Gerçek dünya performansı

Gerçek sistemde o bilgi yoktur.

Model:

```
train → süper
test → süper
production → kötü
```

olur.

---

### 3️⃣ Yanlış kararlar

Özellikle şu sektörlerde çok risklidir:

* finans
* sağlık
* güvenlik
* kredi sistemi

Yanlış model:

* kredi hataları
* yanlış teşhis
* fraud kaçırma
* müşteri kaybı

yaratabilir.

---

# Data Leakage türleri

Genelde iki ana tür vardır.

---

# 1️⃣ Target Leakage

Model, **hedef değişkenden türeyen bilgiyi kullanır.**

Örnek:

Bir model:

```
hasta 30 gün içinde ölecek mi?
```

veriler:

* yaş
* hastalık
* kan değerleri

ama veri setinde şu sütun var:

```
ölüm tarihi
```

Model bunu kullanırsa:

Tahmin yapmaz.
Sadece cevabı okur.

Bu tam anlamıyla **geleceğin sızmasıdır.**

---

# 2️⃣ Train-Test Leakage

Modelin eğitim sürecinde **test verisine ait bilgi kullanılmasıdır.**

Bu genelde veri ön işleme aşamasında olur.

Örnek:

Veri normalize edilir.

Ama yanlış yapılır:

```
Scaler.fit(all_data)
```

Yani:

```
train + test birlikte öğrenilir
```

Doğru yöntem:

```
scaler.fit(train)
scaler.transform(test)
```

Bu küçük hata bile leakage yaratır.

---

# Çok yaygın leakage örnekleri

Makine öğrenmesi projelerinde en sık görülen hatalar şunlardır.

---

## 1️⃣ Feature engineering hataları

Örnek:

Bir churn modeli.

Ama veri setinde şu feature var:

```
abonelik iptal tarihi
```

Model bunu kullanırsa:

churn tahmini yapmaz
cevabı görür.

---

## 2️⃣ Zaman sızıntısı (temporal leakage)

Zaman serilerinde çok görülür.

Örnek:

Amaç:

```
yarın satış tahmini
```

Ama veri setinde:

```
haftalık toplam satış
```

ve bu veri **geleceği içerir.**

---

## 3️⃣ Veri ön işleme hataları

Yanlış pipeline:

```
StandardScaler
PCA
Feature Selection
```

bütün veri üzerinde uygulanır.

Sonra train/test ayrılır.

Bu yanlış.

Çünkü:

Test verisinin bilgisi train'e sızmıştır.

---

## 4️⃣ Duplicate veri

Eğer veri setinde aynı kayıtlar varsa:

```
train set
test set
```

aynı veriyi içerir.

Model:

```
test verisini ezberlemiş olur
```

---

## 5️⃣ Cross validation hataları

Özellikle zaman serilerinde:

Normal K-fold kullanmak leakage yaratabilir.

Çünkü:

gelecek veri geçmişe karışır.

---

# Gerçek dünya örneği

Bir banka fraud modeli geliştiriyor.

Ama veri setinde şu sütun var:

```
fraud_investigation_result
```

Bu sütun aslında **insan incelemesi sonrası oluşuyor.**

Ama model bunu kullanıyor.

Sonuç:

```
Model accuracy = %99
```

Gerçek dünyada:

```
%60
```

Çünkü üretim ortamında bu sütun yok.

---

# Data leakage nasıl tespit edilir?

Şüpheli belirtiler vardır.

### 1️⃣ Çok yüksek doğruluk

```
Accuracy = %99
```

ama problem zor.

Şüphelen.

---

### 2️⃣ Model production'da çöküyor

Test çok iyi ama gerçek sistem kötü.

---

### 3️⃣ Feature importance garip

Model bazı sütunlara aşırı bağımlı olabilir.

---

### 4️⃣ Gelecek bilgisi içeren feature

Örnek:

* işlem sonucu
* iptal tarihi
* ödeme tamamlandı

---

# Data leakage nasıl önlenir?

Şimdi kritik kısmı.

---

## 1️⃣ Train-Test split önce yapılmalı

Yanlış:

```
veri temizleme
feature engineering
split
```

Doğru:

```
split
veri işleme
model
```

---

## 2️⃣ Pipeline kullan

Özellikle:

```
scikit-learn Pipeline
```

Bu sayede:

```
fit(train)
transform(test)
```

mantığı korunur.

---

## 3️⃣ Gelecek bilgisi kullanma

Feature üretirken şu soruyu sor:

```
Bu bilgi tahmin anında var mı?
```

Yoksa → leakage.

---

## 4️⃣ Zaman serilerinde dikkat

Zaman sırasını bozma.

Doğru yöntem:

```
past → train
future → test
```

---

## 5️⃣ Domain bilgisi kullan

Veri bilimciler bazen domain'i bilmez.

Ama bir finans uzmanı hemen fark eder:

```
bu feature geleceği gösteriyor
```

---

# Çok kritik bir ML kuralı

Her feature için şu soru sorulmalı:

```
Bu bilgi tahmin yapılacağı anda mevcut mu?
```

Cevap **hayır** ise:

```
data leakage vardır
```

---

# Data leakage neden ML projelerinin en büyük tuzaklarından biridir?

Çünkü model geliştirme süreci şöyle işler:

```
veri → model → evaluation → deploy
```

Ama leakage varsa:

evaluation tamamen sahte olur.

Bu yüzden veri bilimciler arasında şu söz vardır:

> En tehlikeli hata kötü model değil, **sahte iyi modeldir.**

---

# Kısa özet

Data leakage:

Modelin **gerçek hayatta erişemeyeceği bilgiyi kullanarak öğrenmesidir.**

Sonuçları:

* sahte yüksek doğruluk
* yanlış model seçimi
* production başarısızlığı

En yaygın sebepler:

* hedef değişken sızıntısı
* train-test karışması
* yanlış preprocessing
* zaman verisi hataları
* duplicate veri

---

---------------------------------------------------------------------------------
---------------------------------------------------------------------------------

SORU-4  •     Train/valid/test mantığı (kısa ama net)
Önce ne yapacağımı söyleyeyim:
**Train / Validation / Test veri setlerinin mantığını**, neden üçe bölündüğünü, her birinin görevini ve gerçek bir ML geliştirme sürecinde nasıl kullanıldığını kısa ama net şekilde açıklayacağım.

---

# Train / Validation / Test Mantığı

Makine öğrenmesinde veri genellikle **3 parçaya ayrılır**:

* **Train set**
* **Validation set**
* **Test set**

Amaç şudur:
Modelin **öğrenmesi**, **ayarlanması** ve **gerçek performansının ölçülmesi** birbirinden ayrılmalıdır.

---

# 1️⃣ Train Set (Eğitim Verisi)

Modelin **öğrendiği veri** budur.

Model bu veri üzerinden:

* parametrelerini öğrenir
* ağırlıkları günceller
* örüntüleri keşfeder

Örnek:

```text
Model = train_data üzerinde öğrenir
```

Bu aşamada model:

* hata hesaplar
* parametreleri optimize eder
* gradient descent gibi algoritmalar kullanır

Tipik oran:

```text
Verinin %60–80’i
```

---

# 2️⃣ Validation Set (Doğrulama Verisi)

Validation set modelin **ayar yapmak için kullandığı veri**dir.

Ama model bu veriden **öğrenmez**.

Amaç:

* hyperparameter tuning
* model seçimi
* overfitting kontrolü

Örnek:

* learning rate seçimi
* ağaç derinliği
* regularization parametresi
* neuron sayısı

Model geliştirme sürecinde sürekli şu yapılır:

```text
train → validation performansına bak
```

Tipik oran:

```text
Verinin %10–20’si
```

---

# 3️⃣ Test Set (Gerçek Performans)

Test set **en kritik veri**dir.

Bu veri:

* model eğitimi için kullanılmaz
* model tuning için kullanılmaz

Sadece şu soru için kullanılır:

```text
Bu model gerçek dünyada ne kadar iyi çalışacak?
```

Test set **en sona saklanır.**

Tipik oran:

```text
Verinin %10–20’si
```

---

# Neden üç ayrı veri gerekir?

Çünkü tek veri kullanırsan model şu hataya düşer:

**overfitting**

Yani model:

```text
train verisini ezberler
```

Ama yeni veride başarısız olur.

Validation ve test verisi bu yüzden gerekir.

---

# Basit bir örnek

1000 veri olduğunu düşün.

Veri bölünür:

```text
Train      → 700
Validation → 150
Test       → 150
```

Akış şu olur:

1️⃣ Model train verisi ile öğrenir
2️⃣ Validation ile ayarlar yapılır
3️⃣ En sonunda test ile gerçek performans ölçülür

---

# Çok kritik bir kural

Test verisine **erken bakılmaz.**

Eğer model geliştirme sırasında test verisine bakarsan:

```text
data leakage oluşur
```

ve test artık güvenilir olmaz.

---

# Sürecin görsel mantığı

```text
Veri
 │
 ├── Train → Model öğrenir
 │
 ├── Validation → Model ayarlanır
 │
 └── Test → Final performans ölçülür
```

---

# Kısa özet

| Veri Seti  | Amaç                      |
| ---------- | ------------------------- |
| Train      | Model öğrenir             |
| Validation | Model ayarlanır           |
| Test       | Gerçek performans ölçülür |

---

# Tek cümlelik akıl kuralı

```text
Train → öğren
Validation → ayarla
Test → ölç
```

---


---------------------------------------------------------------------------
---------------------------------------------------------------------------

SORU-5  •     Lab: python küçük bir veri setinde hedef/özellik ayrımı + hızlı keşif
Önce ne yapacağımı söyleyeyim:
Küçük bir veri seti üzerinde **Python ile hedef (target) ve özellik (feature) ayrımı**, ardından **hızlı veri keşfi (quick EDA)** yapacağımız küçük bir laboratuvar hazırlayacağım. Kod tek parça olacak ve direkt çalıştırılabilir olacak.

Bu lab, ML projelerinin **ilk 10 dakikasında yapılan standart keşif adımlarını** gösterir.

---

# Lab: Python ile Feature / Target Ayrımı + Hızlı Veri Keşfi

Bu örnekte klasik bir veri seti kullanacağız:

**Titanic dataset**

Amaç:

```text
Bir yolcunun hayatta kalıp kalmayacağını tahmin etmek
```

Target:

```text
Survived
```

Features:

```text
Age
Fare
Sex
Pclass
SibSp
Parch
```

---

# Python Lab Kodu (tek parça)

```python
# ================================
# ML LAB
# Feature / Target Ayrımı
# Quick Exploratory Data Analysis
# ================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------
# 1) Veri setini yükleme
# -----------------------------
df = sns.load_dataset("titanic")

print("Veri Seti Boyutu:")
print(df.shape)

print("\nİlk 5 Satır:")
print(df.head())


# -----------------------------
# 2) Target ve Feature ayrımı
# -----------------------------

target = "survived"

features = [
    "pclass",
    "sex",
    "age",
    "sibsp",
    "parch",
    "fare"
]

X = df[features]
y = df[target]

print("\nFeature matrisi boyutu:", X.shape)
print("Target boyutu:", y.shape)

print("\nTarget dağılımı:")
print(y.value_counts())


# -----------------------------
# 3) Eksik veri kontrolü
# -----------------------------
print("\nEksik veri analizi:")
print(df[features].isnull().sum())


# -----------------------------
# 4) Temel istatistikler
# -----------------------------
print("\nTemel istatistikler:")
print(df[features].describe())


# -----------------------------
# 5) Hızlı veri görselleştirme
# -----------------------------

# Target dağılımı
plt.figure(figsize=(5,4))
sns.countplot(x="survived", data=df)
plt.title("Target Dağılımı")
plt.show()


# Yaş dağılımı
plt.figure(figsize=(6,4))
sns.histplot(df["age"], kde=True)
plt.title("Yaş Dağılımı")
plt.show()


# Ücret dağılımı
plt.figure(figsize=(6,4))
sns.histplot(df["fare"], kde=True)
plt.title("Bilet Ücreti Dağılımı")
plt.show()


# -----------------------------
# 6) Korelasyon analizi
# -----------------------------
plt.figure(figsize=(8,6))
sns.heatmap(df[features + [target]].corr(), annot=True, cmap="coolwarm")
plt.title("Korelasyon Matrisi")
plt.show()


# -----------------------------
# 7) Feature vs Target ilişkisi
# -----------------------------

# Yaş vs Hayatta Kalma
plt.figure(figsize=(6,4))
sns.boxplot(x="survived", y="age", data=df)
plt.title("Yaş vs Hayatta Kalma")
plt.show()

# Ücret vs Hayatta Kalma
plt.figure(figsize=(6,4))
sns.boxplot(x="survived", y="fare", data=df)
plt.title("Bilet Ücreti vs Hayatta Kalma")
plt.show()


# -----------------------------
# 8) Kategorik feature analizi
# -----------------------------
plt.figure(figsize=(6,4))
sns.countplot(x="sex", hue="survived", data=df)
plt.title("Cinsiyet vs Hayatta Kalma")
plt.show()


# -----------------------------
# 9) Sonuç
# -----------------------------
print("\nLab tamamlandı.")
print("Feature matrisi: X")
print("Target değişkeni: y")
```

---

# Bu Lab’da Öğrenilenler

Bu küçük lab aslında ML pipeline'ın ilk aşamasını öğretir.

### 1️⃣ Hedef değişkeni belirleme

```python
target = "survived"
```

---

### 2️⃣ Feature seçimi

```python
features = [...]
```

---

### 3️⃣ Feature matrisi oluşturma

```python
X = df[features]
```

---

### 4️⃣ Target oluşturma

```python
y = df[target]
```

---

### 5️⃣ Veri keşfi (EDA)

Yapılanlar:

* veri boyutu
* eksik veri
* temel istatistikler
* dağılım grafikleri
* korelasyon
* feature-target ilişkisi

---

# Bu Lab neden önemli?

Gerçek veri bilimi projelerinde zamanın büyük kısmı şurada geçer:

```text
%70 veri analizi
%20 model
%10 tuning
```

Modelden önce veri anlaşılmalıdır.

---

# Hızlı veri keşfi checklist

Bir veri seti geldiğinde ilk bakılanlar:

```
df.head()
df.shape
df.info()
df.describe()
missing values
target distribution
feature distributions
correlation
feature vs target
```

---

# Küçük ama kritik bir ML kuralı

Model kurmadan önce şu sorular sorulmalı:

```
target dengeli mi?
feature dağılımları normal mi?
outlier var mı?
missing data var mı?
feature-target ilişkisi var mı?
```

Bunlar yapılmadan model kurmak çoğu zaman **çöp model** üretir.

---

# Sana ayrıca şu labları da hazırlayabilirim

İstersen sana şunları da hazırlayabilirim:

### 1️⃣ Lab 2

**Scikit-learn ile ilk classification modeli**

* train/test split
* logistic regression
* accuracy

---

### 2️⃣ Lab 3

**Overfitting demonstrasyonu**

---

### 3️⃣ Lab 4

**Feature engineering**

---

### 4️⃣ Lab 5

**Model pipeline (production mantığı)**

---

----------------------------------------------------------------
----------------------------------------------------------------

SORU-XX Hazırla yapay zekâ mühendislerinin en çok kullandığı 100 algoritma

Önce ne yapacağımı söyleyeyim:
Yapay zekâ mühendislerinin en çok kullandığı **100 algoritmayı**, ezbere isim listesi gibi değil; **kategori kategori**, **ne işe yarar**, **hangi problemde kullanılır**, **temel mantığı nedir** şeklinde düzenleyeceğim.
Düzeni şu olacak:

* Klasik ML algoritmaları
* Ensemble yöntemler
* Boyut indirgeme ve özellik seçimi
* Kümeleme ve anomali tespiti
* Olasılıksal modeller
* Zaman serisi
* Reinforcement Learning
* Deep Learning mimarileri ve eğitim algoritmaları
* NLP / CV / Generative AI tarafında sık kullanılan algoritmik yaklaşımlar

Aşağıdaki liste “teorik olarak var olan her şey” değil; **pratikte en çok karşılaşılan ve bilinmesi gereken 100 algoritmalık çekirdek sözlük** gibidir.

---

# Yapay Zekâ Mühendislerinin En Çok Kullandığı 100 Algoritma

---

# 1) Klasik Denetimli Öğrenme Algoritmaları

## 1. Linear Regression

Sürekli sayısal değer tahmini için kullanılır.
Örnek:

* ev fiyatı
* satış tahmini
* maliyet tahmini

Temel mantık:
Girdi değişkenleri ile hedef değişken arasında doğrusal ilişki kurar.

---

## 2. Multiple Linear Regression

Birden fazla bağımsız değişkenle çalışan linear regression türüdür.
Örnek:

* metrekare + oda sayısı + konum → ev fiyatı

---

## 3. Polynomial Regression

Doğrusal olmayan ilişkiyi polinom terimleri ekleyerek modelleyen regresyon yöntemidir.
Düz çizgi yetmezse eğri çizer.

---

## 4. Ridge Regression

L2 regularization kullanan regresyon yöntemidir.
Amaç:

* aşırı öğrenmeyi azaltmak
* katsayıları kontrol altında tutmak

---

## 5. Lasso Regression

L1 regularization kullanır.
Önemli farkı:

* bazı katsayıları sıfıra çekebilir
* feature selection etkisi oluşturur

---

## 6. Elastic Net

L1 + L2 regularization birleşimidir.
Özellikle çok sayıda feature olduğunda kullanışlıdır.

---

## 7. Logistic Regression

Sınıflandırma probleminde kullanılır.
Adı regression ama işi çoğu zaman classification’dır.
Örnek:

* spam / değil
* hasta / değil

---

## 8. Softmax Regression

Çok sınıflı sınıflandırma için logistic regression’ın genişletilmiş halidir.

---

## 9. Perceptron

En temel lineer sınıflandırıcılardan biridir.
Yapay sinir ağlarının tarihsel dedesidir.

---

## 10. Support Vector Machine (SVM)

Sınıfları en iyi ayıran sınırı bulmaya çalışır.
Özellikle orta ölçekli veri setlerinde güçlüdür.

---

## 11. Support Vector Regression (SVR)

SVM’in regresyon versiyonudur.

---

## 12. Kernel SVM

Veri doğrusal ayrılmıyorsa kernel trick kullanarak daha yüksek boyutta ayırmaya çalışır.

---

## 13. k-Nearest Neighbors (KNN)

Yeni veriyi en yakın k komşuya bakarak sınıflandırır veya tahmin eder.
Basit ama bazı veri setlerinde etkili.

---

## 14. Weighted KNN

Komşuların etkisini uzaklığa göre ağırlıklandıran KNN türüdür.

---

## 15. Naive Bayes

Bayes teoremine dayanır, feature’ların bağımsız olduğunu varsayar.
Metin sınıflandırmada klasik silahtır.

---

## 16. Gaussian Naive Bayes

Sürekli verilerde Gaussian dağılım varsayımı yapar.

---

## 17. Multinomial Naive Bayes

Kelime sayımı gibi frekans tabanlı metin verilerinde kullanılır.

---

## 18. Bernoulli Naive Bayes

0/1 tarzı binary feature’lar için uygundur.

---

## 19. Decision Tree

Veriyi kurallarla bölerek karar ağacı oluşturur.
Açıklanabilirliği yüksektir.

---

## 20. CART

Classification and Regression Trees yaklaşımıdır.
Hem sınıflandırma hem regresyon ağacı oluşturabilir.

---

# 2) Ensemble ve Boosting Algoritmaları

## 21. Random Forest

Birden fazla decision tree’nin birleşimidir.
Tek ağaçtan daha kararlı sonuç verir.

---

## 22. Extra Trees (Extremely Randomized Trees)

Random forest’e benzer ama bölmeleri daha rastgele seçer.

---

## 23. Bagging

Birden fazla modeli farklı örneklerle eğitip sonuçlarını birleştiren yöntemdir.

---

## 24. AdaBoost

Zayıf öğrenicileri ardışık şekilde eğiterek hatalı örneklere daha çok odaklanır.

---

## 25. Gradient Boosting

Her yeni model, önceki modelin hatasını azaltmaya çalışır.

---

## 26. XGBoost

Gradient boosting’in çok güçlü ve optimize edilmiş versiyonudur.
Tablo verisinin kralı diye anılır, boşuna değil.

---

## 27. LightGBM

Hızlı ve bellek verimli boosting algoritmasıdır.
Büyük veri setlerinde çok kullanılır.

---

## 28. CatBoost

Kategorik verilerde güçlü performans gösteren boosting algoritmasıdır.

---

## 29. Histogram-Based Gradient Boosting

Histogram mantığıyla daha hızlı gradient boosting eğitimi sağlar.

---

## 30. Stacking

Birden fazla modelin çıktısını üst bir modelde birleştirir.

---

## 31. Blending

Stacking’e benzeyen daha basit ensemble yaklaşımıdır.

---

## 32. Voting Classifier

Birden fazla sınıflandırıcının oylarıyla final karar verir.

---

## 33. Voting Regressor

Birden fazla regresyon modelinin tahminlerini birleştirir.

---

## 34. Bootstrap Aggregation

Bagging’in temel örnekleme mantığıdır.
Yerine koyarak örnekleme ile modeller eğitilir.

---

## 35. Gradient Boosted Decision Trees

Boosting + decision tree birleşimidir. XGBoost ve LightGBM bunun aile fertleridir.

---

# 3) Kümeleme Algoritmaları

## 36. K-Means

Veriyi K adet kümeye ayırır.
Müşteri segmentasyonu için klasik yöntemdir.

---

## 37. K-Medoids

K-means’e benzer ama merkez olarak gerçek veri noktalarını kullanır.

---

## 38. Mini-Batch K-Means

Büyük veri setlerinde daha hızlı çalışan K-means versiyonudur.

---

## 39. Hierarchical Clustering

Veri kümelerini ağaç yapısı şeklinde oluşturur.

---

## 40. Agglomerative Clustering

En küçük kümelerden başlayıp birleştirerek ilerler.

---

## 41. Divisive Clustering

Tek büyük kümeden başlayıp ayırarak ilerler.

---

## 42. DBSCAN

Yoğunluk tabanlı kümeleme algoritmasıdır.
Outlier tespitinde de işe yarar.

---

## 43. HDBSCAN

DBSCAN’in daha gelişmiş ve esnek versiyonudur.

---

## 44. Mean Shift

Yoğunluk tepe noktalarını arayarak kümeleri bulur.

---

## 45. Gaussian Mixture Model (GMM)

Verinin farklı Gaussian dağılımlardan geldiğini varsayar.

---

## 46. Spectral Clustering

Graf tabanlı benzerlik matrisi üzerinden kümeleme yapar.

---

## 47. BIRCH

Büyük veri için hiyerarşik kümeleme yaklaşımıdır.

---

## 48. Affinity Propagation

Küme merkezlerini veriden seçer; K değerini baştan vermek gerekmez.

---

## 49. Fuzzy C-Means

Bir veri noktası birden fazla kümeye belli oranlarda ait olabilir.

---

## 50. OPTICS

DBSCAN benzeri yoğunluk tabanlı kümeleme algoritmasıdır.

---

# 4) Boyut İndirgeme ve Özellik Çıkarma Algoritmaları

## 51. Principal Component Analysis (PCA)

Boyut indirgeme için en klasik yöntemdir.
Varyansı en iyi açıklayan yönleri bulur.

---

## 52. Kernel PCA

Doğrusal olmayan ilişkiler için kernel tabanlı PCA’dır.

---

## 53. Incremental PCA

Büyük veri üzerinde parça parça PCA yapmaya uygundur.

---

## 54. Linear Discriminant Analysis (LDA)

Hem sınıflandırma hem boyut indirgeme için kullanılabilir.
Sınıfları iyi ayıran eksenler bulur.

---

## 55. t-SNE

Yüksek boyutlu veriyi 2D/3D görselleştirmek için çok kullanılır.

---

## 56. UMAP

t-SNE’ye alternatif, hızlı ve yapısal bilgiyi daha iyi koruyabilen yöntemdir.

---

## 57. Independent Component Analysis (ICA)

Sinyalleri bağımsız bileşenlerine ayırır.

---

## 58. Non-Negative Matrix Factorization (NMF)

Negatif olmayan matrisleri bileşenlerine ayırır.
Topic modeling’de de kullanılır.

---

## 59. Truncated SVD

Büyük seyrek matrisler için boyut indirgeme sağlar.

---

## 60. Autoencoder

Sinir ağı tabanlı boyut indirgeme ve temsil öğrenme yöntemidir.

---

# 5) Özellik Seçimi ve Düzenlileştirme Algoritmaları

## 61. Recursive Feature Elimination (RFE)

Feature’ları iteratif olarak eleyerek en iyi alt kümeyi bulur.

---

## 62. SelectKBest

İstatistiksel skorlara göre en iyi K feature’ı seçer.

---

## 63. Chi-Square Feature Selection

Kategorik / sınıflandırma problemlerinde feature önemini ölçmek için kullanılır.

---

## 64. Mutual Information

Feature ile target arasındaki bilgi miktarını ölçer.

---

## 65. Variance Threshold

Varyansı düşük, yani bilgi taşımayan feature’ları eler.

---

## 66. L1 Regularization

Bazı katsayıları sıfıra çekerek özellik seçimi etkisi yapar.

---

## 67. L2 Regularization

Aşırı büyük katsayıları cezalandırır.

---

## 68. Elastic Net Regularization

L1 + L2 birleşimidir.

---

## 69. Embedded Feature Selection

Modelin eğitimi sırasında feature seçimi yapan yöntemlerdir.
Örnek: Lasso, tree-based importance.

---

## 70. Boruta

Random forest tabanlı güçlü feature selection algoritmasıdır.

---

# 6) Anomali Tespiti Algoritmaları

## 71. Isolation Forest

Anormal verileri daha az bölmeyle izole ederek bulur.
Anomaly detection için çok popülerdir.

---

## 72. One-Class SVM

Normal veriyi öğrenir, aykırı veriyi dışarıda bırakır.

---

## 73. Local Outlier Factor (LOF)

Bir noktanın komşularına göre ne kadar aykırı olduğunu ölçer.

---

## 74. Elliptic Envelope

Gaussian varsayımıyla anomali tespiti yapar.

---

## 75. Robust Covariance

Aykırı değerlere dayanıklı kovaryans tabanlı yaklaşım sunar.

---

## 76. Autoencoder-based Anomaly Detection

Normal veriyi iyi yeniden üretir, anormali kötü üretir; rekonstrüksiyon hatasıyla anomaly tespit edilir.

---

## 77. DBSCAN for Outlier Detection

Kümeye girmeyen noktalar anomali olarak düşünülebilir.

---

## 78. Z-Score Method

İstatistiksel olarak aşırı uç değer tespit eder.

---

## 79. IQR Method

Çeyrekler arası aralık ile aykırı değer tespit eder.

---

## 80. Gaussian Density Estimation

Düşük olasılıklı noktaları anomali kabul eder.

---

# 7) Olasılıksal ve Grafiksel Modeller

## 81. Bayesian Network

Değişkenler arası olasılıksal ilişkileri yönlü grafik ile modeller.

---

## 82. Hidden Markov Model (HMM)

Gizli durumları olan zaman bağımlı süreçleri modellemek için kullanılır.

---

## 83. Markov Chain

Bir sonraki durumun yalnızca mevcut duruma bağlı olduğu süreç modelidir.

---

## 84. Conditional Random Fields (CRF)

Özellikle sıralı etiketleme problemlerinde kullanılır.
NLP’de klasik oyunculardandır.

---

## 85. Latent Dirichlet Allocation (LDA Topic Model)

Metinlerde konu modelleme için kullanılır.

---

## 86. Probabilistic PCA

PCA’nın olasılıksal versiyonudur.

---

## 87. Expectation-Maximization (EM)

Gizli değişkenli modellerde parametre tahmini için kullanılan genel algoritmadır.

---

## 88. Maximum Likelihood Estimation (MLE)

Parametreleri en olası hale getirecek şekilde tahmin eder.

---

## 89. Maximum A Posteriori (MAP)

Ön bilgi + veri kullanarak parametre tahmini yapar.

---

## 90. Kalman Filter

Zaman içinde gürültülü ölçümlerden durum tahmini yapar.

---

# 8) Zaman Serisi Algoritmaları

## 91. AR (AutoRegressive)

Geçmiş değerlere bakarak geleceği tahmin eder.

---

## 92. MA (Moving Average)

Geçmiş hata terimlerine bakarak tahmin yapar.

---

## 93. ARMA

AR + MA birleşimidir.

---

## 94. ARIMA

Durağanlaştırma eklenmiş ARMA modelidir.
Zaman serisinin klasik iş atıdır.

---

## 95. SARIMA

Mevsimsellik içeren ARIMA modelidir.

---

## 96. Exponential Smoothing

Zamana göre ağırlıklandırılmış tahmin yaklaşımıdır.

---

## 97. Holt-Winters

Trend ve mevsimselliği birlikte modelleyen klasik yöntemdir.

---

## 98. Prophet

Trend + sezonluk + tatil etkilerini modelleyen pratik zaman serisi algoritmasıdır.

---

## 99. VAR (Vector AutoRegression)

Birden fazla zaman serisinin birbirini etkilediği durumlarda kullanılır.

---

## 100. LSTM for Time Series

Zaman serileri için kullanılan derin öğrenme tabanlı sıralı modeldir.

---

# 9) Reinforcement Learning Algoritmaları

Bonus bölüm veriyorum; 100 doldu ama eksik bırakmak saçma olur.

## 101. Q-Learning

Değer tabanlı reinforcement learning algoritmasıdır.

---

## 102. SARSA

Q-learning’e benzer ama izlenen politika üzerinden öğrenir.

---

## 103. Deep Q Network (DQN)

Q-learning + neural network birleşimidir.

---

## 104. Policy Gradient

Politikayı doğrudan optimize eder.

---

## 105. Actor-Critic

Politika ve değer tahminini birlikte kullanır.

---

## 106. PPO (Proximal Policy Optimization)

Modern RL’de çok sık kullanılan kararlı algoritmalardan biridir.

---

## 107. A3C

Asenkron actor-critic yaklaşımıdır.

---

## 108. TD Learning

Temporal difference ile öğrenme yapar.

---

## 109. Monte Carlo RL

Bölüm sonunda toplam ödülden öğrenir.

---

## 110. Multi-Armed Bandit

Keşif-sömürü dengesini kurmak için kullanılan temel karar modeli.

---

# 10) Derin Öğrenme Eğitim ve Mimari Algoritmaları

## 111. Backpropagation

Sinir ağında hatayı geriye doğru yayarak ağırlıkları günceller.

---

## 112. Gradient Descent

Kayıp fonksiyonunu minimize etmek için kullanılan temel optimizasyon yöntemidir.

---

## 113. Stochastic Gradient Descent (SGD)

Her adımda tek örnek veya küçük parça ile güncelleme yapar.

---

## 114. Mini-Batch Gradient Descent

Pratikte en çok kullanılan gradient descent şeklidir.

---

## 115. Momentum

Optimizasyonda yön bilgisini taşıyarak daha hızlı yakınsama sağlar.

---

## 116. Nesterov Accelerated Gradient

Momentum’un daha öngörülü versiyonudur.

---

## 117. AdaGrad

Her parametre için farklı öğrenme oranı ayarlar.

---

## 118. RMSProp

AdaGrad’in öğrenme oranı sorunlarını iyileştirir.

---

## 119. Adam

Momentum + RMSProp birleşimidir.
Derin öğrenmede en yaygın optimizer’lardandır.

---

## 120. AdamW

Weight decay’i daha doğru yöneten Adam türevidir.

---

## 121. Adadelta

Uyarlanabilir öğrenme oranı kullanan optimizasyon algoritmasıdır.

---

## 122. Nadam

Adam + Nesterov birleşimidir.

---

## 123. MLP (Multi-Layer Perceptron)

Tam bağlı yapay sinir ağıdır.

---

## 124. CNN (Convolutional Neural Network)

Görüntü işleme için temel derin öğrenme mimarisidir.

---

## 125. RNN (Recurrent Neural Network)

Sıralı veriler için tasarlanmış tekrarlayan sinir ağıdır.

---

## 126. LSTM

Uzun bağımlılıkları öğrenebilen RNN türevidir.

---

## 127. GRU

LSTM’den daha sade ve hızlı bir sıralı modeldir.

---

## 128. Seq2Seq

Bir diziyi başka bir diziye dönüştüren mimaridir.
Çeviri gibi işlerde kullanılmıştır.

---

## 129. Attention Mechanism

Modelin girdinin önemli kısımlarına odaklanmasını sağlar.

---

## 130. Transformer

Modern NLP’nin ana mimarisidir.
Şu anki devasa dil modellerinin kalbi budur.

---

# 11) Computer Vision ve NLP’de Çok Kullanılan Mimari Aileler

## 131. ResNet

Residual connection kullanan CNN mimarisidir.

---

## 132. DenseNet

Katmanları yoğun bağlantılarla bağlayan mimaridir.

---

## 133. VGG

Basit ama tarihsel öneme sahip CNN mimarisidir.

---

## 134. Inception

Farklı boyutta filtreleri aynı anda kullanan mimaridir.

---

## 135. U-Net

Segmentation işlerinde çok kullanılır.

---

## 136. YOLO

Gerçek zamanlı object detection ailesidir.

---

## 137. Faster R-CNN

Yüksek doğruluklu nesne tespit mimarisidir.

---

## 138. Mask R-CNN

Object detection + instance segmentation yapar.

---

## 139. BERT

Bidirectional transformer tabanlı dil modeli.

---

## 140. GPT-style Decoder Model

Metin üretimi için decoder-only transformer yaklaşımıdır.

---

# 12) Generative AI Algoritmaları

## 141. Autoencoder

Veriyi sıkıştırıp yeniden üretir.

---

## 142. Variational Autoencoder (VAE)

Olasılıksal latent uzay kullanarak veri üretir.

---

## 143. GAN

Generator ve discriminator’ı karşı karşıya getirerek veri üretir.

---

## 144. DCGAN

CNN tabanlı GAN versiyonudur.

---

## 145. WGAN

GAN eğitimini daha kararlı hale getirmeyi amaçlar.

---

## 146. Conditional GAN

Belirli koşullara göre veri üretebilir.

---

## 147. Diffusion Model

Gürültü ekleyip sonra geri temizleyerek veri üretir.
Görüntü üretiminde son yılların yıldızı.

---

## 148. DDPM

Denoising diffusion probabilistic model yaklaşımıdır.

---

## 149. Stable Diffusion-style Latent Diffusion

Latent uzayda çalışan diffusion yaklaşımıdır.

---

## 150. Beam Search

Özellikle sequence generation’da en olası çıktı dizilerini arar.

---

# Kısa Özet: En kritik 20 algoritma hangileri?

Pratikte en sık karşılaşacağın çekirdek 20’yi ayrıca ayırayım:

* Linear Regression
* Logistic Regression
* Decision Tree
* Random Forest
* XGBoost
* LightGBM
* CatBoost
* SVM
* KNN
* Naive Bayes
* K-Means
* DBSCAN
* PCA
* Isolation Forest
* ARIMA
* Prophet
* CNN
* LSTM
* Transformer
* Adam

Bunları sağlam biliyorsan, zeminin güçlü olur. Geri kalanlar bunların çevresinde büyür.

# Hangi alanda hangi algoritmalar öne çıkar?

## Tablo verisi

* Logistic Regression
* Random Forest
* XGBoost
* LightGBM
* CatBoost

## Görüntü işleme

* CNN
* ResNet
* U-Net
* YOLO
* Mask R-CNN

## NLP

* Naive Bayes
* CRF
* LSTM
* Transformer
* BERT / GPT tarzı modeller

## Zaman serisi

* ARIMA
* SARIMA
* Prophet
* LSTM
* VAR

## Anomali tespiti

* Isolation Forest
* One-Class SVM
* LOF
* Autoencoder

## RL

* Q-Learning
* DQN
* PPO
* Actor-Critic

---

# Çok kritik gerçek

Her algoritmayı her probleme sürmek doğru değildir.
Mühendislikte doğru soru şudur:

**Problem tipi ne? Veri tipi ne? Açıklanabilirlik gerekiyor mu? Veri boyutu ne? Eğitim maliyeti ne?**

Yoksa elinde çekiç var diye her şeyi çivi sanırsın. AI dünyasında bu hatayı yapan çok, maalesef bayağı çok.

---


----------------------------------------------------------------
----------------------------------------------------------------
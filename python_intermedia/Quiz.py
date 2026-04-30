"""
Bu dosya, terminal üzerinden çalışan gelişmiş bir Quiz / Test uygulamasıdır.

Amaç:
- Soruları CSV dosyasından okumak
- Kullanıcıya soruları sırayla sormak
- Cevapları kontrol etmek
- Sonuçları TXT, CSV ve HTML formatında raporlamak
- Soruları rastgele karıştırarak daha dinamik bir deneyim sunmak

Not:
Bu sürümde mevcut çalışan yapı korunmuştur.
Sadece kodun anlaşılmasını kolaylaştırmak için komutların ve blokların üstüne
çok detaylı açıklamalar eklenmiştir.
"""

# csv modülü:
# CSV (Comma Separated Values) dosyalarını okumak ve yazmak için kullanılır.
# Bu projede soru havuzunu 'questions.csv' dosyasından okumak ve
# quiz sonuçlarını '.csv' formatında dışarı aktarmak için kullanılmaktadır.
import csv

# html modülü:
# Kullanıcıya gösterilecek metinlerde yer alan özel karakterlerin
# HTML içinde güvenli biçimde gösterilmesini sağlar.
# Örneğin '<', '>', '&' gibi karakterler HTML yapısını bozmasın diye escape edilir.
# Bu sayede HTML raporunda soru ve şık metinleri güvenli şekilde gösterilir.
import html

# random modülü:
# Rastgelelik gerektiren işlemlerde kullanılır.
# Bu projede soru listesini her quiz başlangıcında karıştırmak için kullanılır.
# Böylece her çalıştırmada sorular farklı sırada gelebilir.
import random

# datetime sınıfı:
# Tarih ve saat bilgisini almak için kullanılır.
# Burada sonuç dosyalarının isimlerini zaman damgası ile üretmek,
# ayrıca raporlara quizin hangi tarihte oluşturulduğunu yazmak için kullanılır.
from datetime import datetime

# Path sınıfı:
# Dosya ve klasör yollarını platformdan bağımsız, güvenli ve okunaklı şekilde
# yönetmek için kullanılır.
# Windows, Linux, macOS gibi sistemlerde dosya yollarını elle birleştirmek yerine
# nesne tabanlı güvenli yaklaşım sağlar.
from pathlib import Path

# BASE_DIR:
# Bu Python dosyasının bulunduğu klasörü temsil eder.
# __file__ -> o anda çalışan dosyanın yolunu verir.
# resolve() -> tam/gerçek yolu çözer.
# parent -> dosyanın bulunduğu klasörü alır.
# Amaç: CSV ve sonuç klasörlerini bu dosyanın bulunduğu dizine göre oluşturmak.
BASE_DIR = Path(__file__).resolve().parent

# CSV_FILE:
# Soruların okunacağı questions.csv dosyasının yolunu temsil eder.
# BASE_DIR / "questions.csv" ifadesi, işletim sistemine uygun biçimde
# dosya yolunu birleştirir.
CSV_FILE = BASE_DIR / "questions.csv"

# RESULTS_DIR:
# Quiz sonuçlarının kaydedileceği klasörü temsil eder.
# TXT, CSV ve HTML raporları bu klasör altına yazılacaktır.
RESULTS_DIR = BASE_DIR / "results"


# ensure_results_dir fonksiyonu:
# Sonuçların yazılacağı klasörün var olup olmadığını kontrol eder.
# Eğer klasör yoksa otomatik olarak oluşturur.
# parents=True  -> gerekirse üst klasörleri de oluşturur.
# exist_ok=True -> klasör zaten varsa hata vermez.
def ensure_results_dir():
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)


# load_questions fonksiyonu:
# Verilen CSV dosyasını okuyarak quiz sorularını belleğe yükler.
# Geriye liste döner.
#
# Beklenen kolonlar:
# - question
# - option_a
# - option_b
# - option_c
# - option_d
# - answer
#
# Bu fonksiyon ayrıca veri doğrulama da yapar:
# - Dosya var mı?
# - Başlıklar okunabiliyor mu?
# - Zorunlu kolonlar eksik mi?
# - Cevap A/B/C/D dışında mı?
# - Soru metni boş mu?
def load_questions(csv_file):
    # questions listesi, geçerli bulunan tüm soruları tutar.
    questions = []

    # Eğer CSV dosyası yoksa kullanıcıya hata gösterilir ve boş liste döndürülür.
    if not csv_file.exists():
        print(f"Hata: CSV dosyası bulunamadı -> {csv_file}")
        return questions

    # CSV dosyasını UTF-8-SIG ile açıyoruz.
    # utf-8-sig seçiminin nedeni:
    # Bazı CSV dosyaları başında BOM karakteri içerir.
    # Bu encoding, başlıkların bozulmadan okunmasına yardımcı olur.
    # newline="" parametresi, CSV okuma/yazma sırasında satır sonu sorunlarını azaltır.
    with open(csv_file, "r", encoding="utf-8-sig", newline="") as file:
        # DictReader, her satırı sözlük (dict) olarak okur.
        # Böylece sütunlara index ile değil isimleriyle erişebiliriz.
        reader = csv.DictReader(file)

        # required_columns kümesi:
        # CSV içinde mutlaka bulunması gereken başlıklar burada tanımlanır.
        required_columns = {
            "question",
            "option_a",
            "option_b",
            "option_c",
            "option_d",
            "answer",
        }

        # fieldnames boşsa başlıklar okunamamış demektir.
        if not reader.fieldnames:
            print("Hata: CSV başlıkları okunamadı.")
            return questions

        # missing hesabı:
        # Beklenen kolonlar ile gerçek kolonları karşılaştırır.
        # CSV'de eksik olan kolonları bulur.
        missing = required_columns - set(reader.fieldnames)
        if missing:
            print("Hata: CSV içinde eksik kolonlar var:", ", ".join(sorted(missing)))
            return questions

        # enumerate(reader, start=2):
        # CSV'de veri satırlarını gezer.
        # start=2 kullanılmasının nedeni:
        # 1. satır başlık satırıdır; gerçek veri satırları 2. satırdan başlar.
        for row_number, row in enumerate(reader, start=2):
            # answer alanı metne çevrilir, boşlukları temizlenir ve büyük harfe dönüştürülür.
            # Amaç: kullanıcı veri girişindeki küçük/büyük harf farklarını normalize etmek.
            answer = str(row["answer"]).strip().upper()

            # Eğer cevap yalnızca A/B/C/D dışında ise satır geçersiz sayılır.
            if answer not in {"A", "B", "C", "D"}:
                print(f"Uyarı: {row_number}. satırdaki cevap geçersiz olduğu için soru atlandı.")
                continue

            # Soru metni boşluklardan temizlenir.
            question_text = str(row["question"]).strip()

            # Şıklar sözlük halinde tutulur.
            # Böylece hem ekrana yazdırmak hem de sonradan karşılaştırmak kolaylaşır.
            options = {
                "A": str(row["option_a"]).strip(),
                "B": str(row["option_b"]).strip(),
                "C": str(row["option_c"]).strip(),
                "D": str(row["option_d"]).strip(),
            }

            # Soru metni boşsa kullanıcıya uyarı verilir ve bu satır alınmaz.
            if not question_text:
                print(f"Uyarı: {row_number}. satırdaki soru boş olduğu için atlandı.")
                continue

            # Geçerli bulunan soru, standart bir veri yapısı ile listeye eklenir.
            questions.append(
                {
                    "question": question_text,
                    "options": options,
                    "answer": answer,
                }
            )

    # Tüm geçerli sorular yüklendikten sonra geri döndürülür.
    return questions


# save_results_html fonksiyonu:
# Sonuçları görsel açıdan daha zengin bir HTML raporu olarak kaydeder.
# Kullanıcı hangi şıkkı işaretledi, doğru cevap neydi, hangi soru doğru/yanlıştı
# gibi bilgiler renkli kutular ve rozetlerle gösterilir.
def save_results_html(base_name, score, total, percent, user_results):
    html_path = base_name.with_suffix(".html")

    # Her soru kartını HTML içinde bir bölüm olarak biriktireceğiz.
    sections = []

    # Tüm kullanıcı sonuçlarını geziyoruz.
    for index, item in enumerate(user_results, start=1):
        options_html = []

        # Her şık için ayrı HTML satırı üretilir.
        for key, value in item["options"].items():
            # Şıkkın hangi görsel sınıfa sahip olacağı hesaplanır.
            css_class = get_option_css_class(key, item["user_answer"], item["correct_answer"])

            # html.escape ile içerik güvenli hale getirilir.
            label_parts = [f"<strong>{key})</strong> {html.escape(value)}"]

            # Kullanıcının seçtiği şık ise rozet eklenir.
            if key == item["user_answer"]:
                label_parts.append('<span class="badge badge-user">İşaretlediğin</span>')

            # Doğru cevap olan şık ise rozet eklenir.
            if key == item["correct_answer"]:
                label_parts.append('<span class="badge badge-correct">Doğru Cevap</span>')

            # Tek bir şık satırı HTML listesi elemanı olarak oluşturulur.
            option_line = f'<li class="{css_class}">{" ".join(label_parts)}</li>'
            options_html.append(option_line)

        # Soru doğru mu yanlış mı bilgisi hem metin hem CSS sınıfı olarak hazırlanır.
        question_status = "Doğru" if item["is_correct"] else "Yanlış"
        question_status_class = "status-correct" if item["is_correct"] else "status-wrong"

        # Tek bir soru kartının HTML içeriği hazırlanır.
        section = f"""
        <div class="question-card">
            <div class="question-header">
                <h2>Soru {index}</h2>
                <span class="status {question_status_class}">{question_status}</span>
            </div>
            <p class="question-text">{html.escape(item["question"])}</p>
            <ul class="options">
                {''.join(options_html)}
            </ul>
            <div class="answer-summary">
                <p><strong>İşaretlediğin:</strong> {item["user_answer"]}) {html.escape(item["options"][item["user_answer"]])}</p>
                <p><strong>Doğru cevap:</strong> {item["correct_answer"]}) {html.escape(item["options"][item["correct_answer"]])}</p>
            </div>
        </div>
        """
        sections.append(section)

    # Tüm raporun ana HTML iskeleti hazırlanır.
    # İçinde CSS stilleri de gömülü olduğu için tek dosya halinde açılabilir.
    html_content = f"""<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Quiz Sonuç Raporu</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background: #f4f6f8;
            color: #1f2937;
            margin: 0;
            padding: 24px;
        }}
        .container {{
            max-width: 1000px;
            margin: 0 auto;
        }}
        .summary {{
            background: #ffffff;
            border-radius: 14px;
            padding: 20px;
            margin-bottom: 24px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        }}
        .summary h1 {{
            margin-top: 0;
        }}
        .summary-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 12px;
            margin-top: 16px;
        }}
        .summary-box {{
            background: #f9fafb;
            border: 1px solid #e5e7eb;
            border-radius: 10px;
            padding: 14px;
        }}
        .question-card {{
            background: #ffffff;
            border-radius: 14px;
            padding: 20px;
            margin-bottom: 18px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        }}
        .question-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
        }}
        .question-text {{
            font-size: 18px;
            font-weight: bold;
        }}
        .status {{
            padding: 8px 12px;
            border-radius: 999px;
            font-weight: bold;
            font-size: 14px;
        }}
        .status-correct {{
            background: #dcfce7;
            color: #166534;
        }}
        .status-wrong {{
            background: #fee2e2;
            color: #991b1b;
        }}
        .options {{
            list-style: none;
            padding: 0;
            margin: 16px 0;
        }}
        .option {{
            background: #f9fafb;
            border: 1px solid #d1d5db;
            border-radius: 10px;
            padding: 12px;
            margin-bottom: 10px;
        }}
        .option-correct {{
            background: #dcfce7;
            border-color: #22c55e;
        }}
        .option-correct-selected {{
            background: #bbf7d0;
            border: 2px solid #15803d;
        }}
        .option-wrong-selected {{
            background: #fee2e2;
            border-color: #ef4444;
        }}
        .badge {{
            display: inline-block;
            margin-left: 8px;
            padding: 4px 8px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: bold;
        }}
        .badge-user {{
            background: #dbeafe;
            color: #1d4ed8;
        }}
        .badge-correct {{
            background: #dcfce7;
            color: #166534;
        }}
        .answer-summary {{
            background: #f9fafb;
            border-radius: 10px;
            padding: 12px;
            border: 1px solid #e5e7eb;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="summary">
            <h1>Quiz Sonuç Raporu</h1>
            <p><strong>Tarih:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
            <div class="summary-grid">
                <div class="summary-box"><strong>Doğru Sayısı</strong><br>{score}</div>
                <div class="summary-box"><strong>Yanlış Sayısı</strong><br>{total - score}</div>
                <div class="summary-box"><strong>Toplam Soru</strong><br>{total}</div>
                <div class="summary-box"><strong>Başarı Oranı</strong><br>%{percent:.2f}</div>
            </div>
        </div>

        {''.join(sections)}
    </div>
</body>
</html>
"""

    # Hazırlanan HTML metni dosyaya UTF-8 ile yazılır.
    html_path.write_text(html_content, encoding="utf-8")
    return html_path


# prompt_menu fonksiyonu:
# Kullanıcıya ana menüyü gösterir ve seçim alır.
# Geçersiz giriş yapılırsa kullanıcıyı yeniden yönlendirir.
# Sadece 1, 2 veya 3 kabul edilir.
def prompt_menu():
    print("\n" + "=" * 70)
    print("Python Quiz / Test Uygulaması")
    print("=" * 70)
    print("1) Quiz başlat")
    print("2) Soru sayısını göster")
    print("3) Çıkış")

    # input ile kullanıcıdan seçim alınır.
    # strip() ile baştaki/sondaki boşluklar temizlenir.
    choice = input("Seçiminiz: ").strip()

    # while döngüsü, geçerli bir menü seçimi yapılana kadar tekrar ister.
    while choice not in {"1", "2", "3"}:
        choice = input("Geçersiz seçim. Lütfen 1, 2 veya 3 girin: ").strip()
    return choice


# ask_question fonksiyonu:
# Tek bir soruyu kullanıcıya gösterir, cevabı alır ve doğru/yanlış kontrolü yapar.
#
# Parametreler:
# - index: Kaçıncı soru olduğu
# - total: Toplam soru sayısı
# - question_data: Soru metni, şıklar ve doğru cevabı içeren sözlük
#
# Geriye, bu soruya ait kullanıcı sonucunu içeren bir sözlük döndürür.
def ask_question(index, total, question_data):
    print("\n" + "=" * 70)
    print(f"Soru {index}/{total}")
    print("-" * 70)
    print(question_data["question"])

    # options sözlüğündeki tüm şıkları sırayla ekranda göstersin
    for key, value in question_data["options"].items():
        print(f"{key}) {value}")

    # Kullanıcıdan cevap alınır.
    # upper() kullanımı sayesinde küçük harf girilirse bile büyük harfe çevirsin.
    user_answer = input("\nCevabınız: (A/B/C/D): ").strip().upper()

    # Geçerli bir cevap girilene akdar kullancıı tekrar yönlendilir.
    while user_answer not in {"A", "B", "C", "D"}:
        user_answer = input("Geçersiz giriş. Lütfen A,B,D veya D giriniz: ").strip().upper()

    # Soru verisindeki doğru cevap alınır.
    correct_answer = question_data["answer"]

    # Kullanıcını cevabı ile dorğu cevap karşılaştırılır.
    is_correct = user_answer == correct_answer

    # Kullanıcı anlık geri bildirim verilir
    if is_correct:
        print("Sonuç: Doğru")
    else:
        print(
            f"Sonuç: Yanlış | Doğru cevap: {correct_answer} "
            f"{question_data['options'][correct_answer]}"
        )

    # Sonuçlar standart yapıda döndürülsün
    return {
        "question": question_data["question"],
        "options": question_data["options"],
        "correct_answer": correct_answer,
        "user_answer": user_answer,
        "is_correct": is_correct,
    }


# Quiz akışının ana  çalıştırıcı fonksiyonudur.
# Tüm soruları rastgele karıştırır ve sırayla kullanıcıya sorar
# puan hesaplar ve sonuç listesinini dönderir.
def run_quiz(questions):
    # Original soru listesini bozmamak için kopyalama yapıyoruz.
    randomized_questions = questions[:]

    # Sorular rastgele karıştırılır
    # Böylece her quiz aynı sırada başlamaz
    random.shuffle(randomized_questions)

    print("\nQuiz başladı. Sroular rastgele karıştırıldı")

    # Sorular rastgele sayısı hespalanır.
    total = len(randomized_questions)

    # Score değişkeni doğru cevap sayısını tutar
    score = 0

    # user_result listesi, her soruya ilişkin kullanıcı sonucunu saklar.
    user_results = []

    # enumarate : soru numaralandırılması
    for index, question_data in enumerate(randomized_questions, start=1):
        result = ask_question(index, total, question_data)
        user_results.append(result)

        # Eğer soru doğru ise skor 1 artırır
        if result["is_correct"]:
            # score =score+ 1
            score += 1

    # Quiz tamamlandıktan sonra puan, toplam soru ve detaylı sonuçları döndersin.
    return score, total, user_results


# create_result_base_names fonksiyonu:
# Sonuç dosyalarını ortak temel isi üretir.
# Örneğin:
# results/quiz_result_20260428_171845
# Sonra buna .txt, .csv, .html uzantıları eklenir
def create_result_base_names():
    # önce sonuç klasörünün var olup olmadığını kontrol edelim
    ensure_results_dir()

    # Şu anki tarih-saat bilgisi dosya adı için uygun formatta çevrilir
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Path nesnesi olarak temel dosya adını oluşturulur
    base_name = RESULTS_DIR / f"quiz_result_{timestamp}"
    return base_name


# save_results_txt dosyasını fonksiyonun
# Quiz sonucu okunabilir bir metin raporu olarak '.txt' dosyanına  kaydeder.
# Text insan gözüyle daha rahat okunur
def save_results_txt(base_name, score, total, percent, user_results):
    txt_path = base_name.with_suffix(".txt")

    # Dosya yazma modunda açılır
    with open(txt_path, "w", encoding="utf-8") as file:
        file.write("PYTHON QUIZ SONUÇ RAPORU\n")
        file.write("=" * 70 + "\n")
        file.write(f"Tarih          : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Doğru sayısı   : {score}\n")
        file.write(f"Yanlış sayısı  : {total - score}\n")
        file.write(f"Toplam soru    : {total}\n")
        file.write(f"Başarı Oranı   : {percent:.2f}\n")
        file.write("=" * 70 + "\n\n")

        # Her soru tek tek rapora detaylı şekilde yazılır.
        for index, item in enumerate(user_results, start=1):
            file.write(f"Soru   {index}: {item['question']}\n")
            file.write(f"İşaretlenen cevap :  {item['user_answer']}) {item['options'][item['user_answer']]}\n")
            file.write(f"Doğru cevap       :  {item['correct_answer']}) {item['options'][item['correct_answer']]}\n")
            file.write(f"Durum             :  {'Doğru' if item['is_correct'] else 'Yanlış'}\n")
            file.write("-" * 70 + "\n")

    return txt_path


# save_result_csv dosyasını fonksiyonun
# Sonuçları tablo yapısında '.csv' olarak kaydeder
# böylece Excel, Google Sheets veya veri analizi araçlarında kolaylıkla açılabilir
# Text insan gözüyle daha rahat okunur
# def save_results_csv
def save_results_csv(base_name, score, total, percent, user_results):
    csv_path = base_name.with_suffix(".csv")

    # Dosya yazma modunda açılır
    with open(csv_path, "w", encoding="utf-8") as file:
        writer = csv.writer(file)

        # özet bilgiler
        writer.writerow(["summary_type", "value"])
        writer.writerow(["date", datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
        writer.writerow(["score", score])
        writer.writerow(["wrong", total - score])
        writer.writerow(["total", total])
        writer.writerow(["percent", f"{percent:.2f}"])
        writer.writerow([])

        # Ardından detay veri başlıkları yazılır.
        writer.writerow([
            "question_no",
            "question",
            "option_a",
            "option_b",
            "option_c",
            "option_d",
            "user_answer",
            "correct_answer",
            "result",
        ])

        # Her sorunun detayları satır satır yazılır.
        for index, item in enumerate(user_results, start=1):
            writer.writerow([
                index,
                item["question"],
                item["options"]["A"],
                item["options"]["B"],
                item["options"]["C"],
                item["options"]["D"],
                item["user_answer"],
                item["correct_answer"],
                "Doğru" if item["is_correct"] else "Yanlış",
            ])

    return csv_path


# get_option_css_class fonksiyonu:
# HTML raporunda her seçeneğin hangi renkle/biçimle gösterileceğini belirler.
#
# Senaryolar:
# - Hem kullanıcı seçti hem doğruysa: özel başarılı seçili stil
# - Doğru cevap ama kullanıcı seçmediysa: doğru cevap stili
# - Kullanıcı yanlış şıkkı seçtiyse: yanlış seçili stil
# - Diğer tüm şıklar: normal stil
#
# Bu fonksiyon yalnızca CSS sınıfı adı döndürür.
def get_option_css_class(option_key, user_answer, correct_answer):
    if option_key == correct_answer and option_key == user_answer:
        return "option option-correct-selected"
    if option_key == correct_answer:
        return "option option-selected"
    if option_key == correct_answer and option_key != user_answer:
        return "option option-wrong-selected"
    return "option"


# save_all_results fonksiyonu:
# Quiz tamamlandıktan sonra tüm rapor dosyalarını tek noktadan üretir.
# TXT, CSV ve HTML dosyalarını oluşturur ve bunların yolunu döndürür.
def save_all_results(score, total, user_results):
    # Başarı oranı yüzde olarak hesaplanacaktır.
    # total sıfır olursa hata olmaması için güvenli kontroller gereklidir
    percent = (score / total) * 100 if total else 0

    # Tüm dosyalarda kullanıalcak ortak temel isim üretilir.
    base_name = create_result_base_names()

    # Üç farklı formatta rapor oluşturulur.
    txt_file = save_results_txt(base_name, score, total, percent, user_results)
    csv_file = save_results_csv(base_name, score, total, percent, user_results)
    html_file = save_results_html(base_name, score, total, percent, user_results)

    return txt_file, csv_file, html_file, percent


# show_final_summary fonksiyonu:
# Quiz bitince kullanıcıya terminal ekranında özet bilgi verir.
# Doğru, yanlış, toplam ve yüzde başarı bilgisi yazdırılır.
# Ayrıca başarı oranına göre kısa bir değerlendirme metni gösterilir.
def show_final_summary(score, total, percent):
    print("\n" + "=" * 70)
    print("Quiz tamamlandı")
    print("=" * 70)
    print(f"Doğru sayısı: {score}")
    print(f"Yanlış sayısı: {total - score}")
    print(f"Toplam soru: {total}")
    print(f"Başarı Oranı: %{percent:.2f}")

    # Başarı oranına göre seviye değerlendirme
    if percent == 100:
        print("Değerlendirme mükemmel")
    elif percent >= 80:
        print("Değerlendirme çok iyi")
    elif percent >= 60:
        print("Değerlendirme iyi")
    elif percent >= 40:
        print("Değerlendirme orta")
    else:
        print("Değerlendirme: Daha iyi olabilir çok çalışmalısınız.")


################################################################################################################
# main fonksiyonu:
# Programın giriş noktasıdır.
# Genel akış burada yönetilir:
# 1) Soruları yükle
# 2) Menü göster
# 3) Kullanıcı seçimine göre quiz başlat / soru sayısını göster / çıkış yap
def main():
    # Önce CSV dosyasındaki sorular yüklenir.
    questions = load_questions(CSV_FILE)

    # Eğer soru listesi boşsa program devam etmez.
    if not questions:
        print("Program sonlandırıldı. Soru listesi boş veya CSV hatalı.")
        return

    # Sonsuz döngü ile menü sürekli gösterilir.
    # Kullanıcı '3' ile çıkış yapana kadar program açık kalır.
    while True:
        choice = prompt_menu()

        # 1 seçildiyse quiz başlatılır.
        if choice == "1":
            score, total, user_results = run_quiz(questions)
            txt_file, csv_file, html_file, percent = save_all_results(score, total, user_results)

            show_final_summary(score, total, percent)
            print("\nSonuç dosyaları oluşturuldu:")
            print(f"TXT  : {txt_file}")
            print(f"CSV  : {csv_file}")
            print(f"HTML : {html_file}")

        # 2 seçildiyse toplam soru sayısı gösterilir.
        elif choice == "2":
            print(f"\nToplam soru sayısı: {len(questions)}")

        # 3 seçildiyse program sonlandırılır.
        elif choice == "3":
            print("Program kapatıldı.")
            break


# Bu koşulun anlamı:
# Dosya doğrudan çalıştırılırsa main() fonksiyonu devreye girsin.
# Ancak bu dosya başka bir Python dosyası içinde import edilirse
# otomatik olarak çalışmasın.
if __name__ == "__main__":
    main()

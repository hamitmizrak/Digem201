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

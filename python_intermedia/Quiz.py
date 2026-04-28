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

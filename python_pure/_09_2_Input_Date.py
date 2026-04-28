
# Date

from datetime import datetime

# Kullanıcıdan veri al
user_input=input("\nTarih Giriniz: (YYYY-MM-DD)")

# Formatter
data_object= datetime.strptime(user_input,"%Y-%m-%d")
print(f"Güncel Format Tarih {data_object}")
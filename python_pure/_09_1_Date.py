
# Date

from datetime import datetime

current_time=datetime.now()
print(f"{current_time}")

# Formatter
formatter=current_time.strftime("%Y-%m-%d")
print(f"{formatter}")


formatter_year=current_time.strftime("%Y")
print(f"{formatter_year}")


formatter_month=current_time.strftime("%m")
print(f"{formatter_month}")

formatter_date=current_time.strftime("%d")
print(f"{formatter_date}")

#
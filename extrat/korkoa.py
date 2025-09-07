import math
from datetime import date

# korkoa korolle -laskuri

# esim: https://raha.fi/korkoa-korolle-laskuri/
# kaava: S × (1+r/100)^t
# esimerkki: 7 000 × (1+7/100)^10 = 13 770,06
# S = alkuperäinen sijoitus, r = korko, t = sijoitusaika (esim. vuosissa)
start_money = 7000
profit = 7

# selvitetään vuosien määrä kahden päivämäärän välillä
save_date = date(2024, 9, 5)
end_date = date(2034, 12, 31)

# lasketaan vuosien määrä päivämäärien välillä
delta = end_date - save_date
days = delta.days
years = days // 365
print(years)

# kaava: S × (1+r/100)^t
total_money = start_money * math.pow(1 + profit / 100, years)
total_money = round(total_money, 2 )
print(total_money)

# lasketaan tuoton määrä ja tulostetaan käyttäjälle
new_money = total_money - start_money
new_money = round(new_money, 2)
print(f"Tuottoa tuli: {new_money} €")
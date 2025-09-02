from datetime import date, timedelta

# tästä päivästä vuoden loppuun aikaleimat
first = date(2025, 9, 2)
second = date(2025, 12, 31)

# lasketaan aikaleimojen ero päivinä
delta = second - first
days = delta.days

# lopputulos
print(f"Päiviä jäljellä tätä vuotta: {days} kpl")

# ESIMERKKI 2

# esim. jos lainataan kirjastosta kirja, mikä on palautuspäivä
# kolmen viikon päästä?
today = date.today()
today = today + timedelta(21)

print(f"Palautuspäivä kolmen viikon päästä on: {today}")
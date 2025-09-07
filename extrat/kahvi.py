# https://www.mathsisfun.com/algebra/exponential-growth.html
# ks. kohta "Half Life" (kahviesimerkki)

import math
from datetime import datetime

# 1 = kahvin määrä, esim 1 kuppi
# kaava: y(9) = 1 e^((ln(0.5)/6)×9) = 0.35
# kaava: cup * exp((ln(0.5)/half_life) * hours)

# kofeiinin puoliintumisaika
half_life = 4

# 300ml tässä tapauksessa yksi kahvikuppi
cup = 300

# milloin kahvi juotiin ja milloin tarkistetaan tulos
then = datetime(2024, 9, 5, 11, 0, 0)
now = datetime(2024, 9, 5, 20,0,0)

# kuinka monta sekuntia oli näiden aikojen välissä
duration = now - then
seconds = duration.total_seconds()

# sekunnit minuuteiksi, ja sitten tunneiksi
minutes = seconds / 60
hours = minutes // 60
print(hours)

# kaava: cup * exp((ln(0.5)/half_life) * hours)
# math.log Pythonissa on sama kuin ln() (luonnollinen logaritmi)
logarithm = math.log(0.5) / half_life
coffee_left = cup * math.exp(logarithm * hours)
coffee_left = int(coffee_left)

print(f"Kahvia jäljellä elimistössä vielä: {coffee_left} ml")
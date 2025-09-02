import math

# piin arvo saadaan helposti math-moduulin kautta
# VIIKKOTEHTÄVISSÄ: aina kun kysytään piin arvoa, käyttäkää tätä!
# ÄLKÄÄ KOODATKO PIIN ARVOA ITSE TYYLIIN 3.14
print(math.pi)

# ympyrän ympärysmitta, 2 * pi * säde
# lasketaan ympärysmitta ja pyöristetään kahteen desimaaliin
radius = 13
border = 2 * math.pi * radius

# pyöristetään tulos
border = round(border, 2)

# HUOM! pelkkä round() ei riitä, jos et tallenna tulosta
# takaisin muuttujaan!, eli pelkkä:
# round(border, 2)
# ei riitä!
print(f"Ympärysmitta: {border} cm")
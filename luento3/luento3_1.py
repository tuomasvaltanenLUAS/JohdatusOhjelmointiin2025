# tämä kooditiedosto esittelee float-tietotyypin ongelmia tietyillä luvuilla
from decimal import Decimal
import math

# Tämä esimerkki havainnollistaa erään tympeän ominaisuuden, joka koskee float-tietotyyppiä
number1 = float(0.1)
number2 = float(0.2)
print(f"Tavanomaiset floatit/desimaaliluvut: {number1} + {number2} =")
print(number1 + number2)

# suoraviivaisin ratkaisu => pyöristä arvo siihen tarkkuuteen mitä tarvitset
total = number1 + number2
total = round(total, 1)
print(total)
print()

# yksi tapa välttää tämä ongelma on käyttää Pythonin decimal -kirjastoa
# huom: muista alkuun import decimal
number3 = Decimal("0.1")
number4 = Decimal("0.2")
print(f"Decimal-kirjaston desimaaliluvut: {number3} + {number4} =")
print(number3 + number4)
# importtaukset ovat aina tiedostokohtaisia, pitää importata
# aina uudestaan jos tarvit samoja moduleja
import math

# math.pow() -> 5 potenssiin 7
total1 = math.pow(5, 7)
print(total1)

# Pythonin oma syntaksi potenssille on myös aivan hyvä!
total2 = 5 ** 7
print(total2)

# neliöjuuri, eli square root => sqrt
value = 9
root_value = math.sqrt(value)
print(root_value)

# koodarin tulee pystyä kääntämään matemaattinen kaava koodiksi
# vaikka kaava ei olisikaan täysin tuttu, esim:
# d = s √3 (tai d = s * sqrt(3))
side = 5
diagonal = side * math.sqrt(3)
print(diagonal)
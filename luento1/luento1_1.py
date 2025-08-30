print("Testi!")

age = 35
print(age)

salary = 3200
print(salary)

name = "Testi Henkilö"
print(name)

tax = 1.255
print(tax)

# tehdään uusi versio age-muuttujasta, joka onkin tekstiä
# jos yritämme tällä tavalla yhdistää numeroita ja tekstiä,
# tulee virhe: TypeError
# tämä on helppo ratkaista käyttämällä f-stringiä (ks. luento1_3.py)
age_text = str(age)
text = "Ikä: " + age_text
print(text)

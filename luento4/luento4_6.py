# 2. Tee yksinkertainen laskinohjelma, jossa käyttäjä voi tehdä seuraavat
# operaatiot: +, -, * ja /. Kysy alussa käyttäjältä kaksi eri numeroa float-muodossa,
# ja kysy lopuksi minkä operaation hän haluaa näiden lukujen välillä suorittaa.

# Kun käyttäjä on valinnut numerot ja operaation, suorita valittu operaatio numeroiden välillä.

# Jos käyttäjä valitsee jakolaskun, tarkista ettei käyttäjän toinen numero ole 0.
# Jos käyttäjä kuitenkin syötti toisena numerona nollan, ilmoita käyttäjälle että
# nollalla ei voi jakaa. Jos käyttäjä valitsee operaation mitä ei ole olemassa,
# ilmoita käyttäjälle: "Vääränlainen operaatio"

# Tulosta lopputulos pyöristettynä yhteen desimaaliin.

# kysytään muuttujat
number1 = input("Syötä ensimmäinen numero:\n")
number1 = float(number1)
number2 = input("Syötä toinen numero:\n")
number2 = float(number2)
operation = input("Mikä laskutoimitus (+, -, * vai /)?\n")

# alustetaan muuttuja joka pitää kirjaa lopputuloksesta
result = 0

# vain yksi laskutoimitus voi kerrallaan käynnistyä
if operation == "+":
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    # HUOM! nollalla ei saa jakaa, tarkistetaan
    if number2 == 0:
        print("Nollalla ei voi jakaa!")
    else:
        result = number1 / number2
else:
    print("Vääränlainen operaatio! (Syötä: +, -, * tai /)")


# pyöristetään ja tulostetaan
# tätä voi vielä jatkokehittää, ettei
# ohjelma tulosta mitään jos yritettiin jakaa nollalla
result = round(result, 1)
print(f"Tulos: {result}")

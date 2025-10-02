# puhelinnumeron tunnistaminen, onko oikeassa formaatissa
# testiluontoinen koodi, tämä ei vielä riittäisi missään varsinaisessa sovelluksessa

# suomen maakoodi = +358
# esimerkki suomalaisesta puhelinnumerosta: +358401234567
# suomalainen puhelinnumero +-muodossa on 13 merkkiä pitkä
# test = "+358401234567"
# print(len(test))

# logiikka:
# - ensimmäinen merkki on aina +
# - maakoodin pituus vaihtelee 1-3 -merkkiä, +-merkin jälkeen
# - pituus on 13 merkkiä?
# - maakoodin jälkeinen osuus on aina 9 merkkiä (2 + 7, operaattorin
# - osuus ilman ensimmäistä nollaa on 2 merkkiä)
# +-merkin jälkeen pelkkiä numeroita

# ---> riippuen maakoodin pituudesta, puhelinnumeron pituus on 11-13
# tosiasiassa puhelinnumerot ovat vieläkin monimutkaisempia,
# kannattaa harkita lisämoduulin käyttämistä tai muuta ratkaisua työelämässä (esim. regexp)
# ks. https://www.tutorialspoint.com/phonenumbers-module-in-python
# ks. https://stackoverflow.com/questions/8406765/international-phone-number-validation

phone_number = input("Syötä puhelinnumero:\n")
phone_number_length = len(phone_number)
phone_number_part = phone_number[1:]

# kokeillaan logiikan sääntöjä yksitellen läpi
# ensimmäinen merkki pitää olla aina +
if phone_number[0] != "+":
    print("Vääränlainen puhelinnumero, +-merkki puuttuu alusta.")
elif phone_number_length < 11 or phone_number_length > 13:
    print("Vääränlainen puhelinnumero, väärä pituus (pitää olla 11-13).")
elif not phone_number_part.isnumeric():
    # haetaan ensin kaikki merkit ensimmäisen merkin jälkeen (eli +)
    # ja tästä lopusta tekstistä katsotaan, että se on pelkästään numeroita
    print("Vääränlainen puhelinnumero, tekstiä seassa.")
else:
    # tässä on testattu vain osa ehdoista, mutta tämäntyylisiä
    # tällaiset validointilogiikat yleensä on
    print("Puhelinnumero ok!")

    country_code = ""

    # ei millään tavalla optimaalinen/dynaaminen ratkaisu
    # jokin hienompi logiikka joka osaa irroittaa
    # maakoodin vaikka pituus muuttuisi, olisi hyvä
    if phone_number_length == 13:
        country_code = phone_number[0:4]

    print(country_code)
# yleensä viikkotehtävissä koodi lähtee siitä että kysytään
# käyttäjältä numeroita tai muuta tietoa

# VAIHE 1: pyydetään käyttäjältä dataa / muuttujia
number1 = input("Anna numero: ")

# muutetaan käyttäjän antama teksti numeroksi
# jos haluat kokonaisluvun sijasta desimaalit,
# käytä number1 = float(number1)
# muista että inputista tulee aina ensin tekstiä
# vaikka siihen olisi kirjoitettu numero
number1 = int(number1)

# VAIHE 2: suoritetaan tarvittava laskutoimitus / laskutoimitukset
total = number1 + 100

# VAIHE 3: tulostetaan lopputulos
print(total)
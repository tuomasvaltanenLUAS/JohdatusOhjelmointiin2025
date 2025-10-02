# 3. Tee ohjelma, joka pyytää käyttäjältä tuotteen nimen, tuotteiden lukumäärän sekä onko
#  hänellä tarjouskuponkia (kyllä/ei). Ohjelman hinnasto on seuraavanlainen:
# - älypuhelin = 599 € per kpl
# - tietokone = 899 € per kpl
# - kahvinkeitin = 129 € per kpl

# Laske käyttäjän tuotteiden kokonaisarvo. Mikäli käyttäjällä on tarjouskuponki,
# vähennä kokonaishinnasta 15%. Tulosta lopuksi kokonaishinta, ja ilmoita käyttäjälle
# mikäli tarjouskuponkia käytettiin tilauksessa.

# vaihe 1: kysytään muuttujat käyttäjältä
product = input("Syötä tuotteen nimi (älypuhelin, tietokone, kahvinkeitin):\n")
amount = input("Kuinka monta kappaletta tuotetta haluat ostaa?\n")
amount = int(amount)
discount = input("Onko sinulla tarjouskuponki? (kyllä/ei)\n")

# hyvän tavan mukaisesti, alustetaan muuttuja, jossa pidetään kirjaa lopputuloksesta
result = 0

# lasketaan tilauksen loppusumma
if product == "älypuhelin":
    result = amount * 599
elif product == "tietokone":
    result = amount * 899
elif product == "kahvinkeitin":
    result = amount * 129
else:
    print("Tuotetta ei ole valikoimassa.")

# jos käyttäjällä oli kuponki, vähennä hinnasta -15%
if discount == "kyllä":
    # vähennetään 15% , eli 1 - 0.15 = 0.85
    result = result * 0.85
    print("Tarjouskuponki -15% käytetty!")

# pyöristetään ja tulostetaan lopputulos
result = round(result, 2)
print(f"Tilauksen loppusumma: {result} €")

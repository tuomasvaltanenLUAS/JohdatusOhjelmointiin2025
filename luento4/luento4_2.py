# nämä voi korvata inputeilla myös!
age = 17
city = "Rovaniemi"

# tarkoitus on tehdä ohjelma, joka toimii näin:
# jos käyttäjä on 18v tai yli => tulostetaan hänen kotikaupunkinsa mukainen
# ohjeistus terveydenhuoltoon.
# jos käyttäjä on alle 18v, ohjeistetaan käyttäjää ottamaan yhteyttä oman
# koulun opiskelijaterveydenhuoltoon

# helpoin tapa tehdä sisennettyjä ehtolauseita on purkaa tehtävänanto osiin:
# jos käyttäjä on 18v tai yli
# => tulostetaan kotikaupungin mukainen ohjeistus terveydenhuoltoon
if age >= 18:
    # tässä vaiheessa tiedetään, että käyttäjä on 18v tai yli
    # seuraavaksi pitää selvittää minkä kaupungin ohjeet tulostetaan
    if city == "Rovaniemi":
        print("Aikuisten terveydenhuolto on osoitteessa Testikuja 12")
    elif city == "Tornio":
        print("Aikuisten terveydenhuolto on osoitteessa Kokeilukatu 4")

else:
    print("Alaikäisten terveydenhuolto oman koulun ohjeiden mukaan.")
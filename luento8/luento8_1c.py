# tehdään lista tuotteista
products = ["Pölynimuri", "Kahvinkeitin", "Jääkaappi",
            "Pakastin", "Älypuhelin", "Kynnysmatto"]

# len()-funktio toimii sekä kokoelmille että tekstille
# eli kuinka monta elementtiä listassa on
# eli montako tuotetta listassa tässä tapauksessa
amount = len(products)

# kysytään käyttäjältä kuinka mones tuote halutaan
# listasta nähdä, HUOM! indeksi on aina kokonaisluku, eli int()
choice = input("Monennenko tuotteen haluat nähdä?\n")
choice = int(choice)

# jos käyttäjän indeksi on alle tuotteiden lukumäärä
# ja samalla indeksi on 0 tai suurempi
# eli esim. jos tuotteita on 4, indeksin pitää olla välillä 0-3
if choice < amount and choice >= 0:
    # haetaan käyttäjän antaman indeksin mukainen tuote
    # huomaa, kuinka koodissa ei ole yhtään ehtolausetta
    # vaikka ohjelma toimii er tavoilla rippuen siitä mitä käyttäjä syötti
    text = products[choice]
    print(text)
else:
    print("Tällä indeksillä ei ole tuotetta!")
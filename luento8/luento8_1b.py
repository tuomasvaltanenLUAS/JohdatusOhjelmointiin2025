# tehdään lista tuotteista
products = ["Pölynimuri", "Kahvinkeitin", "Jääkaappi", "Pakastin"]

# kysytään käyttäjältä kuinka mones tuote halutaan
# listasta nähdä, HUOM! indeksi on aina kokonaisluku, eli int()
choice = input("Monennenko tuotteen haluat nähdä?\n")
choice = int(choice)

# haetaan käyttäjän antaman indeksin mukainen tuote
# huomaa, kuinka koodissa ei ole yhtään ehtolausetta
# vaikka ohjelma toimii er tavoilla rippuen siitä mitä käyttäjä syötti
text = products[choice]
print(text)
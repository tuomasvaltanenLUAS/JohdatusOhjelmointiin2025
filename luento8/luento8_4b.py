# tehdään lista tuotteista
products = ["Pölynimuri", "Kahvinkeitin", "Jääkaappi",
            "Pakastin", "Älypuhelin", "Kynnysmatto"]

# kysytään käyttäjältä monesko tuote muutetaan (indeksi)
choice = input("Monesko tuote muutetaan?\n")
choice = int(choice)

# kysytään käyttäjältä millä tuotteella se korvataan
new_product = input("Korvaavan tuotteen nimi?\n")

# korvataan tuote käyttäjän antamalla uudella tuotteella
products[choice] = new_product

# testataan pikaisesti päivittyikö data
print(products)
# tuple joka sisältää viikonpäivät
weekdays = ("Maanantai", "Tiistai", "Keskiviikko", "Torstai",
            "Perjantai", "Lauantai", "Sunnuntai")

# kysytään käyttäjältä viikonpäivän indeksi
# jotta saadaan täsmäämään käyttäjän numero kokoelman kanssa => -1
choice = input("Kuinka mones viikonpäivä?\n")
choice = int(choice) - 1

# haetaan vastaava päivä ja tulostetaan
text = weekdays[choice]
print(text)
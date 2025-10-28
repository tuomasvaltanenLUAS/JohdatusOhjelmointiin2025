# tuple joka sisältää viikonpäivät
weekdays = ("Maanantai", "Tiistai", "Keskiviikko", "Torstai",
            "Perjantai", "Lauantai", "Sunnuntai")

# HUOM! Tuplea ei voi päivittää lennosta, vaan se pitää tehdä kokonaan uusiksi
# jos jotain pitää muuttaa
# weekdays[2] = "Enstai"

# kysytään käyttäjältä viikonpäivän indeksi
# jotta saadaan täsmäämään käyttäjän numero kokoelman kanssa => -1
choice = input("Kuinka mones viikonpäivä?\n")
choice = int(choice) - 1

# haetaan vastaava päivä ja tulostetaan
text = weekdays[choice]
print(text)
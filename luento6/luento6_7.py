# kannattaa kokeilla tätä esimerkkiä Python Tutorissa!
print("Käynnistetään ohjelma!")

# apumuuttuja, joka pitää kirjaa siitä
# pidetäänkö ohjelmaa vielä käynnissä
running = True

# ohjelman pääsilmukka, ajetaan tätä niin monta kertaa
# kuin käyttäjä haluaa
while running:
    print("Ajetaan ohjelma!\n")

    # tässä voisi olla varsinainen käyttäjän ohjelmalogiikka
    # esim. kysytään lukuja, lasketaan jotakin ym. ym.
    number = input("Anna numero:\n")
    number = int(number)

    # tuplataan käyttäjän numero
    total = number * 2
    print(f"Numero tuplattuna: {total}")

    # VIIMEINEN VAIHE: tarkistetaan haluaako käyttäjä vielä jatkaa
    answer = input("Haluatko jatkaa ohjelman käyttöä? (k/e)?\n")

    # pieni kikka: pakotetaan answer pieneksi kirjaimeksi, jolloin myös iso E käy
    if answer.lower() == "e":
        # tämän jälkeen while-silmukan ehto ei enää päde
        # jonka myötä pääsilmukka lopettaa toiminnan
        # ja koodi hyppää silmukan jälkeiselle riville
        # (voidaan kiittää käyttäjää ym.)
        running = False

# silmukka päättyi, eli ohjelmaa ei enää ajeta
# kiitetään käyttäjää ohjelman käytöstä
print("Kiitos ohjelman käytöstä!")
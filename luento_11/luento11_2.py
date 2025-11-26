# avataan yhteys tiedostoon
file_handle = open("weekdays.txt", "r")

counter = 1

# puretaan tiedoston sisältö rivi kerrallaan
# niin kauan kuin tietoa on vielä jäljellä
# => jos tideostossa on 100 riviä
# ==> tämä silmukka ajetaan 100 kertaa
while True:
    # haetaan seuraava rivi
    line = file_handle.readline()

    # jos tiedoston loppu tulee vastaan
    # eli line == None, lopetetaan silmukka
    if not line:
        break

    # tulostetaan tekstitiedoston rivi + laskuriarvo
    print(f"{counter} - {line}")

    # korotetaan laskuria ennen seuraavaa riviä
    counter = counter + 1


# tiedostoa ei tässä vaiheessa enää tarvita
# => suljetaan yhteys
file_handle.close()
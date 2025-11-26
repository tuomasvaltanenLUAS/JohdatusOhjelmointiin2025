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
    print(f"{counter} - {line}")

    counter = counter + 1

    # jos tiedoston loppu tulee vastaan
    # eli line == None, lopetetaan silmukka
    if not line:
        break


# tiedostoa ei tässä vaiheessa enää tarvita
# => suljetaan yhteys
file_handle.close()
# avataan yhteys tiedostoon
file_handle = open("weekdays.txt", "r")

# luetaan tiedoston sisältö muuttujaan
content = file_handle.read()

# tiedostoa ei tässä vaiheessa enää tarvita
# suljetaan yhteys (koska data on jo ladattu)
file_handle.close()

# muutetaan rivinvaihdon pohjalta listaksi
lines = content.split("\n")

# lines ihan tavallinen Python lista -> for-loopilla läpi
for line in lines:
    print(line)
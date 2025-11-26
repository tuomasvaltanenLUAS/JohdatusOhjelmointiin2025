# avataan yhteys tiedostoon
file_handle = open("weekdays.txt", "r")

# luetaan tiedoston sisältö muuttujaan
# => tietotyyppi on oletuksena string/tekstiä
content = file_handle.read()

# tiedostoa ei tässä vaiheessa enää tarvita
# koska tiedoston sisältö ladattiin jo ylempänä muuttujaan
file_handle.close()

# tulostetaan kuin mikä tahansa muuttuja
print(content)
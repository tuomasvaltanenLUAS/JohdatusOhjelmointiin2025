# avataan yhteys tiedostoon
file_handle = open("weekdays.txt", "r")

# luetaan tiedoston sisältö muuttujaan
# => tietotyyppi on oletuksena string/tekstiä
content = file_handle.read()

# tulostetaan kuin mikä tahansa muuttuja
print(content)
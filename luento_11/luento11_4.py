# avataan yhteys tiedostoon, utf-8-formaatissa
# w => write => yliajaa aiemman tiedoston sisällön
file_handle = open("muistio.txt", "w", encoding="utf-8")

# kysytään käyttäjältä viesti
message = input("Kirjoita viesti:\n")

# tallenetaan käyttäjän antama teksti tiedostoon
file_handle.write(message)

# suljetaan yhteys
file_handle.close()
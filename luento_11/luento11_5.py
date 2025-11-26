# avataan yhteys tiedostoon, utf-8-formaatissa
# a => append => kirjoitetaan tiedoston loppuun uutta dataa
file_handle = open("muistio.txt", "a", encoding="utf-8")

# kysytään käyttäjältä viesti
message = input("Kirjoita viesti:\n")

# tallenetaan käyttäjän antama teksti tiedostoon
file_handle.write(message + "\n")

# suljetaan yhteys
file_handle.close()
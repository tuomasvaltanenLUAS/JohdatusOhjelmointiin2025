# tehdään lista tuotteista
products = ["Pölynimuri", "Kahvinkeitin", "Jääkaappi", "Pakastin"]

# tämä on ns. raakamuoto, voi käyttää debuggauksessa
# tai jos muutoin haluaa nopeasti tietää mitä listan sisällä on
# tätä muotoa ei näytetä yleensä käyttäjälle, koska tämä on liian raaka
# formaatti
# print(products)

# haetaan yksittäinen tuota ylläolevasta listasta
# indeksi 2, eli kolmas tuote
# myös negatiivinen indeksi on mahdollinen, esim. -1 => viimeinen tuote
# negatiivisia indeksejä käytetään yleensä tekstien kanssa,
# ei niinkään kokoelmien kanssa
text = products[2]
print(text)
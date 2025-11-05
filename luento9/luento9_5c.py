# VERSIO 2: yksinkertainen hakukone:
# näytä vain sellaiset tapahtumat, joissa on haettu kategoria

import urllib.request
import var_dump as vd
import json

# get internet data
url = 'https://edu.frostbit.fi/api/events'
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")

# raw_data on nyt raakamuotoinen JSON-data, joka pitää
# vielä erikseen muuntaa Pythonin datamuotoon
data = json.loads(raw_data)

# käyttäjän hakusana kategorialle
choice = input("Millaisia tapahtumia haet?\n")

# käydään jokainen event listassa läpi
for event in data:
    # yhdistetään kategoriat yhdeksi tekstiksi
    categories = ", ".join(event['categories'])

    # continue on kätevä suodatusasioissa
    # eli jos haettu kategoria puuttuu => continue
    # => eli skipataan tämä tapahtuma
    if choice not in categories:
        continue

    # nimitieto tulee suoraan päätasolta (ks. var_dump kommentti ylempää)
    print(event['name'])

    # haetaan osoitetiedot => address => haluttu kenttä
    street_address = event['address']['street_address']
    postal_code = event['address']['postal_code']

    print(f"{postal_code} {street_address}")


    # jos kategoriat puuttuu => ilmoitetaan käyttäjälle
    if categories != "":
        print(f"KATEGORIAT: {categories}")
    else:
        print(f"-- EI KATEGORIOITA --")

    print()


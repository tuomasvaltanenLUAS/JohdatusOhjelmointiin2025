# VERSIO 3: yksinkertainen hakukone:
# näytä vain yksi tapahtuma, eli ensimmäinen joka osuu hakusanaan
# älä hae muita tapahtumia

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

    # tehdään ehtolause joka tunnistaa että nyt löytyi
    # sopiva tapahtuma => tulostetaan tiedot ja break => lopettaa silmukan
    if choice in categories:
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

        break


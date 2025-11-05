import var_dump as vd

# luodaan hotelli no. 1
hotel_1 = {
    "name": "Snow Line Hotels",
    "rating": 4.3,
    "wifi": True,
    "free_breakfast": True,
    "services": ["sauna", "meetings", "restaurant", "parking", "safaris"],
    "price_level": 4
}

# luodaan hotelli no. 2
hotel_2 = {
    "name": "North Ice Hostel",
    "rating": 3.5,
    "wifi": True,
    "free_breakfast": False,
    "services": ["sauna", "parking"],
    "price_level": 2
}

# asetetaan molemmat hotellit samaan listaan
hotels = [hotel_1, hotel_2]

# ks. luento9_4a.py => var_dumpin käyttäminen
# helpompi tutkia dataa tällä tavalla

# ['name'] => str(16) "Snow Line Hotels"
# ['rating'] => float(4.3)
# ['wifi'] => bool(True)
# ['free_breakfast'] => bool(True)
# ['services'] => list(5)
#    [0] => str(5) "sauna"
#    [1] => str(8) "meetings"
#    [2] => str(10) "restaurant"
#    [3] => str(7) "parking"
#    [4] => str(7) "safaris"
# ['price_level'] => int(4)

# silmukoidaan hotellidata läpi
for hotel in hotels:
    print(hotel['name'])

    # myös ylimääräistä lgoiikkaa voidaan tehdä ehtolauseilla
    if "sauna" in hotel['services']:
        print("Hotellissa on sauna.")

    if "restaurant" in hotel['services']:
        print("Hotellissa on ravintola.")

    print()
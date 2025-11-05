# ehdottomasti yleisin datarakenne työelämässä
# eli lista joka koostuu dictionaryistä
# jokainen dictionary yleensä koostuu myös monesta muusta rakenteesta
products = [
    {"name": "Kahvinkeitin", "price": 79},
    {"name": "Astianpesukone", "price": 299},
    {"name": "Arkkupakastin", "price": 199},
    {"name": "Postilaatikko", "price": 49}
]

# kokeile Python Tutorissa!

# tyypillisesti tällaista dataa käsitellään for-silmukalla
for item in products:
    # puretaan tuotteen eri osat apumuuttujiin
    name = item['name']
    price = item['price']

    # tulostetaan tämän hetkisen tuotteen tiedot
    print(f"{name} --- {price} €")
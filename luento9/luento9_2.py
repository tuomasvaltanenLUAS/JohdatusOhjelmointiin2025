# dictionary dictionaryn sisällä
book = {
    "name":  "My Lady Jane",
    "year":  2016,
    "publisher": {
        "name": "HarperTeen",
        "organization": "HarperCollins Publishers",
        "location": "New York"
    }
}

# pelkkä kirjan nimi
print(book['name'])

# tapa 1: tallennetaan alidictionary omaan muuttujaan
publisher = book['publisher']
print(publisher['organization'])

# tapa 2: voidaan myös ketjuttaa suoraan polku,
# mutta jos aiempi tapa on helpompi, käytä sitä
print(book['publisher']['organization'])
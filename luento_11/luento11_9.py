# VAIHE 1: luetaan tämän hetkiset datat tiedostosta
# ja tulostetaan allekkain
import json

# ladataan tiedoston sisältö muuttujaan
# ja suljetaan saman tien yhteys
file_handle = open("cities_data.json", "r", encoding="utf-8")
content = file_handle.read()
file_handle.close()

# muutetaan raaka-JSON => Pythonin dataformaattiin
# => json.loads()
cities = json.loads(content)

# cities on perus lista dictionaryjä Python-datana
# eli voimme vain silmukoida dataa normaalisti läpi
for city in cities:
    print(city['name'])
    print(city['county'])
    print(city['population'])
    print()

# VAIHE 2: kysytään käyttäjältä yksityiskohdat
# ja lisätään uusi kaupunki dataan (Python-lista tässä vaiheessa)
new_city_name = input("Anna uuden kaupungin nimi:\n")
new_city_county = input("Anna uuden kaupungin maakunta:\n")
new_city_population = input("Anna uuden kaupungin asukasluku:\n")
new_city_population = int(new_city_population)

# rakennetaan uuden lisättävän kaupungin DICTIONARY
# ylläolevien muuttujien pohjalta!
new_city = {
    "name": new_city_name,
    "population": new_city_population,
    "county": new_city_county
}

# nyt kun meillä on uusi lisättävä kaupunki
# dictionary-muodossa => lisätään se olemassa olevien kaupunkien
# cities-listaan (joka siis on lista dictionaryjä)
cities.append(new_city)

# VAIHE 3: muutetaan cities-lista (joka koostuu dictionaryistä)
# json-moduulilla Python-datasta => JSON-dataksi (tekstiksi)
json_data = json.dumps(cities, indent=2)

# avataan tiedosto ja tallennetaan uusi versio koko datasta
# vanhan datan päälle (ajetaan yli)
# HUOM! emme voi käyttää "a" -moodia JSONin kanssa
# koska se rikkoo JSON-datan rakenteen / syntaksin
file_handle = open("cities_data.json", "w", encoding="utf-8")
file_handle.write(json_data)
file_handle.close()

print("Uusi kaupunki tallennettu onnistuneesti!")
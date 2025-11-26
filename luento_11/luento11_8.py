# HUOM! JSON LADATAAN JA MUUTETAAN
# PYTHON-FORMAATTIIN SAMANKALTAISESTI MELKEIN AINA
import json

# ladataan tiedoston sisältö muuttujaan
# ja suljetaan saman tien yhteys
file_handle = open("cities.json", "r")
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
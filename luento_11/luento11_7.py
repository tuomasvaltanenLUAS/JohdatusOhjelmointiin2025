import json

# Python dictionary, esim. puhelin
phone = {
    "name": "Nokia 3310",
    "release_year": 2000,
    "battery": "1000mAh",
    "camera": False,
    "weight": 133
}

# koska haluamme tallentaa dataa
# pitää muuntaa Python-data => JSON-muotoon => json.dumps()
# jos haluat JSONin helpommin luettavaan muotoon
# json.dumps(phone, indent=2)
content = json.dumps(phone)

# koska content on nyt JSONia (eli tekstiä)
# => tallennetaan tiedostoon
file_handle = open("nokiaphone.json", "w")
file_handle.write(content)
file_handle.close()

print("Kiitos puhelimen lisäämisestä!")


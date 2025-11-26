import json

# ladataan tiedoston sisältö muuttujaan
# ja suljetaan saman tien yhteys
file_handle = open("app_data.json", "r")
content = file_handle.read()
file_handle.close()

# muutetaan raaka-JSON => Pythonin dataformaattiin
# => json.loads()
city = json.loads(content)

print(city['name'])
print(city['population'])

# jos haluat vertailla datatyyppejä
# JSON vs Python-data:
# import var_dump as vd
# print()
# vd.var_dump(content)
# print()
# vd.var_dump(city)
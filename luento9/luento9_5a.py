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

# tutkitaan dataa hieman tarkemmin
# vd.var_dump(data)

# [0] => dict(4)
#     ['name'] => str(24) "Taaperosirkus valloittaa"
#     ['date'] => str(9) "8.12.2025"
#     ['categories'] => list(6)
#         [0] => str(12) "lapsiperheet"
#         [1] => str(11) "leikkiminen"
#         [2] => str(13) "leikkipuistot"
#         [3] => str(8) "liikunta"
#         [4] => str(14) "osallistuminen"
#         [5] => str(14) "taaperoikäiset"
#     ['address'] => dict(2)
#         ['street_address'] => str(13) "Porvoonkatu 4"
#         ['postal_code'] => str(5) "00510"

# käydään jokainen event listassa läpi
for event in data:
    print(event['name'])
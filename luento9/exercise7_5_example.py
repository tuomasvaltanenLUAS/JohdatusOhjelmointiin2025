import json
import urllib.request

url = "https://edu.frostbit.fi/api/weather/"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")

weather = json.loads(raw_data)

# kannattaa tehdä apumuuttujat ennen silmukkaa, joissa pidetään
# kirjaa eri kaupungeista, eli missä tuulee eniten ja vähiten
strongest_wind = 0
strongest_wind_city = ""
weakest_wind = 0
weakest_wind_city = ""

for city in weather:
    print(city['location'])
    print(city['wind'])
    print()

    # tässä sitten ehtolauseita, jotka pitää kirjaa suurimmasta
    # ja pienimmästä tuulesta, ks. tehtävänannon vinkit ym. ym.
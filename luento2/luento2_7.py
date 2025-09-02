# perusimportilla tämä olisi hassu:
# import datetime
# today = datetime.datetime.now()
from datetime import datetime

today = datetime.now()
print(today)

# formaatti: pv.kk.vvvv tt:mm:ss
# eli %d = päivä, %m = kuukausi, %Y = vuosi, %H = tunti, %M = minuutti, %S = sekunti
# jos haluat %d ja %m edellän olevan nollan pois:
# Windows: %#d ja %#m
# Unix / Linux / MacOS: %-d ja %-m
date_text = today.strftime("%d.%m.%Y %H:%M:%S")
print(date_text)
print(f"Päivämäärä: {date_text}")
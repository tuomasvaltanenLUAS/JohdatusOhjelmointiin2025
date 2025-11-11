from functions import *

# käytetään funktiota tarkistamaan
# onko tilauskoodi oikeassa muodossa

test = "T123456789"
result = check_order(test)

# tulostetaan viesti lopputuloksen perusteella (boolean)
if result:
    print("Tilauskoodi OK!")
else:
    print("Tilauskoodi ei ole OK...")
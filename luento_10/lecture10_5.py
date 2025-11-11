# tarkoittaa: importataan KAIKKI funktiot
# functions.py -tiedoston sisältä
# on myös OK importata funktio kerrallaan
# esim. from functions import reverse_string jne

from functions import *

# kysytään käyttäjältä tuntien määrä
value = input("Anna tuntien lukumäärä:\n")
value = int(value)

# syötetään käyttäjän antama luku
# funktiolle, joka laskee siitä päivien lukumäärän
days = hours_to_days(value)
print(days)


# testimuuttuja, voisi korvata myös inputilla
age = 24

# ehtolause, onko ikä alle 20v?
# jos on => tulostetaan ehtolauseen sisällä oleva teksti
# jos ei => skipataan koko ehtolauseen sisällä oleva koodi

if age < 20:
    print("Olet alle 20v.")
    print("Myös tämä rivi tulostetaan VAIN jos ehto täyttyy!")

print("Tämä koodirivi ei enää kuulu if-lauseen sisälle, JOTEN TÄMÄ AINA!")


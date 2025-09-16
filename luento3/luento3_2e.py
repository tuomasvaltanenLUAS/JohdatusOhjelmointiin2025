# testimuuttuja, voisi korvata myös inputilla
age = input("Syötä ikäsi:\n")
age = int(age)

# kysytään käyttäjän asiointikuukausi
month = input("Minä kuukautena haluat asioida liikkeessä?\n")
month = int(month)

# ehtolause, onko ikä alle 20v?
# jos on => tulostetaan ehtolauseen sisällä oleva teksti
# jos ei => tulostetaan vastakohta
if age < 20:
    print("Olet alle 20v.")
elif age < 30:
    print("Olet alle 30v.")
elif age < 40:
    print("Olet alle 40v.")
else:
    print("Ikäsi on jotain muuta.")

# täysin erillinen if-lausekokonaisuus
# koska month-muuttuja ei liity age-muuttujaan tässä tapauksessa mitenkään
# on parempi tehdä erillinen if-lause
if month == 7:
    print("Liikkeemme on heinäkuussa suljettu!")
    print("Palataan asiaan elokuussa!")

print("Kiitos ohjelman käytöstä!")
# testimuuttuja, voisi korvata myös inputilla
age = input("Syötä ikäsi:\n")
age = int(age)

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

print("Kiitos ohjelman käytöstä!")


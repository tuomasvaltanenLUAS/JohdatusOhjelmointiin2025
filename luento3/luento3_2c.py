# testimuuttuja, voisi korvata myös inputilla
age = input("Syötä ikäsi:\n")
age = int(age)

# ehtolause, onko ikä alle 20v?
# jos on => tulostetaan ehtolauseen sisällä oleva teksti
# jos ei => tulostetaan vastakohta
if age < 20:
    print("Olet alle 20v.")
else:
    print("Olet 20v tai yli")


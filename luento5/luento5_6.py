# juomavalikoima tekstissä
drinks = "mehu, maito, kahvi, tee, vichy"
print(drinks)
print()

# kysytään käyttäjältä juoma
choice = input("Mitä juomaa haluat?\n")

# jos halutaan tietää onko jokin sana tekstimuuttujassa
# voidaan käyttää if in -komentoa
if choice in drinks:
    print("Löytyi!")
else:
    print("Ei löytynyt...")
# testimuuttuja, voisi korvata myös inputilla
age = input("Syötä ikäsi:\n")
age = int(age)

# onko age pienempi kuin 30
if age < 30:
    print("Olet alle 30v")

# onko age suurempi kuin 30
# tyypillisesti käytetään vertailuja
# jossa myös tasaluvut huomioidaan
if age >= 30:
    print("Olet 30v tai yli")

# onko age TASAN 30
if age == 30:
    print("Olet TASAN 30v")

# negaatio, eli ==:n täysi vastakohta
# eli "onko ikä jotain MUUTA kuin TASAN 30?"
if age != 30:
    print("Olet jonkin muun ikäinen kuin tasan 30v!")
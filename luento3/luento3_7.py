# kysytään teksti käyttäjältä
drink = input("Mitä juomaa haluat ostaa?\n")

# tyypillinen "puumainen" rakenne, vain yksi näistä
# voi kerrallaan käynnistyä
# mikä on loogista, koska juoma olla esim. mehu ja kahvi yhtä aikaa
if drink == "maito":
    print("Maidon hinta: 1.5 €")
elif drink == "kahvi":
    print("Kahvipaketin hinta: 8,99 €")
elif drink == "mehu":
    print("Mehutölkin hinta: 2.5 €")
else:
    print("Tuotetta ei löytynyt.")
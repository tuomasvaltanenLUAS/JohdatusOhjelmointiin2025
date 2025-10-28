# luodaan dictionary, sisältää yhden henkilön tiedot
person = {
    "name": "Herra Hakkarainen",
    "age": 47,
    "city": "Korvatunturi"
}

# dictionaryn kohdalla ei yleensä käytetä silmukkaa
# vaan tulostetaan se mitä halutaan suoraan avaimilla
print("Henkilön nimi:")
print(person["name"])

print("Henkilön ikä:")
print(person["age"])

# dictionaryssä sama sääntö, eli harvoin tulostetaan
# koko dictionary raakamuodossa (lähinnä debug-mielessä)
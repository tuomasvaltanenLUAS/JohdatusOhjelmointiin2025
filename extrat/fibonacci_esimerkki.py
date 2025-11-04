# Fibonaccin lukujonossa lasketaan yhteen kaksi edellistä lukua,
# ja siitä saadaan seuraava luku. Jonon 9 ensimmäistä numeroa ovat:
# 0, 1, 1, 2, 3, 5, 8, 13, 21

# TEHTÄVÄNANTO: kysytään käyttäjältä numero, eli kuinka monennen
# Fibonaccin luvun hän haluaa nähdä, ja sen jälkeen lasketaan
# tämä luku for-silmukalla

# Fibonaccissa luku on aina kahden edellisen summa:
# 0, 1, 1, 2, 3, 5, 8, 13, 21
# tämän takia esim.
# 5. luku on 1 + 2 = 3
# 6. luku on 2 + 3 = 5
# 7. luku on 3 + 5 = 8
# 8. luku on 5 + 8 = 13
# x. luku on vanha + uusi = fibonaccin luku

# pidetään näissä muuttujissa kirjaa
# mikä on laskukaavan vanha ja uusi luku
# ensimmäiset kaksi lukua ovat 0 ja 1
old_number = 0
new_number = 1

# annetaan jokin alkuarvo fibonaccille,
# tämä ajetaan silmukassa myöhemmin yli
# fibonaccin luku alussa on 1
fibonacci = 1

# kysytään käyttäjältä monesko luku halutaan, int
choice = input("Monennenko Fibonaccin luvun haluat nähdä?\n")

# pitää ottaa 2 pois kierrosten määrästä, koska fibonaccin
# kaksi ensimmäistä lukua ovat jo alussa tiedossa
# "old_number" ja "new_number" -muuttujat
choice = int(choice) - 2

# for-silmukka joka laskee niin kauan uutta Fibonaccin
# lukua kuin choice-muuttuja määrää

for number in range(choice):
    print("Uusi kierros alkaa!")

    # päivitetään fibonacci tälle kierrokselle
    # ja tulostetaan tekstiä joka näyttää tämän hetkisen tilanteen
    fibonacci = old_number + new_number
    print(f"Fibonacci nyt: {old_number} + {new_number} = {fibonacci}")

    # päivitetään old_number ja new_number
    # alkuperäinen new_umber on nyt old_number
    # ja tämänhetkinen fibonacci on uusi new_number
    old_number = new_number
    new_number = fibonacci

    print(f"Tämän kierroksen jälkeen: vanha luku = {old_number}, uusi luku = {new_number}\n")

print(f"Fibonaccin luku = {fibonacci}")
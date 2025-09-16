# pyydetään käyttäjältä numero
# HUOM! jos vertaat numeroja toisiinsa muuttujissa
# huolehdi että molemmat ovat numeerisessa muodossa (int/float)
number1 = input("Anna jokin numero:\n")
number1 = int(number1)

# tämä on jo valmiiksi int-muodossa
number2 = 234

# verrataan numeromuuttujia toisiinsa
# HUOM! jos toinen näistä on unohtunut tekstimuotoon
# tulee outoja bugeja...
if number1 > number2:
    print("Käyttäjän antama numero on suurempi!")
else:
    print("Toinen numero on suurempi...")
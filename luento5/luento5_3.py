# alkuperäinen teksti
text = input("Syötä tekstiä:\n")

# tekstin pituus saadaan kätevästi len()-funktiolla
text_length = len(text)
print(f"Tekstissä merkkejä: {text_length} kpl")

# text_length on ihan vain kokonaislukumuuttuja (int)
# voidaan käyttää miten halutaan
if text_length > 30:
    print("Pitkä lause!")

    # liian pitkä lause, lyhennetään että mahtuu otsikkoon paremmin
    shortened = text[0:30] + "..."
    print(shortened)
else:
    print("Lyhyt lause...")

# lasketaan pienet a-kirjaimet tekstistä
# HUOM! ohjelmoinnissa pienet ja isot kirjaimet ovat eri kirjaimia

# LISÄTÄÄN MYÖHEMMIN: lisätään myös ominaisuus jossa A + a tulee samaan laskuun
a_letters = text.count("a")
print(f"Tekstissä a-kirjaimia: {a_letters} kpl")

# erikoistapaus, joskus on tarve tarkistaa onko teksti tyhjä
# esim. käyttäjä syötti tyhjän tekstin
if text_length == 0:
    print("Teksti on tyhjä!")
else:
    print("Teksti ei ole tyhjä...")
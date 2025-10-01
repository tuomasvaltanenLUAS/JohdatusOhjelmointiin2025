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
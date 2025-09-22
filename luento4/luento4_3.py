# opiskelijat saa 50% alennusta
# muut asiakkaat maksavat täyden hinnan + palvelumaksu 2.5€
# paitsi jos lipun hinta on yli 100 €, silloin ei palvelumaksua

# vaihe 1: kysytään tarvittavat muuttujat, muutetaan hinta desimaaliksi
status = input("Opiskelija vai aikuinen? (o/a)\n")
price = input("Lipun alkuperäinen hinta:\n")
price = float(price)

# vaihe 2: muutetaan hintaa vaadittavan logiikan mukaisesti (ks. ylempää)

# jos opiskelija, silloin 50% alennus
if status == "o":
    price = price * 0.5
elif status == "a":
    # JOS aikuinen, lisätään palvelumaksu 2.5€
    # PAITSI jos summa on yli 100€, ei palvelumaksua
    if price < 100:
        price = price + 2.5

# oli hinta mikä tahansa (ylläolevien ehtolauseiden vuoksi)
# pyöristetään ja tulostetaan lopullinen hinta
price = round(price, 2)
print(f"Lopullinen hinta: {price} €")

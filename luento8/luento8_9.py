# esimerkki, jossa listojen näppäryys näkyy loistavasti
# HUOM! ei yhtään ehtolausetta tai silmukkaa
grades = [5, 8, 7, 9, 10, 7, 8, 6, 10, 9]

# keskiarvon määritelmä on tämä:
# lukujen summa / lukujen määrällä
total = sum(grades)
amount = len(grades)

# lasketaan keskiarvo
average = total / amount
average = round(average, 2)
print(average)
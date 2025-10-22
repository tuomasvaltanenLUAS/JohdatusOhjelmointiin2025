# laskurimuuttuja while-silmukkaa varten
counter = 1

print("Aloitus!\n")

while counter <= 10:
    print(counter)

    # counteria pitää kasvattaa itse, koska muutoin ehto ei täyty
    # koskaan tässä tapauksessa (koska counter olisi ikuisesi 1)
    counter = counter + 1

print("\nKIITOS OHJELMAN KÄYTÖSTÄ! OHJELMAN LOPETUS")


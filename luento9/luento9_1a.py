# kokoelmat kokoelman sisällä, esim. lista
temp_day_1 = [13.5, 16.4, 11.6, 11.3]
temp_day_2 = [12.1, 15.2, 11.9, 10.4]
temp_day_3 = [15.3, 17.6, 12.5, 11.6]

temperatures = [temp_day_1, temp_day_2, temp_day_3]

# suoraan tulostaminen ei ole muutoin kuin testimielessä hyödyllistä
# koska tätä formaattia ei tavallinen käyttäjä oikein pysty hahmottamaan
# yleensä tällä vain katsotaan nopeasti että tuleehan jotain dataa läpi
# print(temperatures)

# muistisääntö: jos on lista, joka koostuu listoista
# tarvitaan silmukka, jonka sisällä on silmukka
# esim. for-silmukka => sisällä toinen for-silmukka

# silmukoidaan kaikista lämpötiloista yksi päivä kerrallaan
for day in temperatures:
    print(f"Vaihdetaan päivää!")

    # käsitellään tämänhetkisen päivän jokainen lämpötila
    for temperature in day:
        print(temperature)

    print()
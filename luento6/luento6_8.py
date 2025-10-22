# tehdään ensin päätason silmukka
for x in range(3):
    print(f"PÄÄSILMUKKA: x = {x}")

    # alisilmukka, tämä ajetaan kokonaisuudessaan 3 kertaa
    # alisilmukka taas ajaa oman koodinsa 5 kertaa
    # kaikkiaan koodi ajaa silmukoissa sisältöä 3 * 5 = 15 kertaa
    for y in range(5):
        print(f"\t\talisilmukka: y = {y}")
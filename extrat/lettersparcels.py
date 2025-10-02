# miten lasketaan painosta kerroin
# jonka pohjalta voidaan laskea kirjeen
# paino

# tämä on pieni osa tehtävästä 3-7,
# mutta tässä tehtävässä tarvitsee vielä huomattavasti
# monimutkaisemman if-lauserakenteen, joka ottaa huomioon
# eri laskentalogiikan kirjeille (+ kaikki eri painoluokat)
# sekä paketeille (+ kaikki eri painoluokat)
weight = 374
choice = "kirje"
basic_fee = 0.5

# tämä versio huolehtii vain kirjeistä, jotka ovat painovälillä 200-500
if choice == "kirje":
    # esim. jos 200-500, 4snt per täyttä 100g
    # // jakaa siten ettei jää desimaaleja, eli kokonaiset luvut
    multiplier = weight // 100
    price = multiplier * 0.04 + basic_fee
    print(f"{price} €")
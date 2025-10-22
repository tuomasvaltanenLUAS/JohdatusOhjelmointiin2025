# korkoa korolle -laskuri, silmukoilla, ei matemaattista kaavaa

# korkolaskuri
# vuosikorko 7%, kuinka paljon on rahaa tilillä 10v päästä?
# lisätään joka vuosi aina 2000 € lisää
start_money = 15000
yearly_money = 2000

# korkoprosentti, eli 7% korotus => 1.07
interest = 1.07

total = start_money

# tehdään silmukka, mikä käy kaikki vuodet, ja kasvattaa korkopottia sitä mukaa
for year in range(10):
    # lisätään joka vuoden alussa 2000€ tilille
    # jos halutaan että raha lisätään vasta vuoden lopussa
    # aseta tämä korkolaskun jälkeen
    total = total + yearly_money

    # lasketaan vuoden korko
    total = total * interest

# koko rahasumma lopuksi, sis. kaikki sijoitukset
total = round(total, 2)

# paljon tuli voittoa
new_money = total - start_money - (10 * yearly_money)

print(f"Rahaa tilillä 10v jälkeen: {total} €")
print(f"Tienattiin 10v jälkeen:: {new_money} €")
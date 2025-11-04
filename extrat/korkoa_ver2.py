# VERSIO 2 KORKOLASKURISTA, kokeile Python Tutor

# kuinka monta vuotta kestää, että pääsemme sijoituksilla tiettyyn voittoon
start_money = 15000
yearly_money = 2000

# korko+ per vuosi, 7%
interest = 1.07

# säästötavoite
target_savings = 150000

# apumuuttujat silmukkaa varten
total = start_money
winnings = 0

# vuodet, 1 -30
# aloitetaan 1:stä, jotta winnings-muuttujan
# laskukaava kertoo vuodet oikein (eikä esim. ensimmäisenä
# vuonna kerrota 0:lla)
for year in range(1, 31):
    # lisätään vuosittainen sijoitus
    total = total + yearly_money

    # korkoa korolle
    total = total * interest

    # paljon voittoa tähän mennessä
    # eli vähennetään kaikista rahoista sijoitukset
    winnings = total - start_money - (year * yearly_money)

    # tarkistetaan ollaanko jo tavoitteessa
    # jos ollaan => break -> koska ei ole enää syytä jatkaa koodia
    if winnings >= target_savings:
        print(f"Tavoitteeseen päästiin vuonna: {year}")
        break


# jos kävi niin, ettei päästy tavoitteeseen, ilmoitetaan käyttäjälle
if winnings < target_savings:
    print("Tavoite ei ole mahdollinen annetulla aikavälillä ja sijoituksilla.")
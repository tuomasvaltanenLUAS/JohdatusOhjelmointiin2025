# tyypillinen ohjausrakenne käyttäjälle
# monessa viikkotehtävässä
choice = input("Oletko opiskelija vai aikuinen? (a/o)\n")

# mitä käyttäjä syötti?
if choice == "o":
    print("Tämä koodi käsittelee opiskelijakohtaisen koodin...")
    print("Esim. jonku lipun hinnan laskeminen ym.")
elif choice == "a":
    print("Tähän sitten aikuisten laskentalogiikka.")
else:
    print("Valintaa ei tunnistettu. Käynnistä ohjelma uudelleen.")
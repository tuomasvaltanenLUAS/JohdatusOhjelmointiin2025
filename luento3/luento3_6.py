# kysytään käyttäjältä alennuskoodi
# ja katsotaan täsmääkö koodiin tallennettu alennuskoodi
# käyttäjän syöttämän koodin kanssa
sales_code = input("Anna alennuskoodi:\n")
current_code = "WINTER25"

# tekstidatan kanssa (string) yleensä käytetään vain == tai !=
# muiden ehtojen käyttämisessä ei ole järkeä, esim.
# "banaani" > "paloauto" ei tarkoita mitään
if sales_code == current_code:
    print("Olet oikeutettu alennukseen!")
else:
    print("Normaali hinta, ei alennusta.")
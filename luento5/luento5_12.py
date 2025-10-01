# Tämä esimerkki yhdistelee kaikkia, eli ehtolauseita, merkkijono-operaatioita
# sekä virheenkäsittelyä

# Tehdään ohjelma, joka tarkistaa, onko annettu asiakastunnus oikeassa muodossa
# esim. teleoperaattorin asiakastunnus tai vastaava ym.
# esimerkki asiakastunnuksesta: A1234_2345

# Logiikka: tunnus on aina tasan 10 merkkiä pitkä, ja kuudes merkki on aina alaviiva

# tehdään varmuudeksi try/except koko ohjelmalle, ettei tule varsinaista virhettä
# ja ettei ohjelma kaadu/tilttaa

try:
    client = input("Syötä asiakastunnus:\n")

    # otetaan annetun asiakastunnuksen pituus merkkeinä
    text_length = len(client)

    # tarkistetaan että tunnus on tasan 10 merkkiä pitkä
    if text_length != 10:
        print("Tunnus on väärän mittainen (vaaditaan 10 merkkiä tasan")
    elif client[5] != "_":
        print("Tunnuksesta puuttuu alaviiva (kuudes merkki).")
    else:
        print("Tunnus OK!")

        # otetaan osatekstillä tunnuksen alku- ja loppuosa irti
        identifier = client[0:5]
        order = client[6:10]
        order = int(order)

        # tulostetaan lopuksi osat
        print(identifier)
        print(order)

except Exception as e:
    # except ottaa lopuksi viimeistään kiinni, jos jokin menee pieleen
    print(f"Virhe: {e}")
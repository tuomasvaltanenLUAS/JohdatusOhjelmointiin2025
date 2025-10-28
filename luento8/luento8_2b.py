# tehdään lista tuotteista
products = ["Pölynimuri", "Kahvinkeitin", "Jääkaappi",
            "Pakastin", "Älypuhelin", "Kynnysmatto"]

# haetaan tuotteiden lukumäärä
# eli tässä tapauksessa 6 kpl
amount = len(products)

# silmukoidaan tuotelista perinteisellä rangella
# tuotteiden lukumäärän kanssa
for index in range(amount):
    item = products[index]
    print(f"{index + 1}: {item}")

# huom: älä laita len(products) suoraan rangen sisälle
# sillä monessa ohjelmointikielessä koodi silloin laskee
# listan sisällön lukumäärän niin monta kertaa kuin silmukka
# tekee kierroksia. esim. jos olisi 500000 tuotetta
# => koodi laskee listan koon 500000 kertaa
# mikä on turhaa, koska listan koko on joka kierroksella sama
# vertaa tätä esimerkki vastaavaan esimerkkiin
# toistolauseluennolla, jossa tehtiin tekstimuuttuja samalla tavalla lennosta

# tuotelista
products = ["Pölynimuri", "Kahvinkeitin", "Jääkaappi",
            "Pakastin", "Matkapuhelin", "Kynnysmatto"]

# alustetaan tyhjä tekstimuuttuja
text = ""

# silmukoidaan tuotteet läpi ja lisätään jokainen
# tuote vuorollaan tekstin jatkeeksi
for item in products:
    text = text + item + ", "


print(text)

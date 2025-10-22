# alustetaan tyhjä tekstimuuttuja, joka täytetään silmukassa
text = ""

# kokeile tätä myös Python Tutorissa!
for year in range(2019, 2025):
    text = text + str(year) + "-"

# poistetaan viimeinen merkki, ks. substring aiemmilta luennoilta
text = text[:-1]

# kun teksti on rakennettu, tulostetaan se lopuksi
print(text)
# 1. Tee ohjelma, joka tervehtii käyttäjää annetun kellonajan perusteella.
# Pyöristä käytettävä tuntitieto kokonaislukuun.
# Vastaa käyttäjälle seuraavan logiikan mukaisesti:

# Jos kellonaika on 05 - 11 : vastaa "Hyvää huomenta"
# Jos kellonaika on 12 - 17 : vastaa "Hyvää päivää"
# Jos kellonaika on 18 - 21 : vastaa "Hyvää iltaa"
# Jos kellonaika on 22 - 04 : vastaa "Hyvää yötä"

# Lisäominaisuus:
# Jos käyttäjä ei syötä mitään kellonaikaa, käytä automaattisesti tämänhetkistä
# kellonaikaa (esim. datetime-moduuli). Jos käyttäjä valitsi automaattisen kellonajan,
# ilmoita käyttäjälle "Valitaan tunti automaattisesti".

from datetime import datetime

# kysytään käyttäjältä tämänhetkinen tunti => integeriksi
hour = input("Syötä valitsemasi tunti:\n")

# JOS käyttäjä syötti tyhjän tekstin, korvataan
# tuntitieto datetime -moduulin avulla
if hour == "":
    timestamp = datetime.now()
    hour = timestamp.hour
    print(f"Tyhjä teksti! Valitaan tunti automaattisesti: {hour}")

# oli hour mikä tahansa, muutetaan se vihdoin kokonaisuluvuksi
hour = int(hour)

# tehdään ehtolauseet jokaiselle
# on makuasia haluaako korvata elsen vielä elif-lauseella
# joskus myös riippuu tilanteesta kumpi on parempi
if 5 <= hour <= 11:
    print("Hyvää huomenta!")
elif 12 <= hour <= 17:
    print("Hyvää päivää!")
elif 18 <= hour <= 21:
    print("Hyvää iltaa!")
else:
    print("Hyvää yötä...")








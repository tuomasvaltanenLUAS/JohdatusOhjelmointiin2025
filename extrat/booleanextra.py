# KOODIN VAATIMUKSET:

# Tehdään ohjelma, joka päättelee muuttujista, onko ulkona HYVÄ vai HUONO sää
# Sään logiikka on tämä:
# Huono sää: jos lämpötila on alle +10 C
# Huono sää: jos kosteusprosentti on yli 80 %
# Huono sää: jos tuulennopeus on yli 2.5 (m/s)
# Huono sää: jos ulkona on pimeää
# Tässä tapauksessa ulkona on pimeää, jos klo on joko 20-24 tai 0-7

# alustetaan apu-boolean, jonka ainut tehtävä on pitää kirjaa siitä
# onko ulkona hyvä vai huono sää
good_weather = True

# muuttujat, joiden pohjalta pitää päätellä onko hyvä vai huono sää.
# kokeile muuntaa arvoja, jotta voit testata kuinka eri ehdot
# vaikuttavat koodin boolean-ehdon toimintaan
temperature = 15
humidity = 48
wind_speed = 1.7
time = 17

# apumuuttujat:
sun_down = 20
sun_rises = 7

# ehtolause, jolla yritetään ratkaista tehtävän ongelma
# yhdellä if-lauseella alkaa mennä melko monimutkaiseksi tämä ehdon rakentaminen...???
# if temperature < 10 or humidity > 80 or wind_speed > 2.5 or (time > sun_down or ... )

# Huono sää: jos lämpötila on alle +10 C
# Huono sää: jos kosteusprosentti on yli 80 %
# Huono sää: jos tuulennopeus on yli 2.5 (m/s)
# Huono sää: jos ulkona on pimeää

# Boolean-muuttujan idea on tämä: aloitetaan oletuksesta että sää on hyvä (good_weather = True)
# tämän jälkeen yritetään todistaa booleanin tilanne vääräksi, YKSI EHTO KERRALLAAN

# ehto 1: lämpötila
if temperature < 10:
    good_weather = False

# ehto 2: kosteusprosentti
if humidity > 80:
    good_weather = False

# ehto 3: tuulennopeus
if wind_speed > 2.5:
    good_weather = False

# ehto 4: kellonaika
if time > sun_down or time < sun_rises:
    good_weather = False

# jos nyt tulisi muutoksia ohjelmaan, voisimme vain koodata
# lisää ehtolauseita tähän alle

# kun kaikki ehdot on käyty läpi, katsotaan lopuksi tilanne
# mikä on good_weather -muuttujassa
# jos halutaan reagoida booleanin vastaiseen tilanteeseen:
# kokeile => if not good_weather
if good_weather:
    print("Hyvä sää!")
else:
    print("Huono sää...")

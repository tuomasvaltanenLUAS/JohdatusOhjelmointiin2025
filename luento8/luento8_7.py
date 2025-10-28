# KOKEILE TÄTÄ PYTHON TUTORISSA

# lista kaupunkeja
cities = ["oulu", "turku", "rovaniemi", "helsinki", "tampere", "pori"]

# tehdään kaksi uutta tyhjää listaa tai "ämpäriä" valmiiksi
# pitkille ja lyhyille kaupungin nimille oma lista
long_cities = []
short_cities = []

# käydään läpi kaupungit yksitellen/vuorotellen
# ja asetetaan jokainen kaupunki JOKO pitkään tai lyhyeen
# kaupungin nimen listaan
for city in cities:
    if len(city) < 6:
        short_cities.append(city)
    else:
        long_cities.append(city)


# tulostetaan testimielessä sisällöt
print("Pitkät kaupungin nimet:")
print(long_cities)
print()

print("Lyhyet kaupungin nimet:")
print(short_cities)
print()
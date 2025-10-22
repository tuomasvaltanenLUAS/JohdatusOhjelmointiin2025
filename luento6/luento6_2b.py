# apumuuttujat silmukan range():a varten
# aloitus- ja lopetusarvot
start = 2019
end = 2025

# voidaan myös määritellä alku ja loppu valituille kierrosluvuille
# kolmas parametri => step size, eli voidaan hypätä joidenkin arvojen yli
for year in range(start, end, 2):
    print(year)
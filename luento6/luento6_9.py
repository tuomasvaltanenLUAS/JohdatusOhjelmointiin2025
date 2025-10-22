# tätä kannattaa kokeilla myös Python Tutorissa!
print("Ajetaan tilausraportti:\n")

# idea on tämä: meillä on x-määrä tilauksia
# ja jokaisessa tilauksessa on y-määrä tuotteita
# voisi olla myös kolmitasonen
# osasto -> tilaus -> tuote
for order in range(3):
    print(f"KÄSITELLÄÄN TILAUSTA nro = {order + 1}")

    # käsitellään TÄMÄNHETKISEN TILAUKSEN tuotteet
    for product in range(5):
        print(f"\tKäsitellään tilauksen {order + 1} tuotetta {product + 1}")

print(f"\nRaportti valmis, kiitos ohjelman käytöstä!")
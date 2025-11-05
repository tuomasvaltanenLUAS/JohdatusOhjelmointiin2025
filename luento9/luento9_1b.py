# tuotteet omissa kategorioissaan
books = ["Da Vinci Code", "Taru sormusten herrasta", "Light Fantastic"]
movies = ["Jurassic Park", "Interstellar", "Forrest Gump"]

# kaikki verkkokaupan tuotteet ovat omina listoinaan tässä päälistassa
products = [books, movies]

# kannattaa kokeilla tätä myös Python Tutorissa!

# silmukoidaan kategoriat läpi
for category in products:

    # ... ja sitten silmukoidaan tämän hetkisen / aktiivisen
    # kategorian kaikki tuotteet
    for item in category:
        print(item)
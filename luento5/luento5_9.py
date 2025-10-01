# otetaan hallitusti koppi mahdollisesta virhetilanteesta
# esim. jos käyttäjä syöttää numeron sijasta tekstiä (esim. postilaatikko)
try:
    number = input("Anna numero:\n")
    number = int(number)
    number = number * 2
    print(f"Numerosi on: {number}")
except ValueError:
    # exceptin takia, voimme itse tulostaa vikatilanteesta viestin
    # eikä ohjelma varsinaisesti tilttaa/kaadu punaisen virheen myötä
    print("Syötit tekstiä, käynnistä ohjelma uudelleen!")

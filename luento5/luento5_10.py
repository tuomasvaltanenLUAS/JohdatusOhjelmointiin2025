# otetaan hallitusti koppi mahdollisesti virhetilanteesta
# esim. jos käyttäjä syöttää numeron sijasta tekstiä, esim. postilaatikko
try:
    number = input("Anna numero:\n")
    number = int(number)
    number = 100 / number
    print(number)
except ValueError:
    # exceptin takia, voimme itse tulostaa vikatilanteesta viestin
    # eikä ohjelma varsinaisesti tilttaa/kaadu punaisen virheen myötä
    print("Syötit tekstiä. Käynnistä ohjelma uudelleen!")
except ZeroDivisionError:
    # tämä except ottaa huomioon nollalla jakamisen
    # koska ValueError ei ota sitä kiinni (koska 0 on aivan OK kokonaisluku!)
    print("Nollalla ei voi jakaa, syötä jokin muu kokonaisluku.")
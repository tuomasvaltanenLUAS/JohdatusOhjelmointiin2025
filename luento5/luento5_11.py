# otetaan hallitusti koppi mahdollisesti virhetilanteesta
# esim. jos käyttäjä syöttää numeron sijasta tekstiä, esim. postilaatikko
try:
    number = input("Anna numero:\n")
    number = int(number)
    number = 100 / number
    print(number)
except Exception as e:
    print(f"Virhe: {e}")
    print("Ohjelman käytössä tapahtui odottamaton virhe.")
    print("Ota yhteyttä tekniseen ylläpitoon.")

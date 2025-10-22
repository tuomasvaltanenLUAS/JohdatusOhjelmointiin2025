print("Aloitus!")

# myös if-lauseita voidaan käyttää silmukassa
# tässä tapauksessa joka toinen kierros on parillinen
# ja joka toinen on pariton luku
for x in range(10):
    if x % 2 == 0:
        print(f"Parillinen! -> {x}")
    else:
        print(f"Pariton!\t-> {x}")

print("Lopetus!")
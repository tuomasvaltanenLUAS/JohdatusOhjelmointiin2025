print("Aloitetaan!")

# silmukka, joka lopetetaan
# ennenaikaisesti break-komennon avulla
for x in range(10):
    # jos x on tasan 6 ==> skipataan kierros ja
    # jatketaan seuraavasta
    if x == 6:
        print("Skipataan data, viallinen muoto!")
        continue

    print(x)

print("Valmis!")
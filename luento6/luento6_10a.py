print("Aloitetaan!")

# silmukka, joka lopetetaan
# ennenaikaisesti break-komennon avulla
for x in range(10):
    # jos x on tasan 6 ==> katkaistaan silmukan toiminta
    if x == 6:
        print("Data löytyi, lopetetaan etsintä!\n")

        # break lopettaa silmukan ajon välittömästi
        # joten jos halutaan tulostaa jotakin ennen sitä
        # on hyvä muistaa tämä (sama koskee continue:ta)
        break

    print(x)

print("Valmis!")
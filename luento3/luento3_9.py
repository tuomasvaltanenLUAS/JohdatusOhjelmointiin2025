number = input("Syötä numero:\n")
number = int(number)

# klassikko: onko tietty luku parillinen vai pariton
if number % 2 == 0:
    print("Parillinen luku!")
else:
    print("Pariton luku...")
# kysytään käyttäjältä kierrosten lukumäärä
cycles = input("Montako lukua kysytään?\n")
cycles = int(cycles)

total = 0

# kysytään käyttäjältä niin monta lukua kuin hän halusi
for x in range(cycles):
    number = int(input("Anna numero: "))
    total = total + number

print(total)
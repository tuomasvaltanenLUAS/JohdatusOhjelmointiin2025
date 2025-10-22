# alustetaan total muuttuja ennen silmukkaa
total = 0

# tällainen rakenne on nopea ylläpitää
# koska lukumäärää on helppo muuttaa
for x in range(10):
    number = int(input("Anna numero: "))
    total = total + number

# tulostetaan lopputulos
print(total)
choice = input("Opiskelija vai aikuinen? (o/a):\n")

# ennen kuin vertaillaan mitä käyttäjä syötti
# muutetaan käyttäjän syöttämä kirjain pieneksi
# tämän avulla ei tarvitse erikseen if-lauseissa testata
# isoja kirjaimia (esim. if choice == "o" or choice == "O":)
choice = choice.lower()

# nyt vertailun pitäisi toimia sekä isoilla että pienillä kirjaimilla
if choice == "o":
    print("Opiskelija!")
elif choice == "a":
    print("Aikuinen!")
else:
    print("Väärä valinta...")
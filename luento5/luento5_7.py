# käyttäjän syöte
text = input("Anna numero tai tekstiä:\n")

# jos haluaa käyttää desimaaliarvoja
# voidaan ottaa piste pois ennen if-lausetta
# text_new = text.replace(".", "")

# sama asia kuin if text.isnumeric() == True:
# ohjelmassa on nyt kaksi haaraa riippuen siitä
# syöttikö käyttäjä tekstiä vai numeron
# ERITTÄIN HYVÄ LÄHTÖKOHTA LISÄTEHTÄVÄSSÄ 4-7
if text.isnumeric():
    print("Annoit numeron!")

    # tässä tilanteessa voimme olla varmoja, että text on numero
    number = int(text)
    number = number * 2
    print(number)
else:
    print("Annoit tekstiä!")
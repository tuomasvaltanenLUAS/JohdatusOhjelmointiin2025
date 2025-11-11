# functions.py, kaikki omat funktiot
# tänne, ikään kuin "työkalupakki", jossa
# kaikki omat funktiot ovat valmiina
# käytettäväksi muissa ohjelmissa

# määritellään oma funktion nimeltä
# show_text()

# HUOM: oma funktio ei tee koodissa mitään
# ennen kuin sitä kutsutaan/käytetään jossakin'

# funktion määritelmä tarkoittaa sitä, että:
# "mitä koodin tulisi tehdä, jos jokin kutsuisi tätä funktiota"
def show_text():
    print("Tervetuloa ohjelman käyttäjäksi!")
    print("--------------------------------")
    print("Seuraa ohjeita!")
    print()


# funktio joka tulostaa koko nimen ja iän
# PARAMETRIEN avulla
def combine_text(first, last, age):
    print(f"Tervetuloa: {first} {last}!")
    print(f"Ikäsi on: {age} vuotta.")


# funktio joka palauttaa return-komennolla tietoa
# takaisin palautusarvona
def get_year():
    year = 2025
    return year


# funktio, joka päättelee annetusta numerosta
# onko kyseessä parillinen vai pariton luku
def get_even_number_text(number):
    if number % 2 == 0:
        return "Parillinen"
    else:
        return "Pariton"


# apufunktio, joka laskee tunneista
# päivien lukumäärän
def hours_to_days(hours):
    result = hours // 24
    return result


# apufunktio, joka kääntää tekstin toisinpäin
def reverse_string(text):
    return text[::-1]


# apufunktio, joka tarkistaa onko
# annettu teksti palindromi vai ei
def check_palindrome(text):
    # kutsutaan toista omaa funktiota
    reversed_text = reverse_string(text)

    # tarkistetaan onko käyttäjän teksti palindromi
    # ja palautetaan tilanteesta riippuen Boolean
    # (True tai False)
    if text == reversed_text:
        return True
    else:
        return False



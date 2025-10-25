from colorama import Fore, Back, Style

# kysytään käyttäjältä luku
number = input("Anna jokin numero:\n")
number = int(number)

# reagoidaan värillä riippuen siitä
# onko numero positiviinen vai negatiivinen
if number >= 0:
    print(Fore.BLACK + Back.LIGHTGREEN_EX + "Positiivinen luku!")
else:
    print(Fore.BLACK + Back.LIGHTRED_EX + "Negatiivinen luku...")
# muista asentaan ensin colorama, ks. ohje Moodlessa
from colorama import Fore, Back, Style

# muutetaan tekstin väri
print(Fore.CYAN + 'Eri väristä tekstiä!')
print("Lisää tekstiä samalla värillä.")

# muutetaan taustaväri valkoiseksi
print(Back.LIGHTWHITE_EX + 'Eri taustavärikin!')

# palautetaan kaikki normaaliksi
print(Style.RESET_ALL)
print('Nyt ollaan taas normaalissa tilassa!')
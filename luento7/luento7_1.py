from colorama import Fore, Back, Style

print(Fore.CYAN + 'Eri väristä tekstiä!')
print(Back.LIGHTWHITE_EX + 'Eri taustavärikin!')

# palautetaan kaikki normaaliksi
print(Style.RESET_ALL)
print('Nyt ollaan taas normaalissa tilassa!')
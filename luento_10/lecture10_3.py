from functions import *

# kysytään käyttäjältä numero
value = input("Syötä jokin numero:\n")
value = int(value)

# kutsutaan apufunktiota, joka päättelee
# onko numero pariton vai parillinen
result = get_even_number_text(value)
print(result)
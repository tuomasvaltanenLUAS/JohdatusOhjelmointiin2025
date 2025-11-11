# sama logiikka mutta omalla funktiolla
# huomaa yksinkertaisempi rakenne koodissa
from functions import *

numbers = [1, 5, 3, 6, 2, 8, 9]
grades = [5, 4, 5, 2, 3, 4, 1]
temperatures = [5.6, 4.7, 3.6, 7.6, 5.7]

# keskiarvo 1
average = get_list_average(numbers)
print(average)

# keskiarvo 2
average = get_list_average(grades)
print(average)

# keskiarvo 3
average = get_list_average(temperatures)
print(average)
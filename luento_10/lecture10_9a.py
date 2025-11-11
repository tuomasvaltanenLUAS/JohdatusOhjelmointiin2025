# esimerkki koodista, jossa on toistuvaa rakennetta
# jonka voisi asettaa funktioon
numbers = [1, 5, 3, 6, 2, 8, 9]
grades = [5, 4, 5, 2, 3, 4, 1]
temperatures = [5.6, 4.7, 3.6, 7.6, 5.7]

# huomaa kuinka sama logiikka toistuu, vain
# muuttujat välissä muuttuu!
numbers_total = sum(numbers)
numbers_amount = len(numbers)
average_number = numbers_total / numbers_amount
print(f"ka, numerot: {round(average_number, 2)}")

grades_total = sum(grades)
grades_amount = len(grades)
average_grade = grades_total / grades_amount
print(f"ka, arvosanat: {round(average_grade, 2)}")

temperatures_total = sum(temperatures)
temperatures_amount = len(temperatures)
average_temperature = temperatures_total / temperatures_amount
print(f"ka, lämpötilat: {round(average_temperature, 2)}")
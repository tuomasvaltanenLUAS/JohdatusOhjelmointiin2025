from functions import *

word = input('Anna jokin sana:\n')

# käytetään omaa funktiota tarkistamaan
# onko teksti palindromi vai ei
palindrome = check_palindrome(word)

# funktion tuloksen pohjalta
# => ilmoitetaan käyttäjälle onko palindromi vai ei
if palindrome:
    print("Palindromi!")
else:
    print("Ei ole palindromi...")
# ESIMERKKI: miten tunnistetaan käyttäjän valitsema sana
# siten, ettei se ole osana toista sanaa
# esim. jos käyttäjä valitsee sanan "papu"
# silloin koodin ei pitäisi reagoida sanaan "kahvipapu" jne jne

# word = "papu"
word = input("Anna etsittävä sana:\n")
word = f" {word} "

# koodin pitäisi tulostaa "löytyi" vain silloin
# kun seasta löytyy "papu" sellaisenaan, mutta jos osana
# yhdyssanaa -> skipataan
text = "Kahvipapu, papu, papupata, testilause"
original_text = text

# muutetaan pisteet ja pilkut välilyönneiksi, koska muuten
# koodi ei tunnista sanaa, jos se on pisteen tai pilkun vieressä
text = text.replace(".", " ")
text = text.replace(",", " ")
text = " " + text + " "
print()

# löytyikö sana lauseesta
if word in text:
    print(f'Sana "{word.strip()}" löytyi lauseesta:')

else:
    print(f'Sanaa "{word.strip()}" EI LÖYTYNYT lauseesta:')

print(f'"{original_text}"')
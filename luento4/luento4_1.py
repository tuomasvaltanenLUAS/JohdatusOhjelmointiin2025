# helppo tapa, jolla vertailla lukuvälejä
# mutta tarkista aina kaikki vertailut
# että ne ovat oikein, ERITYISESTI RAJA-ARVOT!

# tehdään esimerkki, jossa koodi tunnistaa
# vuosikymmenen, sekä kuvaa sitä lempinimellä

# kysytään käyttäjältä vuosiluku
year = input("Syötä vuosiluku:\n")
year = int(year)

# verrataan vuosiraja-arvoihin
if 1980 <= year < 1990:
    print("Kasari! (1980-1990)")
elif 1990 <= year < 2000:
    print("Ysäri! (1990-2000)")
elif 2000 <= year < 2010:
    print("Nollari! (2000-2010)")
else:
    print("Jokin muu vuosikymmen...")

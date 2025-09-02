# VAIHE 1: pyydetään käyttäjältä inputilla tarvittavat tiedot

# kysytään käyttäjältä säästöt ja muutetaan desimaaliluvuksi
# HUOM: \n on kätevä inputin kanssa => saadaan käyttäjän vastaus
# omalle rivilleen!
savings = input("Kuinka paljon sinulla on säästöjä?\n")
savings = float(savings)
print()

# kysytään käyttäjältä myös viime kuun palkka, ja muutetaan desimaaliksi.
# jos haluat hieman lyhyemmän koodin, myös tämä on OK
# salary = float(input("Anna luku:\n"))
salary = input("Kuinka paljon sait tässä kuussa palkkaa?\n")
salary = float(salary)
print()

# VAIHE 2: ohjelman laskukaava / logiikka
# korkokerroin, +5%
increase = 1.05

# lasketaan lopputulos
total = (savings + salary) * increase

# VAIHE 3: tulostetaan lopputulos mukavassa muodossa
# loppukäyttäjälle / asiakkaalle
# teknisesti on mahdollista tehdä aaltosulkeiden sisällä myös laskutoimituksia
# esim. {total * increase}, mutta lähtökohtaisesti nämä ratkaisu ovat
# aika vaikeaselkoisia, koska koodi ahtaa kaiken logiikan yhteen koodiriviin
print(f"Uusi summa korkojen jälkeen: {total} €")
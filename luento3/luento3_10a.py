number = input("Syötä numero:\n")
number = int(number)

# jos numero on suurempi kuin 0
# JA SAMAAN AIKAAN
# numero on pienempi kuin 30
# eli toisin sanoen, onko numero välillä 0-30
if number > 0 and number < 30:
    print("Numero on 0 ja 30 välillä (eli suurempi kuin 0, pienempi kuin 30)")

if number < 0 or number > 30:
    print("Numero on rajojen ulkopuolella (eli joko alle 0 tai yli 30)")

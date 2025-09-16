number = input("Syötä numero:\n")
number = int(number)

# jos numero on suurempi kuin 0
# JA SAMAAN AIKAAN
# numero on pienempi kuin 30
# eli toisin sanoen, onko numero välillä 0-30

# tämä tyyli on nykyään suositeltu tapa Pythonissa (vrt. mitä matematiikassa tehdään!)
if 0 < number < 30:
    print("Numero on 0 ja 30 välillä (eli suurempi kuin 0, pienempi kuin 30)")
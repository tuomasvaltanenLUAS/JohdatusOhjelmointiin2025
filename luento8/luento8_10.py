berries = ["Mustikka", "Mansikka", "Puolukka", "Hilla", "karpalo"]
print(berries)

# jos on tarkoitus sortata data ennen silmukkaa
# aja sort() vain kerran ennen silmukkaa, koska muutoin
# koodi järjestää datan useita kertoja aakkosjärjestykseen
# ja vain yksi kerta riittää

# sort() -> järjestää alkuperäisen listan aakkosjärjestykseen
# berries.sort()
# print(berries)

# sorted() => tekee uuden kopion listasta, jolloin
# jää alkuperäinen lista ja sortattu lista talteen samalla kertaa
# sorted_berries = sorted(berries)
# print(sorted_berries)

# jotta koodi toimii myös pienillä ja isoilla alkukirjaimilla
# käytetään lambdaa siihen että muutetaan vertailun ajaksi
# kaikki kirjaimet ISOIKSI
berries.sort(key=lambda v: v.upper())
print(berries)
# alkuperäinen teksti
text = input("Syötä tekstiä:\n")

# osateksti, ensimmäisestä merkistä kymmenenteen merkkiin
subtext1 = text[0:10]
print(subtext1)

# osateksti, kuudennesta merkistä viidenteentoista merkkiin
subtext2 = text[5:15]
print(subtext2)

# osateksti, viimeiset viisi merkki
subtext3 = text[-5:]
print(subtext3)

# osateksti, kaikki teksti viidennen merkin jälkeen
subtext4 = text[5:]
print(subtext4)
print()

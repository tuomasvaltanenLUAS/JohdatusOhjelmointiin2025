# alkuperäinen teksti
text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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

# joskus on tarve poistaa AINOASTAAN viimeinen merkki tekstistä
# joskus kun dataa tulee esim. tietokannasta, tämä on näppärä temppu
years = "2020,2019,2018,2017,2016,2015,2014,"
years = years[0:-1]
print(years)

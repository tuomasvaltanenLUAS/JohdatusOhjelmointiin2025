# testimuuttujat
humidity = 92
temperature = 7
raining = False

# jos kosteusprosentti on yli 80% => raining = True
if humidity > 80:
    raining = True

# jos on pakkasta, ei ole kyse enää sateesta
if temperature < 0:
    raining = False

# tässä välissä voisi olla kymmeniä tai jopta satoja
# rivejä koodia, joka säätää raining-muuttujaa suuntaan tai toiseen
# riippuen tilanteesta

# ... oli koodia kuinka paljon tahansa, loppuosio on aika lailla aina sama
# if raining on sama kuin if raining == True
# if not raining on sama kuin if raining == False
if raining:
    print("Sataa vettä.")
else:
    print("Ei sada.")
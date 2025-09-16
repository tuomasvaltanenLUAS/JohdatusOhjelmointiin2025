# muuttujat kokonaishinnan laskemista varten
# nämä voisi kysyä myös käyttäjältä / input
price = 200
age = 25

# HUOM: ehtolauseessa voidaan muokata aiempaa ylätason
# muuttujaa näppärästi ehtolauseesta käsin
if age < 18:
    # jos ikä alle 18v, päivitetään alkuperäinen hinta siten
    # että 10% alennus ja ei postikuluja
    price = price * 0.9
else:
    # muussa tapauksessa (eli 18v tai yli) => normaali hinta + postikulut
    price = price + 4.95

# eli huomaa kuinka price -muuttuja elää tuolla if-elsessä
# riippuen tilanteesta. voimme joka tapauksessa
# lopuksi tulostaa ehtolauseen jälkeen price-muuttuja
# huolimatta sen arvosta
print(f"Loppusumma: {price} €")
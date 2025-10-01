# juomavalikoima tekstissä
drinks = "mehu, maito, kahvi, tee, mehu"
print(drinks)

# oletuksena replace() korvaa KAIKKI sanat mitkä löytyy
# jos käytetään drinks.replace("mehu", "vichy")
# jos haluat korvata esim. vain ensimmäisen, kokeile:
# drinks = drinks.replace("mehu", "vichy", 1)
drinks = drinks.replace("mehu", "vichy")
print(drinks)
print()

# voidaan myös vaihtaa pilkut rivinvaihdoiksi
new_drinks = drinks.replace(", ", "\n")
print(new_drinks)

# jos haluat poistaa tekstistä ylimääräiset välilyönnit,
# muista strip() -funktio


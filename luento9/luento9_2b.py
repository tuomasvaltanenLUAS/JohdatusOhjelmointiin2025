# esimerkki, lista dictionaryn sisällä
book = {
    "name":  "My Lady Jane",
    "year":  2016,
    "authors": ["Cynthia Hand", "Brodi Ashton", "Jodi Meadows"]
}

# jos halutaan yksittäinen kirjoittaja, käytetään indeksiä
# tapa 1: käytetään apumuuttujia
authors = book['authors']
first_author = authors[0]
print(first_author)

# tapa 2: suoraan voi myös ketjuttaa => authors -> ensimmäinen indeksi
print(book['authors'][0])
print()

# jos halutaan kaikki kirjailijat käydä läpi, käytetään koko listaa
for author in book['authors']:
    print(author)
codes = ["TILAUS12345_X3567_2025", "TILAS1242353_X743783246782_2023",
        "ASUDYSIDHSAJKFHDGSYUAGDSADGSHA_LA567834678324I_2021"]

# split():n etu siinä
# että ei ole väliä missä kohdin tekstiä alaviivat (tai muut erotinmerkit) ovat
for code in codes:
    # halkaistaan tämänhetkinen koodi
    # listaksi alaviivan perusteella
    # kunhan jokaisessa tilauskoodissa on kaksi alaviivaa
    parts = code.split("_")

    # puretaan parts-lista muuttujiin
    first = parts[0]
    second = parts[1]
    year = parts[2]

    # tulostetaan tiedot
    print(first)
    print(second)
    print(year)
    print()
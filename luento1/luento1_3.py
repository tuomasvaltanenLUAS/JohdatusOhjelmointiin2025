# muuttujia yleensä yhdistellään eri laskutoimituksiin
salary = 3100
savings = 1850
debt = 400

# lasketaan summa edellisten muuttujien avulla
total_money = salary + savings - debt
print(total_money)

# tehdään tekstimuuttuja
name = "Testi Henkilö"

# kätevin tapa yhdistää tekstejä ja muuttujia on f-string:
# aluksi hieman vaikea käyttää, mutta kun oppii,
# ei tarvitse enää muita tapoja tekstien ja muuttujien yhdistelemiseen
print(f"Nimi: {name}, Saldo: {total_money} €")
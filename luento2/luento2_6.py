# datetimen kanssa käytetään yleensä tarkempaa importia:
# eli datetime-moduulista -> importataan vain ominaisuus nimeltä date
from datetime import date

# UTC-aikaleima
today = date.today()
print(today)
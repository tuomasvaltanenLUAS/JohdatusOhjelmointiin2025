# NOTE: install also lxml, bs4, requests and html5lib before
# pip install pandas
# pip install lxml
# pip install beautifulsoup4
# pip install html5lib
# pip install requests
# attempting to use pandas with web pages in this code
import requests
import pandas as pd
import translations_fi
from io import StringIO

# constants, values based on year 2022 in Finnish taxation
# source: https://www.veronmaksajat.fi/Palkka-ja-elake/
# taxes for driven kilometers on work trips, or property renovation costs
BENEFIT_FOR_KILOMETER_EUR = 0.46

# with this value, maximum reduction is 40% of 5875 = 2250 EUR
# in Finnish: "kotitalousvähennys"
MAXIMUM_RENOVATION_PRICE_FOR_REDUCTION = 5875
RENOVATION_REDUCTION_PERCENTAGE = 0.4

# in Finnish: "pääomatulot"
OTHER_INCOME_UNDER_30K_PERCENTAGE = 0.3
OTHER_INCOME_OVER_30K_PERCENTAGE = 0.34

# in Finnish: "työhuonevähennys"
ALLOWED_WORKROOM_REDUCTIONS = [230, 460, 920]

# for example, if you buy tools for your work with your own money
# and also use it for occasionally, you can use the other reduction field
# in Finnish: tulonhankkimisvähennys
OTHER_REDUCTION_PERCENTAGE = 0.5

# in Finnish: omavastuu
OTHER_REDUCTION_PERSONAL_PART = 750

# ask user for values for incomes and reductions
monthly_income = int(input(f"{translations_fi.monthly_income}:\n"))
other_income = int(input(f"{translations_fi.other_income}:\n"))
driven_kilometers = int(input(f"{translations_fi.kilometers}:\n"))
other_reductions = int(input(f"{translations_fi.other_reductions}:\n"))
workroom_reduction = int(input(f"{translations_fi.workroom_reduction}:\n"))
vacation_money = input(f"{translations_fi.vacation_money}:\n")
renovation_money = int(input(f"{translations_fi.renovation_reduction}:\n"))

# total income for the year
total_income = monthly_income * 12

# add half a month's salary if vacation money is used
if vacation_money.lower() == "k":
    total_income += monthly_income * 0.5

# get tax-table from internet page, use pandas-module for easier data extract
# remove first row, since it has the headers
tax_url = "https://www.veronmaksajat.fi/tutkimus-ja-tilastot/tuloverot/palkansaajan-veroprosentit/palkansaajan-veroprosentit/"

# since this website blocks script-level HTML download
# let's define a user-agent and use requests -module instead
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0.0.0 Safari/537.36"
    )
}

# perform webscrape with requests and
# convert data to expected StringIO -format for pandas
resp = requests.get(tax_url, headers=headers)
raw_html = StringIO(resp.text)

table_taxes = pd.read_html(raw_html)[0]
table_taxes = table_taxes.iloc[1:, :]

# person's tax percent for this amount of income
tax_percent = 0

# find the correct tax percent based on yearly income
# index 0 => total income in year, index 2 => tax percent
for index in table_taxes.index:
    income_value = table_taxes[0][index].replace(" ", "")
    income_value = int(income_value)

    # if the current table income value is too high =>
    # break out of loop and use the previous tax value
    if income_value > total_income:
        break

    # clean up the tax percent value and set it to variable
    tax_value = table_taxes[2][index].replace("%", "").replace(",", ".")
    tax_value = float(tax_value)
    tax_percent = tax_value / 100


# get total tax
total_tax = tax_percent * total_income

# -----------------------------------------
# REDUCTIONS FOR TAXES

total_tax -= driven_kilometers * BENEFIT_FOR_KILOMETER_EUR
other_reductions -= OTHER_REDUCTION_PERSONAL_PART
total_tax -= other_reductions * OTHER_REDUCTION_PERCENTAGE

# reset renovation money to maximum allowed value if it exceeds
if renovation_money > MAXIMUM_RENOVATION_PRICE_FOR_REDUCTION:
    renovation_money = MAXIMUM_RENOVATION_PRICE_FOR_REDUCTION

total_tax -= renovation_money * RENOVATION_REDUCTION_PERCENTAGE

# skip workroom reduction if value is invalid
if workroom_reduction not in ALLOWED_WORKROOM_REDUCTIONS:
    workroom_reduction = 0

total_tax -= workroom_reduction

# total other tax is tax for other income, like income from
# properties etc.
total_other_tax = 0

if other_income > 30000:
    total_other_tax = other_income * OTHER_INCOME_UNDER_30K_PERCENTAGE
else:
    total_other_tax = other_income * OTHER_INCOME_OVER_30K_PERCENTAGE

# -----------------------------------
# combine everything and print result
total_income += other_income - total_other_tax - total_tax
print(f"{translations_fi.net_income}: {total_income} €")
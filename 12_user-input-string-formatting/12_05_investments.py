# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

investment = float(input("Hey what's your investment? "))
interest = float(input("What interest would you like? "))
years = float(input("And how many years will you invest? "))

print(f'OK so you will get {investment * interest * years}')

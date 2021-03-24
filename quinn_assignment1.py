#define constants
from unicodedata import decimal

HOURLY_RATE = 15
COMMISSION_RATE = 0.1

#define function to error check if value entered is a number
def isNumber(message):
    try:
        getInput = float(input(message))
    except ValueError:
        print("Please enter a numerical value ")
        getInput = float(input(message))
    return getInput


#input hours worked and weekly sales amount
hoursWorked = isNumber("Hours worked ")
weeklySales = isNumber("Weekly sales ")

#calculate hourly pay, commission pay and total pay
hourlyPay = hoursWorked * HOURLY_RATE
commissionPay = weeklySales * COMMISSION_RATE
totalPay = hourlyPay + commissionPay

#round pay to nearest cent
roundedPay = "{:.2f}".format(round(totalPay,2))

#output total pay
print("This week you earned $" + str(roundedPay))
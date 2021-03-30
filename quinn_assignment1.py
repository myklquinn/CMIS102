#define constants
HOURLY_RATE = 15
COMMISSION_RATE = 0.1

#define function to error check if value entered is a number
def validateInput(message):
    while True:
        employeeInput = input(message)
        try:
            employeeInput = eval(employeeInput)
            return employeeInput
            break
        except:
            print("Please enter a numerical value ")
            pass

#input hours worked and weekly sales amount
hoursWorked = validateInput("Hours worked ")
weeklySales = validateInput("Weekly sales ")

#calculate hourly pay, commission pay and total pay
hourlyPay = hoursWorked * HOURLY_RATE
commissionPay = weeklySales * COMMISSION_RATE
totalPay = hourlyPay + commissionPay

#round total pay to nearest cent
roundedPay = "{:.2f}".format(round(totalPay, 2))

#output formatted pay value
print("This week you earned $" + str(roundedPay))
#define constants
HOURLY_RATE = 15
COMMISSION_RATE = 0.1

#input hours worked and weekly sales amount
hoursWorked = eval(input("Hours worked "))
weeklySales = eval(input("Weekly sales "))

#calculate hourly pay, commission pay and total pay
hourlyPay = hoursWorked * HOURLY_RATE
commissionPay = weeklySales * COMMISSION_RATE
totalPay = hourlyPay + commissionPay

formatPay = "{:.2f}".format(totalPay)

#output total pay
print("This week you earned $" + str(formatPay))
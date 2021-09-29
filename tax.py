income = int(input("Please provide monthly income: "))

if income <= 38000:
    tax = income * 0.3
elif income > 38000 and income <= 50000:
    tax = ((income - 38000) * 0.35) + 11400
elif income > 50000:
    tax = ((income - 50000) * 0.4) + 11400 + 4200

print("Corresponding income tax:  " + str(tax))
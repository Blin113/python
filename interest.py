S = int(input("Initial savings: "))
P = int(input("Interest rate (in percentages): "))

P_percent = P/100 + 1

S_after = round((P_percent**5) * S)

print("The value of your savings after 5 years is: ", S_after)
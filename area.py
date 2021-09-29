import math

R = float(input("Provide radius: "))

A = R**2 * (math.pi)

A = str(round(A, 1))

print("Corresponding area is " + A)
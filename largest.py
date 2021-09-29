print("Please provide three integers A, B, C.")
A = int(input("Enter A: "))
B = int(input("Enter B: "))
C = int(input("Enter C: "))

if A >= B and A >= C:
    largest = A
elif B >= A and B >= C:
    largest = B
else:
    largest = C

print("The largest number is: ", largest)
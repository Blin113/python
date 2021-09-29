n = int(input("Enter a large positive integer: "))

temp = str(n)

zeros = 0
odd = 0
even = 0

for i in range(len(temp)):
    if int(temp[i]) == 0:
        zeros += 1
    elif int(temp[i]) % 2 != 0:
        odd += 1
    else:
        even += 1

print("\nZeros:", zeros)
print("Odd:", odd)
print("Even:", even)

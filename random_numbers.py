import random

n = int(input("Enter number of integers to be generated: "))

print("Generated values: ", end="")

sum = 0

max = 0

min = 100

for i in range(n):
    x = random.randint(1, 100)
    print(x, end=" ")

    if x > max:
        max = x

    if x < min:
        min = x

    sum += x

avg = round(sum/n, 2)

print("\nAverage, min, and max are", avg, ",", min, "and", max)

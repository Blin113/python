import random

nums = []

while len(nums) < 5:
    nums.append(random.randint(1, 100))

Sum = str(sum(nums))

print("Five random numbers: ", end= '')

print(*nums)

print("The sum is " + Sum)
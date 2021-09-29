num = 0
nums = []

while num < 100 or num > 999:
    num = int(input("Provide a three digit number: "))

num = str(num)

nums.append(int(num[2]))
nums.append(int(num[1]))
nums.append(int(num[0]))

print("Sum of digits: ", sum(nums))

#while num1 != 0:
#    temp = num1 % 10
#    nums.append(temp)
#    num1 //= 10
#    temp = num1 % 10
#    nums.append(temp)
#    num1 //= 10
#    temp = num1 % 10
#    nums.append(temp)
#    num1 //= 10
#
#   kod som jag hadde tänkt använda men den nya känns smidigare.
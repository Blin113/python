import random

num = random.randint(-10, 10)

print("The generated number is " + str(num))

if num < 0 and num % 2 != 0:
    print(str(num) + " is odd and negative")
elif num < 0 and num % 2 == 0:
    print(str(num) + " is even and negative")
elif num > 0 and num % 2 != 0:
    print(str(num) + " is odd and positive")
elif num > 0 and num % 2 == 0:
    print(str(num) + " is even and positive")
elif num == 0:
    print(str(num) + " is even and neither positive nor negative")
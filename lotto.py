import random

numbers = random.sample(range(0, 35), 7)

numbers.sort()

print("The Lotto numbers this week:")
print(*numbers)

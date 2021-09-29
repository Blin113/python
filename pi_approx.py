import random
from math import pi

print("choose N ammount of (x,y) points")
print()
print("1: n = 100")
print("2: n = 10000")
print("3: n = 1000000")

n_select = int(input("input: "))

if n_select == 1:
    n = 100
elif n_select == 2:
    n = 10000
elif n_select == 3:
    n = 1000000
else:
    print("invalid input")
    exit()


def get_pi_approx():
    count = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 < 1:
            count += 1

    return count / n * 4


pi_approx = get_pi_approx()

print("Pi approximate:", pi_approx)
print("Error:", pi - pi_approx)

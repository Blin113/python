import random

d1 = 0
d2 = 0

table_list = {
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0
}

for i in range(10000):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)

    sum = d1 + d2

    if sum in table_list:
        table_list[sum] += 1

print("Frequency table (sum,count) for rolling two dices 10000 times")

for key, value in table_list.items():
    print(key, value, sep="     ")

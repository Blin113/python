import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))


def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)


distance = round(distance(x1, y1, x2, y2), 3)

print("The distance between (", end="")
print(str(x1) + "," + str(y1), end=") ")
print("and (" + str(x2) + "," + str(y2) + ") is", distance)

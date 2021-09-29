n = 2

n = int(input("Enter an odd positive integer: "))
print()

if n % 2 == 0:
    raise ValueError

temp = n
i = 0
blank = 0
right_angle_done = False

print("Right-Angled Triangle:")

while not right_angle_done:
    for i in range(blank):
        print(end=" ")

    for i in range(temp):
        print(end="*")

    blank += 1
    temp -= 1
    print()

    if temp == 0:
        right_angle_done = True


print("\nIsosceles Triangle:")

Isosceles_done = False

blank = (n-1) // 2
k = 1

while not Isosceles_done:
    if k >= n:
        Isosceles_done = True

    for i in range(blank):
        print(end=" ")

    for i in range(k):
        print(end="*")

    if k < n:
        k += 2

    blank -= 1
    print()

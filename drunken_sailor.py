import random

# drunken sailor, Uppg 22(VG)

k = int(input("Enter the size: "))

total_steps = int(input("Enter the number of steps: "))

sailors = int(input("Enter the number of sailors: "))

out_of_bounds = False

steps_left = total_steps


def sailor_sim(out_of_bounds, steps_left):
    pos = [0, 0]    # x and y

    for j in range(total_steps):
        if random.randint(0, 100) >= 50:
            pos[0] += random.randrange(-1, 2, 2)    # either -1 or 1
        else:
            pos[1] += random.randrange(-1, 2, 2)    # either -1 or 1

        if steps_left == 0:
            return False
        elif pos[0] > k or pos[0] < -k or pos[1] > k or pos[1] < -k:
            return True

        steps_left -= 1


drowned = 0

i = 0

while i <= sailors:
    if sailor_sim(out_of_bounds, steps_left):
        drowned += 1
    i += 1

drowned_percentage = round((drowned / sailors) * 100, 2)

p = "(" + str(drowned_percentage) + "%)"

print("Out of", sailors, "drunk sailors,", drowned, p, "fell into the water.")

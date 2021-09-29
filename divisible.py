x = 100

nums = []

done = False

while x <= 200:
    if x % 4 == 0 and x % 5 != 0:
        nums.append(x)
        x += 1
    elif x % 4 != 0 and x % 5 == 0:
        nums.append(x)
        x += 1
    else:
        x += 1


done = True


if done:
    i = 0
    while i < len(nums):
        print(nums[i], " ", end="")
        i += 1

        if i % 10 == 0:
            print()

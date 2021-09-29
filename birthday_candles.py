age = 0
rem = 0  # remaining candles
boxes = 0

while age <= 100:
    i = 0

    if rem < age:
        while rem < age:
            i += 1
            rem += 24

        boxes += i

        if i > 0:
            print("Before birthday", str(age) + ",", "buy", i, "box(es)")

    rem -= age
    age += 1


print("\nTotal number of boxes:", str(boxes) + ",", "Remaining candles:", rem)

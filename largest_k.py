n = int(input("Enter a positive integer: "))

k = 0

sum = 0

done = False

while not done:
    if sum + k >= n:
        print(k, " is the largest k such that 0+2+4+6+...+k < ", n)
        done = True

    k += 2
    sum += k

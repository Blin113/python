import string_functions as sf


s = str(input("enter a string: "))

n = int(input("how many concatenations do you wish to perform ?: "))

x = str(input("entr a str x to see how many like it exist in the 1st str s: "))

print()

print("concatenation: ", sf.concat(s, n))

print("ammount of x in s: ", sf.count(s, x))

print("reverse s: ", sf.reverse(s))

print("first and last characters in s: ", sf.first_last(s))

print("has X:s: ", bool(sf.has_two_X(s)))

print("has duplicates: ", bool(sf.has_duplicates(s)))

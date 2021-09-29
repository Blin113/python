First = str(input("First name: "))
Last = str(input("Last name: "))

name = [First, Last]

init = name[0][0]

Linit = name[1][:4]

print("Short name: " + init + ". " + Linit)

#doesn't matter if the last name is less than 4 letters
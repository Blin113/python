s = int(input("Give a number of seconds: "))

seconds = s%60

min = s // 60

minutes = min%60

hours = s//3600

print("This corresponds to: ", hours, " hours, ", minutes, " minutes and ", seconds, " seconds.")
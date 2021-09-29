import statistics

inputs = input("Provide salaries: ")

string = inputs.split()

string.sort()

salaries = [int(s) for s in string]

average = int(sum(salaries) / len(salaries))

median = int(statistics.median(salaries))

gap = int(max(salaries) - min(salaries))

print("Median:", median)
print("Average:", average)
print("Gap:", gap)

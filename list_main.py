import list_functions as ls

lst = ls.random_list(10)

print("random list: ", lst)  # n = 10

print("average of list: ", ls.average(lst))

print("odd of list: ", ls.only_odd(lst))

print("list in string?: ", ls.to_string(lst))

print("1 and 2 consecutively in list?: ", ls.contains(lst, 1, 2))

print("duplicates?: ", ls.has_duplicates(lst))

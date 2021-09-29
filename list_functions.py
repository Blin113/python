import random


def random_list(n):
    lst = []
    for i in range(n):
        num = random.randint(1, 100)
        lst.append(num)

    return lst


def average(lst):
    return round(sum(lst)/2)


def only_odd(lst):
    temp = []
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            temp.append(lst[i])
    return temp


def to_string(lst):
    return str(lst)


def contains(lst, a, b):
    for i in range(len(lst)):
        if lst[i] == a and lst[i+1] == b:
            return True
    return False


def has_duplicates(lst):
    for i in range(len(lst)):
        if lst[i] in lst[i+1:len(lst)]:
            return True

    return False

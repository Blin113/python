def concat(s, n):
    return s*n


def count(s, x):
    ammount = 0

    for c in s:
        if x == c:
            ammount += 1

    return ammount


def reverse(s):
    return s[::-1]


def first_last(s):
    return s[0], s[-1]


def has_two_X(s):
    ammount = 0

    for c in s:
        if "X" == c:
            ammount += 1

    return ammount == 2


def has_duplicates(s):
    for i in range(len(s)):
        if s[i] in s[i+1:len(s)]:
            return True

    return False

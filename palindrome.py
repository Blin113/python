def is_palindrome(s):
    return s.lower() == rev_s.lower()


s = str(input("input a string: "))
new_s = ""
rev_s = ""

for _ in range(len(s)):
    if s[_].isalpha():
        new_s = new_s + s[_]
        rev_s = s[_] + rev_s


print(new_s, "----->", rev_s)
print(is_palindrome(new_s))

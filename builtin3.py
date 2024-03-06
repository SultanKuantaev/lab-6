#polindrome
str1 = input()
if str1 == ''.join(reversed(str1)):
    print("Yes")
else:
    print("No")

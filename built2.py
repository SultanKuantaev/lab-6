string = input()

def counter(string):
   
    upper_case = len(list(filter(str.isupper, string)))
    lower_case = len(list(filter(str.islower, string)))
    return upper_case, lower_case

upper_case, lower_case = counter(string)
print(f"upper cases: {upper_case} \nlower cases: {lower_case}")

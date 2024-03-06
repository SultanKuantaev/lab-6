from functools import reduce
user_input = input("Введите числа, разделенные пробелами: ")
list1 = [int(item) for item in user_input.split()]

def multiply(list1):
    return reduce(lambda x,y:x*y,list1,)

result = multiply(list1)
print(result)
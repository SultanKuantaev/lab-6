import time
import math

miliseconds = int(input("How many milliseconds? "))
value = int(input("Enter a value: "))

def delaying(value, miliseconds):
    time.sleep(miliseconds / 1000)
    return math.sqrt(value)

result = delaying(value, miliseconds)

print(f"Square root of {value} after {miliseconds} milliseconds is {result}")

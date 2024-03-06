import os

path = input("Enter the path to check:")

def condition(path):
    if os.path.exists(path):
        print("Yes, the path exists.")
    else:
        print("No, the path does not exist.")
        
    if os.access(path, os.R_OK):
        print("The path is readable.")
    else:
        print("The path is not readable.")
        
    if os.access(path, os.W_OK):
        print("The path is writable.")
    else:
        print("The path is not writable.")
        
    if os.access(path, os.X_OK):
        print("The path is executable.")
    else:
        print("The path is not executable.")


condition(path)

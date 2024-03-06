import os
path2 = input()
def path1(path):
    if os.path.exists(path):
        print("Path exists")
        directory, filename = os.path.split(path)
        print(f"it's directory is {directory}")
        print(f"it's name {filename}")
    else:
        print("path does not exist")

path1(path2)
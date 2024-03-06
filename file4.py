import os

path1 = input()

def lenof(path):
    with open(path,'r') as sdf:
        lines = len(sdf.readlines())
        print(f"it has {lines} lines")
lenof(path1)

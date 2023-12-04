import numpy as np

data = []
with open(r".\day3\Test.txt", "r") as file:
    for line in file:
        data.append(list(line.rstrip()))
        
print(data)

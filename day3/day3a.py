import numpy as np

def is_character(char):
    if (char.isalnum() or char == '.'):
        return False
    else:
        return True

def return_bool_ring(data,i,j):
    for scani in range(i-1,i+2):
        for scanj in range(j-1,j+2):
                data[scani][scanj] = True
    return data

data = []
with open(r".\day3\Test.txt", "r") as file:
    for line in file:
        data.append(list(line.rstrip()))

symbolBool = []
for i in range(len(data)):
    a = map(lambda x: is_character(x),data[i])
    symbolBool.append(list(a))

symbolHits = symbolBool
for i in range(len(symbolHits)):
    for j in range(len(symbolHits[0])):
        if symbolBool[i][j] == True:
            symbolHits = return_bool_ring(symbolHits,i,j)

print(symbolHits)

# def return_number(pos_i, pos_j):
#     contLoop = True
#     number = data[pos_i][pos_j]
#     iteration = 1
#     while contLoop:
#         if not data[pos_i][pos_j + iteration].isdigit():
#             return number
#         else:
#             number += data[pos_i][pos_j + iteration]
#             iteration += 1
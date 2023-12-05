total = 0

def is_character(char):
    if (char.isalnum() or char == '.'):
        return False
    else:
        return True

def find_number(data, i, j):
     keepGoing = True
     number = []
     while keepGoing:
          if not data[i][j].isdigit():
               return number
          else:
               number.append(data[i][j])
               j += 1

def is_symbol_near(data, i, j, numDigits):
    for scani in range(i - 1, i + numDigits + 2):
        for scanj in range(-1,2):
                if (i+scani >= 0 and i+scani < len(data) and j+scanj >= 0 and j+scanj < len(data[j])):
                     if is_character(data[scanj][scani]):
                          return True
    return False

def wipe_number(data, i, j, numDigits):
    for x in range(j,j+numDigits):
        data[i][x] = '.'
    return data

data = []
with open(r".\day3\Test.txt", "r") as file:
    for line in file:
        data.append(list(line.rstrip()))

print(data)
for i in range(len(data)):
     for j in range(len(data[0])):
          if data[i][j].isdigit():
               number = find_number(data,i,j)
               if is_symbol_near(data,i,j, len(number)):   
                    total += int(''.join(number))
                    data = wipe_number(data,i,j,len(number))
                
                    
               # add total by number if symbol around
               # if symbol, remove number
print(total)
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
          if j == len(data[i]) or not data[i][j].isdigit():
               return number
          else:
               number.append(data[i][j])
               j += 1

def is_symbol_near(data, i, j, numDigits): # bug in here
    for scanj in range(j - 1, j + numDigits + 2):
        for scani in range(i - 1, i + 2):
                if (scani >= 0 and scani < len(data) and scanj >= 0 and scanj < len(data[i])):
                     if is_character(data[scani][scanj]):
                          return True
    return False

def wipe_number(data, i, j, numDigits):
    for x in range(j,j+numDigits):
        data[i][x] = '.'
    return data

data = []
with open(r".\day3\input.txt", "r") as file:
    for line in file:
        data.append(list(line.rstrip()))

for i in range(len(data)):
     for j in range(len(data[0])):
          if data[i][j].isdigit():
                number = find_number(data, i, j)
                data = wipe_number(data, i, j, len(number))
                if is_symbol_near(data, i ,j , len(number)): # bug here  
                    total += int(''.join(number))
print(total)
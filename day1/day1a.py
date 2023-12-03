numSum = 0

with open(r".\day1\day1aInput.txt", "r") as file:
    for line in file:
        s = ''.join(i for i in line if i.isdigit())

        numSum += int(s[0] + s[-1])

print(numSum)
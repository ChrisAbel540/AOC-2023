numSum = 0

with open(f"C:\\Git\AOC-2023\day1\day1aInput.txt", "r") as file:
    for line in file:
        s = ''.join(i for i in line if i.isdigit())
        if len(s) == 1:
            s += s

        numSum += int(s[0] + s[-1])

print(numSum)
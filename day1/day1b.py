numSum = 0
numberList = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open(r"C:\\Git\AOC-2023\day1\day1aInput.txt", "r") as file:
    for line in file:
        nums = []

        for i, letter in enumerate(line.rstrip()):
            for val, name in enumerate(numberList):
                if name in line[i:i+len(name)]:
                    nums.append(str(val))

            if letter.isdigit():
                nums.append(letter)

        numSum += int(nums[0] + nums[-1])

print(numSum)
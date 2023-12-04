numSum = 0
gameNums = []

gameLims = {'red':12, 'green':13, 'blue':14}

with open(r".\day2\day2Input.txt", "r") as file:
    for line in file:
        addTurn = True
        
        turnData = line.split(':')[1].rstrip().split(';')
        for turn in turnData:
            selections = turn.split(',')
            for selection in selections:
                balls = int(''.join(i for i in selection if i.isdigit()))
                colour = ''.join(i for i in selection if i.isalpha())
                if balls > gameLims[colour]:
                    addTurn = False
        
        if addTurn:
            numSum += int(''.join(i for i in line.split(':')[0] if i.isdigit()))

print(numSum)
                
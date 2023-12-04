numSum = 0

with open(r".\day2\day2Input.txt", "r") as file:
    for line in file:       
        turnData = line.split(':')[1].rstrip().split(';')
        minBalls = {'red':0, 'green':0, 'blue':0}
        
        for turn in turnData:
            selections = turn.split(',')
            for selection in selections:
                balls = int(''.join(i for i in selection if i.isdigit()))
                colour = ''.join(i for i in selection if i.isalpha())
                
                if balls > minBalls[colour]:
                    minBalls[colour] = balls
        
        turnPower = 1
        for key in minBalls:
            turnPower *= minBalls[key]
        numSum += turnPower
                    
print(numSum)
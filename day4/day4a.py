result = 0

with open(r".\day4\input.txt", "r") as file:
    for line in file:
        # Find winning numbers for ticket
        winningNumbers = line.split('|')[0].split(':')[1].split(' ')
        while '' in winningNumbers:
            winningNumbers.remove('')
        
        # Extract guesses from line
        guesses = line.split('|')[1].rstrip().split(' ')
        while '' in guesses:
            guesses.remove('')

        numCorrect = 0
        for guess in guesses:
            if guess in winningNumbers:
                numCorrect += 1
        
        if numCorrect != 0:
            result += 2**(numCorrect - 1)

print(result)
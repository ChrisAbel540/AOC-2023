import numpy as np

def num_wins(guesses, winningNumbers):
    numCorrect = 0
    for guess in guesses:
        if guess in winningNumbers:
            numCorrect += 1
    return numCorrect

def add_multiplier(data, position, numExtras):
    for i in range(numExtras):
        data[position + 1 + i] += data[position]
    return data

result = 0
guesses = []
winningNumbers = []
with open(r".\day4\input.txt", "r") as file:
    for line in file:
        # Find winning numbers for ticket
        lineNumbers = line.split('|')[0].split(':')[1].split(' ')
        while '' in lineNumbers:
            lineNumbers.remove('')
        winningNumbers.append(lineNumbers)
        
        # Extract guesses from line
        lineGuesses = line.split('|')[1].rstrip().split(' ')
        while '' in lineGuesses:
            lineGuesses.remove('')
        guesses.append(lineGuesses)

lineMultipliers = np.ones(len(guesses))

for i in range(len(lineMultipliers)):
    numWins = num_wins(guesses[i], winningNumbers[i])
    lineMultipliers = add_multiplier(lineMultipliers, i, numWins)

    result += lineMultipliers[i]

print(int(result))
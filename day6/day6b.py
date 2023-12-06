data = open(r".\day6\input.txt").read().strip().splitlines()
for i in range(2):
    data[i] = data[i].split(':')[1].split()
time = ''.join(data[0])
distance = ''.join(data[1])

def number_of_wins(time, distance):
    wins = 0
    for charge_time in range(1,time):
        if (time - charge_time) * charge_time > distance:
            wins += 1
    return wins

print(number_of_wins(int(time), int(distance)))

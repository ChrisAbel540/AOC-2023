data = open(r".\day6\input.txt").read().strip().splitlines()
for i in range(2):
    data[i] = data[i].split(':')[1].split()
time = data[0]
distance = data[1]

def number_of_wins(time, distance):
    wins = 0
    for charge_time in range(1,time):
        if (time - charge_time) * charge_time > distance:
            wins += 1
    return wins

return_value = 1
for race_time, race_distance in zip(time, distance):
    return_value *= number_of_wins(int(race_time), int(race_distance))

print(return_value)
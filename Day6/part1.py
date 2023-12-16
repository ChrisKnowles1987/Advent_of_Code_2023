with open('input.txt') as file:
    lines =file.readlines()
times = [int(time) for time in lines[0].split()[1:]]
distances = [int(distance) for distance in lines[1].split()[1:]]
races = list(zip(times, distances))
# print(races)
margin = 1
winners = []
for time, distance in races:
    winner = 0
    for speed in range(1,time):
        race_time = time -speed
        race_distance = speed * race_time
        if race_distance > distance:
            winner += 1
    winners.append(winner)
    x =  margin * winner
    margin = x
print(x)
print(winners)
        
            
    
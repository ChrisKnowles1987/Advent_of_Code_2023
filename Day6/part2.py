with open('input.txt') as file:
    lines =file.readlines()
times = [time for time in lines[0].split()[1:]]
distances = [distance for distance in lines[1].split()[1:]]
time= int(''.join(times))
distance = int(''.join(distances))
# print(time)
# print(distance)

winner=0
for speed in range(1,time):
        race_time = time -speed
        race_distance = speed * race_time
        if race_distance > distance:
            winner += 1
print(winner)

        
            
    
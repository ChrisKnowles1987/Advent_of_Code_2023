import math

with open('input.txt', 'r') as file:
    file = file.read().split('\n')

def get_directions():
    directions = []
    for char in file[0]:
        if char == 'L':
            directions.append(0)
        elif char == 'R':
            directions.append(1)
    return directions

def get_maps(): #call maps with maps['key'][0/1]
        maps ={}
        for line in file[2::]:
            key, value = line.split('=')
            key = key.strip()
            value = value.strip("( )")
            value = tuple(value.split(', '))
            maps[key] = value
        return maps

def part1():
    def run_map(directions, maps):
        counter = 0
        score = 1
        key = 'AAA'
        while key != 'ZZZ' and counter <= len(directions):
            key = maps[key][directions[counter]]
            counter += 1
            score += 1
            if counter == len(directions):
                counter = 0
            
        return score -1
    directions = get_directions()
    maps = get_maps()
    answer = run_map(directions, maps)
    return answer

def part2():
    directions = get_directions()
    maps = get_maps()
    
    def get_start_nodes(maps):
        start_nodes = [key for key in maps if key.endswith('A')]
        return start_nodes
    
    def get_cycles(directions, maps): #gets number of steps each start takes to reach the end
        counter = 0
        cycles = []
        nodes = get_start_nodes(maps)
        for node in nodes:
            cycle = 1
            while not node.endswith('Z'):
                node = maps[node][directions[counter]]
                counter +=1
                cycle += 1
                if counter == len(directions):
                    counter = 0
            cycles.append((cycle-1))
        return cycles
    
    def run_cycles(): #lowest common multipler for the first pair, then factor in each cycle int he list
        #lcm is the product of 2 numbers divided by their lowest common denominator
        def get_lcm(a,b):
            lcm = abs(a * b) // math.gcd(a,b)
            return lcm
            
        cycles = get_cycles(directions,maps)
        cycles.sort()
        
        #start at cycles[0]
        lcm = cycles[0]
        for cycle in cycles[1:]:
            lcm = get_lcm(lcm, cycle) #adds each cycle int he list and calculates the new lcm  
        return lcm              
    answer = run_cycles()       
    return answer

print(f'part1: {part1()}')

print(f'part2: {part2()}')

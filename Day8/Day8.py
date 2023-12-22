#look for py test


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

def part1():
    def get_maps(): #call maps with maps['key'][0/1]
        maps ={}
        for line in file[2::]:
            key, value = line.split('=')
            key = key.strip()
            value = value.strip("( )")
            value = tuple(value.split(', '))
            maps[key] = value
        return maps 
   
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
    # Your code for part 2
    return

print(f'part1: {part1()}')

print(f'part2: {part2()}')

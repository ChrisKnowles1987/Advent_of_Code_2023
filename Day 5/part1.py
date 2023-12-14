'''
create tuples list for each map
source[0] destination[1] range[2]

logic:  

if source <= input <= (input + range):
    new_input = (input + range) - (input - source)
    
repeat this through each map

append location to array
'''

seed_to_soil_map = 'seed-to-soil map:'
soil_to_fertilizer_map = 'soil-to-fertilizer map:'
fertilizer_to_water_map = 'fertilizer-to-water map:'
water_to_light_map = 'water-to-light map:'
light_to_temperature_map = 'light-to-temperature map:'
temperature_to_humidity_map = 'temperature-to-humidity map:'
humidity_to_location_map = 'humidity-to-location map:'


def create_map_from_name(file, map_name):
    
    lines = file.split('\n')
    is_current_map = False
    map_data = []

    for line in lines:
        if line.strip() == map_name:
            # Start of the desired map
            is_current_map = True
        elif line.strip().endswith('map:') or not line.strip():
            # End of the current map or empty line
            is_current_map = False
        elif is_current_map:
            # Parse source, destination, and range into tuples
            source, destination, range_ = map(int, line.split())
            map_data.append((source, destination, range_))

    return map_data


def mapIO(seed, map):
    seed = seed
    for entry in map:
       destination = entry[0]
       source =  entry[1]
       rng = entry[2]
       max_source = source + rng
       
       if source <= seed < max_source:
           #diff source and seed and add to 
           seed = (seed-source + (destination))
           return seed
       else:
           seed = seed
    return seed

def mapIO_2(location, map):
    for entry in map:
       destination = entry[0]
       source =  entry[1]
       rng = entry[2]
       max_destination = destination + rng
       
       if destination <= location <= max_destination:
           location = (location-destination + (source))
           return location
       else:
           location = location
    return location
    
            
with open('input.txt') as file:
    file = file.read()
    lines = file.split('\n')
    
seeds = list(map(int, lines[0].split(': ')[1].split()))
# print(seeds)

seed_to_soil_map = create_map_from_name(file, "seed-to-soil map:")
soil_to_fertilizer_map = create_map_from_name(file, "soil-to-fertilizer map:")
fertilizer_to_water_map = create_map_from_name(file, "fertilizer-to-water map:")
water_to_light_map = create_map_from_name(file, "water-to-light map:")
light_to_temperature_map = create_map_from_name(file, "light-to-temperature map:")
temperature_to_humidity_map = create_map_from_name(file, "temperature-to-humidity map:")
humidity_to_location_map = create_map_from_name(file, "humidity-to-location map:")

map_list = [seed_to_soil_map,
soil_to_fertilizer_map,
fertilizer_to_water_map,
water_to_light_map,
light_to_temperature_map,
temperature_to_humidity_map,
humidity_to_location_map,
]


def main(seeds):
        
    map_steps = []
    for seed in seeds:
        
        counter = 0
        old_seed = seed
        while counter < len(map_list):
            new_seed = mapIO(old_seed,map_list[counter])
            old_seed = new_seed
            counter += 1
        map_steps.append(new_seed)
    
    return map_steps

def main_2():
    # print('Running part 2')
    seed_start = seeds[0::2]
    seed_range = seeds[1::2] 
    seed_found = False
    location = 41222967
    old_location = 0
    while  seed_found == False:
        counter = len(map_list) -1
        old_location = location
        # print(location)
        while counter >= 0:
            new_location = mapIO_2(old_location, map_list[counter])
            # print(f'map{counter} value:{new_location}')
            old_location = new_location
            counter -= 1
        # print(location)
        for x in range(len(seed_start)): 
            seed_min = seed_start[x] 
            seed_max = seed_start[x] + seed_range[x]
            # print(f'{range(seed_min,seed_max)}')  
            if seed_min <= new_location  < seed_max:
                seed_found = True
                return location
            location += 1
   

print(main_2())
# part1 = main(seeds)
# print(f'part1: {min(part1)}')
# print(f'Part2: {main_2()}')





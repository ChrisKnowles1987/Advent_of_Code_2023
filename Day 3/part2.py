'''A gear is any * symbol that is adjacent to exactly two part numbers. 
Its gear ratio is the result of multiplying those two numbers together.

find just *
stop appending found numbers if more than 2
multiply found numbers[0],fund numbers[1] and append to new array
sum new array
'''
not_gears = '0123456789.'
with open('input.txt') as input:
    file = input.read()
    engine_schematic = [list(line) for line in file.split('\n')]

# def get_gears(array):
#     gears = []
#     for x in array:
#         for y in x:
#             if y not in ([item for item in list(not_gears)]) and y not in gears :
#                 gears.append(y)
                
#     return gears

def get_char_coords(array):
    gears = '*'
    coordinates = []
    for x_index, x in enumerate(array):
        for y_index, y in enumerate(x):
            if y == gears:
                coordinates.append(tuple([x_index, y_index]))
    print(coordinates)           
    return coordinates
    
def neighbours(schematic, coords):
    
    directions = [
    (0 , +1),   # right
    (0 , -1),   # left
    (+1 , 0),   # up
    (-1 , 0),   # down
    (+1 , +1),  # up right
    (-1 , -1),  # down left
    (+1 , -1),  # up left
    (-1 , +1)] # down right
        
    array = schematic
    
    gear_ratios = []
    for x, y in coords:
        found_numbers = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(array) and 0 <= ny < len(array[0]) and array[nx][ny].isdigit():
                found_number = ''
                # Move to the start of the number sequence
                while 0 <= nx < len(array) and 0 <= ny <= len(array[0]) and array[nx][ny - 1].isdigit():
                    ny -= 1
                # Concatenate the numbers in the sequence
                while 0 <= ny < len(array[0]) and array[nx][ny].isdigit():
                    found_number += array[nx][ny]
                    array[nx][ny]=array[nx][ny].replace((array[nx][ny]), '.')
                    ny += 1                    
                found_numbers.append(int(found_number))
                if len(found_numbers) >= 2:
                    gear_ratios.append((found_numbers[0] * found_numbers[1]))
                    
    print(f'gear_ratios: {sum(gear_ratios)}')
    return found_numbers

coords = get_char_coords(engine_schematic)

neighbours(engine_schematic, coords)
'''
convert input to array of arrays
find all chars in array
find pos of chars
iterate over char pos and check neighbouirs for numbers
if number get start and return number to array, remove number friom array to avoid duplicates
sum numbers
'''
not_chars = '0123456789.'
with open('input.txt') as input:
    file = input.read()
    engine_schematic = [list(line) for line in file.split('\n')]

def get_chars(array):
    chars = []
    for x in array:
        for y in x:
            if y not in ([item for item in list(not_chars)]) and y not in (chars) :
                chars.append(y)
                
    return chars

def get_char_coords(array):
    chars = get_chars(array)
    coordinates = []
    for x_index, x in enumerate(array):
        for y_index, y in enumerate(x):
            if y in [item for item in list(chars)]:
                coordinates.append(tuple([x_index, y_index]))
                
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
    found_numbers = []
    for x, y in coords:
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

    return found_numbers

coords = get_char_coords(engine_schematic)

neighbours(engine_schematic, coords)

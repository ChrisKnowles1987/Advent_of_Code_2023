'''
1 convert input to array of arrays
2 find pos of charcacters
iterate over character pos and check neighbouirs
try new array.append(int(neigbour)) else return
profit?
'''

with open('input.txt') as input:
    file = input.read()
    engine_schematic = [list(line) for line in file.split('\n')]

def get_char_coords(array):
    #needs to get coords of only symbols
    coordinates = []
    for x_index, x in enumerate(array):
        for y_index, y in enumerate(x):
            if y != '.':
                
                coordinates.append(tuple([x_index, y_index]))
    print(coordinates)
    
def neighbours():
    
    directions = [
    (0 , +1),   # right
    (0 , -1),   # left
    (+1 , 0),   # up
    (-1 , 0),   # down
    (+1 , +1),  # up right
    (-1 , -1),  # down left
    (+1 , -1),  # up left
    (-1. , +1)] # down right
        
    for direction in directions:
        
    #this should find the coordinates of neighbours that contain a number, 
    # then move to the start of the number and return a concat string of all the numbers in the sequence
   
# get_char_coords(engine_schematic) 
       
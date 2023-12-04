def split_string(string):
    pos = string.find(':')
    string = string[pos+1:]

    delimiters = [',',';']
    for delimiter in delimiters:
            
        string=string.replace(delimiter, ',')
    string = string.split(',')
    return [(int(s.split()[0]), s.split()[1]) for s in string]
        
def get_power(touples):
    big_red = 0
    big_blue = 0
    big_green = 0
    for x in touples :
        if (x[1] == 'red') and (x[0] > big_red):
            big_red = x[0]
        if (x[1] == 'green') and (x[0] > big_green):
            big_green = x[0]
        if (x[1] == 'blue') and (x[0] > big_blue):
            big_blue = x[0] 
    power = big_red * big_green * big_blue
    print(f' red {big_red} green {big_green} blue {big_blue}  - power {power}') 
    return power
     
    
    return 

def main():
    counter = 1
    with open('puzzle_input.txt') as file:
        game_powers = []
        for game in file:
            print(f'Game: {counter}')
            touples = split_string(game)
            power = get_power(touples) 
            game_powers.append(power)
            counter +=1
    print(sum(game_powers))
    return sum(game_powers)

main()

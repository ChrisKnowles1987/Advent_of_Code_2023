
game = 'Game 1: 7 red, 14 blue; 2 blue, 3 red, 3 green; 4 green, 12 blue, 15 red; 3 green, 12 blue, 3 red; 11 red, 2 green'
def split_string(string):
    pos = string.find(':')
    string = string[pos+1:]

    delimiters = [',',';']
    for delimiter in delimiters:
            
        string=string.replace(delimiter, ',')
    string = string.split(',')
    return [(int(s.split()[0]), s.split()[1]) for s in string]
        
def count_cubes(touples):
    score = 1
    for x in touples :
        if (x[1] == 'red') and (x[0] > 12):
            score = 0
        if (x[1] == 'green') and (x[0] > 13):
            score = 0
        if (x[1] == 'blue') and (x[0] > 14):
            score = 0
    print(score)   
    return score

def main():
    counter = 1
    with open('puzzle_input.txt') as file:
        possible_games = []
        for game in file:
            touples = split_string(game)
            possible_games.append(counter * count_cubes(touples))
            counter += 1  
    print(possible_games)
    print(sum(possible_games))
    return

main()
        
        
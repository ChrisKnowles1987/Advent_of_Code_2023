'''
process cards into two lists: winning_numbers and game_numbers
set score to 1
loop over winning_numbes and check if they are in game_numbers
if so  double the score
score needs to double for every found number,  but be set to 0 if there are no found nuimbers

Part 2
instead of caclulating score, create an array (cards) that has length = len(lines)
loop winners to check if they are in gamers, count the winners 
loop over the new array and add +1  to each entry for range 
add while loop to repeat at the current loop untill count == cards[xpos] 

sum cards

'''

def split_string(file):
    winners = []
    gamers = []
    
    for line in [line.split(":")[1] for line in file]:
       
        winners.append(line.split("|")[0].split())
        gamers.append(line.split("|")[1].split("\n")[0].split())
     
    return winners, gamers

def part1(winners, gamers):
    scores = []
    for x_index, x in enumerate(winners):
        score = 0
        for y in  x:
            if y in gamers[x_index]:
                if score == 0:
                    score = 1
                    continue 
                score = score * 2
                
        scores.append(score)
    
    print(f'{sum(scores)}')
    return scores 

def get_cards(winners, gamers):
    cards = [1 for x in gamers]
    scores = []
    for x_index, x in enumerate(winners):
        score = 0
        for y_index, y in enumerate(x):
            if y in gamers[x_index]:
                score +=1
        scores.append(score)
    return cards,scores

def count_cards(gamestate):
    for score_index, score in enumerate(gamestate[1]):
        count = 0
        start_index = score_index + 1
        games = gamestate[0][score_index]
        game_count = 0
        while game_count < games:
            count = 0
            start_index = score_index + 1
            while count < score and start_index < len(gamestate[0]):
                gamestate[0][start_index] += 1 
                start_index += 1
                count += 1
                if start_index >= len(gamestate[0]):  # Prevent index out of range
                    break
            game_count += 1
    print(f'sum(gamestate){sum(gamestate[0])}')
    return(gamestate)

def main():                
    with open('input.txt') as file:
        winners, gamers = split_string(file)
        gamestate = get_cards(winners,gamers)
        gamestate =  count_cards(gamestate)
        
if __name__ == '__main__':
    main()
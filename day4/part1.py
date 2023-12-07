'''
process cards into two lists: winning_numbers and game_numbers
set score to 1
loop over winning_numbes and check if they are in game_numbers
if so  double the score
score needs to double for every found number,  but be set to 0 if there are no found nuimbers

'''

    
# def get_winners():
    
#     return

# def get_gamers():
    
#     return

def split_string(file):
    winners = []
    gamers = []
    
    for line in [line.split(":")[1] for line in file]:
       
        winners.append(line.split("|")[0].split())
        gamers.append(line.split("|")[1].split("\n")[0].split())
     
    return winners, gamers

def gizwinner(winners, gamers):
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
                
def main():
    with open('input.txt') as file:
        winners, gamers = split_string(file)
        gizwinner(winners,gamers)
        
        

main()
    
# winning_lines = get_winners()
# game_lines = get_gamers()
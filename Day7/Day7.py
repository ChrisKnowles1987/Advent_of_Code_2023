'''
card : value dictionary
sort input to hand,bid dictionary
sort hands by counting duplicates
'''


with open('input.txt', 'r') as file:
    lines = file.readlines()

def part1():
    deck = {
        "A":14, 
        "K":13, 
        "Q":12, 
        "J":11, 
        "T":10, 
        "9":9, 
        "8":8, 
        "7":7, 
        "6":6, 
        "5":5, 
        "4":4, 
        "3":3,
        "2":2
    }
    
    high_cards = []
    pair = []
    two_pairs =[]
    three_of_a_kind =[]
    full_house =[]
    four_of_a_kind =[]
    five_of_a_kind =[]
    
    order = [high_cards,
             pair,
             two_pairs,
             three_of_a_kind,
             full_house,
             four_of_a_kind,
             five_of_a_kind]
    
    def sort_hands(lines):
        #sort hands into types
        for line in lines:
            hand,bid = line.split()
            hands ={}
            for char in hand:
                #sort hands into dict
                if char not in hands:
                    hands[char] = 0
                hands[char] += 1
            #sort hands dict using the deck as the key so the highest card is first
            hands = sorted(hands.items(), key=lambda item: deck[item[0]], reverse=True)
            # print(hands)
            card_values = [value for card, value in hands]
            card_count = max(value for card, value in hands)     
            
            #high card
            if len(hands) == 5:
                high_cards.append((hand, bid))
                # print(high_cards)
            
            #pair
            if len(hands) == 4:
                pair.append((hand,bid))
                continue
                
            # two pair or 3 of a kind
            if len(hands) == 3:
                #three of a kind
                if card_count == 3:
                    three_of_a_kind.append((hand,bid))
                    
                #two pair
                elif card_count == 2:
                    two_pairs.append((hand,bid))    
                continue
            
            # three of a kind or full house or four of a kind
            if len(hands) == 2:
                #three of a kind
                if card_count == 3 and 2 not in card_values:
                    three_of_a_kind.append((hand,bid))
                
                #full house
                elif card_count == 3 and 2 in card_values:
                    full_house.append((hand,bid))
                
                #four of a kind
                elif card_count == 4 and 2 not in card_values:
                    four_of_a_kind.append((hand,bid))
                continue
            
            #five of a kind
            if len(hands) == 1:
                five_of_a_kind.append((hand,bid))
                continue
        
        return order
    
    
    
    def hand_to_string(hand, deck):
        key = ''. join(str(deck[char]).zfill(2) for char in hand)
        return key
    
    def order_hands(order):
        #sort duplicate hands in the order based on the order of cards in the hand
        for hands in order:
            if len(hands) >1:
                hands.sort(key=lambda hb: hand_to_string(hb[0], deck), )
                
        return order
    
    def count_bids(order):
        #clean up order to new list ithout empties or sublists
        cards_list = []
        answer = 0
        for hands in order:
            for hand in hands:
                cards_list.append(int(hand[1]))
        #add ranks and multiply bids
        for x, bid in enumerate(cards_list):
            bid = (x+1) * bid
            answer += bid
            
            
        return answer
             
    sort_hands(lines)
    order_hands(order)   
    answer = count_bids(order)
    
            
    return answer

def part2():
    
    return

print(f'part1: {part1()}')
print(f'part2: {part2()}')

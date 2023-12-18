
with open('input.txt', 'r') as file:
    lines = file.readlines()
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
    
def sort_hands(lines):
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
        # print(hands)
        for hand in hands:
            cards_list.append(int(hand[1]))
    #add ranks and multiply bids
    for x, bid in enumerate(cards_list):
        bid = (x+1) * bid
        answer += bid
              
    return answer

def part1():
    order = sort_hands(lines)
    order_hands(order)   
    answer = count_bids(order)
    return answer

'''
---------------------------------- Part 2 ----------------------------------
'''

deck2 = {
        "A":14, 
        "K":13, 
        "Q":12,  
        "T":10, 
        "9":9, 
        "8":8, 
        "7":7, 
        "6":6, 
        "5":5, 
        "4":4, 
        "3":3,
        "2":2,
        "J":1,
    }
def sort_hands2(lines):
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
    #sort hands into types
    for line in lines:
        hand,bid = line.split()
        hands ={}
        best_value = 0
        for char in hand:
            #sort hands into dict
            if char not in hands:
                hands[char] = 0
            hands[char] += 1
            if deck2[char] > best_value:
                best_card = char
                best_value = deck2[char]
            
        #sort hands dict using the deck as the key so the highest card is first
        hands = sorted(hands.items(), key=lambda item: deck[item[0]], reverse=True)
        # print(hands)
        card_values = [value for card, value in hands]
        jacks = next((value for card, value in hands if card == 'J'), 0)
        card_count = max(value for card, value in hands) + jacks      
        
        #high card or pair
        if len(hands) == 5:
            if jacks == 0: # all 5 cards are different
                high_cards.append((hand, bid))
                continue
            else: #only 1 jack in a 5 card hand, so a pair
                pair.append((hand,bid))
                continue
        
        #pair
        if len(hands) == 4: 
            '''max 2 jacks
            3 of a kind = JJXYZ or JXXYZ 
            pair if no jacks'''
            if jacks == 0:
                pair.append((hand,bid))
                continue
            else:
                three_of_a_kind.append((hand,bid))
                continue
            
        # two pair or 3 of a kind
        if len(hands) == 3:
            if jacks == 0:
                #three of a kind
                if card_count == 3:
                    three_of_a_kind.append((hand,bid))
                    
                #two pair
                elif card_count == 2:
                    two_pairs.append((hand,bid))    
                continue
            '''max 3 jacks
            XXYYZ
            JJJXY
            JJXXY 4 of a kind
            JXXYY full house'''
            if jacks == 1 and card_count < 4:
                full_house.append((hand,bid))
            elif jacks == 1 and card_count == 4:
                four_of_a_kind.append((hand,bid))
                continue
            else: #jacks must be > 1
                four_of_a_kind.append((hand,bid))
          
        # three of a kind or full house or four of a kind
        if len(hands) == 2:
            if jacks == 0:
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
            else:
                '''max jacks = 4
                JXXXX
                JJXXX
                JJJXX
                JJJJX five of a kind
                '''
                five_of_a_kind.append((hand,bid))
        
        #five of a kind
        if len(hands) == 1:
            five_of_a_kind.append((hand,bid))
            continue
    
    # print('32T3K is still the only one pair\n'
    #       'KK677 is now the only two pair\n'
    #       'T55J5, KTJJT, and QQQJA are now all four of a kind!\n'
    #     f' high cards: {high_cards}\n',
    #       f'pair: {pair}\n',
    #       f'two pair: {two_pairs}\n',
    #       f'three of a kind:{three_of_a_kind}\n',
    #       f'full house: {full_house}\n',
    #       f'four of a kind {four_of_a_kind}\n',
    #       f'five of a kind {five_of_a_kind}\n',
    #       )
         
    return order
def hand_to_string2(hand, deck2):
    key = ''. join(str(deck2[char]).zfill(2) for char in hand)
    # print(hand,key)
    return key

def order_hands2(order):
    #sort duplicate hands in the order based on the order of cards in the hand
    # print(order)
    for hands in order:
        
        if len(hands) >1:
            hands.sort(key=lambda hb: hand_to_string2(hb[0], deck2), )
        hands.sort(key=lambda hb: hand_to_string2(hb[0], deck2), )
    # print(order)   
    return order
def count_bids2(order):
    #clean up order to new list ithout empties or sublists
    cards_list = []
    answer = 0
    for hands in order:
        # print(hands)
        for hand in hands:
            cards_list.append(int(hand[1]))
    #add ranks and multiply bids
    for x, bid in enumerate(cards_list):
        bid = (x+1) * bid
        answer += bid
    return answer

def part2():
    order2 = sort_hands2(lines)
    order2 = order_hands2(order2)   
    answer = count_bids2(order2)
    
    return answer

# print(f'part1: {part1()}')
print(f'part2: {part2()}')

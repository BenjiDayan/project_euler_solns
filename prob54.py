def display_score(score):
    print("high_card: {0}\none_pair: {1}\ntwo_pair: {2}\nthree_of_a_kind: {3}\nstraight: {4}\nflush: {5}\nfull_house: {6}\nfour_of_a_kind: {7}\nstraight_flush: {8}\nroyal_flush: {9}".format(*score))

def actual_score(hand):
    score_list = score(hand)
    return(sum([score_list[num]*int(20**num) for num in range(len(score_list))]))


def score(hand):
    """Takes list of [1-13, 1-4], returns a score_list"""
    values = [card[0] for card in hand]
    
    #score categories' values range from 0-1 to 0-13.
    #below is their order of ranking, so multiply by 20^n to sort
    
    #high_card from 1-13
    high_card = 0 
    one_pair = 0
    two_pair = 0
    three_of_a_kind = 0
    straight = 0
    flush = 0
    full_house = 0
    four_of_a_kind = 0
    straight_flush = 0
    royal_flush = 0
    
    #one_pair from 0-13
    #one_pair's value is the lowest if existing pair
    #Going to be extracting stuff from comp so want baseline
    results = []
    temp = values.copy()
    while temp != []:
        val = temp[0]
        counter = 0
        for num in range(len(temp)):
            if temp[num] == val:
                counter += 1
        
        for num in range(counter):
            temp.remove(val)
        results.append([val, counter])   
 
    by_count = [[] for num in range(4)]
    for pair in results:
        by_count[pair[1]-1].append(pair[0])

    for num_list in by_count:
        num_list.sort()

    if len(by_count[0]) != 0:
        high_card = by_count[0][-1]

    if len(by_count[1]) != 0:
        one_pair = by_count[1][0]
        if len(by_count[1]) == 2:
            two_pair = by_count[1][1]
    
    if len(by_count[2]) == 1:
        three_of_a_kind = by_count[2][0]
    if len(by_count[3]) == 1:
        four_of_a_kind = by_count[3][0]
        
    #straight 0-9
    values.sort()
    straight = values[0]
    for num in range(3):
        if values[num+1] != values[num] + 1:
           straight = 0
    
    #flush 0-1
    is_flush = True
    suit1 = hand[0][1]
    for num in range(1, len(hand)):
        if hand[num][1] != suit1:
            is_flush = False
    
    if is_flush:
        flush = 1
   
    #full_house 0-1
    if three_of_a_kind != 0 and one_pair != 0 and four_of_a_kind == 0:
        full_house = 1 

    #straight_flush 0-9
    #royal_flush 0-1
    if flush == 1 and straight != 0:
        straight_flush = straight
        if straight == 9:
            royal_flush = 1
   
    scores = [high_card, one_pair, two_pair, three_of_a_kind, straight, flush, full_house, four_of_a_kind, straight_flush, royal_flush]

    return(scores)

def rate2hands(text):
    hands = input2hands(text)
    return(actual_score(hands[0]) > actual_score(hands[1]))

def input2hands(text):
    """Takes in e.g. "8C TS KC 9H 4S 7D 2S 5D 3S AC"
    Returns [[hand1], [hand2]] of form hand = [[1-13, 1-4]*5]""" 
    
    cards = text2cards(text)
    return([cards[:5], cards[5:]]) 

def text2cards(text):
    cards = text.split(' ')
    for num in range(len(cards)):
        chars = cards[num]
        cards[num] = [rank2num(chars[0]), suit2num(chars[1])]
    return(cards)    

def rank2num(char):
    if char == 'T':
        return(9)
    elif char == 'J':
        return(10)
    elif char == 'Q':
        return(11)
    elif char == 'K':
        return(12)
    elif char == 'A':    
        return(13)

    else:
        return(int(char)-1)

def suit2num(char):
    if char == 'D':
        return(1)
    elif char == 'C':
        return(2)
    elif char == 'H':
        return(3)
    elif char == 'S':
        return(4)


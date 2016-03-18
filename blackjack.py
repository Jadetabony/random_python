# -*- coding: utf-8 -*-
"""
Blackjack player

@author: Jade
"""

import random

#set score to 0-0 at the beginning
score_player = 0
score_dealer = 0


while True:
    #print score at the beginning of each round
    print "Score- "
    print "Dealer: ", score_dealer
    print "You: ", score_player
    
    #create a deck of cards
    suits = ['D', 'C', 'H', 'S']
    ranks = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    
    deck = []
    
    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)
    
    
    
    
    #Shuffle deck
    random.shuffle(deck)
    
    # deal hand
    dealer_bottom = deck[0]
    deck.remove(dealer_bottom)
    
    player_bottom = deck[0]
    deck.remove(player_bottom)
    
    dealer_top = deck[0]
    deck.remove(dealer_top)
    
    player_top = deck[0]
    deck.remove(player_top)
    
    dealer_hand = [dealer_bottom, dealer_top]
    player_hand = [player_bottom, player_top]
    
  
    # create rank
    def rank(card):
        rk = card[0]
        if rk in ['T','J','Q','K']:
            return 10
        elif rk == 'A':
            return 11
        else:
            return int(rk)
     

    
    # print visible dealer and player hands
    print ("You have a %s visible and a %s." %(player_top, player_bottom))
    print ("The dealer has a %s visible." %(dealer_top))
    
    #create a custom sort function for the card rank order to be used in the score function
    def cmp_sort(a,b):
        ranks = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
        if ranks.index(a[0]) > ranks.index(b[0]):
            return 1
        elif ranks.index(a[0]) == ranks.index(b[0]):
            return 0
        else:
            return -1
    

    # Function to calculate score.  In order to deal with the fact that A can be a 1 or 11, cards are ordered using the custom rank,
    # and then the hand is totaled, dealing with A last.  If total is greater than 10 by the time that you arrive at the A, A == 1. 
    # Else, A == 11
    def score(hand):
        
        total = 0
        #sort cards so that A will always be last
        hand.sort(cmp_sort)
        for card in hand:
            if total > 10 and card[0] == 'A':
                total = total + 1
            else:        
                total = total + rank(card)
        return total
        
    
    # Loop that seeks user input on whether then want to hit or stay and then calculates their score, determines if they got blackjack 
    # or if they bust
    while True:
        if score(player_hand)== 21 and len(player_hand) == 2:
            print ("BLACKJACK!")
            break
        else:
            choice = raw_input("Would you like to hit or stay?  Enter [h or s] and hit enter: ")
            if choice not in ['h','s','H','S']:
                print ("Please enter only an 'h' or 's'.")
                continue
            elif choice in ['h','H']:
                hit1 = deck[0]
                deck.remove(hit1)
                player_hand.append(hit1)
                if score(player_hand) > 21:
                    print ("You were delt a %s." %(hit1))
                    print ("Your hand: ", player_hand)
                    print ("Busted. Sorry, you lose.")
                    break
                else:
                    print ("You were delt a %s." %(hit1))
                    print ("Your hand: ", player_hand)
                    continue
            elif choice in ['s','S']:
                break
    
    # Determine dealer score
    while True:
        if score(player_hand) > 21 :
            break
        elif score(dealer_hand) == 21 and len(dealer_hand) == 2:
            print "Dealer got Blackjack."
            break
        elif score(dealer_hand) <= 16:
            dhit1 = deck[0]
            deck.remove(dhit1)
            dealer_hand.append(dhit1)
            print ("Dealer was delt a %s." %(dhit1))
            if score(dealer_hand) > 16 and score(dealer_hand) <= 21:
                break
            elif score(dealer_hand)>21:
                print ("Dealer has bust.")
                break
            else:
                continue
        else:
            break
            
    #show dealer and player hands
    print ("Dealer hand: ", dealer_hand)
    print ("Your hand: ", player_hand)
    
    
    # determine winner
    if score(player_hand) > 21:
        print "Dealer wins."
        score_dealer += 1
    elif score(dealer_hand) > 21:
        print "Congratulations! You won!"
        score_player += 1
    elif score(player_hand) == score(dealer_hand):
        print ("You tied, but Blackjack rules dictate that the dealer won.")
        score_dealer += 1
    elif score(dealer_hand)> score(player_hand):
        print ("Dealer wins.")
        score_dealer += 1
    elif score(dealer_hand)< score(player_hand):
        print ("Congratulations! You won!")
        score_player += 1
    else:
        print "Error???"
        
    # seeks user input on whether or not they would like to play again, with a loop to ensure that a y or n was entered
    while True:
        cont = raw_input("Would you like to play again? [y/n]: ")
        if cont not in ['y','n','Y','N']:
            print "Please enter only a 'y' or 'n'."
            continue
        else:
            break 
        
    if cont == 'y':
        continue
    else:
        break

print "Score- "
print "Dealer: ", score_dealer
print "You: ", score_player
print "Thanks for playing!!!"

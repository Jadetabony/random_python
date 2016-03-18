# -*- coding: utf-8 -*-
"""
Blackjack player

@author: Jade
"""

# create deck of cards 
import random

score_player = 0
score_dealer = 0

while True:
    print "Score- "
    print "Dealer: ", score_dealer
    print "You: ", score_player
        
    suits = ['D', 'C', 'H', 'S']
    ranks = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    
    deck = []
    
    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)
    
    
    
    # deal hand
    #Shuffle deck
    random.shuffle(deck)
    
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
     
    # Define function to print out the written rank and suit
    """def written(card):
        write =[]
        rk = card[0]
        if rk == 1:
            write[0]= 10
        elif rk =='J':
            write[0]= 'Jack'
        elif rk == 'Q':
            write[0] = 'Queen'
        elif rk =='K':
            write[0]= 'King'
        elif rk == 'A':
            write[0] = 'Ace'
        else:
            write[0] = int(rk)
            
        suit= card[1]
        if suit == 'H':
            write[1]= 'Hearts'
        elif suit =='D':
            write[0]= 'Diamonds'
        elif suit == 'C':
            write[0] = 'Clubs'
        elif suit =='S':
            write[0]= 'Spades' 
            
        return (write[0], " of ", write[1])
        """
    
    
    # print visible dealer and player hands
    print ("You have a %s visible and a %s." %(player_top, player_bottom))
    print ("The dealer has a %s visible." %(dealer_top))
    
    #
    def score(hand):
        
        total = 0
        #sort cards so that A will always be last
        """ranks = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
        sorted(hand, key= ranks)"""
        for card in hand:
            if total > 10 and card[0] == 'A':
                total = total + 1
            else:        
                total = total + rank(card)
        return total
        
    
    # hit vs stay option
    while True:
        if score(player_hand)== 21:
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
        if score(player_hand) > 21:
            break
        elif score(dealer_hand) == 21:
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

    
    cont = raw_input("Would you like to play again? [y/n]: ")
    if cont == 'y':
        continue
    else:
        break

print "Score- "
print "Dealer: ", score_dealer
print "You: ", score_player
print "Thanks for playing!!!"
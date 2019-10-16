
# IMPORT STATEMENTS AND VARIABLE DECLARATIONS:

import random
from properties import *
from deck import Deck
from chips import Chips
from card import Card
from hand import Hand
from game_functionality import *

game_on = True


while True:
    print('Welcome to BlackJack! Aces count as 1 or 11.')
    
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    # Set up the Player's chips
    player_chips = Chips()  # remember the default value is 100
    
    # Prompt the Player for their bet:
    bet(player_chips)
    
    # Show the cards:
    show_some(player_hand,dealer_hand)
    
    while game_on:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
    
    # If Player hasn't busted, play Dealer's hand        
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
            
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Test different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)

    # Inform Player of their chips total    
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    if new_game[0].lower()=='y':
        game_on=True
        continue
    else:
        print("Thanks for playing")
        break
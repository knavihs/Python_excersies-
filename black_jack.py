import os
import random

class Card:
    def __init__(self,suit,card,card_value):
        self.suit=suit
        self.card=card
        self.card_value=card_value

def print_player_cards(player_cards):
    for cardo in player_cards:
        suit = cardo.suit
        card = cardo.card
        print(f'{suit}-->{card}\n')

def balckjack_game(deck):
    computer_cards = []
    player_cards = []
    comp_score = 0
    player_score = 0

    #randomly selecting two cards to start the game
    while len(player_cards) < 2:
        player_card = random.choice(deck)
        player_cards.append(player_card)
        player_score += player_card.card_value
        deck.remove(player_card)

        if len(player_cards)==2:
            if player_cards[0].card_value==11 and player_cards[1].card_value==11:
                player_cards[1].card_value = 1
                player_score -= 10

        print('Player cards:\n')
        print_player_cards(player_cards)
        print(f'player score:{player_score}')
        input()
        comp_card = random.choice(deck)
        computer_cards.append(comp_card)
        comp_score += comp_card.card_value
        deck.remove(comp_card)

        if len(computer_cards)==2:
            if computer_cards[0].card_value==11 and computer_cards[1].card_value==11:
                computer_cards[1].card_value = 1
                comp_score -= 10

            print("Computer's first card :")
            print(f'{computer_cards[0].suit} ---> {computer_cards[0].card}')

    if player_score==21:
        print('Player wins ---  Its a Blackjack!!')
        quit()

    while player_score < 21 :
        choice = input("Type 'H' to hit the deck or 'S' to stand your position \n")      

        if len(choice)>1 or (choice.upper() != 'H' and choice.upper() != 'S'):
            print("Invalide Choice, Please select 'H' to hit the deck or 'S' to stand your position \n")
            os.system("clear")
        
        if choice.upper() == 'H':
            player_card = random.choice(deck)
            player_cards.append(player_card)
            player_score += player_card.card_value
            deck.remove(player_card)

        n = 0
        while player_score > 21 and n < len(player_cards):
            if player_cards[n].card_value == 11 :
                player_cards[n].card_value = 1
                player_score -= 10
        
        os.system("clear")
        print("Players cards:")
        print_player_cards(player_cards)
        print(f'Players score {player_score}')

        if player_score == 21:
            print('Player wins ---  Its a Blackjack!!')
            quit()

        input()
        if choice.upper() == 'S':
            break
    
    while comp_score < 17:
        comp_card = random.choice(deck)
        computer_cards.append(comp_card)
        comp_score += comp_card.card_value
        deck.remove(comp_card)

        while comp_score > 21 and n < len(computer_cards):
            if computer_cards[n].card_value == 11 :
                computer_cards[n].card_value = 1
                comp_score -= 10

    if comp_score == player_score:
        print("Its a TIE")
    
    elif comp_score > player_score: 
        print("Computer wins")
    
    else: print("Player wins!!")

    if comp_score>21:
        print("Player wins!!")
        quit()

if __name__ =='__main__':
    suits=['spades','clubs','hearts','diamonds']
    cards=['A','K','Q','J','1','2','3','4','5','6','7','8','9','10']
    card_value={'A':11,'K':10,'Q':10,'J':10,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10}

    deck=[]

    for suit in suits:
        for card in cards:
            deck.append(Card(suit,card,card_value[card]))

    balckjack_game(deck)

    


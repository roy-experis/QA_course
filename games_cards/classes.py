class card:
    def __init__(self,value, suit):#makes the object card
        self.value=value
        self.suit=suit

    def __str__(self):
        return self.value + "" + self.suit

    def __repr__(self):
        return f' value: {self.value} suit: {self.suit}'

    # # def __eq__(self, other):
    # #     if(self.value==other.value and self.suit==other.suit):
    #         return True
    #     else:
    #         return False

    def return_biger_card(self, other_card):#returns the biger card between the 2 you send
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        suits = ['♦', '♠','♥', '♣']
        otherv = 0
        others = 0
        myv = 0
        mys = 0
        for i in range(0, 13):
            for j in range(0, 4):
                if (self.value == values[i]):
                    myv = i
                if (self.suit == suits[j]):
                    mys = j
                if (other_card.value == values[i]):
                    otherv = i
                if (other_card.suit == suits[j]):
                    others = j
        if (myv > otherv):
            return self
        elif (myv == otherv):
            if (mys > others):
                return self
            else:
                return other_card
        else:
            return other_card


import random
class DeckOfCards:

    def __init__(self):#makes a deck of cards
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        suites = ['♦', '♠','♥', '♣']
        self.deck=[]
        for i in values:
            for j in suites:
                c=card(i,j)
                self.deck.append(c)

    def __repr__(self):
        return f' deck of cards: {self.deck}'

    def shuflle(self):# shuflles the deck of cards
        if(len(self.deck)==52):
            random.shuffle(self.deck)

    def deal_one (self):# deals the last card of the deck
        if(len(self.deck)-1>=0):
            returned_card= self.deck [len(self.deck)-1]
            self.deck.remove(returned_card)
            return returned_card
        else:
            return "there are no cards in the deck"

    def newGame(self):#resets the deck
        self.deck=DeckOfCards()

    def show (self):#shows the card remaining in the deck by the order in the deck
        print(f' deck of cards: {self.deck}')


class player:
    def __init__(self,name,money):#sets a player
        self.name=name
        self.money=money
        self.cards=[]

    def send_hand(self,Deck,num_of_cards=5):#sends cards to the player
        # print("You got:")
        for i in range(num_of_cards):
            if (len(Deck.deck) > 0):
                self.cards.append(Deck.deal_one())
            if (len(Deck.deck)==0):
                print("the deck is empty")

    def get_card(self):#removes a random card from the player
        if(len(self.cards)>0):
            random.shuffle(self.cards)
            removed_card = self.cards[len(self.cards)-1]
            self.cards.remove(removed_card)
            return removed_card
        return "the player has no more cards"

    def add_card(self,DeckOfCards):#gives the player the last card of the deck
        self.cards.append(DeckOfCards.deal_one())

    def reduceAmount(self, amount_reduced):#thakes the amount of money you wont from the player
        if(self.money>=amount_reduced):
            self.money=self.money-amount_reduced

    def addAmount(self, amount_added):#gives the amount of money you wont from the player
        if(amount_added>=0):
            self.money = self.money+ amount_added

    def print(self):
        print( f'players name: {self.name} players amount of money: {self.money} players cards: {self.cards}')

class CardGame:#sets a card game
    def __init__(self,player1,player2,player3,player4,deck_of_cards,amount_of_cards_for_hich_player):
        self.player1=player1
        self.player2=player2
        self.player3=player3
        self.player4=player4
        self.amount_of_cards_for_hich_player=amount_of_cards_for_hich_player
        self.deck=deck_of_cards
        self.player1.send_hand(self.deck, amount_of_cards_for_hich_player)
        self.player2.send_hand(self.deck, amount_of_cards_for_hich_player)
        self.player3.send_hand(self.deck, amount_of_cards_for_hich_player)
        self.player4.send_hand(self.deck, amount_of_cards_for_hich_player)

    def newGame(self):#resets the card game
        self.deck.shuflle()
        self.player1.send_hand(self.deck, self.amount_of_cards_for_hich_player)
        self.player2.send_hand(self.deck, self.amount_of_cards_for_hich_player)
        self.player3.send_hand(self.deck, self.amount_of_cards_for_hich_player)
        self.player4.send_hand(self.deck, self.amount_of_cards_for_hich_player)

    # def return_winner(self): #returns the player whith the most money
    #     if(self.player1.money>self.player2.money and self.player1.money>self.player3.money and self.player1.money>self.player4.money):
    #         return self.player1
    #     if (self.player2.money > self.player1.money and self.player2.money > self.player3.money and self.player2.money > self.player4.money):
    #         return self.player2
    #     if (self.player3.money > self.player2.money and self.player3.money > self.player1.money and self.player3.money > self.player4.money):
    #         return self.player3
    #     if (self.player4.money > self.player2.money and self.player4.money > self.player3.money and self.player4.money > self.player1.money):
    #         return self.player4


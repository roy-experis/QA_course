from games_cards.classes import *

#######test player and deck#############
# deck1=DeckOfCards()
# print(deck1)
# deck1.shuflle()
# print(deck1)
# print(deck1.deal_one())
# print(deck1)
# deck1.shuflle()
# print(deck1)
# deck1.newGame()
# print(deck1)
# deck1.show()


#######test player ###########
# deck1=DeckOfCards()
# print(deck1)
# deck1.shuflle()
#
# Roy= player("roy",1000)
# Roy.send_hand(deck1)
# print(Roy.cards)
# Roy.get_card()
# print(Roy.cards)
# Roy.add_card(deck1)
# print(Roy.cards)
# Roy.reduceAmount(500)
# print(Roy.money)
# Roy.addAmount(5000)
# print(Roy.money)
# Roy.print()


########test card game#########
# deck1=DeckOfCards()
# print(deck1)
# deck1.shuflle()
# Roy= player("roy",1000)
# ori= player("ori",1000)
# bar=player("bar",1000)
# ziv=player("ziv",1000)
# classGame= CardGame(Roy,ori,bar,ziv,deck1,5)

#########main test###########
from random import randint
deck1=DeckOfCards()#sets a deck of cards
deck1.shuflle()#shuflles the deck of cards
amount=randint (5000,10000)#randomaise the amount of money for the players
Roy= player("roy",amount)#set player
ori= player("ori",amount)#set player
bar=player("bar",amount)#set player
ziv=player("ziv",amount)#set player
classGame= CardGame(Roy,ori,bar,ziv,deck1,5)#sets a game
bid=0#sets the bid

for i in range (5):#play 5 rounds
    bid = bid + 100#incrise the bid every round
    Roy.reduceAmount(bid)#takes the bid amount from the player
    ori.reduceAmount(bid)#takes the bid amount from the player
    bar.reduceAmount(bid)#takes the bid amount from the player
    ziv.reduceAmount(bid)#takes the bid amount from the player
    prize=bid*4#sets the prize for the round
    a= Roy.get_card()#takes a random card from the player for the round
    b=ori.get_card()#takes a random card from the player for the round
    c=bar.get_card()#takes a random card from the player for the round
    d=ziv.get_card()#takes a random card from the player for the round
    print("the loot for the round is:", prize)#prints the prize for the round
    print("the cards of the round are:" ,a ,b ,c ,d)#print the cards of the 4 players for the round
    if(a.return_biger_card(b)).return_biger_card(c.return_biger_card(d))==a:#checks if roy wins
        Roy.money=Roy.money+prize
        print(Roy.name,"won the round whit",a)
    if (a.return_biger_card(b)).return_biger_card(c.return_biger_card(d)) == b:#checks if ori wins
        ori.money = ori.money + prize
        print(ori.name, "won the round whit",b)
    if (a.return_biger_card(b)).return_biger_card(c.return_biger_card(d)) == c:#checks if bar wins
        bar.money = bar.money + prize
        print(bar.name, "won the round whit",c)
    if (a.return_biger_card(b)).return_biger_card(c.return_biger_card(d)) == d:#checks if ziv wins
        ziv.money = ziv.money + prize
        print(ziv.name, "won the round whit",d)

print("roy's money:",Roy.money)#prints the amount of money of roy at the end of the game
print("ori's money:", ori.money)#prints the amount of money of ori at the end of the game
print("bar's money:", bar.money)#prints the amount of money of bar at the end of the game
print("ziv's money:", ziv.money)#prints the amount of money of ziv at the end of the game

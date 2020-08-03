from unittest import TestCase, mock
from games_cards.classes import *
from unittest.mock import patch
class TestClasses(TestCase):
    def test_return_biger_card1(self):#c1 value bigger then c2 value
        c1= card(4,"♦")
        c2= card(2,"♠")
        self.assertTrue(c1.return_biger_card(c2))

    def test_return_biger_card2(self):#c1 value equals c2 value and c1 suit is biggerthen c2 suit
        c1 = card(4, "♣")
        c2 = card(4, "♠")
        self.assertTrue(c1.return_biger_card( c2))

    def test_return_biger_card3(self):#c2 value bigger then c1 value
        c1= card(3,"♦")
        c2= card(4,"♠")
        self.assertEqual(c1.return_biger_card(c2),c2)

    def test_return_biger_card4(self):#c2 value equals c1 value and c2 suit is biggerthen c1 suit
        c1= card(4,"♠")
        c2 = card(4, "♣")
        self.assertEqual(c1.return_biger_card(c2),c2)

    def test_shuffle(self):#checks if shuflles a full deck of cards
        deck1=DeckOfCards()
        deck2=deck1
        self.assertTrue(deck1.shuflle()!=deck2)

    def test_shuffle2(self):  # checks if dont shuflles a not full deck of cards
        deck1 = DeckOfCards()
        deck1.deal_one()
        deck2=deck1
        deck1.shuflle()
        self.assertTrue(deck1 == deck2)


    def test_deal_one(self): #checks if deal a card from a full deck of cards
        deck1 = DeckOfCards()
        deck1.deal_one()
        self.assertTrue(len(deck1.deck)==51)

    def test_deal_one2(self):  # checks if dont deal a card from a empty deck of cards
        deck1 = DeckOfCards()
        for i in range (52):
            deck1.deal_one()
        self.assertTrue(len(deck1.deck) == 0)

    def test_deal_one3(self):  # checks if dont deal a card from a empty deck of cards
        deck1 = DeckOfCards()
        for i in range(56):
            deck1.deal_one()
        self.assertTrue(len(deck1.deck) == 0)

    def test_deal_one4(self):#checks if return the correct output when deck if empty
        deck1 = DeckOfCards()
        for i in range(54):
            deck1.deal_one()
        self.assertTrue(deck1.deal_one()=="there are no cards in the deck")

    def test_deal_one5(self):#checks if return the correct card when deck if not empty
        deck1 = DeckOfCards()
        expected_card=deck1.deck[19]
        for i in range(32):
            deck1.deal_one()
        self.assertEqual(expected_card ,deck1.deal_one())

    def test_newGame(self):# checks if the after running the fonction you get a new deck of cards
        deck1 = DeckOfCards()
        deck2=deck1
        deck1.shuflle()
        for i in range(32):
            deck1.deal_one()
        deck1.newGame()
        self.assertTrue(deck1 == deck2)

    def test_newGame2(self):# checks if from a empty deck of cards after running the fonction you get a new deck of cards
        deck1 = DeckOfCards()
        deck2=deck1
        deck1.shuflle()
        for i in range(54):
            deck1.deal_one()
        deck1.newGame()
        self.assertTrue(deck1 == deck2)

    def test_newGame3(self):# checks if from a full deck of cards after running the fonction you get a new deck of cards
        deck1 = DeckOfCards()
        deck2=deck1
        deck1.shuflle()
        deck1.newGame()
        self.assertTrue(deck1 == deck2)

    def test_send_hand(self):#check if stop sending cards when deck is empty
        deck1 = DeckOfCards()
        Roy = player("roy", 5000)
        Roy.send_hand(deck1,60)
        self.assertTrue(len(deck1.deck)==0)

    def test_send_hand2(self):  # check if deals the correct amount of cards
        deck1 = DeckOfCards()
        Roy = player("roy", 5000)
        Roy.send_hand(deck1, 5)
        self.assertTrue(len(deck1.deck) ==47)

    def test_send_hand3(self):  # check if the fonction can get 0 for number of cards to deal
        deck1 = DeckOfCards()
        Roy = player("roy", 5000)
        Roy.send_hand(deck1, 0)
        self.assertTrue(len(deck1.deck) == 52)

    # def test_send_hand4(self):#checks the call of shuffle in new game
    #     # with patch('games_cards.classes.DeckOfCards.deal_one') as mockdeal1:
    #     card1=card(4, "♣")
    #     # mockdeal1.return_value=card1
    #     deck1 = DeckOfCards()
    #     deck1.newGame()
    #     Roy = player("roy", 5000)
    #     Roy.send_hand(deck1,1)
    #     self.assertTrue(True)
    #     # self.assertEqual(Roy.cards[0],card1)
    def test_send_hand4(self):
        with patch('games_cards.classes.DeckOfCards.deal_one') as mockdeal1:
            card1=card(4, "♣")
            mockdeal1.return_value=card1
            deck1 = DeckOfCards()
            Roy = player("roy", 5000)
            Roy.send_hand(deck1,1)
            self.assertEqual(Roy.cards[0],card1)

    def test_send_hand5(self):
        with patch('games_cards.classes.DeckOfCards.deal_one') as mockdeal2:
            card1 = None
            mockdeal2.return_value = card1
            deck1 = DeckOfCards()
            Roy = player("roy", 5000)
            Roy.send_hand(deck1, 1)
            self.assertEqual(Roy.cards[0], card1)


    def test_get_card(self):#checks if takes one card from the players hand
        deck1 = DeckOfCards()
        Roy = player("roy", 5000)
        Roy.send_hand(deck1, 5)
        Roy.get_card()
        self.assertTrue(len(Roy.cards)==4)

    def test_get_card2(self):#checks if dont takes a card from a players empty hand
        deck1 = DeckOfCards()
        Roy = player("roy", 5000)
        Roy.send_hand(deck1, 0)
        Roy.get_card()
        self.assertTrue(len(Roy.cards)==0)

    def test_get_card3(self):#checks if dont takes a card from a players empty hand
        deck1 = DeckOfCards()
        Roy = player("roy", 5000)
        Roy.send_hand(deck1, 0)
        self.assertTrue(Roy.get_card()=="the player has no more cards")

    def test_get_card4(self):
        with patch('games_cards.classes.player.send_hand') as mockget1:
            deck1 = DeckOfCards()
            Roy = player("roy", 5000)
            card1 = None
            mockget1.return_value = card1
            Roy.send_hand(deck1, 0)
            self.assertTrue(Roy.get_card() == "the player has no more cards")

    def test_reduce_amount(self):#checks if reduces the correct amount
        Roy = player("roy", 5000)
        Roy.reduceAmount(2000)
        self.assertTrue(Roy.money==3000)

    def test_reduce_amount2(self):#checks if dont reduces the amount from a player that has not inough money
        Roy = player("roy", 5000)
        Roy.reduceAmount(6000)
        self.assertTrue(Roy.money==5000)

    def test_reduce_amount3(self):  # checks if reduces the exact amount of money from a player
        Roy = player("roy", 5000)
        Roy.reduceAmount(5000)
        self.assertTrue(Roy.money == 0)

    def test_add_amount(self):#checks if the amount added is correct
        Roy = player("roy", 5000)
        Roy.addAmount(5000)
        self.assertTrue(Roy.money == 10000)

    def test_add_amount2(self):#check if add 0 to the amount
        Roy = player("roy", 5000)
        Roy.addAmount(0)
        self.assertTrue(Roy.money == 5000)

    def test_add_amount3(self):  # check if dont add a negative amount
        Roy = player("roy", 5000)
        Roy.addAmount(-5000)
        self.assertTrue(Roy.money == 5000)

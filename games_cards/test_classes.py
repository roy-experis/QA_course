from unittest import TestCase
from games_cards.classes import *
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
        self.assertEqual(deck1.shuflle()!=deck2,True)

    # def test_shuffle2(self):  # checks if dont shuflles a not full deck of cards
    #     deck1 = DeckOfCards()
    #     deck1.deal_one()
    #     deck2=deck1
    #     self.assertEqual(deck1.shuflle() == deck2, True)
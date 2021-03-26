import random as r

ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'T', 'J', 'Q', 'K']
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']


class Deck_is_not_a_list(Exception):
    def __str__(self):
        return('The entered deck is not a list or there are cards not being tuples')


class WrongDeck(Exception):
    def __str__(self):
        return('Please enter card values properly (e.g. {\'A\', \'Clubs\'}')


class RepeatingCards(Exception):
    def __str__(self):
        return('Please enter non-repeating cards')          


class Deck:
    def __init__(self, cards = []):
        try:
            self.cards = list(cards)
            a = len(self.cards)
            while a != 0:
                for i in self.cards:
                    if isinstance(i, tuple):
                        a -= 1
                    else:
                        raise Deck_is_not_a_list
                        break
            else:
                for i in self.cards:
                    if not i[0] in ranks:
                        raise WrongDeck
                        break
                    else:
                        if not i[1] in suits:
                            raise WrongDeck
                            break
        except ValueError:
            raise Deck_is_not_a_list
        for woman in self.cards:
            dababy = self.cards.index(woman) + 1
            if woman in self.cards[dababy:]:
                raise RepeatingCards
    
    def shuffle(self):
        new_deck = []
        a = len(self.cards)
        while a != 0:
            hot_popcorn = r.randint(0, a)
            pol_doma_mne_vzorval = self.cards[hot_popcorn]
            new_deck.append(pol_doma_mne_vzorval)
            a -= 1
        return new_deck
    
dek = Deck([('10', 'Diamonds'), ('9', 'Clubs')])
print(dek.shuffle())
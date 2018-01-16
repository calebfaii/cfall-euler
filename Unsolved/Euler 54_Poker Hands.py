# In the card game poker, a hand consists of five cards and are ranked,
# from lowest to highest, in the following way:
#
#     High Card: Highest value card.
#     One Pair: Two cards of the same value.
#     Two Pairs: Two different pairs.
#     Three of a Kind: Three cards of the same value.
#     Straight: All cards are consecutive values.
#     Flush: All cards of the same suit.
#     Full House: Three of a kind and a pair.
#     Four of a Kind: Four cards of the same value.
#     Straight Flush: All cards are consecutive values of same suit.
#     Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
#
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
#
# If two players have the same ranked hands then the rank made up of the
# highest value wins; for example, a pair of eights beats a pair of fives.
# But if two ranks tie, for example, both players have a pair of queens, then
# highest cards in each hand are compared (see example 4 below); if the highest
# cards tie then the next highest cards are compared, and so on.

# The file, poker.txt, contains one-thousand random hands dealt to two players. Each
# line of the file contains ten cards (separated by a single space): the first five
# are Player 1's cards and the last five are Player 2's cards. You can assume that all
# hands are valid (no invalid characters or repeated cards), each player's hand is in
# no specific order, and in each hand there is a clear winner.
#
# How many hands does Player 1 win?


# Import all
# Split each hand into tuples - value and suit
# Divide hands by round and player
# Find the highest hand that each player has
# if there is a tie, check the card value
# if there is no hand for either player, pull high card
# if high cards match, it's a tie

class Game(object):

    def __init__(self):

        self.all_hands = self.import_hands()
        self.enumerate_hands = enumerate(self.all_hands)

        self.player_1_wins = 0
        self.player_2_wins = 0
        self.ties = 0

    @staticmethod
    def import_hands():

        hands = []
        textfile = 'p054_poker.txt'

        with open(textfile, 'r') as text:
            for line in text:
                hands.append(line.strip('\n').split(' '))
        return hands

    @staticmethod
    def allocate_hands_to_players(hand):

        hands_for_this_round = []
        player_1 = hand[0:5]
        player_2 = hand[5:10]
        hands_for_this_round.append(player_1)
        hands_for_this_round.append(player_2)
        return hands_for_this_round

    def capture_score(self, winner):

        if winner == 'P1':
            self.player_1_wins += 1

        if winner == 'P2':
            self.player_2_wins += 1

        if winner == 'T':
            self.ties += 1

    def execute(self):

        for index, hand in self.enumerate_hands:
            this_round = Round(index, self.allocate_hands_to_players(hand))
            this_round.score_hand()
            winner = this_round.get_winner()
            self.capture_score(winner)

    def return_results(self):

        print "Player 1 wins: ", self.player_1_wins
        print "Player 2 wins: ", self.player_2_wins
        print "Ties: ", self.ties


class Hand(object):

    def __init__(self, hand):

        self.hand = hand
        self.suits = self.create_set_of_suits()
        self.cards = sorted(i[0] for i in self.hand)
        self.high_card = max(self.cards)
        self.low_card = min(self.cards)
        self.score = None
        self.rank = None

    def create_set_of_suits(self):

        suits = set()
        for card in self.hand:
            suits.add(card[1])
        return suits

    def check_royal_flush(self):

        if self.score == None:
            royal_flush = set(i for i in range(10, 15))
            if len(self.suits) == 1:
                if royal_flush == set(i for i in self.cards):
                    self.score = 1

    def check_straight_flush(self):

        if self.score == None:
            if self.low_card + 4 == self.high_card:
                self.score = 2
                self.rank = self.high_card

    def check_four_of_a_kind(self):

        if self.score == None:
            for card in self.cards:
                count = self.cards.count(card)
                if count == 4:
                    self.score = 3
                    self.rank = card

    def check_full_house(self):

        if self.score == None:
            if len(set(self.cards)) == 2:
                a, b = self.cards[0], self.cards[1]
                count_a = self.cards.count(a)
                count_b = self.cards.count(b)
                if (count_a == 2 and count_b == 3) or (count_a == 3 and count_b == 2):
                    self.score = 4
                    self.rank = self.high_card

    def check_flush(self):

        if self.score == None:
            if len(self.suits) == 1:
                self.score = 5

    def check_straight(self):

        if self.score == None:
            if self.low_card + 4 == self.high_card:
                self.score = 6

    def check_three_of_a_kind(self):

        if self.score == None:
            if len(set(self.cards)) == 2 or len(set(self.cards)) == 3:
                for i in self.cards:
                    count_card = self.cards.count(i)
                    if count_card == 3:
                        self.score = 7
                        self.rank = i

    def check_two_pairs(self):

        if self.score == None:
            if len(set(self.cards)) == 2:
                self.score = 8
                self.rank = self.high_card

            if len(set(self.cards)) == 3:
                self.score = 8
                if self.cards.count(self.high_card) > 1:
                    self.rank = self.high_card
                else:
                    second_max = sorted(set(self.cards))[-2]
                    self.rank = second_max


    def check_pair(self):

        if self.score == None:
            for card in self.cards:
                if self.cards.count(card) == 2:
                    self.score = 9
                    self.rank = card

    def check_all(self):

        self.check_royal_flush()
        self.check_straight_flush()
        self.check_four_of_a_kind()
        self.check_full_house()
        self.check_flush()
        self.check_straight()
        self.check_three_of_a_kind()
        self.check_two_pairs()
        self.check_pair()

class Round(object):

    def __init__(self, round_number, hands_for_this_round):

        self.round_number = round_number
        self.winner = None
        self.player_1_hand = Hand(self.convert_to_values(hands_for_this_round[0]))
        self.player_2_hand = Hand(self.convert_to_values(hands_for_this_round[1]))

    def set_winner(self, winner):

        self.winner = winner

    def get_winner(self):

        return self.winner

    @staticmethod
    def convert_to_values(hand):

        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                  '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

        adjusted_hand = []

        for card in hand:
            card_value = values.get(card[0])
            card_suit = card[1]
            adjusted_hand.append([card_value, card_suit])

        return adjusted_hand

    def compare_high_cards(self):

        index = 4
        while index >= 0:
            p1 = self.player_1_hand.hand[index]
            p2 = self.player_2_hand.hand[index]
            if p1 > p2:
                return 'P1'
            if p1 < p2:
                return 'P2'
            if p1 == p2:
                index -= 1
        return 'T'


    def score_hand(self):

        self.player_1_hand.check_all()
        self.player_2_hand.check_all()

        # We have to score hands if they exist; otherwise, follow default poker rules.

        if self.player_1_hand.score and self.player_2_hand.score:  # If both players have a legal hand:

            if self.player_1_hand.score < self.player_2_hand.score:  # If player 1's hand wins
                winner = 'P1'
                self.set_winner(winner)
                return

            if self.player_1_hand.score > self.player_2_hand.score:  # If player 2's hand wins
                winner = 'P2'
                self.set_winner(winner)
                return

            if self.player_1_hand.score == self.player_2_hand.score:  # If they tie hands, default to hand values

                if self.player_1_hand.rank > self.player_2_hand.rank:  # If player 1 has better rank
                    winner = 'P1'
                    self.set_winner(winner)
                    return

                if self.player_1_hand.rank < self.player_2_hand.rank:# If player 2 has better rank
                    winner = 'P2'
                    self.set_winner(winner)
                    return

                if self.player_1_hand.rank == self.player_2_hand.rank:  # If both players have identical rank:

                    if self.player_1_hand.high_card > self.player_2_hand.high_card:  # Player 1 has high card
                        winner = 'P1'
                        self.set_winner(winner)
                        return

                    if self.player_1_hand.high_card < self.player_2_hand.high_card:  # Player 2 has high card
                        winner = 'P2'
                        self.set_winner(winner)
                        return

                    if self.player_1_hand.high_card == self.player_2_hand.high_card:  # Matching high card
                        winner = 'T'
                        self.set_winner(winner)
                        return

                else:
                    print "Conditioned not handled."
                    print "Player 1 hand: ", self.player_1_hand
                    print "Player 2 hand: ", self.player_2_hand


        if self.player_1_hand.score and not self.player_2_hand.score:  # If player 1 has a hand but not player 2
            winner = 'P1'
            self.set_winner(winner)
            return

        if self.player_2_hand.score and not self.player_1_hand.score:  # If player 2 has a hand but not player 1
            winner = 'P2'
            self.set_winner(winner)
            return

        if not self.player_1_hand.score and not self.player_2_hand.score:  # If neither player has a hand

            high_card_winner = self.compare_high_cards() # Compare high cards, then second highest, etc.

            if high_card_winner == 'P1':
                winner = 'P1'
                self.set_winner(winner)
                return

            if high_card_winner == 'P2':
                winner = 'P2'
                self.set_winner(winner)
                return

            if high_card_winner == 'T':
                winner = 'T'
                self.set_winner(winner)
                return

        else:
            print "Conditioned not handled."
            print "Player 1 hand: ", self.player_1_hand
            print "Player 2 hand: ", self.player_2_hand


game = Game()
game.execute()
game.return_results()
print 'ok'
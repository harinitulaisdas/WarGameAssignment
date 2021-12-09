import random

CARD_VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
SUITS = (" ♣", " ♦", " ♥", " ♠")


class Deck:
    """deck of cards"""
    cards = []
    def __init__(self):
        self.cards = [(i,j) for i in CARD_VALUES for j in SUITS]

    def shuffle(self):
        """shuffle the deck"""
        random.shuffle(self.cards)

    def deal_cards(self):
        """return card from top of the list"""
        return self.cards.pop(0)


class Player():

    def __init__(self, name):
        self.name = name
        self.deck = []
        self.war_count = 0

    def cards_on_hand(self):
        """
        :return: number of cards on hand
        """
        return len(self.deck)

    def add_cards(self, card):
        """
        adds card/cards to end of the deck
        """
        if(type(card)== list):
            self.deck.extend(card)
        else:
            self.deck.append(card)

    def has_enough_cards(self):
        """ Check if the players have enough cards to continue the game"""
        return True if len(self.deck) > 4 else False

    def update_war_count(self):
        """ Update the counter every time the player wins a war """
        self.war_count+=1

    def wars_won(self):
        """ return: count of number of times a player won a war during the entire game."""
        return "Player {} has won a war {} times ".format(self.name, self.war_count)

    def play_a_card(self):
        """ Removes a card from top of the deck"""
        return self.deck.pop(0)

    def remove_war_cards(self):
        """ removes 3 cards from top of the deck and returns them as a list"""
        war_cards = self.deck[:3]
        self.deck = self.deck[3:]
        return war_cards

    def get_name(self):
        return self.name

class Game:
    #war_cards : Holds the cards during a war(2 cards that caused a war, 3 cards from each player that were faced down)
    war_cards = []
    game_count =0
    def __init__(self):
        """game cards: cards during the current round pf game. """
        self.game_cards = []


    def add_war_cards(self, cards):
        """Update the war cards list"""
        self.war_cards.extend(cards)

    def get_war_cards(self):
        """ return war cards. """
        return self.war_cards

    def add_game_cards(self, card):
        """ add card to the list """
        self.game_cards.append(card)

    def get_game_cards(self):
        """ return the cards played in the current round"""
        return self.game_cards

    def clear_war_cards(self):
        """ empty the list holding war cards"""
        self.war_cards.clear()


def get_rank(card):
    """Return the value of the card."""
    return  CARD_VALUES.index(card[0])

# def adjust_cards_after_war(player):
#     if player ==1 :
#


def war_game():
    count = 0
    while Player1.has_enough_cards() and Player2.has_enough_cards() and count < MAX_GAME_COUNT:
        # Game object which simulates the table
        WarGame = Game()
        count += 1
        global war
        card1 = Player1.play_a_card()
        card2 = Player2.play_a_card()
        print("The cards played by each player : ")
        print("Player {} : {}".format(Player1.get_name(),card1))
        print("Player {} : {}".format(Player2.get_name(),card2))

        #update the game/table with game cards.
        WarGame.add_game_cards(card1)
        WarGame.add_game_cards(card2)

       #check if there is a war. In case of war,

        if  get_rank(card1) == get_rank(card2):
            print('*' * 17, "Players are at WAR!!", '*' * 17)
            war = True
            WarGame.add_war_cards(WarGame.get_game_cards())
            WarGame.add_war_cards(Player1.remove_war_cards())
            WarGame.add_war_cards(Player2.remove_war_cards())
        else:
        #compare the card values and decide who gets the cards. If there was a war in the previous round, the player who
        #has the card with highest value in the current round gets all the cards from the previous round and the current round.
            if get_rank(card1) > get_rank(card2):
                print("Player 1 wins the round and gets all the cards!!")
                if war:
                        Player1.update_war_count()
                        Player1.add_cards(WarGame.get_war_cards())
                        Player1.add_cards(WarGame.get_game_cards())
                        WarGame.clear_war_cards()
                        war = False
                        print('-' * 55)
                else:
                    Player1.add_cards(WarGame.get_game_cards())
                    player_stat()
                    print('-' * 55)
            else:
                print("Player 2 wins the round and gets all the cards!!")
                if war:
                        Player2.update_war_count()
                        Player2.add_cards(WarGame.get_war_cards())
                        Player2.add_cards(WarGame.get_game_cards())
                        WarGame.clear_war_cards()
                        war = False
                        print('-' * 55)
                else:
                    Player2.add_cards(WarGame.get_game_cards())
                    player_stat()
                    print('-' * 55)
    return count

def player_stat():
    """
    Print the number of cards held by each player.
    :return:
    """
    print("Player {} has {} cards on hand".format(Player1.get_name(),Player1.cards_on_hand()))
    print("Player {} has {} cards on hand".format(Player2.get_name(),Player2.cards_on_hand()))

MAX_GAME_COUNT = 1000
war = False

if __name__ == '__main__':

    # Generate the deck and shuffle the cards.
    MainDeck = Deck()
    MainDeck.shuffle()


    # initialize the players
    # name1 = input("Enter Player 1 name : ")
    Player1 = Player("One")
    # name2 = input("Enter Player 2 name : ")
    Player2 = Player("Two")


    # Deal cards to each Player
    for i in range(26):
        Player1.add_cards(MainDeck.deal_cards())
        Player2.add_cards(MainDeck.deal_cards())


    #Start game
    count = war_game()
    print('*' * 20, "GAME ENDS!!", '*' * 23)
    print("Players do not have enough cards to continue")
    winner = Player1.get_name() if Player1.cards_on_hand() > Player2.cards_on_hand() else Player2.get_name()
    print('-'*55)
    print("WINNER IS : Player", winner)
    print('-' * 55)
    print("Stats : ")
    player_stat()
    print("The game was played :", count, " number of times")
    print(Player1.wars_won())
    print(Player2.wars_won())
    print('*' * 55)



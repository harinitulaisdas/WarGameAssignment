"""
Assumptions:
Suits are ignored.
The card values are used for comparison.
The top card of the deck is represented by the left most element of the list.
Eg : Player 1 ['A','5','4'] :
     'A' is considered as the card at the top of the deck.

During each battle.
"""
import random

CARD_VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
SUITS = (" ♣"," ♦"," ♥"," ♠")
MAX_GAME_COUNT = 1000

def PrepareDeck():
    """
    Generates the deck of cards, shuffles it before dealing them to the two players
    """
    Deck = [(i,j) for i in CARD_VALUES for j in SUITS]
    random.shuffle(Deck)
    player1_deck, player2_deck = [], []
    for i in range(26):
        player1_deck.append(Deck.pop(0))
        player2_deck.append(Deck.pop(0))
    return  player1_deck,player2_deck


def DecideWinner():
    """
    The method to decide the winner of the game. The player with more cards on hand is declared the winner.
    :return:
    """
    print('*' * 20, "WAR ENDS!!", '*' * 23)
    print("Players do not have minimum number of cards needed to play")
    print("Player 1 has :", len(player1_deck), " cards")
    print("Player 2 has :", len(player2_deck), " cards")
    winner = "Player 1" if len(player1_deck) > len(player2_deck) else "Player 2 "
    print("The game was played :", str(games_played), " number of times")
    print("The winner is :", winner)
    print('*' * 55)


def WarGame():
    """
    This method plays the game of war.

    During a round of game, each Player plays one card and the player who has the card with higher value gets all the cards. If both the cards are of same value,
    then there is a war. In case of a war, both the players place the next three cards face down and another card face-up. The player with
    higher face-up card wins the war and gets all the 10 cards.

    Entry condition: The game is played when each player has atleast 4 cards since each player needs 4 cards during a war(3 face down and one face up)

    winning criteria: The player with more cards on hand will be declared the winner. The cards on table arent considered during the
    decision.
    """
    rounds = 0
    while len(player1_deck) > 4 and len(player2_deck) > 4 and rounds < MAX_GAME_COUNT:
        rounds+=1
        print("Player 1 has :", len(player1_deck), " cards")
        print("Player 2 has :", len(player2_deck), " cards")
        global war
        card1 = player1_deck.pop(0)
        card2 = player2_deck.pop(0)
        print('*' * 20, "New Battle", '*' * 23)
        print("The cards played by each player : ")
        print("Player 1  :  ", card1)
        print("Player 2  :  ", card2)
        print('-' * 55)
        # game_cards [] - list to hold the cards played by each player at every battle/round of game.
        game_cards = []
        game_cards.append(card1)
        game_cards.append(card2)
        # check if there is a war
        if CARD_VALUES.index(card1[0]) == CARD_VALUES.index(card2[0]):
            print('*' * 17, "Players are at WAR!!", '*' * 17)
            war = True
            war_cards.extend(game_cards)
            for i in range(3):
                war_cards.append(player1_deck.pop(0))
                war_cards.append(player2_deck.pop(0))
        else:
            if CARD_VALUES.index(card1[0]) > CARD_VALUES.index(card2[0]):
                print( "Player 1 wins the round and gets all the cards!!")
                if war:
                    player1_deck.extend(war_cards)
                    war_cards.clear()
                    war = False
                player1_deck.extend(game_cards)
            else:
                print("Player 2 wins the round and gets all the cards!!")
                if war:
                    player2_deck.extend(war_cards)
                    war_cards.clear()
                    war = False
                player2_deck.extend(game_cards)
    return rounds

def Status():
    """
    Utility method to know the cards on hand and on the table during the game.
    :return:
    """
    print("Player 1 deck :")
    print(player1_deck)
    print("Player 2 deck :")
    print(player2_deck)
    print("war cards/cards on the table: ", war_cards)
    print("Player 1 has :", len(player1_deck), " cards")
    print("Player 2 has :", len(player2_deck), " cards")


if __name__ == '__main__':
    print("******************Welcome to the game of WAR*********************************")
    # war_cards : hold the cards on the table during a war
    war_cards = []
    # deck of cards for each player
    player1_deck, player2_deck = PrepareDeck()
    # war : to hold the status if there was a war.
    war = False
    #A counter to keep track of number of times the game is played.
    games_played = WarGame()
    DecideWinner()

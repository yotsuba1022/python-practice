from game.blackjack.component.deck import Deck
from game.blackjack.component.hand import Hand
from game.blackjack.component.game_operation import deal_cards


def intro():
    statement = '''Welcome to BlackJack! Get as close to 21 as you can without going over!
    Dealer hits until she reaches 17. Aces count as 1 or 11.
    Card output goes a letter followed by a number of face notation'''
    print(statement)


def main():
    # Create a Deck
    deck = Deck()
    # Shuffle it
    deck.shuffle()
    # Create player and dealer hands
    player_hand = Hand()
    dealer_hand = Hand()
    # Print the intro
    intro()
    # Deal out the cards and start the game!
    deal_cards()


if __name__ == '__main__':
    main()

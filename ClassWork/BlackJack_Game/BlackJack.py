import random


values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
         'Queen', 'King', 'Ace')


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.all_cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.money = 100
        self.bet = 0

    def place_bet(self, amount):
        if amount <= self.money:
            self.bet = amount
            self.money -= amount
            return True
        else:
            return False

    def receive_card(self, card):
        self.hand.append(card)

    def calculate_hand_value(self):
        value = sum(card.value for card in self.hand)
        for card in self.hand:
            if card.rank == 'Ace' and value > 21:
                value -= 10
        return value


def blackjack_game():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    dealer = Player("Dealer")
    deck = Deck()
    deck.shuffle()

    while True:
        print(f"\n{player_name}'s Money: ${player.money}")
        bet = int(input("Place your bet: $"))
        if not player.place_bet(bet):
            print("Insufficient funds. Try a lower bet.")
            continue

        for _ in range(2):
            player.receive_card(deck.deal_one())
            dealer.receive_card(deck.deal_one())
        while True:
            print("\nYour Hand:")
            for card in player.hand:
                print(card)
            print(f"Total Value: {player.calculate_hand_value()}")
            action = input("Do you want to 'hit' or 'stand'? ").lower()
            if action == 'hit':
                player.receive_card(deck.deal_one())
                if player.calculate_hand_value() > 21:
                    print("Bust! You lose.")
                    break
            elif action == 'stand':
                while dealer.calculate_hand_value() < 17:
                    dealer.receive_card(deck.deal_one())
                print("\nDealer's Hand:")
            for card in dealer.hand:
                print(card)
            print(f"Total Value: {dealer.calculate_hand_value()}")
            if dealer.calculate_hand_value() > 21 or dealer.calculate_hand_value() < player.calculate_hand_value():
                print("You win!")
                player.money += 2 * player.bet
            elif dealer.calculate_hand_value() > player.calculate_hand_value():
                print("Dealer wins.")
            else:
                print("It's a tie.")
            break
        else:
            print("Invalid input. Enter 'hit' or 'stand'.")
            player.hand.clear()
        dealer.hand.clear()

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing!")


if __name__ == "__main__":
    blackjack_game()

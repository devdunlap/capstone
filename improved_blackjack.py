"""
Improved Blackjack Implementation
Demonstrates better design patterns and proper game logic
"""
import random
from enum import Enum
from typing import List, Optional

class Suit(Enum):
    HEARTS = "♥"
    DIAMONDS = "♦"
    CLUBS = "♣"
    SPADES = "♠"

class Card:
    def __init__(self, rank: str, suit: Suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        return f"{self.rank}{self.suit.value}"
    
    def get_value(self) -> int:
        """Get the base value of the card (before Ace adjustment)"""
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11
        else:
            return int(self.rank)

class Deck:
    def __init__(self):
        self.cards: List[Card] = []
        self.reset_deck()
    
    def reset_deck(self):
        """Create a fresh shuffled deck"""
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(rank, suit) for suit in Suit for rank in ranks]
        random.shuffle(self.cards)
    
    def deal_card(self) -> Card:
        """Deal one card from the deck"""
        if len(self.cards) < 10:  # Reshuffle when running low
            self.reset_deck()
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards: List[Card] = []
    
    def add_card(self, card: Card):
        """Add a card to the hand"""
        self.cards.append(card)
    
    def calculate_score(self) -> int:
        """Calculate the best possible score for the hand"""
        score = 0
        aces = 0
        
        for card in self.cards:
            if card.rank == 'A':
                aces += 1
                score += 11
            else:
                score += card.get_value()
        
        # Adjust for Aces (convert from 11 to 1 as needed)
        while score > 21 and aces > 0:
            score -= 10
            aces -= 1
        
        return score
    
    def is_blackjack(self) -> bool:
        """Check if hand is a natural blackjack (21 with 2 cards)"""
        return len(self.cards) == 2 and self.calculate_score() == 21
    
    def is_bust(self) -> bool:
        """Check if hand is over 21"""
        return self.calculate_score() > 21
    
    def __str__(self):
        card_names = [str(card) for card in self.cards]
        return f"{card_names} (Score: {self.calculate_score()})"

class Player:
    def __init__(self, name: str, money: float = 1000.0):
        self.name = name
        self.hand = Hand()
        self.money = money
        self.current_bet = 0
    
    def reset_hand(self):
        """Reset hand for new game"""
        self.hand = Hand()
    
    def place_bet(self, amount: float) -> bool:
        """Place a bet if player has enough money"""
        if amount <= self.money:
            self.current_bet = amount
            self.money -= amount
            return True
        return False
    
    def win_bet(self, multiplier: float = 1.0):
        """Win the bet (multiplier 1.5 for blackjack, 1.0 for regular win)"""
        winnings = self.current_bet * (1 + multiplier)
        self.money += winnings
        self.current_bet = 0
        return winnings
    
    def lose_bet(self):
        """Lose the bet (money already deducted)"""
        self.current_bet = 0
    
    def push_bet(self):
        """Push (tie) - return the bet"""
        self.money += self.current_bet
        self.current_bet = 0

class Dealer:
    def __init__(self):
        self.hand = Hand()
    
    def reset_hand(self):
        """Reset hand for new game"""
        self.hand = Hand()
    
    def should_hit(self) -> bool:
        """Dealer hits on 16 and below, stands on 17 and above"""
        return self.hand.calculate_score() < 17
    
    def show_partial_hand(self) -> str:
        """Show only the first card (second card hidden)"""
        if len(self.hand.cards) >= 1:
            return f"[{self.hand.cards[0]}, Hidden]"
        return "[]"

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.dealer = Dealer()
    
    def start_new_game(self):
        """Start a new game round"""
        # Reset hands
        self.player.reset_hand()
        self.dealer.reset_hand()
        
        # Get bet
        while True:
            try:
                bet = float(input(f"Place your bet (You have ${self.player.money:.2f}): $"))
                if self.player.place_bet(bet):
                    break
                else:
                    print("Insufficient funds!")
            except ValueError:
                print("Please enter a valid amount.")
        
        # Deal initial cards
        for _ in range(2):
            self.player.hand.add_card(self.deck.deal_card())
            self.dealer.hand.add_card(self.deck.deal_card())
        
        # Show initial hands
        print(f"\nPlayer: {self.player.hand}")
        print(f"Dealer: {self.dealer.show_partial_hand()}")
        
        # Check for natural blackjacks
        if self.player.hand.is_blackjack() and self.dealer.hand.is_blackjack():
            self.end_game("push", "Both have Blackjack! It's a push.")
            return
        elif self.player.hand.is_blackjack():
            self.end_game("blackjack", "Blackjack! You win!")
            return
        elif self.dealer.hand.is_blackjack():
            self.end_game("lose", "Dealer has Blackjack! You lose.")
            return
        
        # Player's turn
        while not self.player.hand.is_bust():
            choice = input("\nHit (h) or Stand (s)? ").lower()
            if choice == 'h':
                self.player.hand.add_card(self.deck.deal_card())
                print(f"Player: {self.player.hand}")
                if self.player.hand.is_bust():
                    self.end_game("lose", "Bust! You lose.")
                    return
            elif choice == 's':
                break
            else:
                print("Please enter 'h' for hit or 's' for stand.")
        
        # Dealer's turn
        print(f"\nDealer reveals: {self.dealer.hand}")
        while self.dealer.should_hit():
            self.dealer.hand.add_card(self.deck.deal_card())
            print(f"Dealer hits: {self.dealer.hand}")
        
        # Determine winner
        player_score = self.player.hand.calculate_score()
        dealer_score = self.dealer.hand.calculate_score()
        
        if self.dealer.hand.is_bust():
            self.end_game("win", "Dealer busts! You win!")
        elif player_score > dealer_score:
            self.end_game("win", "You win!")
        elif player_score < dealer_score:
            self.end_game("lose", "Dealer wins!")
        else:
            self.end_game("push", "It's a push!")
    
    def end_game(self, result: str, message: str):
        """End the game and handle payouts"""
        print(f"\n{message}")
        
        if result == "blackjack":
            winnings = self.player.win_bet(1.5)
            print(f"You won ${winnings:.2f}!")
        elif result == "win":
            winnings = self.player.win_bet(1.0)
            print(f"You won ${winnings:.2f}!")
        elif result == "lose":
            self.player.lose_bet()
            print(f"You lost ${self.player.current_bet:.2f}.")
        elif result == "push":
            self.player.push_bet()
            print("Your bet is returned.")
        
        print(f"Current balance: ${self.player.money:.2f}")

def main():
    """Main game loop"""
    print("Welcome to Improved Blackjack!")
    game = BlackjackGame()
    
    while True:
        if game.player.money <= 0:
            print("You're out of money! Game over.")
            break
        
        play_again = input("\nDo you want to play a hand? (y/n): ").lower()
        if play_again != 'y':
            break
        
        game.start_new_game()
    
    print(f"Thanks for playing! Final balance: ${game.player.money:.2f}")

if __name__ == "__main__":
    main()

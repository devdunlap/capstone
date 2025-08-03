"""
Blackjack Card Game

A console-based implementation of the classic Blackjack card game.
Players try to get as close to 21 as possible without going over.
"""
import os
import random
import art

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


# Global constants should be in UPPER_CASE
CARDS = [
    {"name": "A", "value": 11},     # Ace
    {"name": "2", "value": 2},      # Two
    {"name": "3", "value": 3},      # Three
    {"name": "4", "value": 4},      # Four
    {"name": "5", "value": 5},      # Five
    {"name": "6", "value": 6},      # Six
    {"name": "7", "value": 7},      # Seven
    {"name": "8", "value": 8},      # Eight
    {"name": "9", "value": 9},      # Nine
    {"name": "10", "value": 10},    # Ten
    {"name": "J", "value": 10},     # Jack
    {"name": "Q", "value": 10},     # Queen
    {"name": "K", "value": 10}      # King
]


def deal_card():
    """Returns a random card from the deck."""
    return random.choice(CARDS)

def calculate_score(hand):
    """Calculates the score of a hand."""
    score = sum(card["value"] for card in hand)
    # Adjust for Aces if score exceeds 21
    if score > 21 and any(card["name"] == "A" for card in hand):
        score -= 10
    return score


def format_cards(hand):
    """Format cards for better display."""
    return [card['name'] for card in hand]


def display_hands(player_hand, computer_hand, player_score, show_computer_all=False):
    """Display both hands in a formatted way."""
    print("\n" + "="*50)
    print(f"🃏 YOUR CARDS: {format_cards(player_hand)} | Score: {player_score}")

    if show_computer_all:
        computer_score = calculate_score(computer_hand)
        print(f"🤖 COMPUTER CARDS: {format_cards(computer_hand)} | Score: {computer_score}")
    else:
        print(f"🤖 COMPUTER CARDS: [{computer_hand[0]['name']}, ?] | Score: ?")
    print("="*50 + "\n")


def compare(player_score, computer_score):
    """Compares the scores of the player and computer."""
    if player_score > 21:
        return "You went over. You lose!"
    if computer_score > 21:
        return "Computer went over. You win!"
    if player_score == computer_score:
        return "It's a draw!"
    
    # Check for blackjack scenarios
    if player_score == 21:
        return "Blackjack! You win!"
    if computer_score == 21:
        return "Computer has Blackjack! You lose!"
    
    # Compare scores - no need for separate return, use conditional expression
    return "You win!" if player_score > computer_score else "You lose!"


def play_game():
    """Main function to play the game."""
    clear_screen()
    print(art.LOGO)
    print("🎰 Welcome to Blackjack! 🎰")
    print("Goal: Get as close to 21 as possible without going over!")
    print("Aces count as 11 or 1, Face cards count as 10\n")

    player_hand = [deal_card(), deal_card()]
    computer_hand = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        player_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)

        print(f"   Your cards: {player_hand}, current score: {player_score}")
        print(f"   Computer's first card: {computer_hand[0]}")

        if player_score == 21 or computer_score == 21 or player_score > 21:
            game_over = True
        else:
            # Get user input with better prompts
            while True:
                user_choice = input("🎯 Hit (h) or Stand (s)? ").lower().strip()
                if user_choice in ['h', 'hit', 'y']:
                    player_hand.append(deal_card())
                    new_card = player_hand[-1]
                    print(f"🃏 You drew: {new_card['name']}")
                    break
                if user_choice in ['s', 'stand', 'n']:
                    game_over = True
                    break
                print("❌ Please enter 'h' for hit or 's' for stand")

    while computer_score < 17 and not game_over:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    print(f"   Your final hand: {player_hand}, final score: {player_score}")
    print(f"   Computer's final hand: {computer_hand}, final score: {computer_score}")
    print(compare(player_score, computer_score))


def main():
    """Main game loop function."""
    # Initial welcome
    clear_screen()
    print(art.LOGO)
    print("🎰✨ WELCOME TO BLACKJACK! ✨🎰")

    games_played = 0

    while True:
        choice = input("\n🎮 Would you like to play Blackjack? (y/n): ").lower().strip()

        if choice in ['y', 'yes']:
            games_played += 1
            play_game()

            # Ask to play again with better formatting
            input("\n⏭️  Press Enter to continue...")

        elif choice in ['n', 'no']:
            break
        else:
            print("❌ Please enter 'y' for yes or 'n' for no")

    # Farewell message
    print(f"\n🎉 Thanks for playing! You played {games_played} game(s).")
    print("🃏 Come back anytime for more Blackjack fun! 🃏")


if __name__ == "__main__":
    main()

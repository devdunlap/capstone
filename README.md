# 🎰 Blackjack Game Collection

A collection of console-based Blackjack implementations demonstrating different programming approaches and design patterns in Python.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [How to Play](#how-to-play)
- [Game Implementations](#game-implementations)
- [Code Quality](#code-quality)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project contains two different implementations of the classic Blackjack card game:

1. **Basic Implementation** (`main.py`) - A functional, straightforward approach
2. **Advanced Implementation** (`improved_blackjack.py`) - Object-oriented design with advanced features

Both implementations follow the standard Blackjack rules where players try to get as close to 21 as possible without going over, while competing against a computer dealer.

## ✨ Features

### Basic Implementation (`main.py`)
- ✅ Classic Blackjack gameplay
- ✅ ASCII art logo and enhanced UI
- ✅ Card display with emojis
- ✅ Hit/Stand game mechanics
- ✅ Automatic dealer logic
- ✅ Score calculation with Ace handling
- ✅ Game statistics tracking
- ✅ Clean, readable code structure

### Advanced Implementation (`improved_blackjack.py`)
- ✅ Object-oriented design with proper classes
- ✅ Type hints and comprehensive documentation
- ✅ Money management and betting system
- ✅ Advanced card representation with suits
- ✅ Automatic deck reshuffling
- ✅ Modular, extensible code architecture
- ✅ Enhanced error handling
- ✅ Multiple game rounds with balance tracking

## 📁 Project Structure

```
capstone/
├── main.py                 # Basic Blackjack implementation
├── improved_blackjack.py   # Advanced OOP implementation
├── art.py                  # ASCII art assets
├── README.md              # Project documentation
└── __pycache__/           # Python cache files
```

### File Descriptions

- **`main.py`** - Entry point for the basic game with simple, functional programming approach
- **`improved_blackjack.py`** - Advanced implementation showcasing OOP principles and design patterns
- **`art.py`** - Contains ASCII art logo and visual elements for the game

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- Git (for cloning the repository)

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/devdunlap/capstone.git
   cd capstone
   ```

2. **Run the basic game:**
   ```bash
   python main.py
   ```

3. **Run the advanced game:**
   ```bash
   python improved_blackjack.py
   ```

### Optional: Code Quality Tools

Install pylint for code quality checking:
```bash
pip install pylint
```

Run code quality checks:
```bash
pylint main.py
pylint improved_blackjack.py
```

## 🎮 How to Play

### Basic Rules
1. **Objective:** Get as close to 21 as possible without going over
2. **Card Values:**
   - Number cards (2-10): Face value
   - Face cards (J, Q, K): 10 points
   - Aces: 11 points (automatically adjusts to 1 if needed)
3. **Dealer Rules:** Dealer hits on 16 and below, stands on 17 and above

### Game Controls
- **Hit:** Type `h`, `hit`, or `y` to draw another card
- **Stand:** Type `s`, `stand`, or `n` to keep your current hand
- **Play Again:** Type `y` or `yes` to start a new game
- **Quit:** Type `n` or `no` to exit

### Sample Gameplay

```
🎰✨ WELCOME TO BLACKJACK! ✨🎰

🎮 Would you like to play Blackjack? (y/n): y

==================================================
🃏 YOUR CARDS: ['A', 'K'] | Score: 21
🤖 COMPUTER CARDS: [7, ?] | Score: ?
==================================================

🎉 BLACKJACK! You got 21!
🎉 Blackjack! You win! 🎉
```

## 🔧 Game Implementations

### Basic Implementation (`main.py`)

**Key Features:**
- Functional programming approach
- Simple card representation using dictionaries
- Global constants and functions
- Enhanced user interface with emojis
- Game statistics tracking

**Code Highlights:**
```python
# Card representation
CARDS = [
    {"name": "A", "value": 11},
    {"name": "K", "value": 10},
    # ... more cards
]

# Core game logic
def calculate_score(hand):
    """Calculates the score of a hand with Ace adjustment."""
    score = sum(card["value"] for card in hand)
    if score > 21 and any(card["name"] == "A" for card in hand):
        score -= 10
    return score
```

### Advanced Implementation (`improved_blackjack.py`)

**Key Features:**
- Object-oriented design with proper encapsulation
- Type hints for better code documentation
- Comprehensive class hierarchy
- Money management system
- Advanced error handling

**Class Structure:**
```python
class Card:          # Individual playing card
class Deck:          # 52-card deck with shuffling
class Hand:          # Collection of cards with scoring
class Player:        # Player with money management
class Dealer:        # Dealer with house rules
class BlackjackGame: # Main game controller
```

## 📊 Code Quality

This project maintains high code quality standards:

- ✅ **PEP 8 Compliance** - Follows Python style guidelines
- ✅ **Pylint Score: 10/10** - Passes all linting checks
- ✅ **Type Hints** - Comprehensive type annotations (advanced version)
- ✅ **Documentation** - Detailed docstrings for all functions and classes
- ✅ **Error Handling** - Robust input validation and error management
- ✅ **Clean Architecture** - Separation of concerns and modular design

### Quality Checks Performed
- Import ordering (standard library first)
- Consistent naming conventions
- Proper function/class documentation
- Elimination of code smells
- Trailing whitespace removal
- Optimal complexity management

## 🛠 Technologies Used

- **Python 3.7+** - Core programming language
- **Built-in Libraries:**
  - `random` - Card shuffling and dealing
  - `os` - Cross-platform screen clearing
  - `enum` - Type-safe enumeration for card suits
  - `typing` - Type hints for better code documentation

## 🎨 Design Patterns

### Basic Implementation
- **Functional Programming** - Functions as first-class citizens
- **Procedural Design** - Step-by-step game flow
- **Global State Management** - Shared constants and utilities

### Advanced Implementation
- **Object-Oriented Programming** - Encapsulation and inheritance
- **Single Responsibility Principle** - Each class has one clear purpose
- **Composition** - Game composed of smaller, focused objects
- **Strategy Pattern** - Different scoring and dealer strategies

## 🔄 Version History

- **v1.0** - Basic functional implementation
- **v2.0** - Enhanced UI and user experience improvements
- **v3.0** - Advanced OOP implementation with betting system
- **v4.0** - Code quality improvements and pylint compliance

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Standards
- Follow PEP 8 style guidelines
- Add comprehensive docstrings
- Include type hints where applicable
- Ensure pylint score remains 10/10
- Write descriptive commit messages

## 📄 License

This project is part of a coding bootcamp capstone project. Feel free to use it for educational purposes.

## 🙏 Acknowledgments

- **Nology Bootcamp** - For providing the learning framework
- **Python Community** - For excellent documentation and tools
- **ASCII Art Community** - For card game inspiration

---

**Author:** devdunlap  
**Repository:** [github.com/devdunlap/capstone](https://github.com/devdunlap/capstone)  
**Last Updated:** August 2025

---

*Happy Gaming! 🎰*

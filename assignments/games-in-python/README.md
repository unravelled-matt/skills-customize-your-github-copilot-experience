# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python. In this assignment, you will practice working with strings, loops, conditionals, and user input while creating a complete playable game.

## 📝 Tasks

### 🛠️	Build the Hangman Game Loop

#### Description
Create a Hangman game where the computer selects a random word and the player guesses one letter at a time until they either reveal the full word or run out of attempts.

#### Requirements
Completed program should:

- Randomly select one word from a predefined list of words.
- Accept one letter guess per turn from the player.
- Show the current word progress using placeholders for unguessed letters (for example: `_ _ a _ _`).
- Track and display the number of incorrect guesses remaining.
- End the game with a clear win message when the word is guessed.
- End the game with a clear lose message when attempts are exhausted.


### 🛠️	Handle Input and Game Rules

#### Description
Improve your game logic so that input is handled correctly and repeated guesses do not break the game experience.

#### Requirements
Completed program should:

- Validate player input so only a single alphabetical character is accepted.
- Handle repeated guesses by informing the player and keeping game state accurate.
- Keep guessed letters visible to help the player make informed choices.
- Continue running until a win or lose condition is reached.

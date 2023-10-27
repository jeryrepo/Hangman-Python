# Hangman-Python
Simple hangman game.
# language and libraries used
Python, random ,string

## Overview

This Python script is an implementation of the classic game Hangman. It allows a player to guess letters to complete a hidden word, with a limited number of lives. The game will provide feedback on each guessed letter and reveal the hidden word when the player either wins or runs out of lives.

## How to Run

1. Make sure you have Python installed on your system.

2. Clone or download this repository to your local machine.

3. Open a terminal or command prompt and navigate to the directory where the script is located.

4. Run the script by entering the following command:

   ```
   python hangman.py
   ```

   Replace `hangman.py` with the actual filename if it's different.

5. Follow the on-screen instructions to play the Hangman game.

## Gameplay

- You can guess letters by entering uppercase letters.
- You have a total of 10 lives.
- If you guess a letter that is part of the hidden word, it will be revealed.
- If you guess a letter that is not part of the hidden word, you will lose a life.
- You win the game if you correctly guess the entire word before running out of lives.

## Additional Information

- The script uses a list of predefined words that can be easily customized by modifying the `comp_words` list in the code.
- The game keeps track of your guessed letters and prevents you from guessing the same letter twice.
- If you run out of lives, the game reveals the hidden word.

Feel free to explore and modify the code as needed. Have fun playing Hangman!

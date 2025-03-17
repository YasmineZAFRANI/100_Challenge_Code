import random

logo = """
   _                                             
  | |                                            
  | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
  | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
  | | | | (_| | | | | (_| | | | | | | (_| | | | |
  |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/                       
"""

stages = [
    """
  --------
  |      |
  |      O
  |     \\|/
  |      |
  |     / \\
- - - - - - -
    """,
    """
  --------
  |      |
  |      O
  |     \\|/
  |      |
  |     / 
- - - - - - -
    """,
    """
  --------
  |      |
  |      O
  |     \\|/
  |      |
  |      
- - - - - - -
    """,
    """
  --------
  |      |
  |      O
  |     \\|
  |      |
  |      
- - - - - - -
    """,
    """
  --------
  |      |
  |      O
  |      |
  |      |
  |     
- - - - - - -
    """,
    """
  --------
  |      |
  |      O
  |    
  |      
  |     
- - - - - - -
    """,
    """
  --------
  |      |
  |      
  |    
  |      
  |     
- - - - - - -
    """
]

word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango",
             "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "watermelon",
             "zucchini"]

import random


print(logo)

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)  

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")
        continue

    correct_letters.append(guess)

    if guess in chosen_word:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                placeholder = placeholder[:position] + guess + placeholder[position + 1:]
        print(placeholder)
    else:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(stages[lives])  # Print the hangman stage
        if lives == 0:
            game_over = True
            print("You lose.")

    if "_" not in placeholder:
        game_over = True
        print("You win!")

    print(f"You have {lives} lives left.")

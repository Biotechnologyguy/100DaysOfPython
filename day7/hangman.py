# Step 4

import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)
end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game and lives > 0:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}")
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop, and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        print(f"you guessed {guess}, thats not in the word. You lose a life")
        if lives == 0:
            print("You lose")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # print the ASCII art from 'stages' that corresponds to
    #  the current number of 'lives' the user has remaining.
    print(stages[lives])

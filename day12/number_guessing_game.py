import random

print("Welcome to the number guessing game!\n I am thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard' : ")
lives = 10
won = False
if level.lower() == "hard":
    lives = 5
computer_guess = random.randint(1, 100)
while lives and not won:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess : "))
    if computer_guess == guess:
        won = True
        print(f"You got it. Answer was {computer_guess}")
    elif guess < computer_guess:
        print("Please try entering higher number.")
        lives -= 1
    elif guess > computer_guess:
        print("Please try entering lower number.")
        lives -= 1
    if lives:
        print("Guess Again.")
    else:
        print(f"You have ran out of guesses. The number was {computer_guess}")


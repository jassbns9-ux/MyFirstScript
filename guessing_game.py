import random

def play_game():
    secret_number = random.randint(1, 10)
    attempts = 0

    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")

    while True:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} tries.")
            break

if __name__ == "__main__":
    play_game()

import random

def guess_game():
    print("Welcome to the Guess Game!")
    print("You have 10 chances to guess the right number between 0 and 35.")

    secret_number = random.randint(0, 35)
    guesses = []

    for attempt in range(1, 11):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if guess < 0 or guess > 35:
            print("Your guess is out of the valid range (0 to 35). Try again.")
            continue

        guesses.append(guess)

        if guess == secret_number:
            print(f"Congratulations! You guessed the right number {secret_number} in {attempt} attempts.")
            break
        else:
            if guess < secret_number:
                print("Your guess is too low. Try again.")
            else:
                print("Your guess is too high. Try again.")

    else:
        print("Game Over! You have used all your chances. The secret number was", secret_number)

    print("Your guesses were:", guesses)

if __name__ == "__main__":
    guess_game()

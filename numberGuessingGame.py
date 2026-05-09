import random

guess_the_number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))

        if guess > guess_the_number:
            print("Too high! Try again.")

        elif guess < guess_the_number:
            print("Too low! Try again.")

        else:
            print("Congratulations! You guessed the number.")
            break

    except ValueError:
        print("Please enter a valid number.")
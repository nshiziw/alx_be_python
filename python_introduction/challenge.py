import random

# create the game
def guess_number():
    secret_number = random.randint(1, 10)
    guess_count = 0

    print("Welcome to guess number game")

    while True:
        guess = int(input("Guess a number between 1 and 10: "))
        guess_count += 1
        match guess:
            case _ if guess == secret_number:
                print("Congratulations! You guessed the correct number.")
                print(f"It took you {guess_count} attempts")
                break
            case _ if guess > secret_number:
                print("Too high, try again")
            case _ if guess < secret_number:
                print("Too low, try again")
    play_again = input("Play Again? (y/n): ").lower()
    if play_again == 'y':
        guess_number()
    else:
        print("Thank you for playing!")

guess_number()
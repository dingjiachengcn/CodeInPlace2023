import random

def high_low():
    secret_number = random.randint(1,100)

    guess_str = input("I am thinking of a number from 1 to 100. What number am I thinking of? ")
    guess = int(guess_str)

    while guess != secret_number:
        if guess > secret_number:
            guess_str = input("Nope! That guess was too high! Try again. ")
        if guess < secret_number:
            guess_str = input("Sorry! That guess was too low! Take another guess. ")
        guess = int(guess_str)
    print("You guessed my number! Way to go!")

if __name__ == '__main__':
    high_low()

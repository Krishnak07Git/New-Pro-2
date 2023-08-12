import random

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess a number bet1ween 1 and 100: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

if __name__ == "__main__":
    print("Welcome to the Guessing Number Game!")
    guessing_game()

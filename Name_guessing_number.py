import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    while True:
        try:
            lower_bound = int(input("Enter the lower bound: "))
            upper_bound = int(input("Enter the upper bound: "))
            if lower_bound >= upper_bound:
                print("Invalid range! The lower bound must be less than the upper bound.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter integers only.")

    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    
    while True:
        try:
            guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
            attempts += 1

            if guess < lower_bound or guess > upper_bound:
                print(f"Out of bounds! Please enter a number between {lower_bound} and {upper_bound}.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    number_guessing_game()

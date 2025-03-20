import random

# Set number of rounds
rounds = 5
user_score = 0

# Start the game
for round in range(1, rounds + 1):
    # Generate random numbers for user and computer
    user_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    
    # Display the user's number (but not the computer's)
    print(f"Round {round}: Your number is {user_number}")
    
    # Ask the user to guess whether their number is higher or lower than the computer's number
    guess = input("Is your number higher or lower than the computer's number? (Type 'higher' or 'lower'): ").lower()
    
    # Check if the user's guess is correct
    if (guess == 'higher' and user_number > computer_number) or (guess == 'lower' and user_number < computer_number):
        user_score += 1
        print("You guessed correctly! You earned a point.")
    else:
        print(f"Wrong guess. The computer's number was {computer_number}.")
    
    print()

# End of game
print(f"Game Over! You scored {user_score} out of {rounds}.")

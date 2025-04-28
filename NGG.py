import random
import time
import os
import json

def convert(secs):
    minutes = int(secs // 60)
    seconds = int(secs % 60)
    return minutes, seconds

def load_high_scores(filename):
    """Load high scores from a file."""
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)  # Load high scores as a dictionary
    return {"Easy": float('inf'), "Medium": float('inf'), "Hard": float('inf')}  # Default high scores

def save_high_scores(filename, high_scores):
    """Save high scores to a file."""
    with open(filename, 'w') as file:
        json.dump(high_scores, file)  # Save high scores as a dictionary

def play_game(high_scores):
    number = random.randint(1,100)
    x = 0

    difficulties = {
        1:("Easy",10),
        2:("Medium",5),
        3:("Hard",3),
    }

    print("""
    Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.
    You have 5 chances to guess the correct number.

    Please select the difficulty level:
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)
    """)


    choice = int(input("Enter your choice:"))
    while choice not in range(1,4):
        print("Try again and pick a number in the range of 1 to 3")
        choice = int(input("Enter your choice:"))
    difficulty_name, max_attempts = difficulties[choice]


    print(f"""
    Great you have selected the {difficulty_name} difficulty level
    Let's start the game!
    """)
    start_time = time.time()

    def GuessGame():
        nonlocal x
        global number
        guess = int(input("Enter your guess: "))
        x += 1
        return guess

    for _ in range(max_attempts):
        guess = GuessGame()
        if guess == number:
            end_time = time.time()
            elapsed_time = end_time - start_time
            minutes, seconds = convert(elapsed_time)
            print(f"Congratulations! You guessed the correct number in {x} attempts in {minutes} minutes and {seconds} seconds.")
            # Check for high score
            if x < high_scores[difficulty_name]:
                high_scores[difficulty_name] = x
                print(f"New high score for {difficulty_name}! You guessed the number in {high_scores[difficulty_name]} attempts.")
            break
        elif guess > number:
            print(f"""Incorrect the number is less than {guess}
            """)
        elif guess < number:
            print(f"""Incorrect the number is more than {guess}
            """)

        if x == 2: #Hint 1
            if number % 2 == 0:
                print("Hint: The number is even.")
            else:
                print("Hint: The number is odd.")

        if x == 4 and x < max_attempts:#Hint 2
            random_range = random.randint(5, 20)  # Random range between 5 and 20
            lower_bound = max(1, number - random_range)
            upper_bound = min(100, number + random_range)
            print(f"Hint: The number is between {lower_bound} and {upper_bound}.")

        if x == max_attempts:
            end_time = time.time()
            elapsed_time = end_time - start_time
            minutes, seconds = convert(elapsed_time)
            print(f"You lose. The correct answer was {number} and it took you {minutes} minutes and {seconds} seconds to fail.")
    return high_scores  # Return the updated high scores

if __name__ == "__main__":
    filename = "high_scores.json"
    high_scores = load_high_scores(filename)  # Load high scores from file
    while True:
        high_scores = play_game(high_scores)
        again = input("Do you want to have another round? (y/n): ").strip().lower()
        if again != 'y':
            save_high_scores(filename, high_scores)  # Save high scores to file
            print("Thank you for playing! Goodbye!")
            break
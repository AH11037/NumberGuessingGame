import random
import time

number = random.randint(1,100)
x = 0

difficulties = {
    1:("Easy",10),
    2:("Medium",5),
    3:("Hard",3),
}


def convert(secs):
    minutes = int(secs // 60)
    seconds = int(secs % 60)
    return minutes, seconds


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
    global x
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
        break
    elif guess > number:
        print(f"""Incorrect the number is less than {guess}
        """)
    elif guess < number:
        print(f"""Incorrect the number is more than {guess}
        """)
    if x == max_attempts:
        end_time = time.time()
        elapsed_time = end_time - start_time
        minutes, seconds = convert(elapsed_time)
        print(f"You lose. The correct answer was {number} and it took you {minutes} minutes and {seconds} seconds to fail.")

again = input("""
Do you want to have another round?:""")
if again == "y":
    print("G")
elif again == "n":
    print ("N")
else:
    print("NO")

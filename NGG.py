import random

number = random.randint(1,100)
print(number)

difficulties = {
    1:"Easy",
    2:"Medium",
    3:"Hard"
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


print(f"""
Great you have selected the {difficulties[choice]} difficulty level
Let's start the game!
""")
x=0
def GuessGame():
    global x
    global number
    guess = int(input("Enter your guess: "))
    x += 1
    if guess == number:
        print(f"Congratulations! You guessed the correct number in {x} attempts.")
    else:
        print("Incorrect")


GuessGame()
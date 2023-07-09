import random
from art import gn_logo


def guess(nc,n):
    """Guess the number correctly"""
    if n == nc:
        print(f"You got it. The answer was {nc}")
    elif n > nc:
        print("Too high")
    else:
        print("Too low")



chances = 0
print(gn_logo)
print("Welcome to the Number Guessing Game!")
number = random.randrange(1,100)
print("I am thinking of a number between 1 and 100.")
diff = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if diff == 'easy':
    chances = 10
elif diff == 'hard':
    chances = 5
else:
    print("Wrong choice")

for i in range(chances):
    print(f"You have {chances - i} attempts left")
    num = int(input("Make a guess: "))
    guess(number, num)
    if num == number:
        break
    else:
        print("Guess again.")

    if chances - i == 1:
        print('You lose.')

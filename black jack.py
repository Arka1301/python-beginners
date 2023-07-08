import random
from art import bj_logo
from os import system,name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def get_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    l = random.choice(cards)
    return l


def calc_score(cc):
    if 11 in cc and sum(cc) > 21:
        cc.remove(11)
        cc.append(1)

    if len(cc) == 2 and 11 in cc and 10 in cc:
        return 0

    return sum(cc)


def compare(ucs,ccs):
    if ucs == ccs:
        print("The game is a draw")
    elif ccs == 0:
        print("You lose")
    elif ucs == 0:
        print("You win")
    elif ucs > 21:
        print("You lose")
    elif ccs > 21:
        print("You win")
    else:
        if ccs > ucs:
            print("You lose")
        else:
            print("You win")

new_game = True

while new_game:
    user_cards = []
    computer_cards = []
    game_ends = False

    print(bj_logo)
    print("Welcome to the game of blackjacks.")

    for i in range(2):
        user_cards.append(get_cards())
        computer_cards.append(get_cards())


    while not game_ends:

        user_score = calc_score(user_cards)
        computer_score = calc_score(computer_cards)

        print(f"Your cards are: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            game_ends = True

        else:
            ask = input("Do you want to draw another card ").lower()
            if ask == 'yes':
                user_cards.append(get_cards())
                user_score = calc_score(user_cards)
            else:
                game_ends = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(get_cards())
        computer_score = calc_score(computer_cards)

    print(f"Your final set of cards are: {user_cards} and your final score is {user_score}")
    print(f"Computer's final set of cards are: {computer_cards} and computer's final score is {computer_score}")
    compare(user_score, computer_score)
    ask2 = input("Do you want to restart the game? ")
    if ask2 == 'no':
        print("Thank you for playing our game. ")
        new_game = False
    else:
        clear()

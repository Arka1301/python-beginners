from os import system, name
from art import ba_logo

bid_list = {}



def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def find_max(dict):
    max = 0
    max_name = ""
    for key in dict:
        if dict[key] > max:
            max = dict[key]
            max_name = key
    print(f"The winner is {max_name} with a bid of ${max}.")


def entry():
    bidder = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bid_list[bidder] = bid


print(ba_logo)
print("Welcome to the secret auction program. ")
choice = True
while choice:
    entry()
    result= input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if result == 'yes':
        clear()
    else:
        choice = False

find_max(bid_list)


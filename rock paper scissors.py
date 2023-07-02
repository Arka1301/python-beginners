# __ROCK PAPER SCISSORS GAME___

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# paper > rock 1 > 0
# scissors > paper 3 > 2
# rock > scissors 1 > 3

op=[rock,paper,scissors]
ch = int(input("Enter your choice. 0 for rock, 1 for paper, 2 for scissors "))
ch1=op[ch]
ch_co=random.randint(0,2)
com_ch=op[ch_co]
print(f"Your choice:\n{ch1}")
print(f"Computer's choice:\n{com_ch}")

if ch == ch_co:
    print("scores are tied")
elif ch == 0 and ch_co == 1:
    print("Computer wins")
elif ch == 0 and ch_co == 2:
    print("You win")
elif ch == 1 and ch_co == 0:
    print("You win")
elif ch == 1 and ch_co == 2:
    print("Computer wins")
elif ch == 2 and ch_co == 0:
    print("Computer wins")
elif ch == 2 and ch_co == 1:
    print("You win")
else:
    print("ERROR404")

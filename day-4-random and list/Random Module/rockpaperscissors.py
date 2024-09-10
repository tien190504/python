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

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


choice = [rock, paper, scissor]

user = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors."))


computer = random.randint(0, 2)
print(f"\nyou choice: \n {choice[user]}")
print(f"\ncomputer choice:\n {choice[computer]}")

if user == 0 and user == 2:
    print("You wins!")
elif computer > user:
    print("You lose!")
elif user == computer:
    print("It's a draw!")
else:
    print("You type an invalid number. You lose!")


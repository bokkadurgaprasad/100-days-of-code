import random
#I'm, added images from ASCII art 
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
---'   ___)___
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ___)___
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock,paper,scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You choose a invalid number, You Lose!")
else:
    print(game[user_choice])
    computer_choice = random.randint(0,2)
    print("Computer Choise: ")
    print(game[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Wins!")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose!")
    elif computer_choice > user_choice:
        print("You Lose!")
    elif user_choice > computer_choice:
        print("You Wins!")
    elif computer_choice == user_choice:
        print("It's Draw")
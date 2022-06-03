
import random

#The game sign is represnted by this symbols

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
while True:
    game_picture = [rock, paper, scissors]

    user_options = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    print(game_picture[user_options])

    computer_option = random.randint(0, 2)
    print("Computer opted for:")
    print(game_picture[computer_option])

    if user_options >= 3 or user_options < 0: 
        print("Your number is invalid, you lose!") 
    elif user_options == 0 and computer_option == 2:
        print("You win!")
    elif (computer_option == 0 and user_options == 2) or (computer_option > user_options):
        print("You lose")
    elif user_options > computer_option:
        print("You win!")
    elif computer_option == user_options:
        print("It's a draw")
        
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

#Write your code below this line 👇
import random
g_images = [rock, paper, scissors]
print("Welcome to the Rock Paper Scissors game!")

u_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if u_choice >= 3 or u_choice < 0:
  print("You choose an invalid number, you lose!")
else:
  print(g_images[u_choice])
  c_choice = random.randint(0,2)
  print(f"Computer choose:")
  print(g_images[c_choice])
  if u_choice == 0 and c_choice == 2:
    print("You win!")
  elif c_choice == 0 and u_choice ==2:
    print("You lose!")
  elif c_choice > u_choice:
    print("You lose")
  elif u_choice > c_choice:
    print("You win!")
  elif c_choice == u_choice:
    print("Its a draw")

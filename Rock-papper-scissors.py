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

#Write your code below this line 👇 👇 👇 👇 👇 👇 
import random
l=[rock,paper, scissors]
choice= int(input('What do you chose? 0 for Rock, 1 for papper and 2 for scissors.'))
choice_1= random.randint(0,2)
if choice_1 == choice+1 or  choice_1 == choice -2:
  print(l[choice])
  print(f'\n computer chose\n {l[choice_1]}\n')
  print('You lose!')
if choice_1 == choice -1 or choice == choice_1 -2:
  print(l[choice])
  print(f'\n computer chose\n {l[choice_1]}\n')
  print('You win!')
elif choice == choice_1:
  print(l[choice])
  print(f'\n computer chose\n {l[choice_1]}\n')
  print("It's a Draw!") 

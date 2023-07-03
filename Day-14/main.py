from art import logo, vs
from game_data import data
import random
import replit

def game(A:dict ,B: dict ):
  print(logo)
  print(f"Compare A: {A['name']},{A['description']} from {A['country']}")
  print(vs)
  print(f"\n Against B: {B['name']},{B['description']} from {B['country']} \n")
  choice = input("Who has more followers : type 'A' or 'B'.")
  l={'A':A,'B':B}
  x= l[choice]
  l.pop(choice)
  y= l[list(l.keys())[0]]
  if x['follower_count'] >=   y['follower_count'] :
    print("That's true ! \n *********************************************")
    return [True, x]
  else : 
    print("You lost!")
    return [False, x]
    
score = 1 
A=random.choice(data)
B=random.choice(data)
while score > 0 :
  x= game(A,B)
  if x[0]:
    A = x[1]
    B = random.choice(data)
    replit.clear()
  else:

    score = 0


  
  
  

  
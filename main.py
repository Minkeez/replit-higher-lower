from art import logo, vs
from game_data import data
import random
from replit import clear

def random_data():
  return random.choice(data)

def print_data_format(data):
  return f"{data['name']}, a {data['description']}, from {data['country']}"

def compare_follower(A_count, B_count):
  if A_count > B_count:
    return "A"
  else:
    return "B"
    
def higher_lower():
  print(logo)
  A = random_data()
  score = 0
  is_over = False
  while not is_over:
    B = random_data()
    while B == A:
      B = random_data()
    
    A_data = print_data_format(A)
    B_data = print_data_format(B)
    
    print(f"Compare A: {A_data}")
    print(vs)
    print(f"Against B: {B_data}")
    
    A_follower_count = A["follower_count"]
    B_follower_count = B["follower_count"]
    who_win = compare_follower(A_follower_count, B_follower_count)
    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    clear()
    print(logo)
    if user_guess == who_win:
      score += 1
      print(f"You're right! Current score: {score}.")
      A = B
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      is_over = True

higher_lower()
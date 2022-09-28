import random
from replit import clear
import art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def compare(user_score,computer_score):
  if user_score==computer_score:
    return "Draw 🫤"
  elif computer_score==0:
    return "You lose🥺, Computer has the blackjack"
  elif user_score==0:
    return "You win!!🥳"
  elif user_score>21:
    return "You lose🥺, Computer wins"
  elif computer_score>21:
    return "You win!!🥳"
  elif user_score>computer_score:
    return "You win!!🥳"
  elif user_score<computer_score:
    return "You lose🥺, Computer wins"


def calculate_score(cards):
    if (11 in cards and 10 in cards) and len(
            cards) == 2:  # can also use if sum(cards)==21 and len(cards)==2
        return 0
    if (11 in cards) and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def play_game():  
  print(art.logo)
  user_cards = []
  
  for i in range(2):
      user_cards.append(deal_card())
  
  computer_cards = []
  
  for i in range(0, 2):
      computer_cards.append(deal_card())
  
  is_game_over= False
 
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print(f"Your cards: {user_cards} and the total: {user_score}")
    print(f"The computer's first card: {computer_cards[0]}")
    
    if (user_score==0 or computer_score==0) or user_score>21:
      is_game_over=True
    else:
      choice = input("\nDo you want to add another card? Type 'y' or 'n'\n--> ")
      if choice=='y':
        user_cards.append(deal_card())
      else:
        is_game_over=True
    
  
  
  while computer_score!=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print('\n')
  print(f"Your final hand: {user_cards} and total: {user_score}")
  print(f"Computer's final hand: {computer_cards} and total: {computer_score}")
  print('\n')
  
  print(compare(user_score,computer_score))


while(input("\nDo you want to play Blackjack? Type 'y' or 'n'\n-->")=='y'):
  clear()
  play_game()

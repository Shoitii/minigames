import random

def play():
  count_wins = count_ties = count_losts = 0
  while True:   
    player = input("Type 'r' for rock, 'p' for paper, 's' scissors and '0' to exit: ")
    comp = random.choice(['r','p','s'])
    if player == '0':
      print('Thanks for playing, see you next time!')
      print('-==-==- SCORE -==-==-')
      print(f'Wins:{count_wins}  Losts:{count_losts}  Ties:{count_ties}')
      break
    elif player == comp:
      count_ties += 1
      print('Tie')
    elif win(player, comp):
      count_wins += 1
      print('You won!')
    else:
      count_losts += 1
      print('You lost!')

def win(player,opponent):
  if (player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
    return True


print("JOKENPO GAME")
play()

import random

def guess(x):
  random_num = random.randint(1, x)
  num = 0
  count = 0
  while num != random_num:
    num = int(input(f'Guess a number between 1 and {x}: '))
    if num < random_num:
      print(f'Try again. Too low')
    elif num > random_num:
      print('Try again. Too high')
    count += 1
  if count > 1:
    print(f'Congrats! You guessed the correct number in {count} tries \033[33m({random_num})\033[m')
  else:
    print(f'Congrats! You guessed the correct number in {count} try \033[33m({random_num}\033[m')


guess(10)
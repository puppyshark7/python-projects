import random
import time
def roll_dice(n):
    dice = []
    for i in range(n):
        dice.append(random.randint(1,6))
    return dice
number_dice = input('Enter number of dice: ')
number_dice = int(number_dice)
ready = input('Ready to start? Hit any key to continiue')
user_rolls = roll_dice(number_dice)
print('User first roll: ', user_rolls)
user_choices = input('Enter - to hold or r to roll again :')
while len(user_choices) !=number_dice:
  print('You must enter', number_dice, 'choices')
  user_choices = input('Enter - to hold or r to roll again :')
def roll_again(choices, dice_list):
  print('Rolling again ...')
  time.sleep(10)
  for i in range(len(choices)):
    if choices[i] == 'r':
      dice_list[i] = random.randint(1,6)
  time.sleep(10)
roll_again(user_choices, user_rolls)
print('Player new roll: ', user_rolls)
computer_rolls = roll_dice(number_dice)
print('Computer first roll: ', computer_rolls)
def computer_strategy(n):
  print('Computer is thinking...')
  time.sleep(10)
  choices = ''
  for i in range(n):
    if computer_rolls[i] < 5:
      choices = choices + 'r'
    else:
      choices = choices + '-'
  return choices
computer_choices = computer_strategy(number_dice)
print('Computer Choice: ', computer_choices)
roll_again(computer_choices, computer_rolls)
print('Computer new roll: ', computer_rolls)
def find_winner(dice_list, udice_list):
    computer_total = sum(dice_list)
    user_total = sum(udice_list)
    print('Computer total', computer_total)
    print('User total', user_rolls)
    if user_total > computer_total:
        print('User wins!')
    elif user_total < computer_total:
        print('Computer wins!')
    else:
        print('It is a tie!')
find_winner(computer_rolls,user_rolls)
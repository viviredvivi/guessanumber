import random

list_of_numbers = []
for number in range (1, 101):
  list_of_numbers.append(number)

def guess():
  player_guess = int(input("Guess what number I'm thinking of! "))
  return player_guess

def guess_outcome(player_guess, actual_number, attempts_left, have_attempts):
  if attempts_left == 0:
    print(f"You have {attempts_left - 1} attempts left")
  elif player_guess == actual_number:
    print(f"Your guess was correct! The number is indeed {actual_number}")
    try_again = input("Do you want to play again? Type 'yes or 'no'")
    if try_again == 'yes':
      guessing_game()
    else:
      print("Thank you for playing, see you next time!")
      return 2
  elif player_guess > actual_number:
    print("Too high.")
    print(f"You have {attempts_left - 1} attempts left")
    return 1
  elif player_guess < actual_number:
    print("Too low.")
    print(f"You have {attempts_left - 1} attempts left")
    return 1

def guessing_game():
  actual_number = random.choice(list_of_numbers)
  have_attempts = True
  difficulty_lvl = input("Hello! \nWelcome to my little game: 'Guess a number'! \nI'm thinking of a number between 1 and 100... \nChoose a difficulty. Type 'easy' or 'hard': ")
  if difficulty_lvl == 'easy':
    attempts_left = 10  
    print(f"You have {attempts_left} attempts left.")
    while have_attempts == True:
      if attempts_left > 0:
        player_guess = guess()
        outcome = guess_outcome(player_guess, actual_number, attempts_left, have_attempts)
        if outcome == 2:
          have_attempts = False
        else:
          attempts_left = attempts_left - outcome
      elif attempts_left == 0:
        try_again = input("Sorry, you've run out of guesses, you lose. Do you want to play again? Type 'yes or 'no'")
        if try_again == 'yes':
          guessing_game()
        else:
          print("Thank you for playing, see you next time!")
          have_attempts = False
  elif difficulty_lvl == 'hard':
    attempts_left = 5
    print(f"You have {attempts_left} attempts left.")
    while have_attempts == True:
      if attempts_left > 0:
        player_guess = guess()
        outcome = guess_outcome(player_guess, actual_number, attempts_left, have_attempts)
        attempts_left = attempts_left - outcome
      elif attempts_left == 0:
        try_again = input("Sorry, you've run out of guesses, you lose. Do you want to play again? Type 'yes or 'no': ")
        if try_again == 'yes':
          guessing_game()
        else:
          print("Thank you for playing, see you next time!")
          have_attempts = False
  else:
    return print("Sorry, wrong input.")

guessing_game()
  

from random import random
import random
import utils
import scores

# I am using the difficulty level which was set when the user selected the game, using the value
# which is 1 to 5 with the power of 10
def get_secret_number(difficulty):
    return random.randint(1, 10**difficulty)

# here we let the user guess the number - to be honest slim chance of success
def get_guess_from_user(difficulty):
    while True:
       print("Please select a number between 1 and" , 10**difficulty, ":")
       num = input()
       if utils.is_num_in_range(num ,1 , 10**difficulty):
           break

    return int(num)


# comparing the user guessed value with the random number
def compare_numbers(a , b):
    if a == b:
        return True
    return False

# The actual game
def guess_game(difficulty=1):
    while True:
        secret_number = get_secret_number(difficulty)
        player_guess=get_guess_from_user(difficulty)

        if compare_numbers(secret_number, player_guess):
            print("KUDOS")
            scores.add_scores(difficulty)
        else:
            print("You're a loser baby....")
        if utils.do_you_want_to_quit():
            break




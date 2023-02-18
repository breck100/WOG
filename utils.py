# a method to check if a number is in range
import random

global SCORES_FILE_NAME, BAD_RETURN_CODE
SCORES_FILE_NAME = "scores.txt"
BAD_RETURN_CODE = 499

def is_num_in_range(num ,start ,end):
   if num.isnumeric() and int(num) in range(start, end+1):
          return True
   return False


def do_you_want_to_quit():
    val = input('press Enter to continue or q to quit')
    if val == 'q':
        print("So long and thanks for all the fish")
        return True
    return False
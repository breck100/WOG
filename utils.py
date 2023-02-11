# a method to check if a number is in range
import random

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
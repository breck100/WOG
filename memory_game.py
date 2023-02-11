import random
import utils
import time

def generate_sequence(difficulty):
    n = 0
    sequence = []
    for n in range(0, difficulty):
        sequence.append(random.randint(1, 101))
        n = n+1
    return sequence

def get_list_from_user(difficulty):
    n = 0
    user_list=[]
    for n in range(0, difficulty):
        user_list.append(int(input()))
        n = n +1
    return user_list

# the rules are simple here, you need to remember all the numbers , the order is not a must
def is_list_equal(generated_list, user_list):
    generated_list.sort()
    user_list.sort()
    n = 0
    for n in range(0, len(generated_list)):
        if generated_list[n] != user_list[n]:
            return False
        n = n+1
    return True


def play(difficulty):
    while True:
        sequnece_list=generate_sequence(difficulty)
        print (sequnece_list , end='')
        time.sleep(0.7)
        print ("\rNow it is your turn, please add the numbers you remember:)")
        user_list=get_list_from_user(difficulty)

        # user_list = list(int(n) for n in user_input.split(" "))
        if(is_list_equal(sequnece_list , user_list)):
            print("Ata Totach")
        else:
            print("You are loser, you might be a prime minister one day")
        if utils.do_you_want_to_quit():
            break
import random
import requests
import utils
from currency_converter import CurrencyConverter


# get_money_interval - will try to get the actual conversion from the API,
# if request fails, we will use python internal library
def get_money_interval(difficulty, required_value):
    url="https://v6.exchangerate-api.com/v6/a96bdded76672b79c490ac12/pair/USD/ILS/"+str(required_value)
    response=requests.get(url)
    value = 0
    #print (response.status_code)
    if response.status_code == 200:
        data=response.json()
        value=(data['conversion_result'])
    else:
        c = CurrencyConverter()
        value = c.convert(required_value, 'USD', 'ILS')
    # To make it more conveniant let work with no more than 2 digits
    value = round(value,2)
    # Yes, I know it can be done in one line, but in this case I preferred a more readable way
    returned_list=[]
    difficulty_interval = 5-difficulty
    returned_list.append(value-difficulty_interval)
    returned_list.append(value+difficulty_interval)

    return returned_list

#get the user guess
def get_guess_from_user(difficulty):
    user_guess = input()
    return user_guess

def play(difficulty):
    while True:
        actual_value_in_USD = (random.randint(1, 100))
        interval_list=get_money_interval(difficulty, actual_value_in_USD)
        print("Value in USD is:", actual_value_in_USD, "can you guess the amount in ILS?")
        user_guess=float(get_guess_from_user(difficulty))
        if (user_guess>interval_list[0] and user_guess<interval_list[1]):
            print("True")
        else:
            print ("False")
        if utils.do_you_want_to_quit():
            break











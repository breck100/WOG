# a method to check if a number is in range
def is_num_in_range(num ,start ,end):
   if num in range(start, end+1):
          return True
   return False

# welcome - need some UI
def welcome(name):
    print("Hello", name, " and welcome to the world of Games(WOG).\n Here you can find many cool games to play")

# loaf game  - select game and difficulty level
def load_game():
        game_value=0
        while (game_value==0):
                print("Please choose a game to play: ")
                print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
                print("2. Guess Game - guess a number and see if you chose like the computer")
                print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
                game_value = input()
                if (not game_value.isnumeric() or not is_num_in_range(int(game_value), 1,3)):
                        print ("please enter correct value")
                        game_value = 0
        game_diff_level = 0
        while game_diff_level==0:
                game_diff_level =input("Please choose game difficulty from 1 to 5: ")
                if (not game_diff_level.isnumeric() or not is_num_in_range(int(game_diff_level), 1, 5)):
                        print("please enter correct value")
                        game_diff_level = 0
        return game_value, game_diff_level


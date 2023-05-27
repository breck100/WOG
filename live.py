from Games import currency_roullete_game, memory_game
import utils
from Games.guess_game import guess_game
# welcome - need some UI
def welcome():
    name = input("What is your name, dear Friend?")
    print("Hello", name, " and welcome to the world of Games(WOG).\n Here you can find many cool games to play")

# load game  - select game and difficulty level
def load_game():
        game_value=0
        while (game_value==0):
                print("Please choose a game to play: ")
                print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
                print("2. Guess Game - guess a number and see if you chose like the computer")
                print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
                print("4. Quit world of games")
                game_value = input()
                if (not utils.is_num_in_range(game_value, 1,4)):
                        print ("please enter correct value")
                        game_value = 0
                game_diff_level = 0
                game_value = int(game_value)
                # if the user decided to quit world of games , we will part as friendss
                if (game_value == 4):
                        print("It was fun, see you later")
                        break

                # Select difficulty level
                while game_diff_level==0:
                        game_diff_level =input("Please choose game difficulty from 1 to 5: ")
                        if not utils.is_num_in_range(game_diff_level, 1, 5):
                                print("please enter correct value")
                                game_diff_level = 0
                game_diff_level=int(game_diff_level)

                # time to play according to the selection
                if game_value == 1:
                        memory_game.play(game_diff_level)
                elif game_value == 2:
                        guess_game(game_diff_level)
                elif game_value == 3:
                        currency_roullete_game.play(game_diff_level)
                game_value = 0



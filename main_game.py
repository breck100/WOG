# from live import welcome , load_game

import live

live.welcome("Eran")
game_value, game_diff_level = live.load_game()
print("You have selected: game number:", game_value,"and difficulty level",game_diff_level)
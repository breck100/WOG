# from live import welcome , load_game
import live
import MainScores
import utils
from flask import Flask, request, render_template
live.welcome()
live.load_game()

MainScores.score_server()




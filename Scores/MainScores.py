import utils
from flask import Flask, request, render_template
import os

app = Flask(__name__)
@app.route("/")
def score_server():

    print ("3")
    # f = open(utils.SCORES_FILE_NAME, 'r')
    f = open(utils.SCORES_FILE_FOR_FLASK, 'r')
    score = f.readline()
    f.close()
    print("score=" + score)
    # return("success", 201)
    f1 = 1
    try:
        f1 = render_template('score.html', score=score)
    except Exception as e:
        print("error")
        f1 = render_template('error.html', ERROR=e.message)
    return f1

if __name__ == '__main__':
     app.run('0.0.0.0', debug=True, port=5000)


score_server()
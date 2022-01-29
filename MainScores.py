from flask import Flask, render_template
app = Flask(__name__)

ERROR = 'There was an error somewhere along the way. '


def score_server():
    with open('Scores.txt', 'r') as scores_file:
        content = scores_file.readlines()
        score = content[0]
        return score


@app.route('/failure')
def failure():
    a = f'<html> <head> <title>Scores Game</title> </head> <body> <h1><div id="score" style="color:red">{ERROR}</div></h1> </body> </html>'
    return a, 200


@app.route('/success')
def success():
    SCORE = score_server()
    b = f'<html> <head> <title>Scores Game</title> </head> <body> <h1>The score is <div id="score">{SCORE}</div></h1> </body> </html>'
    return b, 200


app.run(host='127.0.0.1', debug=True, port=30000)
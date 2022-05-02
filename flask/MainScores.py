from flask import Flask
app = Flask(__name__)


def score_server():
    """
    this func checks the first line of Scores.txt and returns it
    :return: int representing user current score
    """
    with open("/home/mruser/Scores.txt", 'r') as scores_file:
        content = scores_file.readlines()
        score = content[0]
        return score


ERROR = 'There was an error somewhere along the way. '


@app.route('/success')
def success():
    SCORE = score_server()
    a = f"""<html>    
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                <h1>The score is <div id="score">{SCORE}</div></h1>
                </body>
            </html>"""
    return a, 200


@app.route('/failure')
def failure():
    b = f"""<html>
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                    <h1><div id="score" style="color:red">{ERROR}</div></h1>
                </body>
            </html>"""
    return b, 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
    # app.run(host='0.0.0.0', debug=True)

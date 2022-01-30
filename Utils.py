import os

SCORES_FILE_NAME = 'Scores.txt'
BAD_RETURN_CODE = 666


def clear_terminal():
    """
    This func clears the screen in windows cmd and linux/macOS terminal
    :return: None
    """
    os.system('cls||clear')


def reset_scores_file():
    """
    create and reset Scores.txt
    :return: None
    """
    with open('Scores.txt', 'w') as scores:
        scores.write('0')

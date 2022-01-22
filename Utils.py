import os

SCORES_FILE_NAME = 'Scores.txt'
BAD_RETURN_CODE = 666


def clear_terminal():
    """
    This func clears the screen in windows cmd and linux/macOS terminal
    :return: None
    """
    os.system('cls||clear')

from threading import Event
from Utils import clear_terminal, reset_scores_file
from games import MemoryGame, GuessGame, CurrencyRouletteGame
import sys
# sys.path.insert(1, '/Users/noy/gits/World_Of_Games/games/')


def welcome(name):
    """
    this func prints a welcome greeting using the player's name entered in previous stage.
    it also initializes the Scores.txt file
    :param name: player's name as string
    :return: None
    """
    clear_terminal()
    reset_scores_file()
    greeting = f"\nHello {name}, and welcome to the World of Games (WoG). Here you can find many cool games to play."
    print(greeting)
    return


def load_game():
    """
    this func gets two inputs from the user, the first for a game (1-3) and the second is for difficulty (1-5)
    it also checks that the input is legal (numbers only) and in range (1-3 and 1-5)
    :return: list where [chosen game, difficulty]
    """

    try:
        game_selection = int(input("""\n\nPlease choose a game to play (1, 2 or 3):
        1. Memory Game - a sequence of numbers will appear for 1 second and you will have to guess it back
        2. Guess Game - guess a number and see if you chose like the computer
        3. Currency Roulette - try and guess the value of a random amount of USD in ILS. \n\t"""))
        difficulty = int(input("\nPlease choose game difficulty from 1 - 5: "))
    except ValueError:
        print("Integers only. Please try again. \n")
        load_game()
    else:
        if (game_selection < 1) or (game_selection > 3):
            print("\n\nUnrecognized game. Please try again. ")
            load_game()
        elif (difficulty < 1) or (difficulty > 5):
            print("No such difficulty level. Please try again. \n\n")
            load_game()
        elif game_selection == 1:
            print(f"\nYou have chosen to play Memory Game in difficulty {difficulty}.")
            Event().wait(2)
            return [game_selection, difficulty]
        elif game_selection == 2:
            print(f"\nYou have chosen to play Guess Game in difficulty {difficulty}.")
            Event().wait(2)
            return [game_selection, difficulty]
        elif game_selection == 3:
            print(f"\nYou have chosen to play Currency Roulette in difficulty {difficulty}.")
            Event().wait(2)
            return [game_selection, difficulty]


def play_da_game(game_selection):
    """
    this func runs the game and difficulty selection function and then sends the data to the corresponding game
    :return: None
    """
    # game_selection = load_game()
    if game_selection[0] == 1:
        state = MemoryGame.play_memory(game_selection[1])
        return state
    elif game_selection[0] == 2:
        state = GuessGame.play_guess(game_selection[1])
        return state
    elif game_selection[0] == 3:
        state = CurrencyRouletteGame.play_roulette(game_selection[1])
        return state

from Live import welcome, load_game, play_da_game
from Utils import clear_terminal
from Score import add_scores

if __name__ == '__main__':

    clear_terminal()
    name = input('Hi. What is your name? ')
    welcome(name)

    replay = 'y'
    while replay.lower() == 'y' or replay.lower() == 'yes':
        chosen_parameters = load_game()
        level_of_diff = chosen_parameters[1]
        did_i_win = play_da_game(chosen_parameters)
        if did_i_win:
            add_scores(level_of_diff)
        replay = input('Would you like to play again? y/n ')

# print(chosen_parameters)
# print(type(chosen_parameters))
# print(level_of_diff)
# print(type(level_of_diff))
# print(did_i_win)
# print(type(did_i_win))

clear_terminal()
print('\n\nThank you for playing WOG.\n\n')

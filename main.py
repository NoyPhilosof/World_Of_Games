from Live import welcome, da_game
from Utils import clear_terminal

if __name__ == '__main__':

    clear_terminal()
    with open('Scores.txt', 'w') as scores:    # create or clean Scores.txt
        scores.write('')

    name = input('Hi. What is your name? ')
    welcome(name)

    replay = "y"    # allowing user to play again. replay is checked each run. if it's not 'y' or 'yes', the game stops.
    while replay.lower() == 'y' or replay.lower() == 'yes':
        da_game()
        replay = input('\n\nWould you like to play again? y/n ')

print('\n\nThank you for playing WOG.')

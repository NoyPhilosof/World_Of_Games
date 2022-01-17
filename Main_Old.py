# if __name__ == '__main__':
from Live import welcome, load_game
from GuessGame_Original import play_guess
from MemoryGame import play_memory, clear_terminal
from CurrencyRouletteGame import play_roulette


def user_choice(user_choices):
    if user_choices[0] == 1:
        play_memory(user_choices[1])
    elif user_choices[0] == 2:
        play_guess(user_choices[1])
    elif user_choices[0] == 3:
        play_roulette(user_choices[1])

# if __name__ == '__main__':


clear_terminal()
name = input('Hi. What is your name? ')
welcome(name)
what_game = load_game()
user_choice(what_game)

replay = input('\n\nWould you like to play again? y/n ')
if replay == 'y' or replay == 'Y' or replay == 'yes' or replay == 'Yes':
    what_game = load_game()
    user_choice(what_game)
else:
    print('\n\nThank you for playing WOG.')



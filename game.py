# -*- coding: utf-8 -*-

# `random` module is used to shuffle field, see§:
# https://docs.python.org/3/library/random.html#random.shuffle
__author__ = 'gia_sebua'
import random
import sys


# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of:
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """
    field = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,EMPTY_MARK]
    random.shuffle(field)
    return field


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """
    for i in range(0,16,4):
        print(field[i:i+4])


def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    if field == [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,EMPTY_MARK]:
        return True
    else:
        return False


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """
    position = field.index(EMPTY_MARK)
    move = MOVES[key]
    if ((key == 'w' and position <= 3) or (key == 's' and position >= 12) or (key == 'a' and (position % 4) == 0) or (key == 'd' and (position % 4) == 3)):
        raise IndexError('you can\'t move out of borders')

    field[position], field[position + move] = field[position + move], field[position]
    return field


def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up,
        's' - down,
        'a' - left,
        'd' - right
    :return: <str> current move.
    """
    move = input('make a move (w,s,a,d):  ')
    while move not in MOVES.keys():
        move = input('make a move (w,s,a,d):  ')
    return move


def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """
    field = shuffle_field()
    turns = 0
    while not is_game_finished(field):
        try:
            print_field(field)
            move = handle_user_input()
            field = perform_move(field, move)
        except IndexError as ex:
            print(ex)
        except KeyboardInterrupt:
            """
    Это исключение не отрабатывается, при нажатии в консоли ctrl+c пишет
    Traceback (most recent call last):
    File hw3_15_puzzle.py, line 124, in <module>
    тут пишут что KeyboardInterrupt не всегда верно отрабатывает,
    но решить эту проблему не получилось
    http://stackoverflow.com/questions/4606942/why-cant-i-handle-a-keyboardinterrupt-in-python
            """
            print('Shutting down')
            sys.exit()
    else:
        print('You win! Yoy made {} turns'.format(turns))




if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do

    main()

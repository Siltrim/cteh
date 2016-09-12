# -*- coding: utf-8 -*-

# `random` module is used to shuffle field, see§:
# https://docs.python.org/3/library/random.html#random.shuffle
__author__ = 'gia_sebua'
import random


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
    if ((key == 'w' and position <= 3) or (key == 's' and position >= 12) or (key == 'a' and position <= 0) or (key == 'd' and position >=15)):
        print('you can\'t move')
    else:
        field.index(EMPTY_MARK) == position + move


def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up,
        's' - down,
        'a' - left,
        'd' - right
    :return: <str> current move.
    """
    pass


def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """
    start_field = shuffle_field()
    print_field(start_field)


if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do

    main()

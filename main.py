# tic tac toe game

import random

board = """ 
           1 | 2 | 3 
         -------------
           4 | 5 | 6    
         -------------
           7 | 8 | 9    """

game_array = ['', '', ''], ['', '', ''], ['', '', '']

print("Welcome to Tic Tac Toe Game")

print(board)

# section = input("Select from 1-9")

game_over = "No"
turn = True


def add_to_array(number, string):
    x = 0
    y = 0
    if number % 3 != 0:
        x = int(number / 3)
        y = int((number % 3) - 1)
    if number == 3:
        x = 0
        y = 2
    if number == 6:
        x = 1
        y = 2
    if number == 9:
        x = 2
        y = 2
    game_array[x][y] = string


def game_win_condition(string):
    # horizontal
    if game_array[0][0] == string and game_array[0][1] == string and game_array[0][2] == string:
        return True
    if game_array[1][0] == string and game_array[1][1] == string and game_array[1][2] == string:
        return True
    if game_array[2][0] == string and game_array[2][1] == string and game_array[2][2] == string:
        return True

    # vertical
    if game_array[0][0] == string and game_array[1][0] == string and game_array[2][0] == string:
        return True
    if game_array[0][1] == string and game_array[1][1] == string and game_array[2][1] == string:
        return True
    if game_array[0][2] == string and game_array[1][2] == string and game_array[2][2] == string:
        return True

    # diagonal
    if game_array[0][0] == string and game_array[1][1] == string and game_array[2][2] == string:
        return True
    if game_array[0][2] == string and game_array[1][1] == string and game_array[2][0] == string:
        return True


while game_over != "Yes":
    section = input("Select from 1-9")
    while turn:
        if board.find(section, 0) != -1:
            turn = False
            board = board.replace(section, "X")
            add_to_array(int(section), "X")
            # print(board)

            if game_win_condition("X"):
                game_over = "Yes"
                print(board)
                print("You Won!")

        else:
            print("Else is running")
            section = input("Please select an open space from 1-9")
            print("Cannot place X there")

    while not turn:
        bot = str(random.randrange(1, 9, 1))
        if board.find(bot, 0) != -1:
            board = board.replace(bot, "O")
            add_to_array(int(bot), "O")
            for i in game_array:
                print(i)
            print(board)

            if game_win_condition("O"):
                game_over = "Yes"
                print("Bot Won")

            turn = True

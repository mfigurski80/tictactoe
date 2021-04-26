# Tic Tac Toe
from board import print_board, whos_winning


def get_user_move(board, symbol):
    print_board(board)
    move = int(input(f"> {symbol} player move ?"))
    b_list = list(board)
    b_list[move - 1] = symbol
    return "".join(b_list)


def get_next_player(cur, count):
    n = cur + 1
    if n >= count:
        n = 0
    return n


symbols = "xo"
players = [get_user_move, get_user_move]
current_player = 0
board = "         "

while whos_winning(board, symbols) == None:
    new_board = players[current_player](board, symbols[current_player])
    board = new_board
    current_player = get_next_player(current_player, len(symbols))

winner = whos_winning(board, symbols)
print(f"

initial_board = "         "


def print_board(board):
    for i, t in enumerate(board):
        if t == " ":
            print(i + 1, end=" ")
        else:
            print(t + 1, end="")
        if i in [2, 5, 8]:
            print()


def size(board):
    return int(len(board) ** (1 / 2))


def whos_winning(board, player_symbols):
    b = board
    for s in player_symbols:
        match = s * 3
        if b[0:3] == match:
            return s
        if b[3:6] == match:
            return s
        if b[6:9] == match:
            return s
        if b[0] + b[3] + b[6] == match:
            return s
        if b[1] + b[4] + b[7] == match:
            return s
        if b[2] + b[5] + b[8] == match:
            return s
        if b[0] + b[4] + b[8] == match:
            return s
        if b[2] + b[4] + b[6] == match:
            return s
    return None


print_board(initial_board)

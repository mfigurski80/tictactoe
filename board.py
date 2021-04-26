initial_board = "         "


def print_board(board):
    board = "".join([l if l != " " else str(i + 1) for i, l in enumerate(board)])
    s = size(board)
    for y in range(s):
        for x in range(s):
            print(board[y * s + x], end=" ")
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
        if b[0] + b[4] + b[7] == match:
            return s
        if b[1] + b[5] + b[8] == match:
            return s
        if b[2] + b[6] + b[9] == match:
            return s
        if b[0] + b[5] + b[9] == match:
            return s
        if b[3] + b[5] + b[7] == match:
            return s
    return None

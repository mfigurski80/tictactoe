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


def split(board):
    s = size(board)
    return [board[i * s : (i + 1) * s] for i in range(s)]


def transpose(board):
    s = size(board)
    t = [board[i : len(board) : s][::-1] for i in range(s)]
    return t


def rotate(board):  # 45 deg
    s = size(board)
    t = []
    for i in range(s):
        t += [board[i : s * (i + 1) - 1 : s - 1][::-1]]
    for i in range(1, s):
        t += [board[s * (i + 1) + (i - 2) :: s - 1][::-1]]
    return t


def whos_winning(board, player_symbols):
    def match_check(b, match):
        for row in b:
            if match in row:
                return True

    for symbol in player_symbols:
        match = symbol * 3
        if match_check(split(board), match):
            return symbol
        if match_check(transpose(board), match):
            return symbol
        if match_check(rotate(board), match):
            return symbol
        if match_check(rotate("".join(transpose(board))), match):
            return symbol
    return None

board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]


def print_board():
    print(board[0])
    print(board[1])
    print(board[2])


def check_mark(row: int, col: int):
    if board[row][col] == '-':
        return True
    elif board[row][col] != '-':
        return False


def place_mark(row: int, col: int, player_id: int):
    if player_id == 1:
        board[row][col] = 'X'
    elif player_id == 2:
        board[row][col] = 'O'


def check_win(player_id: int):
    di1 = []
    di2 = []
    pos1 = 0
    pos2 = -1
    while pos1 < 3:
        di1.append(board[pos1][pos1])
        di2.append(board[pos2][pos1])
        pos1 += 1
        pos2 -= 1

    if player_id == 1:
        if any([all(p == 'X' for p in row) for row in board]) or all(p == 'X' for p in di1) \
                or all(p == 'X' for p in di2):
            return True
    elif player_id == 2:
        if any([all(p == 'O' for p in row) for row in board]) or all(p == 'O' for p in di1) \
                or all(p == 'O' for p in di2):
            return True
    # For some reason with else it is returning None
    # else:
    return False


def main():
    # print_board()
    # check_mark(1, 1)
    # place_mark(0, 2, 2)
    # print_board()
    # place_mark(1, 1, 2)
    #
    # place_mark(2, 0, 2)
    # print_board()
    # print(check_win(2))
    pass


main()


board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]


def print_board():
    for i in range(3):
        print(board[i])


def check_mark(row: int, col: int):
    if board[row][col] == '-':
        return True
    elif board[row][col] != '-':
        return False


def place_mark(player_id: int):
    row = int(input(f'Player {player_id} enter your row: '))
    col = int(input(f'Player {player_id} enter your column: '))
    if player_id == 1 and check_mark(row, col) is True:
        board[row][col] = 'X'
    elif player_id == 2 and check_mark(row, col) is True:
        board[row][col] = 'O'
    else:
        print(f'Position ({row}, {col}) is taken, please choose another.')
        place_mark(player_id)


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


def check_draw():
    for i in range(3):
        if '-' in board[i]:
            return
    return True


def main():
    print('Let the game begin')
    while True:
        print_board()
        place_mark(1)
        if check_win(1) is True:
            print('Player 1 has won the game!')
        if check_draw() is True:
            print("It's a draw!")
            break
        print_board()
        place_mark(2)
        if check_win(2) is True:
            print('Player 2 has won the game!')
        if check_draw() is True:
            print("It's a draw!")
            break


main()

#Name: Emma Ward
#Assignment: Tic-Tac-Toe Game

def main():
    print('')
    print('***********************************************************************************')
    print('*Welcome to the Tic-Tac-Toe game!                                                 *')
    print('*Instructions:                                                                    *')
    print('*In order to win, select numbers on the board. Whoever gets 3 in a row first wins!*')
    print('***********************************************************************************')
    
    board = make_board()
    player = next_move('')

    while not (end_game(board) or tie(board)):

        print_board(board)
        move(player,board)
        player = next_move(player)

    print_board(board)
    print('Good Job!')


def make_board():
    board = []

    for spot in range(9):
        board.append(spot + 1)
    return board


def print_board(board):

    print()
    print(f' {board[0]} | {board[1]} | {board[2]}')
    print('---+---+---')
    print(f' {board[3]} | {board[4]} | {board[5]}')
    print('---+---+---')
    print(f' {board[6]} | {board[7]} | {board[8]}')
    print()


def tie(board):

    for spot in range(9):
        if board[spot] != 'x' and board[spot] != 'o':
            return False
    return True


def move(player, board):

    spot = int(input(f"{player}'s turn! (1-9): "))
    board[spot - 1] = player


def next_move(now):

    if now == '' or now == 'o':
        return 'x'

    elif now == 'x':
        return 'o'    


def end_game(board):
    return (board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8] or board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or board[0] == board[4] == board[8] or board[2] == board[4] == board[6])

    
main()


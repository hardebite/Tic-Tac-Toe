board = ['-','-','-',
         '-','-','-',
         '-','-','-',]
game=True
def display_board():
    print(board[0] + ' | ' + board[1]  + ' | ' +board[2])
    print(board[3] + ' | ' + board[4]  + ' | ' +board[5])
    print(board[6] + ' | ' + board[7]  + ' | ' +board[8])

def handle_turn():
    player= input("Choose which letter: X or O : ")
    position = input("Choose a position from 1-9:  ")
    position = int(position) - 1

    board[position] =  player.title()


def play_game():
    # Display initial board
    display_board()
    handle_turn()
#
def winner():
    if board[0] == "O" and board[3] == "O" and board[6] == "O":
        print("Player O you win")
        return True
    elif board[0] == "O" and board[1] == "O" and board[2] == "O":
        print("Player O you win")
        return True
    elif board[3] == "O" and board[4] == "O" and board[5] == "O":
        print("Player O you win")
        return True
    elif board[6] == "O" and board[7] == "O" and board[8] == "O":
        print("Player O you win")
        return True
    elif board[2] == "O" and board[5] == "O" and board[8] == "O":
        print("Player O you win")
        return True
    elif board[1] == "O" and board[4] == "O" and board[7] == "O":
        print("Player O you win")
        return True
    elif board[6] == "O" and board[4] == "O" and board[2] == "O":
        print("Player O you win")
        return True
    elif board[0] == "O" and board[4] == "O" and board[8] == "O":
        print("Player O you win")
        return True
    elif board[0] == "X" and board[3] == "X" and board[6] == "X":
        print("Player X you win")
        return True
    elif board[0] == "X" and board[1] == "X" and board[2] == "X":
        print("Player X you win")
        return True
    elif board[3] == "X" and board[4] == "X" and board[5] == "X":
        print("Player X you win")
        return True
    elif board[6] == "X" and board[7] == "X" and board[8] == "X":
        print("Player X you win")
        return True
    elif board[2] == "X" and board[5] == "X" and board[8] == "X":
        print("Player X you win")
        return True
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":
        print("Player X you win")
        return True
    elif board[6] == "X" and board[4] == "X" and board[2] == "X":
        print("Player X you win")
        return True
    elif board[0] == "X" and board[4] == "X" and board[8] == "X":
        print("Player X you win")
        return True
while game == True:
    if "-" not in board:
        display_board()
        break
    if winner() == True:
        display_board()
        break

    play_game()






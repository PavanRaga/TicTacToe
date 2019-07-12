print("Welcome to TicTacToe")

board = [['_','_','_'],['_','_','_'],['_','_','_']]
board_template = [['1','2','3'],['4','5','6'],['7','8','9']]
game = 1
players = ['X', 'O']

def print_board(b, template=0):
    for row,value in enumerate(b):
        for index,value in enumerate(value):
            if template:
                value = value if board[row][index] == '_' else '_'
            print("__{0}__".format(value), end="")
            if index != 2:
                print("|", end="")
            else:
                print("\n")
        if row == 2:
            print("     |     |     ")

def get_row(pos):
    if pos < 4:
        return 0
    elif pos < 7:
        return 1
    else:
        return 2

def get_col(pos):
    if pos in [1, 4, 7]:
        return 0
    if pos in [2 ,5, 8]:
        return 1
    else:
        return 2

def pos_available(pos):
    if board[get_row(pos)][get_col(pos)] != "_":
        return 0
    else:
        return 1

def assign_pos(pos,player):
    board[get_row(pos)][get_col(pos)] = player

def check_row():
    for row in board:
        if row.count('X') == 3 or row.count('O') == 3:
            return 1
def check_col():
    i = 0;
    while(i<len(board)):
        lis = [row[i] for row in board]
        i += 1
        if lis.count('X') == 3 or lis.count('O') == 3:
            return 1

def check_diag():
    lis = [val[index] for index,val in enumerate(board)]
    if lis.count('X') == 3 or lis.count('O') == 3:
        return 1
    lis = [val[-index-1] for index,val in enumerate(board)]
    if lis.count('X') == 3 or lis.count('O') == 3:
        return 1

def check_game():
    if check_row() or check_col() or check_diag():
        return 1

def check_deadlock():
    x_list = list(filter(lambda x:x.count('_') == 0,board))
    if (len(x_list) == 3):
        return 1
    return 0

def play_again():
    print("Do you want to play again?(0/1)")
    global game
    game = int(input())
    if game != 0 and game !=1:
        print("Try again!(0/1)")
        play_again()
    global board
    global board_template
    board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    board_template = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

while(game):
    players.reverse()
    print_board(board_template, 1)
    print("Player {}, pick a position?".format(players[0]))
    pos = int(input())
    if not pos_available(pos):
        print("Position {} unaaviable, pls try again".format(pos));
    assign_pos(pos,players[0])
    print_board(board)
    if check_deadlock():
        print("Eff! Deadlock. Both players won!")
        play_again()
    if check_game():
        print("Game Over! Player {} has won!".format(players[0]))
        play_again()



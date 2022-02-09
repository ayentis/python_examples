board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]


def display_board(board):
    print("+", "-" * 7, "+", "-" * 7, "+", "-" * 7, "+", sep="")
    for board_row in board:
        print("|", " " * 7, "|", " " * 7, "|", " " * 7, "|", sep="", end="\n|")
        for board_col in board_row:
            print(" " * 3, board_col," " * 3, "|", sep="", end="")
        print("\n", "|", " " * 7, "|", " " * 7, "|", " " * 7, "|", sep="")
        print("+", "-" * 7, "+", "-" * 7, "+", "-" * 7, "+", sep="")


def enter_move(board):
    try:
        player = int(input("enter your step (digit 1-9) "))
    except TypeError:
        print("Wrong value. try again")
        # continue


def make_list_of_free_fields(board):
    pass
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):
    pass
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    pass
    # The function draws the computer's move and updates the board.


display_board(board)
# while True:


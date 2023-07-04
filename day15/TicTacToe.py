def welcome():
    print("\nWelcome to the Tic Tac Toe Game.")
    print("Board Place Refrence:")
    print("\t top-L | top-M | top-R ")
    print("\t-------+-------+-------")
    print("\t mid-L | mid-M | mid-R ")
    print("\t-------+-------+-------")
    print("\t low-L | low-M | low-R ")
    print(end="\n\n")

def print_board(board: dict):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print("-+-+-")
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print("-+-+-")
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def whoWon(board: dict):
    if board['top-L'] == board['top-M'] == board['top-R'] and board['top-L'] in ("X","O") : return f"{board['top-L']}"
    elif board['mid-L'] == board['mid-M'] == board['mid-R'] and board['mid-L'] in ("X","O"): return f"{board['mid-L']}"
    elif board['low-L'] == board['low-M'] == board['low-R'] and board['low-L'] in ("X","O"): return f"{board['low-L']}"
    elif board['top-L'] == board['mid-L'] == board['low-L'] and board['top-L'] in ("X","O"): return f"{board['top-L']}"
    elif board['top-M'] == board['mid-M'] == board['low-M'] and board['top-M'] in ("X","O"): return f"{board['top-M']}"
    elif board['top-R'] == board['mid-R'] == board['low-R'] and board['top-R'] in ("X","O"): return f"{board['top-R']}"
    elif board['top-L'] == board['mid-M'] == board['low-R'] and board['mid-M'] in ("X","O"): return f"{board['mid-M']}"
    elif board['top-R'] == board['mid-M'] == board['low-L'] and board['mid-M'] in ("X","O"): return f"{board['mid-M']}"
    else: return None

def start(board: dict):
    turn = "X"

    while True:
        print_board(board) # prints board
        who_won = whoWon(board)
        if who_won is not None: # checks won or not
            print(f"\n{who_won} WON\n")
            break
        
        if " " not in board.values(): #checks for remaining moves
            print("\nDRAW\n")
            break

        move = input(f"\nEnter the move of {turn}: ").strip() #takes move 
        if move not in board.keys() or board[move] != " ": # checks valid or move or not and the move is already taken or not
            print("\nINVALID MOVE\n")
            continue
        
        board[move] = turn #sets X or O in that move

        turn = "X" if turn == "O" else "O" # switches player

myBoard = {
    'top-L':' ',
    'top-M':' ',
    'top-R':' ',
    'mid-L':' ',
    'mid-M':' ',
    'mid-R':' ',
    'low-L':' ',
    'low-M':' ',
    'low-R':' ',
}

if __name__ == "__main__":
    welcome()
    start(myBoard)

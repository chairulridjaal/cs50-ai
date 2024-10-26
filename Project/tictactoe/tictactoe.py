"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Declare counters
    count_x = 0
    count_o = 0

    # Skim every row and column on board to see if there's an X or O
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X: 
                count_x += 1
            if board[row][col] == O: 
                count_o += 1
    
    # Determine who's turn it is by seeing if X has put more than O
    if count_x > count_o:
        return O
    else: 
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Declare the tuple
    legal_actions = set()

    # Skim every row and col on board to see if there's an EMPTY spot
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                legal_actions.add((row, col))

    # Returns list of all the EMPTY spots
    return legal_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Check if action is valid (legal actions)
    if action not in actions(board):
        raise Exception("Not a valid action")
    
    # Action divided into row and col
    row, col = action

    # Create a deep copy and insert the action
    copy_board = copy.deepcopy(board)
    copy_board[row][col] = player(board)
    
    # Return copy of the board
    return copy_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Checks if either X or O has won the game
    if checkHorizontal(board, X) or checkVertical(board, X) or checkMaindiagonal(board, X) or checkAntidiagonal(board, X):
        return X
    elif checkHorizontal(board, O) or checkVertical(board, O) or checkMaindiagonal(board, O) or checkAntidiagonal(board, O):
        return O

def checkHorizontal(board,player):
    # Checks if every col in a row is equal
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return False

def checkVertical(board, player):
    # Checks if every row in col is equal
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    return False

def checkMaindiagonal(board, player):
    # Checks if the main diagonal "/" is equal
    count = 0
    for row in range(len(board)):
        for col in range(len(board)):
            if row == col and board[row][col] == player:
                count += 1
    if count == 3:
        return True
    else:
        return False
        
def checkAntidiagonal(board, player):
    # Checks if the anti-diagonal "\" is equal
    count = 0
    for row in range(len(board)):
        for col in range(len(board)):
            if (len(board) - row - 1) == col and board[row][col] == player:
                count += 1
    if count == 3:
        return True
    else:
        return False

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Checks if there is a winner
    if winner(board) == X:
        return True
    if winner(board) == O:
        return True
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Determines the value of the board
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def MaxValue(board):
    # Maximizing value from the MinValue until terminal(board) is reached
    if terminal(board):
        return utility(board)
    
    v = float('-inf') # Important, for some reason -math.inf didn't work
    for action in actions(board):
        v = max(v, MinValue(result(board, action)))
    return v

def MinValue(board):
    # Minimizing value from the MaxValue until terminal(board) is reached
    if terminal(board):
        return utility(board)
    
    v = float('inf') # Important, for some reason math.inf didn't work
    for action in actions(board):
        v = min(v, MaxValue(result(board, action)))
    return v

def minimax(board):
    # Finds the minimax value of a given board
    if terminal(board):
        return None

    # Finds best action by maximizing value gathered from the MinValue
    if player(board) == X: 
        best_value = float('-inf')
        best_action = None
        for action in actions(board):
            value = MinValue(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
        return best_action
    
    # Finds best action by minimizing value gathered from the MaxValue
    else:
        best_value = float('inf')
        best_action = None
        for action in actions(board):
            value = MaxValue(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action
        return best_action
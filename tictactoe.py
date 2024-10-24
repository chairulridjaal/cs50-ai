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
    count_x = 0
    count_o = 0

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X: 
                count_x += 1
            if board[row][col] == O: 
                count_o += 1
    
    if count_x > count_o:
        return O
    else: 
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    legal_actions = set()

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                legal_actions.add((row, col))

    return legal_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Not a valid action")
    
    row, col = action
    copy_board = copy.deepcopy(board)
    copy_board[row][col] = player(board)
    
    return copy_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkHorizontal(board, X) or checkVertical(board, X) or checkMaindiagonal(board, X) or checkAntidiagonal(board, X):
        return X
    elif checkHorizontal(board, O) or checkVertical(board, O) or checkMaindiagonal(board, O) or checkAntidiagonal(board, O):
        return O

def checkHorizontal(board,player):
        for row in range(len(board)):
            if board[row][0] == player and board[row][1] == player and board[row][2] == player:
                return True
        return False

def checkVertical(board, player):
        for col in range(len(board)):
            if board[0][col] == player and board[1][col] == player and board[2][col] == player:
                return True
        return False

def checkMaindiagonal(board, player):
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
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def MaxValue(board):
    if terminal(board):
        return utility(board)
    
    v = float('-inf')
    for action in actions(board):
        v = max(v, MinValue(result(board, action)))
    return v

def MinValue(board):
    if terminal(board):
        return utility(board)
    
    v = float('inf')
    for action in actions(board):
        v = min(v, MaxValue(result(board, action)))
    return v

def minimax(board):
    if terminal(board):
        return None

    if player(board) == X: 
        best_value = float('-inf')
        best_action = None
        for action in actions(board):
            value = MinValue(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
        return best_action
    
    else:
        best_value = float('inf')
        best_action = None
        for action in actions(board):
            value = MaxValue(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action
        return best_action
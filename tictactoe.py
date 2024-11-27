"""
Tic Tac Toe Player
"""

import math

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
    # Flatten the board to make counting easier
    flattened_board = [cell for row in board for cell in row]

    # Count moves of X and O
    x_moves = flattened_board.count(X)
    o_moves = flattened_board.count(O)

    # Determine the next player
    return O if x_moves > o_moves else X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    availableActions = set()  # Use a set to store unique actions

    for i, row in enumerate(board):         # Loop through rows with index
        for j, cell in enumerate(row):     # Loop through columns with index
            if cell == EMPTY:              # Check if the cell is empty
                availableActions.add((i, j))  # Add the (row, column) tuple to the set

    return availableActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Unpack the action tuple
    i, j = action

    # Validate the action before accessing the board
    if not (0 <= i < 3 and 0 <= j < 3):  # Simplified range check
        raise ValueError("Invalid action: Out-of-bounds position.")
    
    if board[i][j] is not EMPTY:
        raise ValueError("Invalid action: Position already taken.")

    # Create a deep copy of the board
    new_board = [row[:] for row in board]

    # Get the current player
    current_player = player(board)

    # Apply the action
    new_board[i][j] = current_player

    return new_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if there is a winner
    if winner(board) is not None:
        return True

    # Check if the board is full
    return all(cell is not EMPTY for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    results = winner(board)
    if results == X:
        return 1
    elif results == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None  # No moves available if the game is over

    current_player = player(board)

    if current_player == X:
        _, action = maxValue(board)  # Maximize for X
    else:
        _, action = minValue(board)  # Minimize for O

    return action


def maxValue(board):
    """
    Returns the maximum utility and the corresponding action.
    """
    if terminal(board):
        return utility(board), None

    v = -math.inf
    best_action = None
    for action in actions(board):  # Iterate over possible actions
        next_board = result(board, action)
        if terminal(next_board):  # Short-circuit for terminal boards
            return utility(next_board), action
        value, _ = minValue(next_board)  # Evaluate further
        if value > v:
            v = value
            best_action = action
    return v, best_action



def minValue(board):
    """
    Returns the minimum utility and the corresponding action.
    """
    if terminal(board):
        return utility(board), None

    v = math.inf
    best_action = None
    for action in actions(board):  # Iterate over possible actions
        next_board = result(board, action)
        if terminal(next_board):  # Short-circuit for terminal boards
            return utility(next_board), action
        value, _ = maxValue(next_board)  # Evaluate further
        if value < v:
            v = value
            best_action = action
    return v, best_action


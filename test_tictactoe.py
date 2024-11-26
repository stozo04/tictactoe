import pytest
 
from tictactoe import EMPTY, O, X, actions, initial_state, player, terminal, utility, winner


def test_initial_state():
    assert initial_state() == [[EMPTY, EMPTY, EMPTY],
                               [EMPTY, EMPTY, EMPTY],
                               [EMPTY, EMPTY, EMPTY]]
    
def test_player():
    board = initial_state()
    assert player(board) == X
    board[0][0] = X
    assert player(board) == O
    board[0][1] = O
    assert player(board) == X
    board[0][2] = X
    assert player(board) == O
    board[1][0] = O
    assert player(board) == X
    board[1][1] = X
    assert player(board) == O
    board[1][2] = O
    assert player(board) == X
    board[2][0] = X
    assert player(board) == O
    board[2][1] = O
    assert player(board) == X
    board[2][2] = X
    assert player(board) == O
    
def test_actions():
    board = initial_state()
    res = actions(board)
    assert res == {(0, 1), (1, 2), (2, 1), (0, 0), (1, 1), (2, 0), (0, 2), (2, 2), (1, 0)}
    board[0][1] = X
    res = actions(board)
    assert res == {(1, 2), (2, 1), (0, 0), (1, 1), (2, 0), (0, 2), (2, 2), (1, 0)}
    board[1][2] = O
    res = actions(board)
    assert res == {(2, 1), (0, 0), (1, 1), (2, 0), (0, 2), (2, 2), (1, 0)}
    board[2][1] = X
    res = actions(board)
    assert res == {(0, 0), (1, 1), (2, 0), (0, 2), (2, 2), (1, 0)}
    board[0][0] = X
    res = actions(board)
    assert res == {(1, 1), (2, 0), (0, 2), (2, 2), (1, 0)}
    board[1][1] = O
    res = actions(board)
    assert res == {(2, 0), (0, 2), (2, 2), (1, 0)}
    board[1][0] = O
    res = actions(board)
    assert res == {(2, 0), (0, 2), (2, 2)}
    board[2][0] = X
    res = actions(board)
    assert res == {(0, 2), (2, 2)}
    board[2][2] = X
    res = actions(board)
    assert res == {(0, 2)}
    board[0][2] = X
    res = actions(board)
    assert res == set()

def test_winner():
    # First Row
    board = initial_state()
    board[0][0] = X
    board[0][1] = X
    board[0][2] = X
    assert winner(board) == X
    # Second Row
    board = initial_state()
    board[1][0] = X
    board[1][1] = X
    board[1][2] = X
    assert winner(board) == X
    # Third Row
    board = initial_state()
    board[2][0] = X
    board[2][1] = X
    board[2][2] = X
    assert winner(board) == X
    # First Column
    board = initial_state()
    board[0][0] = X
    board[1][0] = X
    board[2][0] = X
    assert winner(board) == X
    # Second Column
    board = initial_state()
    board[0][1] = X
    board[1][1] = X
    board[2][1] = X
    assert winner(board) == X
    # Third Column
    board = initial_state()
    board[0][2] = X
    board[1][2] = X
    board[2][2] = X
    assert winner(board) == X
    # Right Diagnol
    board = initial_state()
    board[0][2] = X
    board[1][1] = X
    board[2][0] = X
    assert winner(board) == X
    # Left Diagnol
    board = initial_state()
    board[0][0] = X
    board[1][1] = X
    board[2][2] = X
    assert winner(board) == X

def test_terminal():
    board = initial_state()
    # test empty state
    assert terminal(board) == False
    board[1][0] = X
    board[1][1] = X
    board[1][2] = X
    # test with winner
    assert terminal(board) == True
    board = initial_state()
    board[0][0] = O
    board[0][1] = X
    board[0][2] = O
    board[1][0] = O
    board[1][1] = X
    board[1][2] = X
    board[2][0] = X
    board[2][1] = O
    board[2][2] = X
    # test tie full board
    assert terminal(board) == True

def test_utility():
    board = initial_state()
    board[1][0] = X
    board[1][1] = X
    board[1][2] = X
    # test X win
    assert utility(board) == 1
    board = initial_state()
    board[1][0] = O
    board[1][1] = O
    board[1][2] = O
    # test O win
    assert utility(board) == -1
    board = initial_state()
    board[0][0] = O
    board[0][1] = X
    board[0][2] = O
    board[1][0] = O
    board[1][1] = X
    board[1][2] = X
    board[2][0] = X
    board[2][1] = O
    board[2][2] = X
    # test tie full board
    assert utility(board) == 0

# Tic Tac Toe with AI

This project is a Python-based Tic Tac Toe game featuring an interactive graphical user interface (GUI) created with Pygame and an AI opponent powered by the Minimax algorithm.

## Features

- **GUI Interface**: The game uses Pygame for an intuitive and interactive gaming experience.
- **Play Modes**: Choose to play as either "X" or "O".
- **AI Opponent**: The AI uses the Minimax algorithm to ensure optimal gameplay.
- **Game State Management**: Functions to handle board states, validate moves, determine winners, and check for terminal states.

## Files

### 1. `runner.py`
- The main script that initializes the game and manages the GUI using Pygame.
- Allows the player to interact with the game board and handles AI moves.
- Displays the current state of the game, including win, lose, or draw conditions.

### 2. `tictactoe.py`
- Contains the game logic for Tic Tac Toe, including:
  - Initializing the board.
  - Determining the current player and available actions.
  - Applying actions and determining the result.
  - Checking for winners or if the game has ended.
  - Implementing the Minimax algorithm for the AI.

## Requirements

- Python 3.x
- Pygame library

## How to Run

1. Install the required library:
    ```bash
    pip install pygame
    ```

2. Run the game:
    ```bash
    python runner.py
    ```

## How to Play

1. Select your player ("X" or "O") at the start screen.
2. Take turns clicking on the board to make your move.
3. The AI will play optimally to either block you or secure its win.

## Game Logic

- The AI uses the **Minimax algorithm** to evaluate the optimal move.
- The game terminates when:
  - A player wins (three in a row horizontally, vertically, or diagonally).
  - The board is full, resulting in a draw.

## Customization

You can modify the game's visuals or tweak the AI's logic by editing the respective functions in `runner.py` or `tictactoe.py`.

---

Have fun playing Tic Tac Toe!

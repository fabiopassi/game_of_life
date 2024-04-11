""" This module contains all the functions for ... script """

# Importing modules
import numpy as np
import curses
from numba import njit

# Functions

def print_canvas(stdscr, N_ROWS, N_COLS) :

    for i in range(0, N_ROWS + 2) :
        stdscr.addstr(i, 0, "#")
        stdscr.addstr(i, N_COLS+1, "#")

    for i in range(0, N_COLS + 2) :
        stdscr.addstr(0, i  , "#")
        stdscr.addstr(N_ROWS+1, i, "#")



def print_board(board, stdscr) :

    for i in range(1, board.shape[0] - 1):
        for j in range(1, board.shape[1] - 1):
            if board[i][j] > 0.5 : 
                stdscr.addstr(i, j, ' ', curses.color_pair(1))
            else :
                stdscr.addstr(i, j, ' ')
            


@njit
def eval_new_gen(board) :

    survived = 0
    new_board = np.zeros(board.shape)

    for i in range(1, board.shape[0] - 1) :
        for j in range(1, board.shape[1] - 1) :

            alive_neigh = 0                                         # Number of alive neighbours
            new_board[i][j] = board[i][j]                           # Copy the initial state

            alive_neigh += board[i+1][j] + board[i-1][j]            # Same column       : 2 neighbours
            alive_neigh += board[i][j+1] + board[i][j-1]            # Same row          : 2 neighbours
            alive_neigh += board[i+1][j+1] + board[i-1][j-1]        # First diagonal    : 2 neighbours
            alive_neigh += board[i-1][j+1] + board[i+1][j-1]        # Second diagonal   : 2 neighbours
            alive_neigh = int(alive_neigh)

            # Case 1 : Death of cell
            if alive_neigh < 2 : new_board[i][j] = 0
            if alive_neigh > 3 : new_board[i][j] = 0

            # Case 2: New-born cell
            if alive_neigh == 3 : 
                new_board[i][j] = 1
            
            # Check survived
            if new_board[i][j] > 0.5 : survived = survived + 1

    return new_board, survived
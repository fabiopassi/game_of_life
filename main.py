# ***********************************
# *                                 *
# *         GAME OF LIFE            *
# *                                 *
# ***********************************

# Importing modules
from utils.functions import *
import numpy as np
import curses
from curses import wrapper
import time


# Game
def main(stdscr) :

    # Green background color pair
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)

    # Variables
    N_ROWS = 40                                         # Number of rows
    N_COLS = 80                                         # Number of columns
    board = np.zeros((N_ROWS+2, N_COLS+2))              # Game board
    x_curs = 1                                          # Cursor x position
    y_curs = 1                                          # Cursor y position
    generation = 0                                      # Number of the current generation
    survived = -1                                       # Survived cells

    # Print canvas
    print_canvas(stdscr, N_ROWS, N_COLS)
    stdscr.move(y_curs, x_curs)

    # Game initialization
    key = "A"
    while( True ) :

        # Print board
        print_board(board, stdscr)
        stdscr.addstr(int(board.shape[0]/2)-2, int(board.shape[1] + 20), f"Commands:")
        stdscr.addstr(int(board.shape[0]/2),   int(board.shape[1] + 20), f"- Arrows : move in the board")
        stdscr.addstr(int(board.shape[0]/2)+1, int(board.shape[1] + 20), f"- d : place/remove life")
        stdscr.addstr(int(board.shape[0]/2)+2, int(board.shape[1] + 20), f"- q : start game")
        stdscr.move(y_curs, x_curs)

        # Update screen and get input
        stdscr.refresh()
        key = stdscr.getkey()

        # Process input
        match key :
            # Move in the canvas
            case "KEY_UP" :
                if y_curs > 1 : y_curs -= 1
            case "KEY_DOWN" :
                if y_curs < N_ROWS : y_curs += 1
            case "KEY_RIGHT" :
                if x_curs < N_COLS : x_curs += 1
            case "KEY_LEFT" :
                if x_curs > 1 : x_curs -= 1
            # Place or remove life
            case "d" :
                if board[y_curs][x_curs] < 0.5 : 
                    board[y_curs][x_curs] = 1
                else :
                    board[y_curs][x_curs] = 0
            # Quit option, aka start game
            case "q":
                break
            # Default: nothing
            case _:
                pass


    # Game loop
    stdscr.clear()                                      # Clear screen
    curses.curs_set(0)                                  # Hide cursor
    stdscr.nodelay(True)

    print_canvas(stdscr, N_ROWS, N_COLS)
    print_board(board, stdscr)
    stdscr.addstr(int(board.shape[0]/2)-1, int(board.shape[1] + 20), f"Generation : {generation}")
    stdscr.refresh()
    
    while(survived != 0) :

        # Check for quit
        try :
            key = stdscr.getkey()
        except :
            key = None

        if key == "q" : break

        # Calculate the new state
        board, survived = eval_new_gen(board)

        # Increment generation
        generation += 1

        # Print the new board
        print_board(board, stdscr)

        # Print the generation
        stdscr.addstr(int(board.shape[0]/2)-1, int(board.shape[1] + 20), f"Generation : {generation}")
        stdscr.addstr(int(board.shape[0]/2)+1, int(board.shape[1] + 20), f"Survived   : {survived:<4}")

        # Show the screen
        stdscr.refresh()

        # Pause
        time.sleep(0.4)
    
    # Reset curses settings
    curses.curs_set(1)
    stdscr.nodelay(False)

    # Final status
    stdscr.addstr(board.shape[0] + 2, 0, "Finished! Press any key to exit.")
    stdscr.refresh()
    stdscr.getch()


# Curses wrapper
wrapper(main)
# game_of_life

Conway's Game of Life on LINUX terminal.

The game is written in python. The only additional packages required to run the game are `numpy` and `numba`; if you have conda installed, the command:

```bash
conda create -n game_of_life numba
```

should create an environment with all the necessary packages.

After this, you can start the game with the commands:

```bash
conda activate game_of_life
python main.py
```

In the initial screen, use the key "d" to place or remove life from the board. When you obtain the desired initial state, simply press "q" to start the game.  
During the game, press "q" to stop the execution.

DISCLAIMER: This procedure was tested only on ubuntu 22.04, but it should work also on other distros.

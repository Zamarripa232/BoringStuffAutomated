# conway.py
# Automate the Boring Stuff
# Chapter 4
# Conway's Game of Life :D

import random
import time
import copy

WIDTH = 60
HEIGHT = 20

# Createa  list of list for the cells:

nextCells = []
for x in range(WIDTH):
    column = [] # Create a fresh column.
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#') # Add a living cell
        else:
            column.append(' ') # Add a dead cell
    nextCells.append(column) # nextCElls is a list of column lists.

while True: # Main loop of the program
    print('\n\n\n\n\n') # Separate each step with newlines.
    currentCells = copy.deepcopy(nextCells)
    # Print currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # Print the # or space
        print() # Print a newline at the end of a row
    
    # Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coords:
            # '% WIDTH' ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count the number of living neighbors
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # top-left is alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # top is alive
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # top-right is alive
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # Left is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # Right is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-left is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # Bottom is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-right is alive.

            # Set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with 2 or 3 stay alive
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive
                nextCells[x][y] = '#'
            else:
                # Everything else DIESSSSS
                nextCells[x][y] = ' '
    time.sleep(1) # 1 second pause
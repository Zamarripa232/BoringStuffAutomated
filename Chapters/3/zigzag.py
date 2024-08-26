# zigzag.py
# Automate the Boring Stuff
# Chapter 3

import time, sys
indent = 0 # how many spaces to indent
indentIncreasing = True # Whether the indentation is increasing or not.

try:
    while True: # main program loop.
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second.
        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction:
                indentIncreasing = False
        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()

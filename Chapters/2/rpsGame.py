# rpsGame.py

import random, sys

# Fancy Title Art
print('##########################')
print('# ROCK, PAPER, SCISSORS! #')
print('##########################')

# initialize variables
wins    = 0
losses  = 0
ties    = 0

# main game loop
while True:
    print('Current Score:')
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    print('')
    # Player Input Loop
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
        playerMove = input()

        if playerMove == 'q':
            sys.exit()

        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break

        print('Enter one of r, p s or q only.')

    #Display what the player chose:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('We have a tie!')
        ties += 1
    elif playerMove == 'r' and computerMove == 's':
        print('Player wins!')
        wins += 1
    elif playerMove == 'p' and computerMove == 'r':
        print('Player wins!')
        wins += 1
    elif playerMove == 's' and computerMove == 'p':
        print('Player wins!')
        wins += 1
    else:  # If it isn't a tie, and the player didn't win, then they lost.
        print('You lose!')
        losses += 1

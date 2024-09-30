# coinFlips.py
# Automate the Boring Stuff
# Chapter 4
# Practice Project 2
# flip coins, create a list of h/t, 
# check list for streak(s) of 6
# goal: 10,000 coin flips

import random

numberOfStreaks = 0
flips = []

for experimentNumber in range(1):
    # create list of h/t values.
    flipResult = random.randint(0,1)
    print('Doing a coin flip')
    print('The result was ' + str(flipResult))
    print('adding flip to list')
    print('going back to flip again')
    # check for 6 streak.
    print('I\'m checking for a streak of 6...') # look at six at a time?

print('Chance of streak: %s%%' % (numberOfStreaks / 100))

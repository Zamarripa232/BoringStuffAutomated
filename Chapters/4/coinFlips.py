# coinFlips.py
# Automate the Boring Stuff
# Chapter 4
# Practice Project 2
# flip coins, create a list of h/t, 
# check list for streak 6 after 100 flips
# goal: repeat 10,000 times, print % of experiments that had a streak of 6

import random

FLIPCOUNT = 100
TOTALEXPERIMENTS = 10000

totalFlips = FLIPCOUNT * TOTALEXPERIMENTS
numberOfStreaks = 0

def flipCoin():
    """Returns the result of a coin flip, either 1 for heads, 0 for tails."""
    return random.randint(0,1)

def createFlipList(amtOfFlips):
    """Returns a list of coin flips"""
    tmpFlips = []
    for i in range(amtOfFlips):
        flipResult = flipCoin()
        tmpFlips.append(flipResult)
    return tmpFlips

def checkStreak(headsTails, flipList):
    """Returns 1 if a streak is found"""
    streak = 0
    for i in flipList:
        if i == headsTails:
            streak += 1
            if streak == 6:
                return 1
        else:
            streak = 0
    return 0

for experimentNumber in range(TOTALEXPERIMENTS):
    flips = createFlipList(FLIPCOUNT)
    if checkStreak(1, flips) > 0:
        numberOfStreaks += 1
        continue
    elif checkStreak(0, flips) > 0:
        numberOfStreaks += 1
        continue

print('Chance of streak: %s%%' % (numberOfStreaks / 100))

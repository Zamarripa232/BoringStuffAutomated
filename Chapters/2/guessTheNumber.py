# guessTheNumber.py

import random

secretNumber = random.randint(1, 100)
print('I\'ve got a number between 1 and 100.')

# Ask to guess 6 times
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low!')
    elif guess > secretNumber:
        print('Your guess is too high!')
    else:
        break # Only if they guess the number!

# Check answer
if guess == secretNumber:
    print('You did it! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('You failed me. I am so disappointed. It was ' + str(secretNumber))

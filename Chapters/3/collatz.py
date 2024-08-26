# collatz.py
# Automate the Boring Stuff
# Chapter 3 Practice Project

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1
loopyNum = 0
print("Enter number:")
while loopyNum != 1:
    try:
        intInput = int(input())
    except ValueError:
        print('You must enter an integer.')
        continue
    loopyNum = collatz(intInput)

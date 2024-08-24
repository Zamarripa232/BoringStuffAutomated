# spamHowdy.py
# Practice Question 9

# Write code that prints Hello if 1 is stored in spam,
# prints Howdy if 2 is stored in spam, and prints Greetings!
# if anything else is stored in spam.

# I added a little more here, namely the exception handling

while True:
    print('Type 1 for a Hello, 2 for a Howdy, and any other integer for a standard boring greeting.')
    try:
        spam = int(input())
        break
    except ValueError:
        print('That\'s not a valid integer, try again.')

if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')

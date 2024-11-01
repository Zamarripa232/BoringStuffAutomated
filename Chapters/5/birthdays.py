# birthdays.py
# Automate the Boring Stuff
# Chapter 5
# Data about friends birthdays

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print()
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have any birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated')
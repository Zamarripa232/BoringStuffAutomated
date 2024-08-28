# allMyCats1
# Automate the Boring Stuff
# Chapter 4

catNames = []

while True:
    print('Enter the name of a cat ' + str(len(catNames) + 1) + ' or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation

print('The cat names are:')

for name in catNames:
    print(' ' + name)
# commaCode.py
# Automate the Boring Stuff
# Chapter 4
# Practice Project 1
# concatenating a list into a string with commas and 'and'
# also handles empty lists.

testList = ['apples', 'bananas', 'tofu', 'cats']
finalIndex = len(testList) - 1
concatString = ''

for i in range(0, len(testList)-1):
    concatString = concatString + testList[i] + ', '

if testList != []:
    print(concatString + 'and ' + testList[finalIndex])
else:
    print('There was nothing in the list.')
# myPets.py
# Automate the Boring Stuff
# Chapter 4
# a very pets based chapter it seems

myPets = ['PZ Meowers', 'Steven', 'Farore', 'Takis Fuego']
print('Enter a pet name:')
name = input()

if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')

### Multiple Assignment
### Tuple Unpacking

cat = ['chonky', 'orange', 'friendly']
size, color, disposition = cat # Assigns all at once!
# Will return a ValueError if number of variables and length of list
# are not exactly the same.

### Enumerate() Example
for index, item in enumerate(cat):
    print('Pet #' + str(index) + ' is ' + item)
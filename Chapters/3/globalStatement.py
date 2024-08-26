# globalStatement.py
# Automate the Boring Stuff
# Chapter 3

def spam():
    global eggs
    eggs = 'spam'
eggs = 'global'
spam()
print(eggs)

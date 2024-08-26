# sameNameLocalGlobal.py
# Automate the Boring Stuff
# Chapter 3

def spam():
    global eggs
    eggs = 'spam' # this is the global
def bacon():
    eggs = 'bacon' # this is the locals
def ham():
    print(eggs) # this is the global
eggs = 42 # this is the global

spam()
print(eggs)

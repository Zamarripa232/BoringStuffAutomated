# fiveTimes.py
# for Loops and the range() Function

print('My name is')
for i in range(5):
    print('Jimmy Five times (' + str(i) + ')')

## Done as a while loop:
i = 0
print('My name is')
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1

## Another for loop example
total = 0
for num in range(101):
    total += num
print(total)

from collections import deque

d=deque('love') # making a new deque with items

# Stack functions: append(),pop()

d.append('m') # adding a new entry to the right side
d.pop() # return and remove the rightmost item
print(d) # printing the representation of the deque

# appendleft(),popleft()
d.appendleft('f') # adding a new entry to the left side
d.popleft() # return and remover the leftmost item

# list the content of the deque
list(d)

# Extending deque
d.extend(['you'])
print(d)
d.extendleft(['l'])
print(d)

#reversing deque
d.reverse()
print(d)


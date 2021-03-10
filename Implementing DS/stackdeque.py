from collections import deque
 
stack = deque()
 
# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
print("length of stack is",len(stack))
 
print('Initial stack: ', stack) 

print('\nElements poped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
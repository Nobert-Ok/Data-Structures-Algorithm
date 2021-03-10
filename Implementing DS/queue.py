from collections import deque

s = deque()

s.appendleft(10)
s.appendleft(20)
s.appendleft(30)
s.appendleft(40)

print(s)

s.popleft()

print(s[-1])


print(s)
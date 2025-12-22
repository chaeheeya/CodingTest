from collections import deque

L = deque()
for i in range(1, int(input())+1):
    L.append(i)

while len(L) > 1:
    L.popleft()
    L.append(L.popleft())

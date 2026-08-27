import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)
count = 0

for start in range(1,n+1):
    if visited[start]:
        continue
    count += 1
    visited[start] = True
    q = deque([start])
    while q:
        curr = q.popleft()
        for next in graph[curr]:
            if not visited[next]:
                visited[next] = True
                q.append(next)

print(count)
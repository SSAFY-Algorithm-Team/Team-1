# 코더스패스 1145 너비 우선 탐색
from collections import deque

def dfs(graph, start):
    visited = [False] * len(graph)
    q.append(start)
    visited[start] = True
    order = []

    while q:
        v = q.popleft()
        order.append(v)
        for next_node in graph[v]:
            if visited[next_node] == False:
                visited[next_node] = True
                q.append(next_node)

    for i in order:
        print(i, end=' ')

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
q= deque()

for t in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for row in graph:
    row.sort()

dfs(graph, v)
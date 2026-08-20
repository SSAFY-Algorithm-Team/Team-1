# swea 5102 노드의 거리
from collections import deque

T = int(input())

def bfs(S, G):
    visited[S] = True
    queue = deque([(S, 0)])

    while queue:
        cur_node, dis = queue.popleft()

        if cur_node == G:
            return dis

        for next_node in graph[cur_node]:
            if visited[next_node] == False:
                visited[next_node] = True
                queue.append((next_node, dis+1))

    return 0
    

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [False] * len(graph)
    res = 0

    for i in range(E):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    for row in graph:
        row.sort()

    S, G = map(int, input().split())

    res = bfs(S, G)

    print(f"#{test_case} {res}")

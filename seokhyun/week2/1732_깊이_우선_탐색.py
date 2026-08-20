# 코더스패스 1732 깊이 우선 탐색
def dfs(graph, start):
    order.append(start)
    visited[start] = True
    
    for next_node in graph[start]:
        if visited[next_node] == False:
            visited[next_node] = True
            dfs(graph, next_node)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * len(graph)
order = []

for t in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for row in graph:
    row.sort()

# print(graph)
# print(visited)
dfs(graph, v)

for i in order:
    print(i, end=' ')
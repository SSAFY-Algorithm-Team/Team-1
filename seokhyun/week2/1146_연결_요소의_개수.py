# 코더스패스 1146 연결 요소의 개수

def dfs(graph, start, edge):
    if visited[start] == False:
        visited[start] = True
        edge += 1

    for next_node in graph[start]:
        if visited[next_node] == False:
            visited[next_node] = True
            dfs(graph, next_node, edge)

    return edge

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * len(graph)
edge = 0

for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for i in range(1, n+1):
    edge = dfs(graph, i, edge)

print(edge)
# 간선의 배열과 인접행렬

A, B = map(int, input().split())

graph = [list([0] * B) for _ in range(B)]

for t in range(A):
    n1, n2 = map(int, input().split())
    n1 = n1 - 1
    n2 = n2 - 1

    graph[n1][n2] = 1
    graph[n2][n1] = 1

for i in range(B):
    for j in range(B):
        print(graph[i][j], end=' ')
    print()
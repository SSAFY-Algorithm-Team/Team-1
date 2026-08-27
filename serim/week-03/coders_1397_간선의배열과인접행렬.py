# 코더스패스 1397 간선의 배열과 인접행렬 level3
#

# 간선, 정점
A, B = map(int, input().split())

adj_matix = [[0]*(B+1) for _ in range(B+1)]

for _ in range(A):
    start, end = map(int, input().split())
    adj_matix[start][end] = 1
    adj_matix[end][start] = 1

print(adj_matix)
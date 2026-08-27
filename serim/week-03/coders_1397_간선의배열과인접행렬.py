# 코더스패스 1397 간선의 배열과 인접행렬 level3
#

# 간선, 정점
A, B = map(int, input().split())

# 탐색 문제와 다르게 0행과 0열 필요없어서 B+1 안해도 됨
adj_matix = [[0]*(B) for _ in range(B)]

for _ in range(A):
    start, end = map(int, input().split())
    # 대신에 노드번호-1 인덱스에 저장해주기
    adj_matix[start-1][end-1] = 1
    adj_matix[end-1][start-1] = 1

print(adj_matix)
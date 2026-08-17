A, B = map(int, input().split()) # 간선의 수 A, 정점의 수 B
arr = [[0] * B for _ in range(B)] # 그래프를 저장하는 리스트

for _ in range(A):
    e1, e2 = map(int, input().split()) # 정점
    arr[e1 - 1][e2 - 1] = 1 # 각 정점 연결
    arr[e2 - 1][e1 - 1] = 1 # 각 정점 연결

for i in range(B):
    for j in range(B):
        print(arr[i][j], end = ' ')
    print()
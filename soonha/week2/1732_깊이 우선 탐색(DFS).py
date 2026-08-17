'''
DFS알고리즘(현재정점 : v)
    점 v 방문 표시
    FOR v와 연결된 모든 정점 w
        IF w가 방문되어있지 않다면
            DFS알고리즘(w)
'''

def dfs(v):
    visit[v] = 1 # 점 v 방문 표시
    print(v, end = ' ')
    for w in gp[v]: # v와 연결된 모든 정점 w
        if visit[w] == 0:
            dfs(w)

n, m, v = map(int, input().split())

gp = [[] for _ in range(n + 1)] # 그래프
visit = [0] * (n + 1) # 방문 배열

for i in range(m):
    a, b = map(int, input().split())
    gp[a].append(b) # 정점 연결
    gp[b].append(a) # 정점 연결

for i in range(1, n + 1):
    gp[i].sort() # 정렬(문제 조건)

dfs(v)
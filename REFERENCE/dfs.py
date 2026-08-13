# DFS reference code
'''
DFS알고리즘(현재정점 : v)
    점 v 방문 표시
    FOR t와 연결된 모든 정점 w
        IF w가 방문되어있지 않다면
            DFS알고리즘(w)
'''

def dfs(v):
    visit[v] = 1 # 점 v 방문 표시
    print(v, end = ' ')
    for w in gp[v]: # FOR t와 연결된 모든 정점 w
        if visit[w] == 0: # IF w가 방문되어있지 않다면
            dfs(w) # DFS알고리즘(w)

A, B, V = map(int, input().split()) # A: 정점, B: 간선 수, V: 시작 정점

gp = [[] for i in range(A + 1)]

for i in range(B):
    s, e = map(int, input().split())
    gp[s].append(e)
    gp[e].append(s)

for i in range(1, A + 1):
    gp[i].sort()

visit = [0 for i in range(A + 1)]
dfs(V)

'''
[입력 예시]
5 5 1
4 5
5 2
3 5
2 1
3 2
[출력 예시]
1 2 3 5 4 
'''
'''
BFS알고리즘(시작정점 : v)
    큐 생성
    방문 배열 생성
    시작점 v를 큐에 추가
    점 v 방문 표시
    WHILE 큐가 비어있지 않은 경우
        t = 큐에서 하나 가져오기(삭제)
        FOR t와 연결된 모든 정점 w
            IF w가 방문되어있지 않다면
                w를 큐에 넣고, 방문 표시
'''

from collections import deque

def bfs(graph, start, n):
    visit = [0] * (n + 1) # 방문 배열 생성
    q = deque([start]) # 큐 생성, 시작점 v를 큐에 추가
    visit[start] = 1 # 점 v 방문 표시
    print(start, end = ' ')

    while q: # 큐가 비어있지 않은 경우
        t = q.popleft() # t = 큐에서 하나 가져오기(삭제)
        for w in graph[t]: # t와 연결된 모든 정점 w
            if visit[w] == 0: # w가 방문 되어있지 않다면
                visit[w] = 1
                print(w, end = ' ')
                q.append(w) # w를 큐에 넣고, 방문 표시

n, m, v = map(int, input().split()) # 정점의 갯수 n, 간선의 갯수 m, 탐색 시작 정점 번호 v

gp = [[] for _ in range(n + 1)] # 그래프

for _ in range(m): # 정점 연결
    a, b = map(int, input().split())
    gp[a].append(b)
    gp[b].append(a)

for i in range(1, n + 1): # 정렬(문제 조건)
    gp[i].sort()

bfs(gp, v, n)
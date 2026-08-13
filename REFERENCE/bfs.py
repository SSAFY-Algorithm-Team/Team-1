# BFS reference code
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
    q = deque([start]) # 큐 생성 / 시작점 v를 큐에 추가
    visit[start] = 1 # 점 v 방문 표시
    print(start, end=' ')

    while q: # 큐가 비어있지 않은 경우
        t = q.popleft() # t = 큐에서 하나 가져오기(삭제)
        for w in graph[t]: # FOR t와 연결된 모든 정점 w
            if visit[w] == 0: # IF w가 방문되어있지 않다면
                visit[w] = 1 # 방문 표시
                print(w, end=' ')
                q.append(w) # w를 큐에 넣기


n, m, v = map(int, input().split())
'''
n: 정점(노드)의 갯수
m: 간선(edge)의 갯수
v = 탐색을 시작할 정점 번호
'''

gp = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    gp[a].append(b)
    gp[b].append(a)

for i in range(1, n + 1):
    gp[i].sort()

bfs(gp, v, n)

'''
[입력 예시]
5 5 3
5 4
5 2
1 2
3 4
3 1
[출력 예시]
3 1 4 2 5
'''
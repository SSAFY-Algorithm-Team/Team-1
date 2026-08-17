from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split()) # 노드 갯수 V, 간선 정보 E
    gp = [[] for _ in range(V + 1)] # 그래프

    for _ in range(E): # 정점 연결
        a, b = map(int, input().split())
        gp[a].append(b)
        gp[b].append(a)

    S, G = map(int, input().split()) # 출발 노드 S, 도착 노드 G


    def bfs(start, goal):
        visited = [0] * (V + 1) # 방문 배열 생성
        dist = [0] * (V + 1) # 거리 계산 배열 생성

        q = deque() # 큐 생성
        q.append(start) # 큐에 시작 정점 삽입
        visited[start] = 1 # 해당 정점 방문 표시

        while q:
            t = q.popleft() # 연결된 정점 가져오기
            if t == goal: # 해당 정점이 목표 정점이면
                return dist[t] # 현재 거리값 return
            for next in gp[t]: # 현 정점(t)과 연결된 정점들 중
                if not visited[next]: # 방문을 아직 안했으면
                    visited[next] = 1 # 방문 추가
                    dist[next] = dist[t] + 1 # 거리 +1
                    q.append(next) # q에 삽입

        return 0 # 도달 불가능한 경우

    result = bfs(S, G)
    print(f'#{test_case} {result}')
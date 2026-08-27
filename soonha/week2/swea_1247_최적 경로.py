T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    company = (arr[0], arr[1]) # 회사의 좌표
    house = (arr[2], arr[3]) # 집의 좌표

    clients = [] # 고객들의 좌표
    for i in range(4, 4 + 2 * N, 2): # 고객 좌표 저장
        clients.append((arr[i], arr[i + 1]))

    visited = [False] * N  # 고객 방문 여부
    best = float('inf')    # 최단 이동거리

    # 두 좌표 사이의 맨해튼 거리(문제 조건)
    def dist(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    def dfs(current, count, total):
        global best
        if total >= best:  # 가지치기: 이미 최단 기록보다 길면 더 볼 필요 없음
            return
        
        if count == N:  # 모든 고객을 다 방문했다면
            total_final = total + dist(current, house)  # 집까지 가는 거리 추가
            if total_final < best:
                best = total_final
            return
        
        for i in range(N):  # 아직 방문 안 한 고객들을 하나씩 다음 목적지로 시도
            if not visited[i]:
                visited[i] = True
                dfs(clients[i], count + 1, total + dist(current, clients[i]))
                visited[i] = False  # 백트래킹: 다른 경로를 시도하기 위해 되돌림

    dfs(company, 0, 0)  # 회사에서 출발
    print(f'#{test_case} {best}') # 출력
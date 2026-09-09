T = int(input()) # 테스트케이스
for test_case in range(1, T + 1):
    N = int(input()) # 사무실 및 관리구역 총 번호
    e = [list(map(int, input().split())) for _ in range(N)] # 각 관리구역 별 소비량

    visited = [False] * N # 사무실 방문 여부
    visited[0] = True          # 0번 = 사무실(1번 구역), 출발점 고정
    min_val = float('inf') # 최소 배터리 사용량

    def dfs(cur, cnt, cost):
        global min_val
        if cost >= min_val: # 가지치기: 이미 최솟값 이상이면 더 볼 필요 없음
            return
        if cnt == N: # 모든 구역 방문 완료
            min_val = min(min_val, cost + e[cur][0]) # 사무실로 복귀하는 소비량까지 포함 후 비교
            return
        for next in range(1, N):
            if not visited[next]: # 아직 방문 안했으면
                visited[next] = True # 방문 표시
                dfs(next, cnt + 1, cost + e[cur][next]) # dfs 재귀 실행
                visited[next] = False # 백트래킹

    dfs(0, 1, 0) # 탐색 실행
    print(f'#{test_case} {+++min_val}') # 출력
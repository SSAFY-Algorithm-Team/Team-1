def compute(N, M, arr):
    max_sum = -1 # 파리 퇴치 최댓값 수를 저장할 변수
    for r in range(N):
        for c in range(N):
            # + 모양
            s = arr[r][c]
            for k in range(1, M):
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr, nc = r + dr*k, c + dc*k
                    if 0 <= nr < N and 0 <= nc < N: # 배열 범위 안에 들어가면
                        s += arr[nr][nc] # 잡은 파리 갯수 추가
            max_sum = max(max_sum, s) # 최댓값 비교
            # x 모양
            s2 = arr[r][c]
            for k in range(1, M):
                for dr, dc in [(-1,-1),(-1,1),(1,-1),(1,1)]:
                    nr, nc = r + dr*k, c + dc*k
                    if 0 <= nr < N and 0 <= nc < N: # 배열 범위 안에 들어가면
                        s2 += arr[nr][nc] # 잡은 파리 갯수 추가
            max_sum = max(max_sum, s2) # 최댓값 비교
    return max_sum # 최댓값 반환

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split()) # 파리 배열 범위와 스프레이 범위 값
    arr = [] # 파리 배열
    for _ in range(N): # 파리 배열 삽입
        arr.append(list(map(int, input().split())))
    val = compute(N, M, arr) # 파리 퇴치 최댓값을 계산 및 저장
    print(f'#{test_case} {val}') # 출력
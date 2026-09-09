# SWEA 2001. 파리 퇴치

T = int(input()) # 테스트 케이스 T
for test_case in range(1, T + 1):
    N, M = map(int, input().split()) # 파리 배열 N * N, 파리채 배열 M * M
    fly = [] # 파리 배열 N * N
    for _ in range(N): # 파리 배열 입력받기
        arr = list(map(int, input().split()))
        fly.append(arr)
    max_val = -1 # 파리채로 죽일 수 있는 파리의 최댓값

    for row in range(N - M + 1): # 파리채의 좌측 상단 좌표의 범위: 0부터 N - M까지 가능
        for col in range(N - M + 1):
            cnt = 0 # 현재 파리채에서 죽일 수 있는 파리 개수
            for i in range(M): # 파리채 격자(행)
                for j in range(M): # 파리채 격자(열)
                    cnt += fly[row + i][col + j]
            # 파리 개수 비교
            if(max_val < cnt): # 현재값이 기존 최댓값보다 크다면
                max_val = cnt # 최댓값 교체

    print(f'#{test_case} {max_val}') # 출력
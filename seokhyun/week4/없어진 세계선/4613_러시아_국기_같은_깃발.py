# SWEA 4613 러시아 국기 같은 깃발

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [list(map(str, input().strip())) for _ in range(N)]

    res = float('inf')

    R = 0
    B = 0
    W = 0

    for i in range(1, N-1):                 # B, R 범위를 뺀 위치
        for j in range(i+1, N):             # B의 마지막 범위
            W = i * M  - sum(row.count('W') for row in flag[:i])
            B = (j-i) * M - sum(row.count('B') for row in flag[i:j])
            R = (N-j) * M  - sum(row.count('R') for row in flag[j:])

            if res > R + B + W:
                res = R + B + W

    print(f"#{test_case} {res}")
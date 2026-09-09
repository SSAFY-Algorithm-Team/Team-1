# SWEA 2805 농작물 수확하기
import sys
sys.stdin = open("input.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input().strip())) for _ in range(N)]
    ans = 0
    mid = N // 2

    for i in range(N):
        # 중심 행과의 거리 계산
        dis = abs(mid - i)
        # 수확할 범위 (가로범위)
        ans += sum(farm[i][dis : N - dis])

    print(f"#{test_case} {ans}")
# SWEA 2115 벌꿀 채취
#import sys
#sys.stdin = open("input.txt", "r")
from itertools import combinations

def search(x, y):
    sub_list = honey[y][x:x+M]
    max_profit = 0

    # 1개부터 M개까지 모든 조합에 대해 검사
    for r in range(1, len(sub_list) + 1):
        for comb in combinations(sub_list, r):
            if sum(comb) <= C:
                # 꿀의 양의 합이 C 이하일 때, '제곱의 합' 최댓값을 직접 갱신
                profit = sum(v**2 for v in comb)
                max_profit = max(max_profit, profit)

    return max_profit

T = int(input())

for test_case in range(1, T + 1):
    # N은 가로세로 크기 || M은 한 일꾼당 수확가능한 벌통 개수 || C는 채취할 수 있는 최대 꿀의 양
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    # 모든 칸에서 스타트할 필요는 없음.
    for y1 in range(N):
        for x1 in range(N-M+1):
            profit1 = search(x1, y1)

            # 1번 일꾼의 탐색 범위를 제외한 범위를 탐색한다.
            for y2 in range(y1, N):
                if y1 == y2:
                    start_x2 = x1 + M
                else:
                    start_x2 = 0

                for x2 in range(start_x2, N-M+1):
                    profit2 = search(x2, y2)
                    ans = max(ans, profit1 + profit2)

    print(f"#{test_case} {ans}")

# SWEA 4836 색칠하기
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    grid = [[0] * 10 for _ in range(10)]    # 색칠할 빈 격자판(도화지)
    res = 0

    for _ in range(N):
        # r1, c1 은 시작점의 좌표 || r2, c2 는 끝 점의 좌표 || color는 해당 범위에 칠해질 색
        r1, c1, r2, c2, color = map(int, input().split())

        # 입력이 들어온 사각형의 크기만큼 순회하며 각 좌표에 color 값 더하기(색칠하기)
        # red와 blue가 구분없이 각자의 영역에 값을 더한다. red색 칸은 1, blue색 칸은 2, purple색 칸은 3
        # 같은 색상은 영역이 겹치지 않기 때문에 누적합의 형태로 풀 수 있다.
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                grid[r][c] += color

    # 칸을 순회하며 보라색(값이 3인)칸을 카운팅한다.
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 3:
                res += 1

    print(f"#{test_case} {res}")
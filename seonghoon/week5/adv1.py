# cy, cx 기준 시계 방향으로 90도 돌렸을 때 결과점 위치
# cy, cx가 원점이고, ty, tx를 돌릴 때, 결과좌표는
# 결과 X좌표 = +ty | 결과 Y좌표 = -tx가 된다.
# 다만 문제에서 x, y좌표를 반대로 줬기 때문에 반시계 방향으로 90도 돌린 것과 같다. f(x, y) -> (+y, -x)
def rotate90d(cy, cx, ty, tx):
    delta_y = ty-cy
    delta_x = tx-cx
    return (cy + delta_x, cx - delta_y)

N = int(input())
grid = [[0] * 101 for _ in range(101)]  # 드래곤 커브가 포함된 꼭짓점 좌표

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
for _ in range(N):
    # x와 y를 반대로 입력받아 우리가 사용하는 좌표계와 맞춘다.
    y, x, d, g = map(int,input().split())
    curv = [(y, x), (y+dy[d], x+dx[d])]

    # 차수만큼 반복해서 하나의 드래곤 커브 만들기
    for step in range(g):
        centy, centx = curv[-1] # 드래곤 커브의 마지막 부분이 곧 중심점
        
        # 중심점 제외 모든 점을 역순으로 순회하며 각 점을 90도 돌린 좌표를 드래곤 커브에 append
        for idx in range(2**step-1, -1, -1):
            curv.append(rotate90d(centy, centx, curv[idx][0], curv[idx][1]))

    # 하나의 드래곤 커브가 완성되었다면, 이를 grid에 전부 입력
    # print(curv)
    for y,x in curv:
        grid[y][x] = 1

# grid의 모든 점을 순회하면서, 현재 위치 기준 4칸의 점이 전부 1이라면 정사각형으로 판정
ans = 0
for y in range(100):
    for x in range(100):
        if grid[y][x] * grid[y+1][x] * grid[y][x+1] * grid[y+1][x+1] == 1:
            ans += 1

print(ans)
from itertools import combinations

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
hospitals = []
persons = []
res = float('inf')

# 만들어 놓은 사람 리스트와 병원 리스트에 좌표를 저장한다.
for y in range(N):
    for x in range(N):
        if grid[y][x] == 2:
            hospitals.append((x, y))
        elif grid[y][x] == 1:
            persons.append((x, y))

# 조합을 사용하여 병원 좌표를 M의 조합으로 나타낸다.
for comb_hospitals in combinations(hospitals, M):
    total_distance = 0

    # 첫 번째 사람부터 맨하튼 거리 구하기 순회 시작
    for px, py in persons:
        per_to_hos_dist = float('inf')

        # 현재 사람이 조합의 각 병원 당 거리를 비교하여 최소를 선택함
        for hx, hy in comb_hospitals:
            temp_distance = abs(px - hx) + abs(py - hy)
            per_to_hos_dist = min(per_to_hos_dist, temp_distance)

        total_distance += per_to_hos_dist

    res = min(res, total_distance)

print(res)

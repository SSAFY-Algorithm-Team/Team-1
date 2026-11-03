# SWEA 5648 원자 소멸 시뮬레이션

# x, y 좌표값을 key로 방향 dir 와 에너지 k를 value로 사용하는 딕셔너리
atoms = {}

# 방향에 대해 델타 dy, dx 매핑하는 딕셔너리
direction = {
    0 : (0, 1),
    1 : (0, -1),
    2 : (-1, 0),
    3 : (1, 0)
}

def simulation(atoms):
    global ans

    while atoms:
        temp = 0
        # dict를 키벨류로 분해
        # 딕셔너리의 값을 제거해야 하는데 딕셔너리 순회 중 제거, 삽입은 불가
        # 따라서 list를 활용하여 딕셔너리를 복사하여 사용한다.
        for (x, y), atom_list in list(atoms.items()):
            # 사용한 값 제거
            atoms.pop((x, y))

            # 만약 list의 길이가 1보다 크다면,
            # 한 좌표에 원자가 두 개 이상 들어있다 = 충돌났다 = 모두 소멸한다.
            if len(atom_list) > 1:
                temp = 0
                # 한 좌표에 2개 이상인 원소들 가중합 후 다음 loop으로 이동
                for dir, k in atom_list:
                    temp += k
                ans += temp
                continue

            # 방향과 에너지로 분리
            for dir, k in atom_list:
                # 이동 방향과 현재 좌표
                dx, dy = direction[dir]
                nx, ny = x+dx, y+dy

                # 다음 좌표가 격자 안이면 딕셔너리에 다시 삽입
                if -2000 < nx < 2000 and -2000 < ny < 2000:
                    atoms.setdefault((nx, ny), []).append((dir, k))


T = int(input())

for test_case in range(1, T+1):
    N = int(input())        # 원자들의 개수
    ans = 0

    # 좌표 튜플을 키값으로 하여 방향, 에너지 튜플을 저장
    for _ in range(N):
        x, y, dir, k = map(int, input().split())
        atoms[(x*2,y*2)] = [(dir, k)]

    simulation(atoms)
    print(f"#{test_case} {ans}")
# SWEA 최적 경로

# def 백 트래킹
def dfs(idx, dis):
    global res

    # 최대 거리(res)를 넘었다면 더 이상 볼 필요 없음.
    if dis >= res:
        return 

    # 모두 방문했다면 집으로 가야함 (퇴근은 중요하지)
    if False not in visited:
        x1, y1 = pairs[idx]
        x2, y2 = home
        diff = abs(x1 - x2) + abs(y1 - y2)

        # (현재 루트가 res 보다 작다면 업데이트)
        if res > dis + diff:
            res = dis + diff
        return

    # 다음 노드 까지 거리를 구해서 다음 재귀에 넘겨줌
    for new_idx in range(len(pairs)):
        if not visited[new_idx]:
            visited[new_idx] = True

            x1, y1 = pairs[idx]
            x2, y2 = pairs[new_idx]
            diff = abs(x1 - x2) + abs(y1 - y2)
            
            dfs(new_idx, dis + diff)

            visited[new_idx] = False

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    pairs = [(data[i], data[i+1]) for i in range(0, len(data), 2)]

    # 컴퍼니와 홈은 떼어서 보는 것이 좋음. AI가 그렇다 함.
    company = pairs.pop(0)
    home = pairs.pop(0)

    visited = [False] * len(pairs)
    res = float('inf')

    for i in range(N):
        visited[i] = True
        x1, y1 = company
        x2, y2 = pairs[i]

        diff = abs(x1 - x2) + abs(y1 - y2)
        dfs(i, diff)
        visited[i] = False

    print(f"#{test_case} {res}")
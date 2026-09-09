from itertools import combinations

def taste(group):
    total = 0
    for i in group:
        for j in group:
            if i != j:
                total += arr[i][j]
    return total

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = float("inf")
    for comb in combinations(range(N), N // 2):
        A = comb
        B = [i for i in range(N) if i not in comb]
        cur_result = abs(taste(A) - taste(B))
        result = min(result, cur_result)

    print(f"#{tc} {result}")

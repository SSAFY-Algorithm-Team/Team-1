# swea 5215. 햄버거 다이어트 D3

# 민기가 매긴 햄버거 재료에 대한 점수
# 재료의 칼로리
# 둘다 보관하고 sum

T = int(input())

for tc in range(1, T+1):
    # 재료수, 제한칼로리
    N, L = map(int, input().split())

    ingredients = []

    for _ in range(N):
        score, calorie = map(int, input().split())
        ingredients.append((score, calorie))

    answer = 0  # 맛 점수 저장

    def dfs(idx, score_sum, calorie_sum):
        global answer

        if calorie_sum > L: # 칼로리제한을 넘어가면 return
            return

        if idx == N:
            answer = max(answer,score_sum)
            return

        score, calorie = ingredients[idx]
        # 선택하거나
        dfs(idx+1, score_sum+score, calorie_sum+calorie)
        # 선택안하거나
        dfs(idx+1, score_sum, calorie_sum)

    dfs(0, 0, 0)

    print(f"#{tc} {answer}")

        

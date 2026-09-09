# SWEA 숫자 카드

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().strip()))
    count = [0] * 10                            # 각 숫자를 카운팅 하는 리스트
    max_idx = 0
    max_val = 0

    # 숫자 카운팅
    for i in cards:
        count[i] += 1

    # 카운팅 값중 가장 큰 값 찾기
    for j in range(10):
        if max_val <= count[j]:
            max_idx = j
            max_val = count[j]

    print(f"#{test_case} {max_idx} {max_val}")

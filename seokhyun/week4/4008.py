# SWEA 4008 숫자 만들기

def DFS(idx, current_val, plus, minus, mul, div):
    global max_val, min_val

    # 모든 연산자를 다 사용한 경우 (N번째 숫자까지 계산)
    if idx == N:
        max_val = max(max_val, current_val)
        min_val = min(min_val, current_val)
        return

    # 연산자가 남아있을 때만 진행 (앞에서부터 순서대로 계산)
    if plus > 0:
        DFS(idx + 1, current_val + numbers[idx], plus - 1, minus, mul, div)
    if minus > 0:
        DFS(idx + 1, current_val - numbers[idx], plus, minus - 1, mul, div)
    if mul > 0:
        DFS(idx + 1, current_val * numbers[idx], plus, minus, mul - 1, div)
    if div > 0:
        # 음수 나눗셈 시 소수점 버림 처리 [int(a / b)]
        DFS(idx + 1, int(current_val / numbers[idx]), plus, minus, mul, div - 1)

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    plus, minus, mul, div = map(int, input().split())
    numbers = list(map(int, input().split()))
    min_val = 100000001
    max_val = -100000001

    exp = numbers[0]
    DFS(1, numbers[0], plus, minus, mul, div)

    print(f"#{test_case} {max_val-min_val}")
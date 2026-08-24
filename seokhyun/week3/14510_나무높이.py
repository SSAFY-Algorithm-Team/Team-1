# swea 14510 나무높이

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    tree = list(map(int, input().split()))
    max_tree = max(tree)
    even = 0
    odd = 0

    # 짝수 날과 홀수 날을 다 카운팅함.
    for i in range(N):
        diff = max_tree - tree[i]

        even += diff // 2
        odd += diff % 2

    # 짝수 날은 절대 홀수 날 보다 많을 수 없음
    while even > odd + 1:
        odd += 2
        even -= 1

    # 홀수날과 짝수날이 같음
    if even == odd:
        res = even * 2
    # 홀수 날이 짝수 날 보다 하루 많음
    elif even < odd:
        res = odd * 2 - 1
    # 짝수 날이 홀수 날 보다 많음
    elif even > odd:
        res = even * 2
    
    print(f"#{test_case} {res}")
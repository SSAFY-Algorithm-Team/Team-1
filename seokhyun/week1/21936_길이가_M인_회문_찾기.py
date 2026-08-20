# swea 21936 길이가 M인 회문 찾기

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = input()
    result = 'NONE'

    for i in range(0, N - M + 1):
        valid = arr[i : i + M]

        if valid == valid[::-1]:
            result = valid
            break

    print(f"#{test_case} {result}")
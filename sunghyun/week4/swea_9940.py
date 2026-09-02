T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    print(f'#{tc}', 'Yes' if len(set(arr)) == N else 'No')
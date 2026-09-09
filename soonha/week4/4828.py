T = int(input()) # 테스트 케이스 T
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_val = arr[0]
    min_val = arr[0]
    for i in range(len(arr)):
        if(max_val < arr[i]):
            max_val = arr[i]
        if(min_val > arr[i]):
            min_val = arr[i]

    result = max_val - min_val
    print(f'#{test_case} {result}')
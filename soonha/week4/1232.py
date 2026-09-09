T = 10
for test_case in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    for i in range(N):
        arr = list(input().split())
        if(arr[1] == '+' or arr[1] == '-' or arr[1] == '*' or arr[1] == '/'):
            idx = int(arr[0])
            tree[idx] = arr[1]
        else:
            idx = int(arr[0])
            num = int(arr[1])
            tree[idx] = num

    def calculate(idx):
        if(tree[idx] == '+'): # 더하기인 경우
            left = calculate(idx * 2)
            right = calculate(idx * 2 + 1)
            return left + right
        elif(tree[idx] == '-'): # 뺄셈인 경우
            left = calculate(idx * 2)
            right = calculate(idx * 2 + 1)
            return left - right
        elif(tree[idx] == '*'):
            left = calculate(idx * 2)
            right = calculate(idx * 2 + 1)
            return left * right
        elif(tree[idx] == '/'):
            left = calculate(idx * 2)
            right = calculate(idx * 2 + 1)
            return left // right
        else:
            return tree[idx]

    result = calculate(1)
    print(f'#{test_case} {result}')
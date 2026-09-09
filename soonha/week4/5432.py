T = int(input())
for test_case in range(1, T + 1):
    s = input()

    cnt = 0
    ans = 0

    pre = ''
    for c in s:
        if c == '(':
            cnt += 1
        else:
            cnt -= 1
            if pre == '(':
                ans += cnt
            else:
                ans += 1
        pre = c

    print(f'#{test_case} {ans}')
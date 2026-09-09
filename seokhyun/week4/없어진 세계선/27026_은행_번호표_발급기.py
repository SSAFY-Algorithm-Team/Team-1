# SWEA 27026 은행 번호표 발급기

T = int(input())

for test_case in range(1, T + 1):
    M = int(input())
    oper = list(map(int, input().split()))
    order = 1
    

    for i in oper:
        if oper == 1:
            order += 1
        elif oper == 2:
            
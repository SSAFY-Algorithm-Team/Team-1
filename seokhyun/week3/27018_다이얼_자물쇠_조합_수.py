# swea 27018 다이얼 자물쇠 조합 수

def dial(temp, D):
    global res
    global S

    if D < 0:
        return 
    
    for num in range(10):
        if D == 0 and (temp+num) == S:
            res += 1

        dial((temp+num), D-1)

T = int(input())

for test_case in range(1, T + 1):
    D, S = map(int, input().split())
    res = 0

    dial(0, D-1)

    print(f"#{test_case} {res}")
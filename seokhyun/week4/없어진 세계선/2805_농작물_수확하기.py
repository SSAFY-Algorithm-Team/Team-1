# SWEA 2805 농작물 수확하기

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input().strip())) for _ in range(N)]
    total = 0
    mid = N//2
    start = mid+1
    end = mid

    for i in range(N):
        if i <= mid:
            start -= 1
            end += 1
            for j in range(start, end):
                #print(start, end, j)
                total += farm[i][j]
        
        elif i == mid:
            total += sum(farm[i])

        elif i > mid:
            start += 1
            end -= 1 
            for j in range(start, end):
                #print(start, end, j)
                total += farm[i][j]

    print(f"#{test_case} {total}")
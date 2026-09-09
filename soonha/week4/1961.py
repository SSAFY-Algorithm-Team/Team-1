# SWEA_1961
T = int(input()) # 테스트 케이스 T
for test_case in range(1, T + 1):
    N = int(input()) # N * N 행렬의 크기 N
    grid = [] # N * N을 저장할 행렬
    for _ in range(N):
        li = list(map(int, input().split()))
        grid.append(li)

    '''
    회전 시 규칙
    - 회전한 배열의 N번째 행의 값은 회전하기 전 배열의 N번째 열의 인덱스 역순(N - 1 -> 0 순으로)이다 
    '''
    def rotate(arr): # 회전을 구현한 함수
        result = []
        for col in range(N):
            li = [] # 각 행을 담을 배열
            for row in range(N - 1, -1, -1):
                val = arr[row][col]
                li.append(val) # 값 추가
            result.append(li)
        return result

    rotate_90 = rotate(grid) # 90도 회전한 배열
    rotate_180 = rotate(rotate_90) # 180도 회전한 배열
    rotate_270 = rotate(rotate_180) # 270도 회전한 배열
    # 출력
    print(f'#{test_case}')
    for i in range(N):
        # 방법 1
        for val in rotate_90[i]:
            print(val, end='')
        print(end=' ')
        for val in rotate_180[i]:
            print(val, end='')
        print(end=' ')
        for val in rotate_270[i]:
            print(val, end='')
        print(end=' ')
        # 방법 2
        #print(*rotate_90[i], sep = '', end = ' ')
        #print(*rotate_180[i], sep = '', end = ' ')
        #print(*rotate_270[i], sep = '', end = ' ')
        print()
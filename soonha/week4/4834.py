T = int(input()) # 테스트 케이스 T
for test_case in range(1, T + 1):
    N = int(input()) # 카드 장수 N
    arr = [0] * 10
    sentence = input()

    for i in sentence:
        num = int(i)
        arr[num] += 1

    max_num = -1
    max_cnt = -1
    for i in range(len(arr)):
        if(max_cnt <= arr[i]):
            max_num = i
            max_cnt = arr[i]

    print(f'#{test_case} {max_num} {max_cnt}')
import sys
sys.stdin = open('sample_input.txt', 'r')

# 테스트 케이스의 수
T = int(input())

# 전체 테스트 케이스에 대하여 반복문
for tc in range(1, T + 1):  # 1부터 T까지의 tc(test case)진행
    print(f'#{tc}', end=' ')

    N = int(input())  # input.txt에서 카드 장수 확인하기
    cnt_lst = [0] * 10  # 각 숫자별 카드 장수 세기 위한 초기 리스트
    max_cnt = 0
    max_num = 0

    num = list(input())  # input.txt에서 카드에 쓰인 숫자들 리스트화하기
    for n in num:  # num 리스트에 있는 index 0부터 N까지의 값 반복
        n = int(n) # 정수화
        cnt_lst[n] += 1 # 해당 숫자 카드 장수 1 증가

        if max_cnt < cnt_lst[n]: # 만약 최대수가 지금 센 카드 장수보다 작으면
            max_cnt = cnt_lst[n] # 지금 카드 장수를 최대 장수로 바꾼다.
            max_num = n # 그리고 해당 숫자를 카드가 많은 숫자로 인식한다.

        elif max_cnt == cnt_lst[n]: # 만약에 최대 장수가 지금 센 카드 장수와 겹친다면
            if max_num < n: # 해당 숫자와 과거 최대 장수의 숫자와 어떤 것이 큰 지 확인한다.
                max_num = n

    print(f'{max_num} {max_cnt}')
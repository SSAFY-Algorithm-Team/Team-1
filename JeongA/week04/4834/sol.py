import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')

    N = int(input())
    a = list(map(int, input()))

    # 카드에 적힌 숫자의 개수 세기 위한 리스트 생성
    # 숫자 0~9가 각각 몇 번 등장했는지 저장
    counts = [0] * 10

    # 카드에 적힌 숫자의 개수 세기
    # 각 카드 숫자의 등장 횟수 세기
    for i in a:
        counts[i] += 1

    # max 의 초기값 설정
    # 현재 가장 많이 등장한 카드의 개수와 숫자
    max_card = counts[0]
    max_num = 0

    # num_lst 에서 가장 많은 카드에 적힌 숫자 찾기
    for j in range(10):
        # 카드 장수가 같을 때는 적힌 숫자가 더 크려면
        # 부등호가 <가 아니라 <= 이어야 한다.
        if max_card <= counts[j]:
            max_card = counts[j]
            max_num = j

    # 결과 출력
    print(max_num, max_card)
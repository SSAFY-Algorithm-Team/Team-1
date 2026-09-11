import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')

    N = int(input())
    a = list(map(int, input().split()))

    # max, min 초기값 설정
    # 첫 번째 원소를 최댓값과 최솟값의 초기 기준으로 설정
    max_value, min_value = a[0], a[0]

    # a 리스트를 순회하면서 max, min을 찾는다.
    # 첫 번째 값을 기준으로 최댓값과 최솟값을 갱신
    for i in a:
        if max_value < i:
            max_value = i

        if min_value > i:
            min_value = i

    # 결과 계산 및 출력
    # 최댓값과 최솟값의 차이 출력
    result = max_value - min_value
    print(result)
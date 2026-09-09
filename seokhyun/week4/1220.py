T = 10

for test_case in range(1, T + 1):
    cnt = 0
    length = int(input())
    matrix = [input().split() for _ in range(length)]

    for i in range(length):
        dl = 0                                                  # 데드록의 시작을 알리는 상태변수
        line = ''.join(matrix[k][i] for k in range(length))     # 90도 돌린 격자의 한 라인을 떼어옴, 계산 편함

        # 떼어온 한 라인을 순회할 것임
        for j in range(length):
            # N극(1) 발견 데드록 상태 변수를 시작(1)로 변경
            if line[j] == '1':
                dl = 1
            # S극(2) 발견 데드록 상태변수도 1인지 함께 검사 후 count 증가
            elif line[j] == '2' and dl == 1:
                cnt += 1
                dl =0

    print(f"#{test_case} {cnt}")
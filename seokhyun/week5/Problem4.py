def solution(mats, park):
    # 큰 돗자리부터 확인
    mats.sort(reverse=True)

    rows = len(park)
    cols = len(park[0])

    # 각 돗자리를 확인
    for mat in mats:

        # 돗자리의 왼쪽 위 좌표
        for r in range(rows - mat + 1):
            for c in range(cols - mat + 1):

                # mat x mat 영역이 모두 비어있는지 확인
                can_place = True

                for i in range(r, r + mat):
                    for j in range(c, c + mat):
                        if park[i][j] != "-1":
                            can_place = False
                            break

                    if not can_place:
                        break

                # 놓을 수 있다면 바로 반환
                if can_place:
                    return mat

    # 놓을 수 있는 돗자리가 없다면
    return -1
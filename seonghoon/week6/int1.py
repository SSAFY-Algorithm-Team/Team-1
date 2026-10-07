def solution(numbers):
    # 레전트 테케. [0, 0] => "00"이 아닌 "0"으로 출력
    if max(numbers) == 0:
        return "0"

    # 숫자를 문자열로 변환
    numbers = list(map(str, numbers))
    # 숫자가 최대 4자리이기 때문에 그냥 3이 32보다 우선되고 34보다 후순위인 경우를 처리하기 위해
    # 각 숫자를 최대 자리 수만큼 반복하면 올바른 순서대로 정렬할 수 있다.
    numbers.sort(key=lambda x: x*4, reverse=True)
    answer = ''.join(numbers)
    return answer
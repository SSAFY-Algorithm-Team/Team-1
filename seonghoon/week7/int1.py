# idx = 사용한 숫자의 개수, value = 해당 개수로 만들 수 있는 숫자들의 집합
possibleNums = [set() for _ in range(9)]
def solution(N, number):
    answer = -1
    
    # 2, 22, 444와 같이 같은 숫자를 반복해서 만든 수를 미리 추가
    for i in range(1, 9):
        sameNum = int(str(N) * i)   # 같은 숫자를 i번만큼 반복해서 붙이기
        possibleNums[i].add(sameNum)
        if sameNum == number:
            return i

    for i in range(2, 9):           # i = depth, 사용한 숫자의 개수. 최대 8개의 수를 쓸 때까지 반복
        for k in range(1, i):
            """
            각 숫자집합의 괄호 -
            (사용수 1개) (연산자) (사용수 depth-1개)
            (사용수 2개) (연산자) (사용수 depth-2개)
            ...
            (사용수 depth-1개) (연산자) (사용수 1개)
            """
            for n1 in possibleNums[k]:
                for n2 in possibleNums[i-k]:
                    possibleNums[i].add(n1 - n2)
                    if n1 - n2 == number:
                        return i
                    if n2 != 0:
                        possibleNums[i].add(n1 // n2)
                        if n1 // n2 == number:
                            return i
                    if k > i-k:
                        continue
                    possibleNums[i].add(n1 + n2)
                    if n1 + n2 == number:
                        return i
                    possibleNums[i].add(n1 * n2)
                    if n1 * n2 == number:
                        return i
    return answer
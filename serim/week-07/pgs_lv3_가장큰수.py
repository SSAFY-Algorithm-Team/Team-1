
def solution(numbers):
    answer = ''
    
    max_number = 0
    
    # 일단 완전 탐색을 다 해보자
    # 주어진 정수를 다 이어붙여서 대소 비교 먼저
    # 근데 완탐을 하기에는 nuumbers의 범위가 너무 큼
    # 그러면 그냥 큰 수부터 배치하는 방법 써보자
    # 근데 이제 두자리수 이상이면 10으로 나눠서 한자리씩 보기
    
    # 두자리 수 이상 수가 있을 땐 
    # 그 수의 첫째자리 부터 대소를 비교해야하는거임
    
    
    # 일단 단순한 것부터 구현하고
    # 이거 정렬 문제인가?


    """
    for numbers 배열 안의 원소들 순회:
        if 그 원소가 두자리수 이상이라면:
            첫째자리만 보자
            어떻게?-> str로 바꾼다음에 elem[0]
    """

    
    numbers.sorted()

    for number in numbers:
        
        if number >= 10:
            first_num = str(number)[0]

    
    
    
    return answer
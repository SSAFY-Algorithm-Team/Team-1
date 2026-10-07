def solution(word):
    # 공백을 '-'로 채우고 최대 길이를 5로 맞춤.
    word = word+"----"[:5]

    # 알파벳 5자리일 때, 각 자리에서 다음 알파벳으로 넘어갈 때의 사전순 번호 증가량이
    # dict_weight에 정의되어 있다. 각 자리의 공식은
    # (n번째 자리) = (n+1번째 자리) * 5 + 1
    dict_weight = [781, 156, 31, 6, 1]
    alphabet_seq = ['A', 'E', 'I', 'O', 'U']

    # 각 자리의 알파벳을 확인하고, 각 자리마다 사전순 번호를 증가시킴
    answer = 0
    for i, c in enumerate(word):
        if c == '-':
            break
        answer += dict_weight[i] * alphabet_seq.index(c) + 1
    
    return answer
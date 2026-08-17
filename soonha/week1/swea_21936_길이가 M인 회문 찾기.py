# 회문 : 거꾸로 읽거나 똑바로 읽거나 같은 단어(기러기, 스위스 등)
T = int(input()) # 테스트케이스 갯수
for i in range(1, T + 1): # 테스트케이스 갯수만큼 반복
    N, M = map(int, input().split()) # N, M 값 입력받기
    sentence = input() # 길이가 N인 문자열
    sentence_list = [] # 문자열의 각 문자를 담을 리스트
    sen_check_val = 'NONE' # 회문 여부를 판단할 변수
    for j in range(0, N):
        if(j < M - 1): 
            sentence_list.append(sentence[j]) # 리스트에 문자 추가
        else: # 리스트가 회문 길이가 되면(회문 여부를 판단할 수 있으면)
            sentence_list.append(sentence[j]) # 리스트에 문자 추가
            s1, s2 = '', '' # 회문을 확인할 변수
            for k in range(0, len(sentence_list)): # 순방향으로 확인할 변수 s1
                s1 = s1 + sentence_list[k]
            for k in range(len(sentence_list) - 1, -1, -1): # 역방향으로 확인할 변수 s2
                s2 = s2 + sentence_list[k]
            if(s1 == s2): # 회문이 맞으면
                sen_check_val = s1 # 회문을 저장
            else:
                sentence_list.pop(0) # 리스트의 첫 번째 값을 지움(다음 문자를 받아 비교하기 위해서)
    print(f'#{i} {sen_check_val}') # 출력
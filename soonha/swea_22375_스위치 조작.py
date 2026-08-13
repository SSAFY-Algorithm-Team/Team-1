T = int(input())
for i in range(1, T + 1):
    N = int(input()) # 스위치 갯수
    Ai = list(map(int, input().split())) # 스위치 상태를 리스트로 입력
    Bi = list(map(int, input().split())) # 스위치 상태를 리스트로 입력
    cnt, idx = 0, 0 # cnt: 스위치 조작 카운트, idx: 스위치 상태 비교할 인덱스
    while(True):
        while(True):
            if(Ai[idx] == Bi[idx]): # idx 번의 현재 스위치와 목표 스위치 상태가 같은 지 비교
                idx += 1 # 같으면 idx 추가
                if(idx == N): # 만약 인덱스 끝까지 같으면 비교 종료
                    break
            else: # idx 번의 현재 스위치와 목표 스위치 상태가 다르면 비교 종료
                break
        if(idx == N): # 인덱스가 끝까지 갔으면
            break # while 문 탈출
        # 스위치 조작 과정
        cnt += 1 # 스위치 조작 필요하므로 조작 횟수 1 추가 
        for j in range(idx, N): # 현재 인덱스부터 끝까지 스위치 상태 전환 필요
            if(Ai[j] == 0): # 스위치 상태가 0이면
                Ai[j] = 1 # 1로 변환
            elif(Ai[j] == 1): # 스위치 상태가 1이면
                Ai[j] = 0 # 0으로 변환
    print(f'#{i} {cnt}') # 출력
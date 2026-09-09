T = int(input())
for test_case in range(1, T + 1):
    player1 = list(map(int, input().split()))
    player2 = []
    # player 2 카드 확인
    for i in range(1, 19):
        if i not in player1:
            player2.append(i)
    player2_case = []
    def recursive(depth, idx):
        if(depth == 9):
            return
        # 경우의 수 판단
        arr = []

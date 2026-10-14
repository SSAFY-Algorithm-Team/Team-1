"""
아직못품
"""

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

piece_to_id = {}  # key : 퍼즐 조각 정보, value : 조각 ID
id_to_count = {}  # key : 조각 ID, value : 해당 조각의 개수
BOARD_SIZE = 1
ID_CNT = 0
answer = -1

# game_board는 0을, table은 1을 기준으로 퍼즐 조각을 추출
# target_num은 퍼즐 조각 기준 숫자
# 각 piece의 좌표 리스트가 완성될 경우 
def extract_pieces(board, target_num):
    wall_num = 1 if target_num == 0 else 0
    pieces = []
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            if board[y][x] == target_num:
                piece = []
                queue = [(y, x)]
                board[y][x] = wall_num
                while queue:
                    cy, cx = queue.pop(0)
                    piece.append((cy, cx))
                    for i in range(4):
                        ny, nx = cy + dy[i], cx + dx[i]
                        if 0 <= ny < BOARD_SIZE and 0 <= nx < BOARD_SIZE and board[ny][nx] == target_num:
                            board[ny][nx] = wall_num
                            queue.append((ny, nx))
                pieces.append(piece)
    return pieces

# 원본 조각 정보를 piece_to_id에 넣는 함수. target_num이 0이면 정상적 추가, 
# 1이면 매칭되는 조각이 있는지 확인하고 존재한다면 카운트 1 감소하고 answer에 1 증가
def put_pieces(pieces, target_num):
    global piece_to_id, id_to_count, ID_CNT
    for piece in pieces:
        normalized_piece = convert_piece(piece)
        if normalized_piece not in piece_to_id:
            for _ in range(4):
                piece_to_id[normalized_piece] = ID_CNT
                normalized_piece = convert_piece(rotate_piece(normalized_piece))
            id_to_count[ID_CNT] = 1
            ID_CNT += 1
        else:
            if target_num == 1:
                id_to_count[piece_to_id[normalized_piece]] -= 1
                if id_to_count[piece_to_id[normalized_piece]] >= 0:
                    global answer
                    answer += 1
            else:
                id_to_count[piece_to_id[normalized_piece]] += 1
    

# 조각 정보를 0,0 기준으로 정규화
def convert_piece(piece):
    min_y = min(y for y, x in piece)
    min_x = min(x for y, x in piece)
    new_p = sorted((y - min_y, x - min_x) for y, x in piece)
    return new_p

# 조각을 시계방향으로 90도 회전
def rotate_piece(piece):
    return [(x, -y) for y, x in piece]


def solution(game_board, table):
    global BOARD_SIZE, answer
    BOARD_SIZE = len(game_board)
    
    put_pieces(extract_pieces(table, 1), 1)
    put_pieces(extract_pieces(game_board, 0), 0)
    return answer
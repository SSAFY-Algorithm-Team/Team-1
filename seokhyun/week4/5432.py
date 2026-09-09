# SWEA 5432 쇠막대기 자르기

class Stack:
    def __init__(self, size=100000):
        self.size = size
        self.items = [None] * size
        self.top = -1

    def push(self, pairwise):
        # 스택이 꽉차있으면 return
        if self.is_full():
            return
        else:
            self.top += 1
            self.items[self.top] = pairwise

    def pop(self):
        # 스택이 비어있다면 return
        if self.is_empty():
            return
        else:
            delete_item = self.items[self.top]
            self.items[self.top] = None
            self.top -= 1
            return delete_item

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size-1

    def get_count(self):
        return self.top + 1

def check_stack(laser):
    near = False            # 근접한 곳에 여는 괄호쌍이 있었는지 체크하는 상태 변수
    ans = 0
    target = {
        ')': '('
    }

    stack = Stack()

    for item in laser:
        open_pair = target.get(item)

        # 입력으로 닫는 괄호가 들어옴 (스택에서 pop)
        if open_pair is not None:                # None이 아니라면 닫는 괄호
            stack.pop()
            # near이 True이고 닫는 괄호라면 레이저이다.
            # 스택 내부에는 여는 괄호 밖에 없음 = 남아있는 여는 괄호는 전부 쇠막대기이다.
            # 남아있는 쇠막대기 만큼 갯수 ++
            if near:
                ans += stack.get_count()
            # near이 False이고 닫는 괄호라면 인접한 쌍"()"이 아니므로 쇠막대기 이다. 자르고 남은 1조각을 더해준다.
            else:
                ans += 1
            near = False                    # 닫는 괄호가 끝났으니 near를 False로 초기화

        # 입력으로 여는 괄호가 들어옴 (스택에 push)
        elif item in target.values():
            near = True                     # 여는 괄호가 들어왔으니 True로 바꾼다.
            stack.push(item)
    return ans

T = int(input())

for test_case in range(1, T + 1):
    laser = list(map(str, input().strip()))
    ans = check_stack(laser)

    print(f"#{test_case} {ans}")
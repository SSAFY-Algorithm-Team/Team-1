# SWEA 계산기1

# 강의에서 배움 stack class 구현
class Stack:
    def __init__(self, size):
        self.size = size
        self.items = [False] * size
        self.top = -1

    def push(self, oper):
        if self.is_full():
            return
        else:
            self.top += 1
            self.items[self.top] = oper

    def pop(self):
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

def in_to_post(exp):
    stack = Stack(10)                       # 더하기 밖에 없어서 큰 스택이 필요 없음
    postfix = []                            # 후위 표현식을 저장하기 위한 변수
    # 문자열동안 순회
    for char in exp:
        if char == '+':                     # 연산자라면 stack에 push
            if not stack.is_empty():
                postfix.append(stack.pop()) # 다른 연산자가 없기 때문에 그냥 pop하고 후위표현식에 붙이기
            stack.push(char)                # 현재 연산자를 push
        else:                               # 피연산자면 바로 list로 직행
            postfix.append(char)            # 피연산자는 바로 표현식에 붙임

    while not stack.is_empty():             # stack에 남은 연산자들 전부 표현식에 붙이기
        postfix.append(stack.pop())

    return postfix

def calc(postfix, size):
    stack = Stack(size)
    # 후위 표현식 길이만큼 순회
    for char in postfix:
        if char == '+':                     # 연산자이면 stack에서 피연산자 두 개 꺼내어 연산
            oper1 = stack.pop()
            oper2 = stack.pop()
            stack.push(oper1 + oper2)       # 연산된 값을 다시 push
        else:                               # 피연산자는 stack에 바로 push
            stack.push(int(char))
    return stack.pop()                      # 최종적으로 계산된 값 반환

for test_case in range(1, 11):
    length = int(input())
    exp = list(map(str, input().strip()))
    postfix = in_to_post(exp)
    res = calc(postfix, length)

    print(f"#{test_case} {res}")
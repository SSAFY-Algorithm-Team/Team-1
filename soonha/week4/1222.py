for test_case in range(1, 11):
    length = int(input())
    sentence = input()

    class Stack:
        def __init__(self, capacity = 10):
            self.capacity = capacity # 스택의 최대 용량
            self.items = [None] * capacity # 스택을 저장할 리스트
            self.top = -1 # 스택의 top 위치(초기값 -1)

        def push(self, item):
            if self.is_full():
                raise IndexError("Stack is Full")
            self.top += 1 # top 위치를 1 증가
            self.items[self.top] = item # 새 항목을 top 위치에 추가

        def pop(self):
            if self.is_empty():
                raise IndexError("Stack is Empty")
            item = self.items[self.top] # top 위치의 항목을 가져옴
            self.items[self.top] = None # 해당 위치를 None으로 설정
            self.top -= 1 # top 위치를 1 감소
            return item # 가져온 항목 반환

        def is_empty(self):
            # top이 -1이면 스택이 비어있음
            return self.top == -1

        def is_full(self):
            # top이 capacity -1이면 스택이 가득 참
            return self.top == self.capacity - 1

        def peek(self):
            if self.is_empty():
                raise IndexError("Stack is Empty")
            return self.items[self.top] # top 위치의 항목 반환

        def get_size(self):
            # 현재 스택에 있는 항목의 갯수 반환
            return self.top + 1

    # 후위 표기식 계산
    def infix_to_postfix(expr):
        stack = Stack()  # 연산자를 임시 보관하는 스택
        postfix = []  # 후위 표기식 결과를 담을 리스트

        for ch in expr:
            if ch != '+':
                # 피연산자(숫자)는 바로 결과에 추가
                postfix.append(int(ch))
            else:
                # 연산자를 만나면, 스택에 남아있는 연산자를 먼저 결과로 꺼낸 뒤
                # (지금은 '+'뿐이라 우선순위 비교 없이 그냥 다 꺼내면 됨)
                while not stack.is_empty():
                    postfix.append(stack.pop())
                stack.push(ch)  # 현재 연산자를 스택에 push

        # 남아있는 연산자를 모두 결과에 추가
        while not stack.is_empty():
            postfix.append(stack.pop())

        return postfix
    
    postfix = infix_to_postfix(sentence) # 후위 표기식으로 바꾼 리스트
    
    # 계산
    s = Stack(len(sentence))
    for val in postfix:
        if(val != '+'):
            s.push(val)
        else:
            num1 = s.pop()
            num2 = s.pop()
            num = num1 + num2
            s.push(num)
    result = s.pop()
    print(f'#{test_case} {result}')
# SWEA 26930 코드 편집기의 괄호 짝 검사

T = int(input())

for test_case in range(1, T + 1):
    text = list(map(str, input().strip()))
    stack = []
    is_valid = True

    for char in text:
        if char == '(' or char == '{':
            stack.append(char)
            
        elif char == ')':
            if not stack or stack.pop() != '(':
                is_valid = False
                break

        elif char == '}':
            if not stack or stack.pop() != '{':
                is_valid = False
                break

    if is_valid and not stack:
        res = 1
    else:
        res = 0

    print(f"#{test_case} {res}")
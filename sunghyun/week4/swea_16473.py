def solve(line):
    pair = {')': '(', '}': '{'}
    stack = []
    quote = None          

    for ch in line:
        if quote:                      
            if ch == quote:
                quote = None
            continue
        if ch in "'\"":
            quote = ch
        elif ch in "({":
            stack.append(ch)
        elif ch in ")}":
            if not stack or stack.pop() != pair[ch]:
                return 0               
    return 0 if stack else 1         

T = int(input())
for tc in range(1, T + 1):
    line = input().rstrip('\n')
    print(f'#{tc} {solve(line)}')
package huiwon2.week4;
import java.util.Scanner;
import java.util.Stack;

public class d2_26930 {
	// 코드 편집기의 괄호 짝 검사 
	// 처음에 소괄호 기준으로 러프하게 구성한 로직
	// edge 케이스 중 중괄호가 문항 속에 있는 것을 파악하지 못했음
	// 따옴표가 있을 때는 문자열이라 괄호가 의미가 없는 상태임을 표시했어야 함
	private static int getPair(String s) {
		int answer = 0;
		// !! 따옴표 안에 있는 괄호인지 아닌지 확인 필요함
		boolean inSingleQuote = false;
		boolean inDoubleQuote = false;
		
		// stack 정의
		Stack<Character> stack = new Stack<Character>();
		// for 순회를 통해 문자열을 돌면서 stack을 채움
		for(int i = 0; i< s.length(); i++) {
			char ch = s.charAt(i);
			
			// !! escape 문자 처리
			if(ch == '\\' && i+1 < s.length()) {
				i++; // !! 다음 문자 건너뜀
				continue;
			}
			
			// !! 따옴표 플래그 토글(문자열 내부 진입/탈출)
			if(ch == '\'' && !inDoubleQuote) {
				inSingleQuote = !inSingleQuote;
				continue;
			}
			if(ch == '"' && !inSingleQuote) {
				inDoubleQuote = !inDoubleQuote;
				continue;
			}
			// !! 따옴표 내부(문자열)라면 괄호 검사를 하지 않고 스킵
			if(inSingleQuote || inDoubleQuote) {
				continue;
			}
			
			// !! 따옴표 외부일 때만 괄호 스택 처리
			if(ch == '(' || ch == '{') {
				// 여는 괄호가 나왔다면 push
				stack.push(ch);
			}else if(ch == ')' || ch == '}'){
				// 닫는 괄호가 나왔다면 여는 괄호가 들어간 stack에서 pop해준다.
				// !! 여는 괄호도 없는데 닫는 괄호가 먼저 나오는 경우가 있음
				// stack이 비어있을 경우 pop 시 에러가 나니 isEmpty가 아닐 경우에만 pop
				if(stack.isEmpty()) {
					// return 하는 이유 : 매칭되는 여는 괄호가 없는데 닫는 괄호부터 나왔으니
					// 이미 올바른 괄호 매칭이 안됨
					return 0;
				}
				// pop을 했는데, 현재 닫는괄호와 stack에서 뺀 괄호 모양이 맞지 않는다면
				// 그것도 올바른 괄호라고 볼 수 없음
				char top = stack.pop();
				if((ch == ')' && top != '(') || (ch == '}' && top != '{')) {
					return 0;
				}
				
			}
		}
		
		// stack의 empty 여부 확인(비어있지 않으면 괄호가 남아있음)
		if(!stack.isEmpty()) {
			answer = 0;
		}else {
			answer = 1;
		}
		
		return answer;
	}
	public static void main(String[] args) throws Exception{
		Scanner sc = new Scanner(System.in);
		int T;
		T = sc.nextInt();
		// 문자열을 nextLine으로 받아서 일부 문장 데이터가 안넘어가는 현상 발생
		sc.nextLine();
		for(int test_case = 1; test_case <= T; test_case++) {
			String str = sc.nextLine();
			int result = getPair(str);
			
			System.out.println("#" + test_case + " " + result);
		}
		sc.close();
	}

}

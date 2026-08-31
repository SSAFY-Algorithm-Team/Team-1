package huiwon2.week4;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
public class d1_27023 {
    // 은행 번호표 발급기 
	private static ArrayList<Integer> getMachine(int[] arr) {
		// 발급번호 배열 반환 메서드
		// ArrayList로 받기로 한 이유: index보다 add 되는 부분이 유동적이기 때문
		// 배열처럼 인덱스가 필요하지 않아 add로 처리
		ArrayList<Integer> number = new ArrayList<Integer>();
		
		// queue 정의
		Queue<Integer> queue = new LinkedList<>();
		
		// 배열을 순회하면서 1이면 offer를 2면 poll을 통해 number list add
		// queue가 Empty인지 아닌지 확인할 필요가 없다
		// 왜? 인자로 받은 arr의 2일 때만 poll 할 것이기 때문
		int order = 1; // 순서 계산 
		for(int i = 0; i < arr.length; i++) {
			if(arr[i] == 1) {
				// 1일 때 offer(순서가 계속 증가해야 1 2 3 으로 나옴)
				queue.offer(order++);
			}
			else if(arr[i] == 2){
				// 2일 때 queue에서 poll한 후 number list에 add
				number.add(queue.poll());
			}
		}
		return number;
	}
	public static void main(String[] args) throws Exception{
		Scanner sc = new Scanner(System.in);
		int T;
		T = sc.nextInt();
		for(int test_case = 1; test_case <= T; test_case++) {
			// 총 발급과 호출의 개수
			int count = sc.nextInt();
			int[] arr = new int[count];
			
			for(int i = 0; i < count; i++) {
				arr[i] = sc.nextInt();
			}
			
			// 결과 값 출력
			ArrayList<Integer> result = getMachine(arr);
			System.out.print("#" + test_case + " ");
			for(Integer r : result) {
				System.out.print(r + " ");
			}
			System.out.println();
		}
		sc.close();
	}
}

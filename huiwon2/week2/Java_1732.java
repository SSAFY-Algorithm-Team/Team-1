package huiwon2.week2;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Java_1732 {
    // 깊이 우선 탐색 
	/** 
	 * 전역 변수 선언
	 * DFS 메서드에서 사용할 변수를 static으로 정의, 사용 
	**/
	static int N = 0;
  static int M = 0;
  static ArrayList<ArrayList<Integer>> graph;
  static int answer = 0;
  static boolean[] checked;
  private static void DFS(int v) {
  	checked[v] = true;
    System.out.print(v + " "); // 방문 시점 출력
        
    for(int next:graph.get(v)) {
    	if(!checked[next]) {
    		checked[next] = true;
        DFS(next);
        //checked[next] = false;
        // 이 위의 것은 backtrack을 통해 가능한 모든 경로를 체크하는 구간임
        // 한 번 길을 갔다면 checked를 true로 하고 넘어가야 함 
    	}
    }
  }
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		int v = sc.nextInt();
		
		checked = new boolean[N+1];
		graph = new ArrayList<ArrayList<Integer>>();
		for(int i = 0; i < N+1; i++) {
			graph.add(new ArrayList<Integer>());
		}
		
		// 간선 입력
		for (int i = 0; i < M; i++) {
		   int a = sc.nextInt();
		   int b = sc.nextInt();
		   // 그래프에 1(visited 표시)
		   if(a <= N && b <= N){
			   graph.get(a).add(b);
			   graph.get(b).add(a);
		   }
		}
		
		// graph 정렬(한 정점에서 여러 정점으로 이어질 때, 더 작은 정점을 우선순위에 넣고자 하는 것(정렬))
		for(int i = 1; i < N+1; i++) {
			Collections.sort(graph.get(i));
		}
		
		DFS(v);
		sc.close();
	}
}

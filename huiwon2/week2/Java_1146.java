package huiwon2.week2;

import java.util.ArrayList;
import java.util.Scanner;

public class Java_1146 {
  // 연결 요소의 개수
	static int N = 0;
  static int M = 0;
  static ArrayList<ArrayList<Integer>> graph;
  static int answer = 0;
  static boolean[] checked;
  private static int DFS(int v) {
    int count = 1;
    checked[v] = true;
    for(int next : graph.get(v)) {
    	if(!checked[next]) {
    		checked[next] = true;
        DFS(next);
    	}
    }
    return count;
  }
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		// 정점의 개수
		N = sc.nextInt();
		// 간선의 개수
		M = sc.nextInt();
		
		graph = new ArrayList<ArrayList<Integer>>();
		for(int i = 0; i < N+1; i++) {
			graph.add(new ArrayList<Integer>());
		}
		
		// 간선 입력
		for(int i = 0; i < M; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			graph.get(a).add(b);
			graph.get(b).add(a);
		}
		
		int answer = 0;
		checked = new boolean[N+1];
		
		// 연결요소 개수(간선 1부터 시작)
		for(int i = 1; i < N+1; i++) {
			// DFS를 통해 checked되지 않았음 -> 연결된 간선이 아님
			// (count가 추가됨)
			if(!checked[i]) {
				answer += DFS(i);
			}
		}
		System.out.println(answer);
		sc.close();
	}
}

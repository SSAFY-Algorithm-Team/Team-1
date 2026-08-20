package huiwon2.week2;

import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Java_1145 {
  // 너비 우선 탐색
	// 간선 개수 
	static int N = 0;
	// 정점 개수 
  static int M = 0;
  static ArrayList<ArrayList<Integer>> graph;
  static boolean[] checked;
  private static void BFS(int v) {
    // Queue 정의 
    Queue<Integer> queue = new LinkedList<>();
    checked[v] = true;
    queue.offer(v);

    // 처음 시작 정점 출력
    System.out.print(v + " ");

    while(!queue.isEmpty()) {
      // 현재 queue의 값을 추출
    	int current = queue.poll();
    	for(int next : graph.get(current)) {
        // 다음 노드가 체크되어있지 않다면
    		if(!checked[next]) {
    			checked[next] = true;
          // 다음 요소를 큐에 추가
    			queue.offer(next);
          // print
    			System.out.print(next + " ");
    		}
    	}
    }
  }
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		// 시작 정점 
		int v = sc.nextInt();
		
		graph = new ArrayList<ArrayList<Integer>>();
		for(int i = 0; i < N+1; i++) {
			graph.add(new ArrayList<Integer>());
		}
		
		checked = new boolean[N+1];
		// 간선 입력
		for (int i = 0; i < M; i++) {
      int a = sc.nextInt();
      int b = sc.nextInt();
      // 그래프에 1(visited 표시)
      // 양쪽 graph add 필요
      // add 안할 시 인접하지 않은 부분이 생겨 출력하지 못하고 빠져나오는 상황 발생
      if(a <= N && b <= N){
        graph.get(a).add(b);
      	graph.get(b).add(a);
      }
    }
		
		// 더 작은 정점부터 접근하려고 할 때, graph의 오름차순 정렬이 필요
		for(int i = 1; i < N+1; i++) {
			Collections.sort(graph.get(i));
		}
		BFS(v);
		sc.close();
	}
}

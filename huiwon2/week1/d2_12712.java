package huiwon2.week1;
import java.util.Scanner;
//파리퇴치 3
public class d2_12712 {
	public static void main(String args[]) throws Exception{
        Scanner sc = new Scanner(System.in);
        int T;
        T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
        {
            // 배열 수
            int N = sc.nextInt();
            // 분사 세기
            int M = sc.nextInt();
            int sum = 0;

            int[][] area = new int[N][N];
            for (int i = 0; i < area.length; i++) {
                for (int j = 0; j < area[i].length; j++) {
                    area[i][j] = sc.nextInt();
                }
            }

            // + 형태
            int[] dr = { -1, 1, 0, 0 };
            int[] dc = { 0, 0, 1, -1 };
            for (int r = 0; r < N; r++) {
                for (int c = 0; c < N; c++) {
                    int tmp = area[r][c];
                    for (int m = 1; m < M; m++) {
                        for (int d = 0; d < 4; d++) {
                            int nr = r + dr[d] * m;
                            int nc = c + dc[d] * m;
                            if (nr >= 0 && nr < N && nc >= 0 && nc < N) {
                                tmp += area[nr][nc];
                            }
                        }

                    }
                    if (tmp > sum) {
                        sum = tmp;
                    }
                }
            }

            // x 형태
            int[] drx = { -1, 1, -1, 1 };
            int[] dcx = { -1, 1, 1, -1 };
            for (int r = 0; r < N; r++) {
                for (int c = 0; c < N; c++) {
                    int tmp = area[r][c];
                    for (int m = 1; m < M; m++) {
                        for (int d = 0; d < 4; d++) {
                            int nr = r + drx[d] * m;
                            int nc = c + dcx[d] * m;
                            if (nr >= 0 && nr < N && nc >= 0 && nc < N) {
                                tmp += area[nr][nc];
                            }
                        }

                    }
                    if (tmp > sum) {
                        sum = tmp;
                    }
                }
            }
            System.out.println("#" + test_case + " " + sum);


        }
        sc.close();
    }
}

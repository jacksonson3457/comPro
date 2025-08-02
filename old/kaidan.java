package old;

import java.util.*;

public class kaidan {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        // 改行を読み飛ばす
        scanner.nextLine();
        int A = scanner.nextInt();
        int B = scanner.nextInt();

        // 小さい方を判定
        int min = Math.min(A, B);
        int max = Math.max(A, B);

        // ボードの状態を格納する配列
        int[][] board = new int[2][N / min + 1];
        // [][0]に初期値を入れておく
        board[0][0] = 0;
        board[1][0] = 0;
        board[0][1] = A;
        board[1][1] = B;

        // A,Bの倍数を記録していく
        for (int i = 0; i < 2; i++) {
            for (int j = 2; j < N / min + 1; j++) {
                board[i][j] = board[i][j - 1] + board[i][1];
            }
        }

        boolean[] kaidan = new boolean[N + 1];
        kaidan[N] = true;

        // 調べるのはi=0の時だけで良い
        for (int i = 0; i < N / min + 1; i++) {
            for (int j = 0; j < N / min + 1; j++) {
                int temp = board[0][i] + board[1][j];
                if (temp <= N) {
                    kaidan[temp] = true;
                }
            }
        }

        int counter = 0;

        for (boolean a : kaidan) {
            if (a == false) {
                counter++;
            }
        }

        System.out.println(counter);
    }
}
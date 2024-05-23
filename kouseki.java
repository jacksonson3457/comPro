import java.util.*;
import java.math.BigInteger;

//集合被覆問題

public class kouseki {
    /**
     * @param args
     */
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int L = scanner.nextInt();
        // 改行を読み飛ばす
        scanner.nextLine();

        // 二重配列に入れる
        int[][] numArray = new int[N][L];

        // 二重配列に値を入力
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < L; j++) {
                numArray[i][j] = scanner.nextInt();
            }
        }

        // グループに分けて追加していく用のリスト
        // 二重配列に入れる
        int[][] checkArray = new int[N][L];

        for (int i = 0; i < L; i++) {
            for (int j = 0; j < N; j++) {
                int count1 = 0;

                if (numArray[j][i] == 1) {
                    count1++;
                }

            }
        }

        System.out.println();
    }

    public static int saiki(int[][] array, int n, int l) {
        // グループに分けて追加していく用のリスト
        // 二重配列に入れる
        int[][] checkArray = new int[n][n];
        for (int i = 0; i < l; i++) {
            for (int j = 0; j < n; j++) {
                int count1 = 0;
                int count0 = 0;
                int[] max = new int[2];
                max[0] = 100;

                if (array[j][i] == 1) {
                    count1++;
                } else {
                    count0++;
                }
                if (Math.abs(count0 - count1) < max[0]) {
                    max[0] = Math.abs(count0 - count1);
                    max[1] = i;
                }

            }
        }
    }
}
import java.util.Scanner;
import java.util.LinkedList;

//san
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Integer N = sc.nextInt();
        Integer Q = sc.nextInt();

        int L = 1;
        int R = 2;

        int result = 0;

        for (int i = 0; i < Q; i++) {
            String hand = sc.next();
            int location = sc.nextInt();

            if (hand.equals("L")) {
                int iterator = L;
                int counter = 0;

                // 対角線
                int angle = (L + N / 2) % N;
                if (L < R && R < angle) {
                    counter = (L - location + N) % N;
                } else {
                    counter = (location - L);
                }

                if (location == L) {
                    counter = 0;
                }
                // 最後にcounterを加えて、LRの現在地を更新しておく
                result += counter;
                L = location;
            }

            if (hand.equals("R")) {
                int iterator = R;
                int counter = 0;

                // 対角線
                int angle = (R + N / 2) % N;
                if (R < L && L < angle) {
                    counter = (R - location + N) % N;
                } else {
                    counter = (location - R);
                }

                if (location == R) {
                    counter = 0;
                }
                // 最後にcounterを加えて、LRの現在地を更新しておく
                result += counter;
                R = location;
            }

        }
        System.out.println(result);
    }
}
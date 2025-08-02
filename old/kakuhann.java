package old;

import java.util.*;
import java.math.BigInteger;

public class kakuhann {
    /**
     * @param args
     */
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        // 改行を読み飛ばす
        scanner.nextLine();

        ArrayList<String> list = new ArrayList<String>();

        for (int i = 0; i < 2 * N; i++) {
            list.add(scanner.nextLine());
        }

        // カードの位置を保存するマップ
        Map<Integer, List<Integer>> positions = new HashMap<>();

        for (int i = 0; i < 2 * N; i++) {
            int card = Integer.parseInt(list.get(i));
            // すでにpositionsに存在しているならcardの値にもう一個追加、ないならcardの値をキーにしてマップを作りiを追加
            if (!positions.containsKey(i)) {
                List<Integer> initialList = new ArrayList<>();
                initialList.add(i);
                positions.put(card, initialList);
            } else {
                positions.get(card).add(i);
            }
        }

        BigInteger counter = BigInteger.ZERO;

        for (int i = 1; i <= N; i++) {
            List<Integer> positionList = positions.get(i);
            int startPoint = positionList.get(0);
            int endPoint = positionList.get(1);

            counter = counter.add(BigInteger.valueOf(endPoint - startPoint - 1));
        }

        // スタックを使ったほうがいいのかなあ
        // Stack<Integer> stack = new Stack<>();

        System.out.println(counter);
    }
}
import java.util.*;

public class Map {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        Scanner scanner = new Scanner(System.in);
        int H = scanner.nextInt();
        int W = 5;

        // 改行を読み飛ばす
        scanner.nextLine();

        // ボードの状態を格納する配列
        String[][] board = new String[H][W];

        // 各行を読み取り、ボードに格納
        for (int i = 0; i < H; i++) {
            String line = scanner.nextLine();
            for (int j = 0; j < W; j++) {
                board[i][j] = String.valueOf(line.charAt(j));
            }
        }

        // チェック用配列の定義
        boolean[][] checkFlg = new boolean[H][W];

        do {

            // checkFlg配列をリセット
            for (int i = 0; i < H; i++) {
                Arrays.fill(checkFlg[i], false);
            }
            // iが縦、jが横
            for (int i = 0; i < H; i++) {
                for (int j = 0; j < W; j++) {
                    // 1つずつチェックする
                    // 上端の時 流石に全パターンはえぐい
                    if (i == 0) {
                        if (j == 0)// 左端
                        {
                            if ((board[i][j].equals(board[i + 1][j])) && (board[i][j].equals(board[i][j + 1]))) {
                                checkFlg[i][j] = true;
                                checkFlg[i + 1][j] = true;
                                checkFlg[i][j + 1] = true;

                            }
                        } else if (j == W - 1) // 右端
                        {
                            if ((board[i][j].equals(board[i + 1][j])) && (board[i][j].equals(board[i][j - 1]))) {
                                checkFlg[i][j] = true;
                                checkFlg[i + 1][j] = true;
                                checkFlg[i][j - 1] = true;
                            }
                        } else // はじではない
                        {
                            if ((board[i][j].equals(board[i + 1][j])) && (board[i][j].equals(board[i][j - 1]))
                                    && (board[i][j].equals(board[i][j + 1]))) {
                                checkFlg[i][j] = true;
                                checkFlg[i + 1][j] = true;
                                checkFlg[i][j - 1] = true;
                                checkFlg[i][j + 1] = true;
                            }
                        }
                    } // 下端の時
                    else if (i == H - 1) {
                        if (j == 0)// 左端
                        {
                            if ((board[i][j].equals(board[i - 1][j])) && (board[i][j].equals(board[i][j + 1]))) {
                                checkFlg[i][j] = true;
                                checkFlg[i - 1][j] = true;
                                checkFlg[i][j + 1] = true;

                            }
                        } else if (j == W - 1) // 右端
                        {
                            if ((board[i][j].equals(board[i - 1][j])) && (board[i][j].equals(board[i][j - 1]))) {
                                checkFlg[i][j] = true;
                                checkFlg[i - 1][j] = true;
                                checkFlg[i][j - 1] = true;
                            }
                        } else // はじではない
                        {
                            if ((board[i][j].equals(board[i - 1][j])) && (board[i][j].equals(board[i][j - 1]))
                                    && (board[i][j].equals(board[i][j + 1]))) {
                                checkFlg[i][j] = true;
                                checkFlg[i - 1][j] = true;
                                checkFlg[i][j - 1] = true;
                                checkFlg[i][j + 1] = true;
                            }
                        }
                    } // 左端の時
                    else if (j == 0) {
                        if (i == 0)// 上端
                        {
                            if ((board[i][j].equals(board[i + 1][j])) && (board[i][j].equals(board[i][j + 1]))) {
                                checkFlg[i][j] = true;
                                checkFlg[i + 1][j] = true;
                                checkFlg[i][j + 1] = true;

                            }
                        } else if (i == H - 1) // 下端
                        {
                            if ((board[i][j].equals(board[i - 1][j])) && (board[i][j].equals(board[i][j + 1]))) {
                                checkFlg[i][j] = true;
                                checkFlg[i - 1][j] = true;
                                checkFlg[i][j + 1] = true;
                            }
                        } else // はじではない
                        {
                            if ((board[i][j].equals(board[i - 1][j])) && (board[i][j].equals(board[i][j + 1]))
                                    && (board[i][j].equals(board[i + 1][j]))) {
                                checkFlg[i][j] = true;
                                checkFlg[i - 1][j] = true;
                                checkFlg[i][j + 1] = true;
                                checkFlg[i + 1][j] = true;
                            }
                        }
                    } // 右端の時
                    else if (j == W - 1) {
                        if (i == 0)// 上端
                        {
                            if ((board[i][j].equals(board[i + 1][j])) && (board[i][j].equals(board[i][j - 1]))) {
                                checkFlg[i][j] = true;
                                checkFlg[i + 1][j] = true;
                                checkFlg[i][j - 1] = true;

                            }
                        } else if (i == H - 1) // 下端
                        {
                            if ((board[i][j].equals(board[i - 1][j])) && (board[i][j].equals(board[i][j - 1]))) {
                                checkFlg[i][j] = true;
                                checkFlg[i - 1][j] = true;
                                checkFlg[i][j - 1] = true;
                            }
                        } else // はじではない
                        {
                            if ((board[i][j].equals(board[i - 1][j])) && (board[i][j].equals(board[i][j - 1]))
                                    && (board[i][j].equals(board[i + 1][j]))) {
                                checkFlg[i][j] = true;
                                checkFlg[i - 1][j] = true;
                                checkFlg[i][j - 1] = true;
                                checkFlg[i + 1][j] = true;
                            }
                        }
                    } // はじではない
                    else {
                        if ((board[i][j].equals(board[i - 1][j])) && (board[i][j].equals(board[i][j - 1]))
                                && (board[i][j].equals(board[i + 1][j])) && (board[i][j].equals(board[i][j + 1]))) {
                            checkFlg[i][j] = true;
                            checkFlg[i - 1][j] = true;
                            checkFlg[i][j - 1] = true;
                            checkFlg[i + 1][j] = true;
                            checkFlg[i][j + 1] = true;
                        }
                    }

                }
            }

            // 落とす
            for (int j = 0; j < W; j++) {
                int writeIndex = H - 1;
                for (int i = H - 1; i >= 0; i--) {
                    if (!checkFlg[i][j]) {
                        board[writeIndex][j] = board[i][j];
                        writeIndex--;
                    }
                }
                while (writeIndex >= 0) {
                    board[writeIndex][j] = ".";
                    writeIndex--;
                }
            }

        } while (hasAnyTrue(checkFlg)); // 全てのcheckFlgがfalseになるまで

        // 結果の出力
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                System.out.print(board[i][j]);
            }
            System.out.println();
        }
    }

    // checkFlg配列にtrueが存在するかをチェックするメソッド
    private static boolean hasAnyTrue(boolean[][] checkFlg) {
        for (int i = 0; i < checkFlg.length; i++) {
            for (int j = 0; j < checkFlg[i].length; j++) {
                if (checkFlg[i][j]) {
                    return true;
                }
            }
        }
        return false;
    }
}
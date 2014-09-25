import java.util.*;

public class Main {
    public static void reportMove(int turn, int[] x, int i, int newValue) {
        System.out.println(turnToName(turn) + " takes " + (x[i] - newValue) + " from pile " + i);
    }

    public static int lambda(int x) {
        return 31 - Integer.numberOfLeadingZeros(x);
    }

    public static String turnToName(int turn) {
        return turn == 0 ? "John" : "Brother";
    }

    public static void printState(int n, int[] x, int turn) {
        System.out.println("Turn = " + turnToName(turn));
        for(int i = 0; i < n; i++ ){
            System.out.print(x[i] + " ");
        }
        System.out.println();
        System.out.println("--");
    }

    public static int solveFull(
                                int n,
                                int[] x,
                                int one_count,
                                int zero_count,
                                int turn,
                                int s
                            ) {
        while(true) {
            printState(n, x, turn);
            if(one_count == n - zero_count) {
                if(one_count % 2 == 0) {
                    System.out.println("Even number of ones left. Current player wins.");
                    return turn;
                } else {
                    System.out.println("Odd number of ones left. Current player loses.");
                    return 1 - turn;
                }
            } else if(one_count + 1 == n - zero_count) {
                System.out.println("Only one heap with more than 1 left.");
                for(int i = 0; i < n; i++ ) {
                    if(x[i] > 1) {
                        if(one_count % 2 == 0) {
                            reportMove(turn, x, i, 1);
                            x[i] = 1;
                            one_count ++;
                        } else {
                            reportMove(turn, x, i, 0);
                            x[i] = 0;
                            zero_count ++;
                        }
                        break;
                    }
                }
                return turn;
            }

            if(s == 0) {
                // Does not matter what we do, things will not go well
                // So let's make one x[i] zero
                for(int i = 0; i < n; i++ ){
                    if(x[i] != 0) {
                        if(x[i] == 1) {
                            one_count --;
                        }
                        zero_count ++;
                        x[i] = 0;
                    }
                }
            } else {
                /* System.out.println("lambda = " + (1 << lambda(s))); */
                for(int k = 0; k < n; k++) {
                    int bit = x[k] & (1 << lambda(s));
                    if(bit != 0) {
                        /* System.out.println("k = " + k); */
                        /* System.out.println("x[k] = " + x[k]); */
                        int old_xi = x[k];
                        x[k] = s ^ x[k];
                        s ^= old_xi ^ x[k];
                        /* System.out.println("y[k] = " + x[k]); */
                        if(x[k] == 1) {
                            one_count ++;
                        } else if (x[k] == 0) {
                            zero_count ++;
                            if(old_xi == 1) {
                                one_count --;
                            }
                        }
                        break;
                    }
                }
            }

            turn = 1 - turn;
        }
    }

    public static int solve(
                                int n,
                                int[] x,
                                int one_count,
                                int zero_count,
                                int turn,
                                int s
                            ) {
        if(one_count == n) {
            return one_count % 2;
        } else if (one_count == n - 1) {
            return 0;
        } else {
            return s == 0 ? 1 : 0;
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t;
        t = in.nextInt();
        for(int c = 0; c < t; c++ ){
            /* System.out.println("----"); */
            int n = in.nextInt();
            int[] heaps = new int[n];
            int one_count = 0;
            int s = 0;
            for(int i =0; i<n; i++) {
                heaps[i] = in.nextInt();
                if (heaps[i] == 1) {
                    one_count ++;
                }
                s ^= heaps[i];
            }

            int winner = solve(n, heaps, one_count, 0, 0, s);
            /* System.out.print("Winner = "); */
            System.out.println(turnToName(winner));
        }
    }
}

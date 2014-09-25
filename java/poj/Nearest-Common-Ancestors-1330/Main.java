import java.util.*;
import java.util.Scanner;

public class Main{

    /* public static int find(int x, int[] S) { */
    /*     if(S[x] == 0) return x; */
    /*     int p = find(S[x], S); */
    /*     S[x] = p; */
    /*     return p; */
    /* } */

    /* public static void union(int x, int y, int[] S) { */
    /*     int p1 = find(x, S); */
    /*     int p2 = find(y, S); */
    /*     S[p1] = p2; */
    /* } */

    /* public static void print(int[] S) { */
    /*     for (int i = 1; i < S.length; i++) { */
    /*         System.out.println("" + i + "\t" + S[i]); */
    /*     } */
    /* } */

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int T = in.nextInt();
        for(int c = 1; c <= T; c++) {
            int u, v;
            int N = in.nextInt();
            boolean[] S = new boolean[N + 1];
            int[] tree = new int[N + 1];
            // Read N - 1 edges
            for(int i = 1; i < N; i++) {
                u = in.nextInt();
                v = in.nextInt();
                tree[v] = u;
            }

            // Find the closest common ancestor of u and v
            u = in.nextInt();
            v = in.nextInt();

            int p = u;
            while(p != 0) {
                S[p] = true;
                p = tree[p];
            }

            p = v;
            while(p != 0) {
                if(S[p]) {
                    System.out.println(p);
                    break;
                }
                p = tree[p];
            }
        }
    }
}


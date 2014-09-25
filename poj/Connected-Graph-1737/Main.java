import java.util.*;
import java.util.Scanner;

public class Main{
    public static int MAX = 50;
    public static long[][] C;

    public static void precalculateC()
    {
        C = new long[MAX + 1][MAX + 1];
        for(int i = 0; i <= MAX; i++) {
            C[i][0] = 1;
            C[0][i] = 1;
            C[i][1] = i;
        }
        for(int i = 1; i <= MAX; i++) {
            for(int j = 2; j <= i; j++) {
                C[i][j] = C[i-1][j] + C[i-1][j-1];
            }
        }
    }

    public static void solve(int n) {
        // Assume 1 <= n <=5
        long c = 0;
        int m = n * (n - 1) / 2;
        for(int i = n - 1; i <= m; i++) {
            System.out.format("%d %d %d\n", i, m, C[m][i]);
            c+= C[m][i];
        }
        System.out.println(c);
    }

    public static void main(String[] args) {
        precalculateC();
        Scanner in = new Scanner(System.in);
        while(true) {
            int n = in.nextInt();
            if(n == 0) break;
            System.out.format("Working on %d\n", n);
            System.out.println(C[n][2]);
            solve(n);
        }
    }
}


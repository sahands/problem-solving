import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static int mod(int a, int q) {
        int r = a % q;
        if(r < 0) r += q;
        return r;
    }

    public static int gcd(int a, int b) {
        b = Math.abs(b);
        while(b != 0) {
            int r = mod(a, b);
            a = b;
            b = r;
        }
        return a;
    }

    public static int process(int[] A, int n) {
        if(n == 1) {
            return A[0];
        }
        if(n == 2) {
            /* int d = Math.abs(Math.abs(A[0]) - Math.abs(A[1])); */
            int d = Math.abs(A[0] - A[1]);
            if(d == 0) {
                return Math.abs(A[0]);
            }
            return d;
        }
        int d = Math.abs(A[0] - A[1]);
        int m = A[0];
        for(int i = 2; i < n; i++) {
            if(m < A[i]) m = A[i];
            d = gcd(d, A[i - 1] - A[i]);
        }
        if(d == 0)
            d = m;

        return d;
    }

    public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
        int[] A = new int[1000];
        while(true) {
            int n = 0;
            for(n = 0; n < 1000; n++) {
                int a = in.nextInt();
                if(a == 0) break;
                A[n] = a;
            }
            if(n == 0) break;

            int d = process(A, n);
            System.out.println(d);
        }
    }
}

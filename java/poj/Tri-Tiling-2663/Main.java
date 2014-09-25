import java.util.*;
import java.util.Scanner;

public class Main{

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int count = 0;
        final int N = 31;
        int[] A = new int[N + 1];
        int[] B = new int[N + 1];

        A[0] = B[0] = B[1] = 1;

        /* System.out.println("" + 0 + " - " + A[0]); */
        /* System.out.println("" + 1 + " - " + A[1]); */
        for(int n = 2; n <= N; n++) {
            A[n] = A[n-2] + 2 * B[n-1];
            B[n] = A[n-1] + B[n-2];
            /* System.out.println("" + n + " - " + A[n]); */
        }

        for(;;) {
            int n = in.nextInt();
            if(n < 0) {
                break;
            }
            if(n % 2 == 1) {
                System.out.println(0);
            } else {
                System.out.println(A[n]);
            }
        }
    }
}


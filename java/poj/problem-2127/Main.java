import java.util.*;
import java.util.Scanner;

public class Main{

    public static int[] readSequence(Scanner in) {
        int n = in.nextInt();
        int[] A = new int[n];
        for(int i = 0; i<n; i++) {
            A[i] = in.nextInt();
        }
        return A;
    }


    public static int LICSS(int[] A, int[] B, int n, int m) {
        int[][] M = new int[n][m];
        for(int i = 0;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int[] A = readSequence(in);
        int[] B = readSequence(in);
        int n = A.length;
        int m = B.length;
        System.out.println(LICSS(A, B, n, m);
    }
}


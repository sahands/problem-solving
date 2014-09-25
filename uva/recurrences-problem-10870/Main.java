import java.util.Arrays;
import java.util.Scanner;

public class Main {

    // Calculates C = A * B
    static long[][] matrixMultiply(long[][] A, long[][] B, int d, long m) {
        long[][] C = new long[d][d];
        for(int i = 0; i < d; i++) {
            for(int j = 0; j < d; j++) {
                C[i][j] = 0;
                for(int k = 0; k < d; k++) {
                    C[i][j] += (A[i][k] * B[k][j]) % m;
                }
            }
        }
        return C;
    }

    static long[][] identityMatrix(int d) {
        long[][] I = new long[d][d];
        for(int i = 0; i < d; i++ ){
            for(int j = 0; j < d; j++ ){
                I[i][j] = i == j? 1 : 0;
            }
        }
        return I;
    }

    static void printMatrix(long[][] M, int d) {
        System.out.println("M");
        for(int i = 0; i < d; i ++) {
            for(int j = 0; j < d; j ++) {
                System.out.print(M[i][j] + " ");
            }
            System.out.print("; ");
        }
        System.out.println("\n----");
    }

    static long[][] matrixPow(long[][] A, int d, int n, long m) {
        if(n == 0) {
            return identityMatrix(d);
        } else if(n == 1) {
            return A;
        } else {
            long[][] C = matrixPow(A, d, n / 2, m);
            long[][] D = matrixMultiply(C, C, d, m);
            if(n % 2 == 1) {
                return matrixMultiply(A, D, d, m);
            } else {
                return D;
            }
        }
    }

	public static long solve(int d, int n, long m, long[] f, long[] a) {
        // Create the recurrence matrix
        long M[][] = new long[d][d];
        for(int i = 0; i < d; i ++) {
            M[0][i] = a[i];
        }

        for(int i = 1; i < d; i ++) {
            for(int j = 0; j < d; j ++) {
                M[i][j] = i == j + 1 ? 1 : 0;
            }
        }

        long[][] T = matrixPow(M, d, n - d, m);
        long fn = 0;
        for(int i = 0; i < d; i++) {
            fn += (T[0][i] * f[i]) % m;
            fn %= m;
        }

        return fn;
	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
        while(true) {
            int d, n, m;
            d = in.nextInt();
            n = in.nextInt();
            m = in.nextInt();

            long a[] = new long[d];
            long f[] = new long[d];

            if(d == 0 && n == 0 && m == 0) {
                break;
            }

            for(int i = 0; i < d; i++) {
                a[i] = in.nextLong() % m;
            }

            for(int i = d - 1; i >= 0; i--) {
                f[i] = in.nextLong() % m;
            }

            if(n <= d) {
                System.out.println(f[n-1]);
            } else {
                System.out.println(solve(d, n, m, f, a));
            }
		}
	}
}

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
                C[i][j] %= m;
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

    public static long fib(int n, long m) {
        long[][] M = {{1, 1}, {1, 0}};
        long[][] T = matrixPow(M, 2, n, m);
        return T[0][1];
    }

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
        while(in.hasNext()) {
            int n, m;
            n = in.nextInt();
            m = in.nextInt();
            System.out.println(fib(n, 1 << m));
		}
	}
}


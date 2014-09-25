import java.util.Arrays;
import java.util.Scanner;

public class Arbitrage2 {
    static final int N = 20;
    static int n;
	static double W[][] = new double[N][N];
	static double W1[][] = new double[N][N];
	static double W2[][] = new double[N][N];
	static int P[][][] = new int[N][N][N];

	public static String printPath(int i, int j, int d) {
		if (W2[i][j] == 0) {
			return "";
		}

        if (d < 0) {
            /* return Integer.toString(j + 1); */
            return "";
        }

		int k = P[i][j][d];
        /* System.out.format("%d to %d going through %d\n", i, j, k); */
		if (k == -1) {
			return "";
		} else {
			return printPath(i, k, d - 1) + " " + (k + 1);
		}
	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		while (in.hasNext()) {
			n = in.nextInt();
            // Initialization
			for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    W[i][j] = W1[i][j] = W2[i][j] = 0;
                    for(int d = 0; d < n; d++ ){
                        P[i][j][d] = -1;
                    }
                }
			}

            // Read Input
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					if (i == j) {
						W[i][i] = 1.0;
						continue;
					}
					W1[i][j] = W[i][j] = in.nextDouble();
				}
			}

            // Calculate arbitrage with at least 1.01 profitability of shortest
            // length
			boolean arbitrage = false;

            for (int d = 0; d < n; d ++) {
                for (int k = 0; k < n ; k++) {
                    for (int i = 0; i < n ; i++) {
                        for (int j = 0; j < n ; j++) {
                            // If there is a path from i to j consisting of of
                            // a path of length d+1 from i to k and a path of
                            // length 1 from k to j that is more profitable,
                            // use that path instead
                            if (W2[i][j] < W1[i][k] * W[k][j]) {
                                P[i][j][d] = k;
                                W2[i][j] = W1[i][k] * W[k][j];
                            }
                        }
                    }
                }

                /* System.out.format("d = %d\n", d); */
                /* for (int i = 0; i < n; i++) { */
                /*     for (int j = 0; j < n; j++) { */
                /*         System.out.format("%.3f\t", W2[i][j]); */
                /*     } */
                /*     System.out.println(); */
                /* } */

                for(int i = 0; i < n; i++) {
                    if(W2[i][i] > 1.01) {
                        /* System.out.println("Found arbitrage starting at " + i + " with d=" + d ); */
                        /* System.out.println("P[i][i][d] = " + P[i][i][d]); */
                        System.out.println((i+1) + printPath(i, i, d) + " " + (i+1));
                        d = n;
                        arbitrage = true;
                        break;
                    }
                }

                /* for (int i = 0; i < n; i++) { */
                /*     for (int j = 0; j < n; j++) { */
                /*         W1[i][j]=W2[i][j]; */
                /*         W2[i][j]=0; */
                /*     } */
                /* } */
                double[][] temp = W1;
                W1 = W2;
                W2 = temp;
            }

			if (!arbitrage) {
				System.out.println("no arbitrage sequence exists");
			}
		}
	}
}

import java.util.Scanner;
import java.lang.StringBuilder;

public class Arbitrage {
    static final int N = 20;
	static double W[][] = new double[N][N];
	static double W1[][] = new double[N][N];
	static double W2[][] = new double[N][N];
	static int P[][][] = new int[N][N][N];

	public static String getPathString(int i, int j, int d) {
        if (W2[i][j] == 0) {
            return "";
        }
        StringBuilder sb = new StringBuilder();
        sb.insert(0, i+1);
        sb.insert(0, " ");
		int k = P[i][j][d];
        while(k != -1 && d>=0) {
            sb.insert(0, k + 1);
            sb.insert(0, " ");
            d--;
            if(d<0) {
                break;
            }
            k = P[i][k][d];
        }
        sb.insert(0, j+1);
        return sb.toString();
	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		while (in.hasNext()) {
			int n = in.nextInt();
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
                    W1[i][j] = W[i][j] = i==j? 1.0 : in.nextDouble();
				}
			}

			boolean arbitrage = false;

            // Calculate arbitrage with at least 1.01 profitability of shortest
            // length. d+1 is the current number of transactions.
            for (int d = 0; d < n; d ++) {
                // Loop invariant: W1[i][j] is the shorest path from i to j
                // using at most d vertices in between.
                // Base case of this loop invariant is that W1 is the same W, the initial weights.
                // Hence W1[i][j] is the shortest path from i to j with d=0
                // vertices in between, which is another waying of saying it is
                // the edge weights.
                // We maintain the loop invariant by setting W2[i][j] to be the
                // shortest path from i to j with at most d+1 vertices in
                // between, and at the end, we set W1 = W2.
                for (int k = 0; k < n ; k++) {
                    for (int i = 0; i < n ; i++) {
                        for (int j = 0; j < n ; j++) {
                            // To get a shortest path from i to j using d+1
                            // vertices, we assume k is the (d+1)th vertex and
                            // see if we get a shorter path using it.
                            if (W2[i][j] < W1[i][k] * W[k][j]) {
                                P[i][j][d] = k;
                                W2[i][j] = W1[i][k] * W[k][j];
                            }
                        }
                    }
                }

                for(int i = 0; i < n; i++) {
                    if(W2[i][i] > 1.01) {
                        System.out.println(getPathString(i, i, d));
                        d = n;
                        arbitrage = true;
                        break;
                    }
                }

                // At this point W2 is the shortest path from i to j using d+1
                // paths. So switch W1 and W2 to maintain the loop invariant.
                // (Instead of re-initializing W2 to all zeros, I simply set it
                // to old W1 since old W1 values will no longer be needed and
                // will be overwritten next time around.)
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

import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static final int N = 101;
	static double W[][] = new double[N][N];

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int c = 1;
		while (true) {
			// Initialization
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					W[i][j] = Integer.MAX_VALUE;
				}
			}

			// Read Input
			int n = -1;
			int a, b;
			do {
				a = in.nextInt();
				b = in.nextInt();
				n = a > n ? a : n;
				W[a][b] = 1;
			} while (a != 0 && b != 0);

			if (n <= 0) {
				break;
			}

			for (int k = 1; k <= n; k++) {
				for (int i = 1; i <= n; i++) {
					for (int j = 1; j <= n; j++) {
						if (W[i][j] > W[i][k] + W[k][j]) {
							W[i][j] = W[i][k] + W[k][j];
						}
					}
				}
			}

			double count = 0;
			double sum = 0;
			for (int i = 1; i <= n; i++) {
				for (int j = 1; j <= n; j++) {
					if (i == j) {
						continue;
					}
					if (W[i][j] < Integer.MAX_VALUE) {
						count++;
						sum += W[i][j];
					}
				}
			}
			
			System.out.format(
					"Case %d: average length between pages = %.3f clicks\n", c,
					sum/count);

			c++;
		}
	}
}

import java.util.Scanner;

public class Problem10616 {
	public static int mod(int n, int q) {
		int r = n % q;
		return r < 0 ? r + q : r;
	}

	public static long solve(int[] numbers, int d, int m) {
		// M[i][j][k] is the number of ways to pick i elements of numbers
		// numbers[0] to numbers[j] so that their sum is k modulo d
		int n = numbers.length;
		long[][][] M = new long[m + 1][n][d];
		for (int j = 0; j < n; j++) {
			M[0][j][0] = 1;
		}

		for (int i = 1; i <= m; i++) {
			for (int j = 0; j < n; j++) {
				for (int k = 0; k < d; k++) {
					int q = mod(numbers[j], d);
					if (j + 1 < i) {
						M[i][j][k] = 0;
					} else if (j == 0) {
						M[i][j][k] = q == k ? 1 : 0;
					} else {
						int r = mod(k - q, d);
						M[i][j][k] = M[i - 1][j - 1][r] + M[i][j - 1][k];
					}
				}
			}
		}

		return M[m][n - 1][0];
	}

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int set = 1;
		while (scanner.hasNext()) {
			int n = scanner.nextInt();
			int q = scanner.nextInt();
			if (n == 0 && q == 0) {
				break;
			}
			int[] numbers = new int[n];
			System.out.format("SET %d:\n", set);
			for (int i = 0; i < n; i++) {
				numbers[i] = scanner.nextInt();
			}
			for (int i = 1; i <= q; i++) {
				int d = scanner.nextInt();
				int m = scanner.nextInt();
				long count = solve(numbers, d, m);
				System.out.format("QUERY %d: %d\n", i, count);
			}
			set++;
		}
	}
}

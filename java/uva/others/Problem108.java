import java.util.Scanner;

public class Problem108 {
	public static long maxSumSubarray(long[] right, long[] left, int n) {
		long local_max, global_max;
		local_max = global_max = right[0] - left[0];

		for (int i = 1; i < n; i++) {
			long num = right[i] - left[i];
			if (local_max > 0) {
				local_max += num;
			} else {
				local_max = num;
			}

			if (local_max > global_max) {
				global_max = local_max;
			}
		}

		return global_max;
	}

	public static long maxSumSubmatrix(int[][] m, int n) {
		long[][] M = new long[n + 1][n]; // Partial sums of columns
		for (int i = 1; i < n + 1; i++) {
			for (int j = 0; j < n; j++) {
				M[i][j] = m[i - 1][j] + M[i - 1][j];
			}
		}

		long global_max = m[0][0];
		for (int row_start = 1; row_start < n+1; row_start++) {
			for (int row_end = row_start; row_end < n+1; row_end++) {
				long local_max = maxSumSubarray(M[row_end], M[row_start-1], n);
				if(local_max > global_max) {
					global_max = local_max;
				}
			}
		}
		
		return global_max;
	}

	public static void main(String[] args) {
		int n;
		int[][] m;
		Scanner scanner = new Scanner(System.in);
		n = scanner.nextInt();
		m = new int[n][n];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				m[i][j] = scanner.nextInt();
			}
		}

		long maxSum = maxSumSubmatrix(m, n);
		System.out.println(maxSum);
	}
}
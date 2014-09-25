import java.util.Scanner;


public class Problem100 {
	public static final int M = 1000000;
	public static int[] C;
	
	public static int collatzCycles(int n) {
		int cycles = 0;
		int m = n;
		while(true) {
			if(1 <= m && m < M && C[m]>0) {
				if(1 <= n && n < M) {
					C[n] = C[m] + cycles;
				}
				return C[m] + cycles;
			}
			cycles += 1;
			m = m%2 == 0 ? m/2 : 3*m + 1;
		}
	}
	
	
	public static void main(String[] args) {
		C = new int[M];
		C[1] = 1;
		
		int i,j, i0, j0;
		java.util.Scanner scanner = new Scanner(System.in);
		while(scanner.hasNext()) {
			i = scanner.nextInt();
			j = scanner.nextInt();
			i0 = i<j? i : j;
			j0 = i<j? j : i;
			int m = 0;
			for(int k = i0; k <= j0; k++) {
				int c = collatzCycles(k);
				m = m > c? m : c;
			}
			System.out.format("%d %d %d\n", i, j , m);
		}
	}

}

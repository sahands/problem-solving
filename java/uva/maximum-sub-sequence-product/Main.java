import java.util.Arrays;
import java.util.Scanner;
import java.math.BigInteger;

public class Main {
	static final int N = 100;
	static int A[] = new int[N];

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		while (in.hasNext()) {
			// Initialization
			int n = 0;
			do {
				A[n++] = in.nextInt();
			} while(A[n-1] != -999999);
			
			n--;
			
			if (n <= 0) {
				break;
			}
			
			// a will hold the largest product seen so far that uses A[i-1]
			// b will hold the smallest product seen so far that uses A[i-1]
			// m is the global max seen
			BigInteger a, b, m;
			a = BigInteger.valueOf(A[0]);
			b = BigInteger.valueOf(A[0]);
			m = BigInteger.valueOf(A[0]);
			for(int i = 1 ; i < n ; i++) {
				BigInteger x = BigInteger.valueOf(A[0]);
				if(A[i] == 0 ) {
					a = b = BigInteger.valueOf(0);
				} else if (A[i] < 0) {
					BigInteger temp = BigInteger.valueOf(a);
					a = b.multiply(x);
					b = temp.multiply(x);
					if (b.compareTo(BigInteger.valueOf(0))>0) {
						b = x;
					}
				} else {
					// A[i] > 0 
					if (a.compareTo(BigInteger.valueOf(0))>0) {
						a = a.multiply(x) ;
						b = b.multiply(x);
					}
				}
				m = m > a ? m : a;
//				System.out.format("%d - x=%d  a=%d  b=%d  m=%d\n", i, A[i], a, b, m);
			}

			System.out.println(m);
		}
	}
}

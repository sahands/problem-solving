import java.util.Arrays;
import java.lang.Math;
import java.util.Scanner;
import java.util.HashMap;

public class Main {
	public final static double EPS = 0.0000001;
	static final int N = 100;
	static Point P[] = new Point[N];
	static HashMap<Point, Integer> M = new HashMap<Point, Integer>();

	// Returns the most number of points collinear to point X[i], Y[i]
	public static int mostCollinear(int i, int n) {
		double A[] = new double[n-1];
		int c = 2;
		int k = 0;
		for(int j=0;j<n;j++) {
			if(j==i) continue;
			double a = Math.atan2(P[j].y-P[i].y, P[j].x-P[i].x);
			if(a<0) {
				a = Math.PI/2.0 + a;
			}
			A[k++] = a;
		}
		java.util.Arrays.sort(A);
		int local_c = 2;
		for(int j = 1; j < k; j++) {
			if(Math.abs(A[j] - A[j-1]) > EPS) {
				local_c = 2;
			} else {
				local_c++;
			}
			
			if(c < local_c) {
				c = local_c;
			}
		}
		return c;
	}
	
	public static int solve(int n) {
		int best = 0;
		for(int i = 0; i<n; i++) {
			int c = mostCollinear(i, n);
			if(c > best) {
				best = c;
			}
		}
		return best;
	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int T = in.nextInt();
		for(int ts = 1; ts <= T; ts++) {
			M.clear();
			int nn = in.nextInt();
			int n = 0;
			for(int i = 0; i < nn; i++) {
				Point p = new Point();
				p.x = in.nextDouble();
				p.y = in.nextDouble();
				if(!M.containsKey(p)) {
					P[n++] = p;
					M.put(p, new Integer(1));
				}
			}
			
			if(n == 1) {
				System.out.format("Data set #%d contains a single gnu.\n", ts);
			} else {
				int best = solve(n);
				System.out.format("Data set #%d contains %d gnus, out of which a maximum of %d are aligned.\n", ts, n, best);
			}
		}
	}
}

class Point {
	public double x;
	public double y;
	
	@Override
    public int hashCode() {
		String s = String.format("%.4f, %.4f", this.x, this.y);
		int h = s.hashCode();
		return h;
    }
	
	@Override
	public boolean equals(Object p) {
		if(p instanceof Point){
			Point pp = (Point)p;
			return Math.abs(this.x-pp.x) < Main.EPS && Math.abs(this.y-pp.y) < Main.EPS;
		}
		return false;
	}
}
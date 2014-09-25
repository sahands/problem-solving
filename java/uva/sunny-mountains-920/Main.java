import java.util.Arrays;
import java.lang.Math;
import java.util.Scanner;
import java.lang.Comparable;

public class Main {
	public final static double EPS = 0.0000001;
	static final int N = 100;
	static Point P[];
	
	public static double solve(int n) {
		Arrays.sort(P);
		double sum = 0.0;
		double h = 0.0;
		for(int i = n-2; i>=0; i--) {
			// Loop invariant: h >= q.y
			Point q = P[i+1];
			Point p = P[i];
			// The line is from q to p
//			System.out.println(h);
			if(p.y > h) {
				double mi =  (p.x - q.x) / (p.y - q.y);
				double x = (h - p.y) * mi + p.x;
				double dx = (p.x - x);
				double dy = (p.y - h);
				double l = Math.sqrt(dx * dx + dy * dy);
//				System.out.format("Point (%.3f, %.3f) is being added with x = %.3f and l = %.3f\n", p.x, p.y, x, l);
				sum += l;
				h = p.y;
			} else {
//				System.out.format("Ignoring point (%.3f, %.3f)\n", p.x, p.y);
			}
		}
		return sum;
	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int T = in.nextInt();
		for(int ts = 1; ts <= T; ts++) {
//			System.out.println("--------");
			int n = in.nextInt();
			P = new Point[n];
			for(int i = 0; i < n; i++) {
				P[i] = new Point();
				P[i].x = in.nextDouble();
				P[i].y = in.nextDouble();
			}
			double s = solve(n);
			System.out.format("%.2f\n", s);
		}
	}
}

class Point implements Comparable<Point> {
	public double x;
	public double y;
	
	
	@Override
	public int compareTo(Point p) {
		if(p instanceof Point) {
			return Double.compare(this.x, p.x);
		}
		return -1;
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
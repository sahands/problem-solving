import java.util.*;

class Point {
	public int x, y;

	public Point(int x, int y) {
		this.x = x;
		this.y = y;
	}


    public Point minus(Point o) {
        return new Point(this.x - o.x, this.y - o.y);
    }


    public double dot(Point o) {
        return (double)(this.x * o.x + this.y * o.y);
    }

    public double distance(Point a, Point b) {
        // Calculate distance from this to line given by a -> b
        // Translate everything so a is the origin
        b = b.minus(a);
        Point c = this.minus(a);

        double y = b.dot(c);
        double z = b.dot(b);
        double t = y / z;
        // If the base of the perpendicular is before a
        // or after b, take a or b as the closest points.
        t = Math.max(t, 0);
        t = Math.min(t, 1);
		double dist_sq = c.dot(c) - 2 * t * y + t * t * z;
		return Math.sqrt(dist_sq);
    }
}

public class Main {
    public static Point[] readPolygon(Scanner in) {
		Point[] P = new Point[in.nextInt()];
		for(int i=0 ; i < P.length; i++) {
            P[i] = new Point(in.nextInt(), in.nextInt());
		}
        return P;
    }

	public static void processTestCase(Scanner in) {
		Point[] P1 = readPolygon(in);
		Point[] P2 = readPolygon(in);

        double min_distance = 10000000.0;
		for(int i=0; i < P1.length; i++)
            for(int j=0; j < P2.length; j++) {
                int ip = i + 1 < P1.length ? i + 1 : 0;
                int jp = j + 1 < P2.length ? j + 1 : 0;
                double d1 = P1[i].distance(P2[j], P2[jp]);
                double d2 = P2[j].distance(P1[i], P1[ip]);
                min_distance = Math.min(min_distance, d1);
                min_distance = Math.min(min_distance, d2);
			}

		System.out.println(min_distance / 2.0);
	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int t = in.nextInt();
        for(int i = 0; i < t; i++ ){
            processTestCase(in);
        }
	}
}


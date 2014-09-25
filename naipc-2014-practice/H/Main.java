import java.util.*;

public class Main {
    static int[] req = new int[] {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};

    static boolean canUseDigit(int n, int min, int i, int d) {
        if( d + i <= 1) {
            return false;
        }
        int r = n - req[d];
        if(r < 2 * (min - i) ){
            return false;
        }
        if( r > 7 * (min - i) ) {
            return false;
        }
        return true;
    }

    static String solve(int n, int min, boolean forward) {
        String s = "";
        for (int i = 1; i <= min; ++i) {
            if(forward) {
                for (int d = 0; d <= 9; d++) {
                    if(canUseDigit(n, min, i, d)) {
                        s += d;
                        n -= req[d];
                        break;
                    }
                }
            } else {
                for (int d = 9; d >= 0; d--) {
                    if(canUseDigit(n, min, i, d)) {
                        s += d;
                        n -= req[d];
                        break;
                    }
                }
            }
        }
        return s;
    }

	public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
		int t = in.nextInt();
		for(int i=0;i < t;++i) {
            int n = in.nextInt();
            int min = (n + 6) / 7;
            System.out.println("" + solve(n, min, true) +
                               " "+ solve(n, n, false));
        }
	}
}

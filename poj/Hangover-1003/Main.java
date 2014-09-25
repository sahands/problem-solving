import java.util.*;
import java.util.Scanner;

public class Main{
    public static int binarySearch(double[] H, double h) {
        int start = 0;
        int end = H.length - 1;
        while(start < end - 1) {
            int m = (start + end) / 2;
            if(H[m] <= h) {
                start = m;
            } else{
                end = m;
            }
        }
        return end;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = (int) Math.exp(5.2 + 1.0) + 2;
        double[] H = new double[N];

        H[0] = 0.0;
        for(int i = 1; i < N; i++ ) {
            H[i] = H[i-1] + 1.0 / (i + 1);
        }

        while(true) {
            double h = in.nextDouble();
            if(h < 0.001) {
                break;
            }
            int index = binarySearch(H, h);
            System.out.format("%d card(s)\n", index);
        }
    }
}

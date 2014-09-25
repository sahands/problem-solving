import java.util.*;
import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        for(int i = 1; i <= N; i++ ) {
            double R = in.nextDouble();
            int n = in.nextInt();
            double alpha = Math.sin(Math.PI / n);

            System.out.format("Scenario #%d: %f\n", i,  (alpha * R) / (1.0 + alpha));
        }
    }
}

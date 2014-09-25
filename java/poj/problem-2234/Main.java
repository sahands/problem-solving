import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        while(in.hasNext()) {
            int n = in.nextInt();
            int s = 0;
            for(int i =0; i<n; i++) {
                s ^= in.nextInt();
            }
            System.out.println( s == 0 ? "No" : "Yes");
        }
    }
}


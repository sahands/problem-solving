import java.util.*;

public class Main {
    public static int a, b;

    public static int next(int x) {
        return ( a * x + b) % 10001;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        int[] x = new int[t];
        for(int i =0; i<t; i++ ) {
            x[i] = in.nextInt();
        }

        boolean found = false;
        for(a = 0; a <= 10000 && !found; a++ ){
            for(b = 0; b <= 10000 && !found; b++ ){
                found = true;
                for(int j = 1; j < t; j++) {
                    int y = next(next(x[j-1]));
                    if(y != x[j]){
                        found = false;
                        break;
                    }
                }
                if(found) {
                    for(int j = 0; j < t; j++) {
                        System.out.println(next(x[j]));
                    }
                    return;
                }
            }
        }

    }
}

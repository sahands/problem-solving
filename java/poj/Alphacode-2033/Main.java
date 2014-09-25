import java.util.*;
import java.util.Scanner;

public class Main{
    public static long decodings(String s) {
        char[] c = s.toCharArray();
        long T0 = 1;
        long T1 = 1;
        long T2 = 0;
        long result = T0;
        for(int n = 2; n <= s.length(); n++) {
            if(c[n - 1] != '0') {
                T2 = T1;
            }
            if( c[n-2] == '1' || (c[n-2] == '2' && c[n - 1] <= '6')) {
                T2 += T0;
            }
            T0 = T1;
            T1 = T2;
            result = T2;
            T2 = 0;
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        while(true) {
            String s = in.next();
            if(s.equals("0")) {
                break;
            }
            System.out.println(decodings(s));
        }
    }
}



import java.util.Scanner;

public class Main{
    public static int palindrome(String s) {
        int n = s.length();
        int[] M0 = new int[n];
        int[] M1 = new int[n];
        int[] M2 = new int[n];
        char[] c = s.toCharArray();
        for(int k = 1; k <= n; k++) {
            for(int i = n - 1 - k; i >= 0; i--) {
                if(c[i] == c[i + k]) {
                    M2[i] = M0[i + 1];
                } else {
                    int t1 = M1[i];
                    int t2 = M1[i + 1];
                    int t = t1 < t2 ? t1: t2;
                    M2[i] = t + 1;
                }
            }
            for(int j = 0; j < n; j++) {
                M0[j] = M1[j];
                M1[j] = M2[j];
            }
        }
        return M2[0];
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        in.nextInt();
        String s = in.next();
        System.out.println(palindrome(s));
    }
}

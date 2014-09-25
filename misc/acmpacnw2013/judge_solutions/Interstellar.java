import java.text.DecimalFormat;
import java.util.Scanner;


public class Interstellar {
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    int T = s.nextInt();
    for (int tc = 0; tc < T; tc++) {
    
      int N = s.nextInt();
      int[] arr = new int[N];
      int max = Integer.MIN_VALUE, min = Integer.MAX_VALUE;
      for (int i = 0; i < N; i++) {
        arr[i] = s.nextInt();
        max = Math.max(max, arr[i]);
        min = Math.min(min, arr[i]);
      }
      double mid = ((double) (max + min)) / 2;
      int left = min, right = max;
      for (int loc : arr) {
        if (loc < mid) left = Math.max(left, loc);
        else right = Math.min(right, loc);
      }
      System.out.println(Math.max(left - min, max - right));
    }
  }
}

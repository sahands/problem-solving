import java.util.Scanner;


public class Assignments {
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    int T = s.nextInt();
    for (int tc = 0; tc < T; tc++) {
      int N = s.nextInt(), D = s.nextInt();
      int count = 0;
      for (int i = 0; i < N; i++) {
        if (s.nextInt() * s.nextInt() / s.nextInt() >= D) count++;
      }
      System.out.println(count);
    }
  }
}

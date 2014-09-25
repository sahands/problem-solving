import java.text.DecimalFormat;
import java.util.Scanner;


public class Holodeck {
  static long[] pow10 = new long[19];
  static DecimalFormat[] fmt = new DecimalFormat[19];
  static {
    pow10[0] = 1;
    for (int i = 1; i < 19; i++) pow10[i] = 10 * pow10[i-1];
    String s = "";
    for (int i = 1; i < 19; i++) {
      s += "0";
      fmt[i] = new DecimalFormat(s);
    }
  }
  
  static int count(long total, boolean zeroAllowed, boolean carry, int len) {
    if (len < 3) {
      if (total < 10 && total % 2 == 0 && len == 1) return 1;
      if (total < 20 && total % 2 == 0 && carry) return 1;
      
      if (total < 100) {
        if (total % 10 == total / 10 && (!carry || !zeroAllowed)) {
          return (int) (total % 10) + (zeroAllowed ? 1 : 0);
        }
      }
      return 0;
    }
    
    String s = fmt[len].format(total);
    int first = s.charAt(0) - '0';
    int last = s.charAt(s.length() - 1) - '0';
    
    int ans = 0;
    if (first == last && (!carry || !zeroAllowed)) {
      long middle = Long.parseLong(s.substring(1, len - 1));
      ans += (last + (zeroAllowed ? 1 : 0)) * count(middle, true, false, len - 2);
    } else if (first == last + 1 && (!carry || !zeroAllowed)) {
      long middle = Long.parseLong(s.substring(1, len - 1)) + pow10[len - 2];
      ans += (last + (zeroAllowed ? 1 : 0)) * count(middle, true, true, len - 1);
    }
    
    if (first == 1 && carry) {
      int second = s.charAt(1) - '0';
      if (second == last) {
        if (len > 3) {
          long middle = Long.parseLong(s.substring(2, len - 1)) - 1;
          ans += (9 - last) * count(middle, true, false, len - 3);
        }
      } else if (second == last + 1) {
        if (len > 3) {
          long middle = Long.parseLong(s.substring(2, len - 1)) - 1 + pow10[len - 3];
          if (Long.parseLong(s.substring(2, len - 1)) == 0) {
            ans += (9 - last) * count(middle, true, false, len - 3);
          } else {
            ans += (9 - last) * count(middle, true, true, len - 2);
          }
        } else {
          ans += 9 - last;
        }
      } else if (second == 0 && last == 9) {
        if (len > 3) {
          long middle = Long.parseLong(s.substring(2, len - 1)) + pow10[len - 3];
          ans += (last + (zeroAllowed ? 1 : 0)) * count(middle, true, true, len - 2);
        }
      }
    }
    return ans;
  }
  
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    int T = s.nextInt();
    for (int tc = 0; tc < T; tc++) {
      long Y = s.nextLong();
      String str = Y + "";
      System.out.println(count(Y, false, true, str.length()));
    }
  }
}

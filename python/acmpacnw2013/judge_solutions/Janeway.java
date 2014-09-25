import java.util.* ;
public class Janeway {
   public static double calcang(double x, double y) {
      // clockwise; don't use atan2; always positive
      if (x >= 0) {
         if (y >= 0) // quadrant 1:  y - x ;
            return 2 + y - x ;
         else        // quadrant 4:  x + y
            return 11 + x + y ;
      } else {
         if (y >= 0) // quadrant 2:  - y - x
            return 5 - y - x ;
         else        // quadrant 3:  x - y
            return 8 + x - y ;
      }
   }
   public static void main(String[] args) {
      Scanner sc = new Scanner(System.in) ;
      int kases = sc.nextInt() ;
      for (int kase=1; kase<=kases; kase++) {
         int n = sc.nextInt() ;
         double x[] = new double[n] ;
         double y[] = new double[n] ;
         double r[] = new double[n] ;
         for (int i=0; i<n; i++) {
            double xx = sc.nextDouble() ;
            double yy = sc.nextDouble() ;
            x[i] = xx ;
            y[i] = yy ;
            x[i] = 0.6 * xx + 0.8 * yy ;
            y[i] = 0.6 * yy - 0.8 * xx ;
            r[i] = sc.nextDouble() ;
         }
         int res = 2 ;
         if (res > n)
            res = n ;
         double plus[] = new double[2*n-2] ;
         double minus[] = new double[2*n-2] ;
         for (int i=0; i<n; i++) {
            int at = 0 ;
            int zeroval = 1 ;
            for (int j=0; j<n; j++) {
               if (i == j)
                  continue ;
               double dx = x[j]-x[i] ;
               double dy = y[j]-y[i] ;
               double dist = Math.sqrt(dx*dx+dy*dy) ;
               dx /= dist ;
               dy /= dist ;
               double ev[] = new double[4] ;
               for (int sides=0; sides<4; sides++) {
                  double oneside = ((sides & 2) == 0) ? r[i] : -r[i] ;
                  oneside += ((sides & 1) != 0) ? r[j] : -r[j] ;
                  double sin = oneside / dist ;
                  double cos = Math.sqrt(1-sin*sin) ;
                  double a = dy * cos + dx * sin ;
                  double b = dy * sin - dx * cos ;
                  double ab = Math.sqrt(a*a+b*b) ;
                  if ((sides & 2) != 0)
                     ab = - ab ;
                  a /= ab ;
                  b /= ab ;
                  ev[sides] = calcang(a, b) ;
               }
               plus[at] = ev[0] ;
               plus[at+1] = ev[2] ;
               minus[at] = ev[1] ;
               minus[at+1] = ev[3] ;
               at += 2 ;
               if (ev[1] < ev[0])
                  zeroval++ ;
               if (ev[3] < ev[2])
                  zeroval++ ;
            }
            Arrays.sort(plus) ;
            Arrays.sort(minus) ;
            int ri = zeroval ;
            int atp = 0 ;
            int atm = 0 ;
            int curr = zeroval ;
            while (atp < plus.length) {
               if (atm == minus.length || plus[atp] <= minus[atm]) {
                  curr++ ;
                  atp++ ;
               } else {
                  curr-- ;
                  atm++ ;
               }
               if (curr > ri)
                  ri = curr ;
            }
            if (ri > res)
               res = ri ;
         }
         System.out.println(res) ;
      }
   }
}

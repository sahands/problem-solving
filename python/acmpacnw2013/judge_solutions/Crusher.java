import java.util.* ;
public class Crusher {
   static long index(int[] perm) {
      long r = 0 ;
      int n = perm.length ;
      for (int i=0; i<n; i++)
         r = r * n + perm[i] ;
      return r ;
   }
   static double cost(int[] perm, HashMap<Long, Double> permcost, boolean gap) {
      long v = index(perm) ;
      if (permcost.get(v) != null)
         return permcost.get(v) ;
      int n = perm.length ;
      double r = 0 ;
      double nc = 0 ;
      double good = 0 ;
      double probes = 0 ;
      for (int i=0; i<n; i++) {
         for (int j=0; j<n; j++) {
            if (!gap && j != i+1)
               continue ;
            probes++ ;
            if (perm[i] != perm[j] && (i > j) != (perm[i] > perm[j])) {
               int t = perm[i] ; perm[i] = perm[j] ; perm[j] = t ;
               r += cost(perm, permcost, gap) ;
               t = perm[i] ; perm[i] = perm[j] ; perm[j] = t ;
               good++ ;
            } else {
               nc++ ;
            }
         }
      }
      if (nc == probes)
         r = 0 ;
      else {
         r /= good ;
         r = r + probes / good ;
      }
      permcost.put(v, r) ;
// System.out.println("Cost of " + v + " is " + r) ;
      return r ;
   }
   public static void main(String[] args) throws Exception {
      Scanner sc = new Scanner(System.in) ;
      int kases = sc.nextInt() ;
      for (int kase=1; kase<=kases; kase++) {
         int n = sc.nextInt() ;
         int a[] = new int[n] ;
         int b[] = new int[n] ;
         for (int i=0; i<n; i++) {
            b[i] = sc.nextInt() ;
            boolean matched = false ;
            int hilo = -1 ;
            for (int j=0; j<i; j++)
               if (b[i] == b[j]) {
                  a[i] = a[j] ;
                  matched = true ;
               } else if (b[j] < b[i] && a[j] > hilo)
                  hilo = a[j] ;
            if (!matched) {
               for (int j=0; j<i; j++)
                  if (a[j] > hilo)
                     a[j]++ ;
               a[i] = hilo + 1 ;
            }
         }
         HashMap<Long, Double> hm = new HashMap<Long, Double>() ;
         HashMap<Long, Double> hm2 = new HashMap<Long, Double>() ;
         double test1 = cost(a, hm, true) ; // no gaps allowed
         double test2 = cost(a, hm2, false) ; // can use gap
         System.out.format("Monty %.6f Carlos %.6f", test1, test2) ;
         System.out.println() ;
      }
   }
}

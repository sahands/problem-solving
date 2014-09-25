// Binary search on all-pairs shortest paths.
import java.util.* ;
public class Bones {
   final static long INFINITY = 1000000000000000000L ;
   static void apsp(long[][] dist) {
      int n = dist.length ;
      for (int k=0; k<n; k++)
         for (int i=0; i<n; i++)
            for (int j=0; j<n; j++)
               if (dist[i][k] + dist[k][j] < dist[i][j])
                  dist[i][j] = dist[i][k] + dist[k][j] ;
   }
   static long highval(long[][] dist) {
      int n = dist.length ;
      long r = 0 ;
      for (int i=0; i<n; i++)
         for (int j=0; j<n; j++)
            if (dist[i][j] > r)
               r = dist[i][j] ;
      return r ;
   }
   public static void docase(Scanner scan) throws Exception {
      int n = scan.nextInt() ;
      int k = scan.nextInt() ;
      int nr = scan.nextInt() ;
      long dist[][] = new long[n][n] ;
      for (int i=0; i<n; i++)
         for (int j=0; j<n; j++)
            if (i != j)
               dist[i][j] = INFINITY ;
      for (int i=0; i<nr; i++) {
         int src = scan.nextInt() ;
         int dst = scan.nextInt() ;
         long d = scan.nextLong() ;
         if (src != dst && dist[src][dst] > d)
            dist[src][dst] = dist[dst][src] = d ;
      }
      apsp(dist) ;
      long maxdist = highval(dist) ;
      long gooddist = maxdist ;
      long wd[][] = new long[n][n] ;
      for (int bp=60; bp>=0; bp--) {
         long testdist = gooddist - (1L<<bp) ;
         if (testdist <= 0)
            continue ;
         for (int i=0; i<n; i++)
            for (int j=0; j<n; j++)
               if (i == j)
                  wd[i][j] = 0 ;
               else if (dist[i][j] > testdist)
                  wd[i][j] = INFINITY ;
               else
                  wd[i][j] = 1 ;
         apsp(wd) ;
         if (highval(wd) <= k)
            gooddist = testdist ;
      }
      System.out.println(gooddist) ;
   }
   public static void main(String[] args) throws Exception {
      Scanner scan = new Scanner(System.in) ;
      int kases = scan.nextInt() ;
      for (int kase=1; kase<=kases; kase++)
         docase(scan) ;
   }
}

import java.io.* ;
import java.util.* ;
public class M5 {
   final static long BIG = 1000000000L * 1000000000L ;
   static String[] s2sa(String s) {
      StringTokenizer t=new StringTokenizer(s.trim());
      String[]r=new String[t.countTokens()];
      int i=0;
      while(t.hasMoreTokens())try{
         r[i++]=t.nextToken();
      }catch(Exception e){};
      return r;
   }
   static long[][] mincostflow(long[][] g, long[][] cost) {
      int n = g.length ;
      long[][] flow = new long[n][n] ;
      int prev[] = new int[n] ;
      long min[] = new long[n] ;
      while (true) {
         Arrays.fill(prev, -1) ;
         Arrays.fill(min, BIG) ;
         min[0] = 0 ;
         while (true) {
            boolean changed = false ;
            for (int i=0; i<n; i++)
               for (int j=0; j<n; j++) {
                  if (flow[i][j] < g[i][j] && min[j] > min[i] + cost[i][j]) {
                     changed = true ;
                     min[j] = min[i] + cost[i][j] ;
                     prev[j] = i ;
                  }
               }
            if (!changed)
               break ;
         }
         if (min[n-1] == BIG)
            return flow ;
         long maxflow = BIG ;
         int j ;
         for (int i=n-1; (j=prev[i])>=0; i=j)
            maxflow = Math.min(maxflow, g[j][i] - flow[j][i]) ;
         for (int i=n-1; (j=prev[i])>=0; i=j) {
            flow[j][i] += maxflow ;
            flow[i][j] -= maxflow ;
         }
      }
   }
   public static void main(String[] args) throws Exception {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in)) ;
      int kases = Integer.parseInt(br.readLine()) ;
      for (int kase=1; kase<=kases; kase++)
         doone(br) ;
   }
   public static void doone(BufferedReader br) throws Exception {
      String sf[] = s2sa(br.readLine()) ;
      int M = Integer.parseInt(sf[0]) ;
      int N = Integer.parseInt(sf[1]) ;
      int A = Integer.parseInt(sf[2]) ;
      int B = Integer.parseInt(sf[3]) ;
      int[][] a = new int[M][N] ;
      int[] conf0 = new int[N] ;
      int[] conf1 = new int[N] ;
      String sf0[] = s2sa(br.readLine()) ;
      String sf1[] = s2sa(br.readLine()) ;
      long tot0 = 0, tot1 = 0 ;
      for (int i=0; i<N; i++) {
         conf0[i] = Integer.parseInt(sf0[i]) ;
         conf1[i] = Integer.parseInt(sf1[i]) ;
         tot0 += conf0[i] ;
         tot1 += conf1[i] ;
      }
      if (tot0 != tot1)
         System.out.println("Mismatch " + tot0 + " " + tot1) ;
      for (int i=0; i<M; i++) {
         sf = s2sa(br.readLine()) ;
         for (int j=0; j<N; j++)
            a[i][j] = Integer.parseInt(sf[j]) ;
      }
      int nn = 2 * N + M + 2 ;
      long[][] g = new long[nn][nn] ;
      long[][] cost = new long[nn][nn] ;
      for (int i=0; i<N; i++) {
         g[0][i+1] = A * B * tot1 * conf0[i] ;
         g[i+1+N+M][nn-1] = A * B * tot0 * conf1[i] ;
         for (int j=0; j<M; j++) {
            g[i+1][j+N+1] = BIG ;
            g[j+N+1][i+N+M+1] = BIG ;
            cost[i+1][j+N+1] = A * tot0 * a[j][i] ;
            cost[j+N+1][i+N+M+1] = B * tot1 * a[j][i] ;
            cost[j+N+1][i+1] = - A * tot0 * a[j][i] ;
            cost[i+N+M+1][j+N+1] = - B * tot1 * a[j][i] ;
         }
      }
      long[][] f = mincostflow(g, cost) ;
      long totflow = 0 ;
      long totcost = 0 ;
      for (int i=0; i<nn; i++)
         totflow += f[0][i] ;
      for (int i=0; i<nn; i++)
         for (int j=0; j<nn; j++)
            if (f[i][j] > 0)
               totcost += cost[i][j] * f[i][j] ;
      if (totcost != 0 && totcost % (A*tot0*B*tot1) != 0)
         System.out.println("Not divisible " + totcost + " " + (A*tot0*B*tot1)) ;
      if (totcost != 0)
         totcost /= (A*tot0*B*tot1) ;
      System.out.println(totcost) ;
   }
}

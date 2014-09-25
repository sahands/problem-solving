import java.util.* ;
public class Escape {
   final static int INFINITY = 1000000000 ;
   public static class NodeVal implements Comparable<NodeVal> {
      int i, j ;
      int p ;
      NodeVal(int i_, int j_, int p_) {
         i = i_ ;
         j = j_ ;
         p = p_ ;
      }
      public boolean equals(Object o) {
         if (!(o instanceof NodeVal))
            return false ;
         NodeVal b = (NodeVal)o ;
         return i==b.i && j==b.j && p==b.p ;
      }
      public int compareTo(NodeVal b) {
         if (p < b.p)
            return -1 ;
         if (p > b.p)
            return 1 ;
         if (i < b.i)
            return -1 ;
         if (i > b.i)
            return 1 ;
         if (j < b.j)
            return -1 ;
         if (j > b.j)
            return 1 ;
         return 0 ;
      }
   }
   static int doprob(Scanner sc) throws Exception {
      int cn = sc.nextInt() ;
      int w = sc.nextInt() ;
      int h = sc.nextInt() ;
      int kc[] = new int[256] ;
      int a[][] = new int[h][w] ;
      int p[][] = new int[h][w] ;
      int ei = -1, ej = -1 ;
      TreeSet<NodeVal> ts = new TreeSet<NodeVal>() ;
      for (int i=0; i<cn; i++) {
         String c = sc.next() ;
         kc[c.charAt(0)] = sc.nextInt() ;
      }
      for (int i=0; i<h; i++) {
         char[] classes = sc.next().toCharArray() ;
         for (int j=0; j<w; j++)
            if (classes[j] == 'E') {
               a[i][j] = 1 ;
               p[i][j] = 0 ;
               ei = i ;
               ej = j ;
               ts.add(new NodeVal(i, j, 0)) ;
            } else {
               a[i][j] = kc[classes[j]] ;
               p[i][j] = INFINITY ;
            }
      }
      long iter = 0 ;
      while (ts.size() > 0) {
         iter++ ;
         NodeVal nv = ts.first() ;
         ts.remove(nv) ;
         if (nv.i == 0 || nv.j == 0 || nv.i == h-1 || nv.j == w-1)
            return p[nv.i][nv.j] ;
         if (nv.i > 0 && nv.p + a[nv.i-1][nv.j] < p[nv.i-1][nv.j]) {
            p[nv.i-1][nv.j] = nv.p + a[nv.i-1][nv.j] ;
            ts.add(new NodeVal(nv.i-1, nv.j, p[nv.i-1][nv.j])) ;
         }
         if (nv.j > 0 && nv.p + a[nv.i][nv.j-1] < p[nv.i][nv.j-1]) {
            p[nv.i][nv.j-1] = nv.p + a[nv.i][nv.j-1] ;
            ts.add(new NodeVal(nv.i, nv.j-1, p[nv.i][nv.j-1])) ;
         }
         if (nv.i+1 < h && nv.p + a[nv.i+1][nv.j] < p[nv.i+1][nv.j]) {
            p[nv.i+1][nv.j] = nv.p + a[nv.i+1][nv.j] ;
            ts.add(new NodeVal(nv.i+1, nv.j, p[nv.i+1][nv.j])) ;
         }
         if (nv.j+1 < w && nv.p + a[nv.i][nv.j+1] < p[nv.i][nv.j+1]) {
            p[nv.i][nv.j+1] = nv.p + a[nv.i][nv.j+1] ;
            ts.add(new NodeVal(nv.i, nv.j+1, p[nv.i][nv.j+1])) ;
         }
      }
      return -1 ;
   }
   static public void main(String[] args) throws Exception {
      Scanner sc = new Scanner(System.in);
      int kases = sc.nextInt() ;
      for (int kase=1; kase<=kases; kase++)
         System.out.println(doprob(sc)) ;
   }
}

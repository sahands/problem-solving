import java.util.*;

class Edge implements Comparable<Edge> {
    public int s;
    public int t;
    public int w;
    public int compareTo(Edge e) {
        return this.w - e.w;
    }
}

class Set {
    public int[] S;
    public int n;

    public Set(int n) {
        this.n = n;
        this.S = new int[n];
        for(int i =0; i < n;i ++ ){
            this.S[i] = i;
        }
    }

    public int find(int x) {
        if(S[x] == x) {
            return x;
        }
        int y = find(S[x]);
        S[x] = y;
        return y;
    }

    public void union(int x, int y) {
        int p1 = find(x);
        int p2 = find(y);
        S[p1] = p2;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        Edge[] E = new Edge[m];
        Set S = new Set(n);

        for(int i = 0; i < m ; i ++ ){
            int v, u, w;
            v = in.nextInt();
            u = in.nextInt();
            w = in.nextInt();
            E[i] = new Edge();
            E[i].t = u - 1;
            E[i].s = v - 1;
            E[i].w = w;
        }

        Arrays.sort(E);

        int max = -1;
        for(Edge e : E) {
            int sp = S.find(e.s);
            int tp = S.find(e.t);
            if(sp != tp) {
                max = Math.max(max, e.w);
                /* System.out.println("" + e.s + " - " + e.t); */
                S.union(sp, tp);
            }
        }
        System.out.println(max);
    }
}

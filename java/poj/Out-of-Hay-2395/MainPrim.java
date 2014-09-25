import java.util.*;

class Edge implements Comparable<Edge> {
    public int s;
    public int t;
    public int w;

    public int compareTo(Edge e) {
        return this.w - e.w;
    }

    public Edge dual() {
        Edge e = new Edge();
        e.s = this.t;
        e.t = this.s;
        e.w = this.w;
        return e;
    }
}

class Vertex {
    LinkedList<Edge> A;
    public Vertex() {
        A = new LinkedList<Edge>();
    }
}

public class MainPrim {
    public static void scan(PriorityQueue<Edge> Q, Edge[] E, Vertex[] V, boolean[] seen, int v) {
        if(!seen[v]) {
            for(Edge e : V[v].A) {
                if(!seen[e.t]) {
                    Q.add(e);
                }
            }
            seen[v] = true;
        }
    }

    public static LinkedList<Edge> mst(Edge[] E, Vertex[] V, int n, int m, int s) {
        LinkedList<Edge> T = new LinkedList<Edge>();
        PriorityQueue<Edge> Q = new PriorityQueue<Edge>();
        boolean[] seen = new boolean[n];
        scan(Q, E, V, seen, s);

        while(!Q.isEmpty()) {
            Edge e = Q.poll();
            if(!seen[e.t]) {
                T.add(e);
                scan(Q, E, V, seen, e.s);
                scan(Q, E, V, seen, e.t);
            }
        }

        return T;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        Edge[] E = new Edge[m];
        Vertex[] V = new Vertex[n];
        for(int i =0; i < n;i++) {
            V[i] = new Vertex();
        }

        for(int i = 0; i < m ; i ++ ){
            int v, u, w;
            v = in.nextInt() - 1;
            u = in.nextInt() - 1;
            w = in.nextInt();
            E[i] = new Edge();
            E[i].t = u;
            E[i].s = v;
            E[i].w = w;
            V[v].A.add(E[i]);
            V[u].A.add(E[i].dual());
        }

        int max = -1;
        LinkedList<Edge> T = mst(E, V, n, m, 0);
        for(Edge e : T) {
            max = Math.max(max, e.w);
            /* System.out.println("" + e.s + " - " + e.t); */
        }
        System.out.println(max);
    }
}

import java.util.*;

class Edge {
    public int source, target;
    public int weight = 0;
    public Edge(int s, int t) {
        source = s;
        target = t;
    }

    public int calculateWeight(Vertex[] V) {
        if(weight > 0) {
            return weight;
        }
        weight = 1;
        for(Edge e: V[target].edges) {
            if(e.target != source) {
                weight += e.calculateWeight(V);
            }
        }
        /* System.out.println("Edge weight(" + source + ", " + target + ") = " + weight); */
        return weight;
    }
}

class Vertex {
    public LinkedList<Edge> edges = new LinkedList<Edge>();
    private int _balance = -1;
    public int balance() {
        if(_balance >= 0) {
            return _balance;
        }
        for(Edge e : edges) {
            _balance = _balance > e.weight ? _balance : e.weight;
        }
        return _balance;
    }
}


public class Main {
    public static void process(Vertex[] V, LinkedList<Edge> Q, int n) {
        while(Q.size() > 0) {
            Edge e = Q.pop();
            if(e.weight == 0) {
                e.calculateWeight(V);
            }
        }

        int best = 1;
        for(int i = 2; i<= n; i++) {
            if(V[i].balance() < V[best].balance()) {
                best = i;
            }
        }
        System.out.println("" + best + " " + V[best].balance());
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int T = in.nextInt();
        for(int t = 0; t < T ; t ++) {
            int n = in.nextInt();
            Vertex[] V = new Vertex[n + 1];
            LinkedList<Edge> Q = new LinkedList<Edge>();
            for(int i = 0; i < n - 1 ; i++)  {
                int u = in.nextInt();
                int v = in.nextInt();
                if(V[u] == null) V[u] = new Vertex();
                if(V[v] == null) V[v] = new Vertex();
                Edge e1 = new Edge(u, v);
                Edge e2 = new Edge(v, u);
                V[u].edges.add(e1);
                V[v].edges.add(e2);
                Q.add(e1);
                Q.add(e2);
            }
            process(V, Q, n);
        }
    }
}

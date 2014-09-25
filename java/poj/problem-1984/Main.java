import java.util.*;
import java.util.Scanner;

class Edge {
    public int source;
    public int target;
    public int length;
    public int dx, dy;

    public Edge dual() {
        Edge ee = new Edge();
        ee.target = source;
        ee.source = target;
        ee.length = length;
        ee.dx = -dx;
        ee.dy = -dy;
        return ee;
    }
}

class Node {
    public LinkedList<Edge> edges = new LinkedList<Edge>();
    public boolean seen = false;
    public int x;
    public int y;

    public int manhattanDist(Node n) {
        return Math.abs(n.x - x) + Math.abs(n.y - y);
    }
}

public class Main {
    public static int current_q_i = 0;

    public static int find(int[] S, int x) {
        if(S[x] == x) return x;
        int p = find(S, S[x]);
        S[x] = p;
        return p;
    }

    public static void union(int[] S, int x, int y) {
        int p1 = find(S, x);
        int p2 = find(S, y);
        S[p1] = p2;
    }

    public static void calculateCoordinates(Node[] nodes) {
        LinkedList<Node> Q = new LinkedList<Node>();
        Q.add(nodes[1]);
        while(Q.size() > 0) {
            Node v = Q.poll();
            v.seen = true;
            for(Edge e : v.edges) {
                Node t = nodes[e.target];
                if(!t.seen) {
                    Q.add(t);
                    t.x = v.x + e.dx * e.length;
                    t.y = v.y + e.dy * e.length;
                }
            }
        }
    }

    public static int query(Node[] nodes, Edge[] E, int[] S, int source, int target, int k) {
        for(int i = current_q_i; i < k; i++ ) {
            union(S, E[i].source, E[i].target);
        }
        current_q_i = k;
        if(find(S, source) != find(S, target)) {
            return -1;
        }
        return nodes[source].manhattanDist(nodes[target]);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int N, M;

        N = in.nextInt();
        M = in.nextInt();

        Node[] nodes = new Node[N + 1];
        Edge[] E = new Edge[N];
        int[] S = new int[N + 1];

        for(int i = 1; i <= N; i++) {
            S[i] = i;
            nodes[i] = new Node();
        }

        for(int i = 0; i < M; i++ ){
            Edge e = new Edge();
            e.source = in.nextInt();
            e.target = in.nextInt();
            e.length = in.nextInt();
            E[i] = e;
            char dir = in.next().charAt(0);
            e.dx = dir == 'E'? 1 : ( dir == 'W'? -1 : 0);
            e.dy = dir == 'N'? 1 : ( dir == 'S'? -1 : 0);
            nodes[e.source].edges.add(e);
            nodes[e.target].edges.add(e.dual());
        }

        calculateCoordinates(nodes);

        int K = in.nextInt();
        for(int i = 0; i < K; i++ ){
            int d = query(nodes, E, S, in.nextInt(), in.nextInt(), in.nextInt());
            System.out.println(d);
        }
    }
}


import java.util.*;

class Adj extends ArrayList<LinkedList<Edge>> {
    public Adj(int m) {
        super(m);
        for(int i = 0; i < m; i ++) {
            this.add(new LinkedList<Edge>());
        }
    }

    public void addEdge(int u, int v, int c) {
        Edge e = new Edge(u, v, 0, c);
        this.get(u).add(e);
        this.get(v).add(e.dual());
    }
}

class Edge {
    public int u, v, f, c;
    private Edge d;

    public Edge dual() {
        if(d == null) {
            d = new Edge(v, u, 0, 0);
        }
        return d;
    }

    public Edge(int from, int to, int flow, int capacity) {
        this.u = from;
        this.v = to;
        this.f = flow;
        this.c = capacity;
    }
}

public class Main {
    static int bfs(Adj A, int source, int target) {
        int m = A.size();
        Edge[] path = new Edge[m];
        boolean[] seen = new boolean[m];
        Queue<Integer> Q = new LinkedList<Integer>();
        Q.add(source);
        while(!Q.isEmpty()) {
            int u = Q.remove();
            if(u == target) {
                break;
            }
            seen[u] = true;
            for(Edge e : A.get(u)) {
                if(e.c > 0 && !seen[e.v]) {
                    path[e.v] = e;
                    Q.add(e.v);
                }
            }
        }
        if(path[target] != null) {
            int min_capacity = Integer.MAX_VALUE;
            Edge e = path[target];
            // Find the minimum capacity on the path
            while(e != null ) {
                min_capacity = Math.min(min_capacity, e.c);
                e = path[e.u];
            }

            // Update the flow and capacities
            e = path[target];
            while(e != null ) {
                e.f += min_capacity;
                e.c -= min_capacity;
                e.dual().c += min_capacity;
                e = path[e.u];
            }

            return min_capacity;
        }
        return 0;
    }

    static int maxFlow(Adj A, int source, int target) {
        int max_flow = 0;
        while(true) {
            int flow = bfs(A, source, target);
            max_flow += flow;
            if(flow == 0) {
                return max_flow;
            }
        }
    }


    static void processCase(Scanner in) {
        int n = in.nextInt(); // Cows
        int m = in.nextInt(); // Stalls
        Adj A = new Adj(2 + m + n);
        int source = 0;
        int target = m + n + 1;

        for(int u = 1 + n; u < target; u ++) {
            A.addEdge(u, target, 1);
        }
        for(int u = 1; u <= n; u ++) {
            A.addEdge(source, u, 1);
            int k = in.nextInt(); // number of edges
            for(int j = 0; j < k; j ++) {
                int v = n + in.nextInt();
                A.addEdge(u, v, 1);
            }
        }
        System.out.println(maxFlow(A, source, target));
    }

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
        while(in.hasNext()) {
            processCase(in);
        }
	}
}



import java.util.*;

class Adj extends ArrayList<LinkedList<Edge>> {
    public Adj(int m) {
        super(m);
        for(int i = 0; i < m; i ++) {
            this.add(new LinkedList<Edge>());
        }
    }

    public void addEdge(int u, int v, int c, int cost) {
        Edge e = new Edge(u, v, c, cost);
        this.get(u).add(e);
        this.get(v).add(e.dual());
    }
}

class Edge {
    public int u, v, f, c;
    public int cost;
    private Edge d;

    public Edge dual() {
        if(d == null) {
            d = new Edge(v, u, 0, this.cost);
        }
        return d;
    }

    public Edge(int from, int to, int capacity, int cost) {
        this.u = from;
        this.v = to;
        this.f = 0;
        this.c = capacity;
        this.cost = cost;
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

    static int maxFlowMinCost(Adj A, int source, int target) {
        int max_flow = 0;
        int min_cost = 0;
        while(true) {
            int flow = bfs(A, source, target);
            max_flow += flow;
            if(flow == 0) {
                break;
            }
        }


        /* return min_cost; */
        return max_flow;
    }


    static void bellmanFord(Adj A, int source, int target) {
        int n = A.size();
        for(int i = 1; i < n; i++ ) {
            for(
        }
    }

    static void processCase(Scanner in) {
        int k = in.nextInt();  // milking machines
        int c = in.nextInt();  // cows
        int m = in.nextInt();  // maximum capacity of milking machines
        int n = k + c + 2;
        int source = 0;
        int target = n - 1;

        Adj A = new Adj(n);
        for(int u = 1; u <= k; u ++ ) {
            A.addEdge(u, target, m, 0);
        }

        for(int u = k + 1; u < target; u ++ ) {
            A.addEdge(source, u, 1, 0);
        }

        for(int u = 1; u < target; u ++) {
            for(int v = 1; v < target; v ++) {
                int cost = in.nextInt();
                /* System.out.print("" + cost + " "); */
                // Symmetric matrix. Ignore the bottom left half.
                if(v > u) {
                    Edge e = new Edge(u, v, 20000, cost);
                    e.dual().c = 1;
                    A.get(u).add(e);
                    A.get(v).add(e.dual());
                }
            }
            /* System.out.println(); */
        }
        System.out.println(maxFlowMinCost(A, source, target));
    }

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
        while(in.hasNext()) {
            processCase(in);
        }
	}
}



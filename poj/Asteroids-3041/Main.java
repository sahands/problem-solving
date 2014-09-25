import java.util.*;


class List extends LinkedList<Integer> {}


public class Main {
    static final int INF = Integer.MAX_VALUE;
    static int n;
    static List[] Adj;
    static int[] PG1;
    static int[] PG2;
    static int[] D;

    public static boolean bfs () {
        List Q = new List();
        for(int v = 1; v <= n; v++) {
            if(PG1[v] == 0 ) {
                D[v] = 0;
                Q.add(v);
            }
            else {
                D[v] = INF;
            }
        }
        D[0] = INF;
        while(!Q.isEmpty()) {
            int v = Q.poll();
            if(D[v] < D[0]) {
                for(int u : Adj[v]) {
                    if(D[PG2[u]] == INF) {
                        D[PG2[u]] = D[v] + 1;
                        Q.add(PG2[u]);
                    }
                }
            }
        }
        return D[0] != INF;
    }

    public static boolean dfs (int v) {
        if(v != 0) {
            for(int u : Adj[v]) {
                if(D[PG2[u]] == D[v] + 1) {
                    if(dfs(PG2[u])) {
                        PG2[u] = v;
                        PG1[v] = u;
                        return true;
                    }
                }
            }
            D[v] = INF;
            return false;
        }
        return true;
    }

    public static int hopcroftKarp(int n, List[] Adj) {
        PG1 = new int[2 * n + 1];
        PG2 = new int[2 * n + 1];
        D = new int[2 * n + 1];
        int matching = 0;
        while(bfs()) {
            for(int v = 1; v <= n; v++) {
                if(PG1[v] == 0) {
                    if(dfs(v)) {
                        matching ++;
                    }
                }
            }
        }
        return matching;
    }


    public static void processTestCase() {
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        int k = in.nextInt();
        int N = 2 * n + 1;
        Adj = new List[N];
        for(int i = 0; i < N; i++) {
            Adj[i] = new List();
        }
        for(int i = 0; i < k; i ++) {
            int x = in.nextInt();
            int y = in.nextInt();
            y += n;  // nodes 1...n represent the rows, n+1...2n the cols
            Adj[x].add(y);
            Adj[y].add(x);
        }

        System.out.println(hopcroftKarp(n, Adj));
    }


    public static void main(String[] args) {
        processTestCase();
    }
}



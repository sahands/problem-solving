import java.util.*;


class List extends LinkedList<Integer> {}


public class Main {
    static List dog_lovers;
    static List cat_lovers;
    static final int INF = Integer.MAX_VALUE;
    static int n;
    static List[] Adj;
    static int[] PA;
    static int[] PB;
    static int[] D;

    public static boolean bfs () {
        List Q = new List();
        for(int v : dog_lovers) {
            if(PA[v] == 0 ) {
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
                    if(D[PB[u]] == INF) {
                        D[PB[u]] = D[v] + 1;
                        Q.add(PB[u]);
                    }
                }
            }
        }
        return D[0] != INF;
    }

    public static boolean dfs (int v) {
        if(v != 0) {
            for(int u : Adj[v]) {
                if(D[PB[u]] == D[v] + 1) {
                    if(dfs(PB[u])) {
                        PB[u] = v;
                        PA[v] = u;
                        return true;
                    }
                }
            }
            D[v] = INF;
            return false;
        }
        return true;
    }

    // Returns size of maximum matching for bipartite
    // graph of the voters
    public static int hopcroftKarp(int V) {
        PA = new int[V + 1];
        PB = new int[V + 1];
        D = new int[V + 1];
        int matching = 0;
        while(bfs()) {
            for(int u : dog_lovers) {
                if(PA[u] == 0) {
                    if(dfs(u)) {
                        matching ++;
                    }
                }
            }
        }
        /* System.out.println("Matching = " + matching); */
        return matching;
    }


    public static void processTestCase(Scanner in) throws Exception {
        int c = in.nextInt();
        int d = in.nextInt();
        int V = in.nextInt();  // number of voters
        // Reserve vertex 0 for Hopcroft-Karp
        int[] votes_against = new int[V + 1];
        int[] votes_for = new int[V + 1];
        dog_lovers = new List();
        cat_lovers = new List();
        Adj = new List[V + 1];

        for(int i = 0; i <= V; i++) {

            Adj[i] = new List();
        }

        for(int i = 1; i <= V; i ++) {
            String a, b;
            a = in.next();
            b = in.next();
            char c1 = a.charAt(0);
            int x = Integer.parseInt(a.substring(1));
            int y = Integer.parseInt(b.substring(1));
            if(c1 == 'D') {
                /* System.out.println("" + i + " is a dog lover."); */
                dog_lovers.add(i);
            } else if(c1 == 'C') {
                /* System.out.println("" + i + " is a cat lover."); */
                cat_lovers.add(i);
            }

            votes_for[i] = x;
            votes_against[i] = y;
            /* System.out.println("" + i + " votes for " + votes_for[i]); */
            /* System.out.println("" + i + " votes against " + votes_against[i]); */
        }

        // Poor dogs...
        if(dog_lovers.size() == 0) {
            System.out.println(V);
            return;
        }

        // Good.... GOOOD... :)
        if(cat_lovers.size() == 0) {
            System.out.println(V);
            return;
        }


        // Let's build the bipartite graph
        // Connect a dog lover to a cat lover iff their votes conflict
        // Meaning we can't not make both of them happy
        for(int dog_lover : dog_lovers) {
            for(int cat_lover : cat_lovers) {
                /* System.out.println("Checking " + dog_lover + " and " + cat_lover); */
                /* System.out.println("" + dog_lover + " votes for " + votes_for[dog_lover]); */
                /* System.out.println("" + dog_lover + " votes against " + votes_against[dog_lover]); */
                /* System.out.println("" + cat_lover + " votes for " + votes_for[cat_lover]); */
                /* System.out.println("" + cat_lover + " votes against " + votes_against[cat_lover]); */
                if(votes_for[dog_lover] == votes_against[cat_lover] ||
                   votes_for[cat_lover] == votes_against[dog_lover]) {
                    Adj[dog_lover].add(cat_lover);
                    Adj[cat_lover].add(dog_lover);
                    /* System.out.println("Adding edge between " + dog_lover + " and " + cat_lover); */
                }
            }
        }

        // By Konig's theorem the size of the maximum matching is the same
        // as minimum cover. We need maximal independent set so v - max_matching
        // is the answer.
        System.out.println(V - hopcroftKarp(V));
    }


    public static void main(String[] args) throws Exception {
        Scanner in = new Scanner(System.in);
        int t;
        t = in.nextInt();
        for(int i = 0; i < t; i ++) {
            processTestCase(in);
        }
    }
}

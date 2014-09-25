import java.io.*;
import java.util.*;

class Edge {
  public int from;
  public int to;
  public long time;

  public Edge(int from, int to, long time) {
    this.from = from;
    this.to = to;
    this.time = time;
  }
}

public class DeltaQuadrant {

  /**
   * recurse()
   *
   * @param edges -- a list of edges
   * @param prev -- identity of the parent node (to prevent back recursion)
   * @param from -- identity of the current node
   * @param counts -- counts[i] = number of nodes in the subtree beneath i
   * @param totals -- totals[i] = weight of subtree beneath i
   * @param weights -- weights[i][k] = max possible weight trimmed by omitting
   *                   exactly k edges from the subtree beneath i
   *
   * For counts[], i is included.  For weights[][], i is assumed to be
   * retained.
   */
  public static void recurse(
    ArrayList<ArrayList<Edge> > edges,
    int prev,
    int from,
    int[] counts,
    long[] totals,
    long[][] weights
  ) {
    counts[from] = 1;
    totals[from] = 0;
    for (Edge e : edges.get(from)) {
      if (e.to == prev) continue;
      recurse(edges, from, e.to, counts, totals, weights);
      counts[from] += counts[e.to];
      totals[from] += totals[e.to] + e.time;
      long[] next = new long[weights[0].length];
      for (int j = 0; j < weights[e.to].length; j++)
        for (int k = j; k < next.length; k++)
          next[k] = Math.max(next[k], weights[from][k - j] + weights[e.to][j]);
      for (int k = counts[e.to]; k < next.length; k++)
        next[k] = Math.max(
          next[k],
          weights[from][k - counts[e.to]] + totals[e.to] + e.time
        );
      long[] temp = next;
      next = weights[from];
      weights[from] = temp;
    }
  }

  public static long solve(ArrayList<ArrayList<Edge> > edges, int k) {
    int n = edges.size();
    long result = 0;
    for (int from = 0; from < Math.min(n, k + 1); from++) {
      int[] counts = new int[n];
      long[] totals = new long[n];
      long[][] weights = new long[n][k + 1];
      recurse(edges, -1, from, counts, totals, weights);
      result = Math.max(result, weights[from][k]);
    }
    return result;
  }

  public static void main(String[] args) throws Exception {
    Scanner scanner = new Scanner(System.in);
    int numProblems = scanner.nextInt();
    for (int i = 0; i < numProblems; i++) {
      int n = scanner.nextInt();
      int k = scanner.nextInt();
      long sum = 0;
      ArrayList<ArrayList<Edge> > edges =
        new ArrayList<ArrayList<Edge> >();
      for (int j = 0; j < n; j++)
        edges.add(new ArrayList<Edge>());
      for (int j = 0; j < n - 1; j++) {
        int from = scanner.nextInt();
        int to = scanner.nextInt();
        long time = scanner.nextLong();
        sum += time;
        edges.get(from).add(new Edge(from, to, time));
        edges.get(to).add(new Edge(to, from, time));
      }
      System.out.println(2 * (sum - solve(edges, k)));
    }
  }
}

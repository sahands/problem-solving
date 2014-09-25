import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;
import java.util.Set;


public class Klingons {
  static class Node {
    final int label;
    final List<Node> children = new LinkedList<Node>();
    int size = 1;
    boolean hashCached = false;
    int hashCache = 0;
    
    public Node(int label) {this.label = label;}
    
    public int computeSize() {
      for (Node n : children) size += n.computeSize();
      return size;
    }
    
    public void addAllSubtreesTo(Set<Node> set) {
      if (!set.contains(this)) {
        set.add(this);
        for (Node n : children) n.addAllSubtreesTo(set);
      }
    }

    @Override
    public int hashCode() {
      if (hashCached) return hashCache;
      hashCached = true;
      final int prime = 31;
      int result = 1;
      result = prime * result + children.hashCode();
      result = prime * result + label;
      result = prime * result + size;
      return hashCache = result;
    }

    @Override
    public boolean equals(Object obj) {
      if (this == obj)
        return true;
      if (obj == null)
        return false;
      if (getClass() != obj.getClass())
        return false;
      if (hashCode() != obj.hashCode())
        return false;
      Node other = (Node) obj;
      if (label != other.label)
        return false;
      if (size != other.size)
        return false;
      if (!children.equals(other.children))
        return false;
      return true;
    }
    
  }
  
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    int T = s.nextInt();
    for (int tc = 0; tc < T; tc++) {
      int M = s.nextInt(), N = s.nextInt();
      Node[] treeA = new Node[M], treeB = new Node[N];
      for (int i = 0; i < M; i++) {
        treeA[i] = new Node(s.next().charAt(0) - 'A');
        int parent = s.nextInt();
        if (parent != -1) treeA[parent].children.add(treeA[i]);
      }
      for (int i = 0; i < N; i++) {
        treeB[i] = new Node(s.next().charAt(0) - 'A');
        int parent = s.nextInt();
        if (parent != -1) treeB[parent].children.add(treeB[i]);
      }
      treeA[0].computeSize();
      treeB[0].computeSize();
      treeA[0].hashCode();
      treeB[0].hashCode();
      HashSet<Node> setA = new HashSet<Node>();
      treeA[0].addAllSubtreesTo(setA);
      Arrays.sort(treeB, new Comparator<Node> () {
        public int compare(Node a, Node b) {
          return b.size - a.size;
        }
      });
      boolean found = false;
      for (Node n : treeB) {
        if (setA.contains(n)) {
          System.out.println(n.size);
          found = true;
          break;
        }
      }
      if (!found) System.out.println(0);
    }
  }
}

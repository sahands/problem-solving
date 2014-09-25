import java.util.*;

class Node {
    public Node left, right;
    public int w;
    public int depth;

    public Node(int w) {
        this.w = w;
        this.depth = 0;
    }

    public int weight() {
        if(this.left == null || this.right == null) {
            return this.w;
        }
        else {
            return this.left.weight() + this.right.weight();
        }
    }


    public static int i = 0;

    public static Node parse(String s, LinkedList<Node> leaves) {
        i = 0;
        return _parse(s, 0, leaves);
    }

    private static Node _parse(String s, int depth, LinkedList<Node> leaves) {
        // Skips all the checks... assumes input is well-formed
        if(s.charAt(i) == '[') {
            i++; // consume the [
            Node n = new Node(0);
            n.left = _parse(s, depth + 1, leaves);
            i++; // consume the ,
            n.right = _parse(s, depth + 1, leaves);
            i++; // consume the ]
            n.depth = depth;
            return n;
        } else {
            int w = 0;
            String num = "";
            while(i < s.length() && Character.isDigit(s.charAt(i))) {
                num += s.charAt(i);
                i++;
            }

            Node n = new Node(Integer.parseInt(num));
            n.depth = depth;
            leaves.add(n);
            return n;
        }
    }
}

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int j = 0; j < t; j ++) {
            String s = in.next();
            LinkedList<Node> leaves = new LinkedList<Node>();
            Node root = Node.parse(s, leaves);
            HashMap<Long, Integer> M = new HashMap<Long, Integer>();
            int max = -1;
            for(Node leaf : leaves) {
                long uses = 1 <<  leaf.depth; // 2 ^ d
                long key = leaf.w * uses;
                if(M.containsKey(key)) {
                    int count = M.get(key) + 1;
                    M.put(key, count);
                } else {
                    M.put(key, 1);
                }
                max = Math.max(M.get(key), max);
            }
            System.out.println(leaves.size() - max);
        }
    }
}

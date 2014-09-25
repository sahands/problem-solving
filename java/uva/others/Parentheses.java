import java.util.Scanner;

public class Parentheses {
    public static int currentIndex = 0;

    public static boolean matches(char c1, char c2) {
        if(c1 == '[') {
            return c2 == ']';
        } else if(c1 == '(') {
            return c2 == ')';
        }
        return false;
    }

    public static boolean isBalanced(char[] p, int depth) {
        //System.out.println(depth);
        if(p.length <= currentIndex) {
            return true;
        }

        char c = p[currentIndex];
        if(c == ']' || c==')') {
            return depth>0;
        }
        currentIndex++;
        if(!isBalanced(p, depth+1)) {
            return false;
        }
        if(currentIndex >= p.length || !matches(c, p[currentIndex])) {
            return false;
        }
        currentIndex++;
        return isBalanced(p, depth);
    }
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String firstLine = in.nextLine(); // Get rid of the first line with number of inputs in it.
        int n = Integer.parseInt(firstLine);
        int i = 0;
        while(i<n && in.hasNext()) {
            String line = in.nextLine();
            currentIndex = 0;
            System.out.println(isBalanced(line.toCharArray(), 0) ? "Yes" : "No");
            i++;
        }
    }
}

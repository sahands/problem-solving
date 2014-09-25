import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        while(in.hasNext()) {
            int x = in.nextInt();
            int y = in.nextInt();
            if(x == 0 && y == 0) {
                break;
            }
            int a = Math.max(x, y);
            int b = Math.min(x, y);

            // The basic idea is that the game reduces to k piles, with pile
            // x_k = floor(a_k / b_k) players take turns taking r or more from
            // piles, in order: pile k needs to be emptied before pile k+1 is.
            // So the winning strategy is the following: if there is only one
            // item in the leading pile, then the player has no choice. If
            // there is more than one, then the player can determine who gets
            // to the next pile with more than 1 item in it, and can hence win.
            // So basically, the first person to get to a pile with more than 1
            // item in it wins. If there is only one pile with one item in it,
            // first player wins.
            int c = 1;
            while(b > 0) {
                int q = a / b;
                int r = a % b;
                a = b;
                if(q == 1) {
                    c++;
                }else {
                    c ++;
                    break;
                }
                a = b;
                b = r;
            }
            if(c % 2 == 0 ) {
                System.out.println("Stan wins");
            } else {
                System.out.println("Ollie wins");
            }
        }
    }
}


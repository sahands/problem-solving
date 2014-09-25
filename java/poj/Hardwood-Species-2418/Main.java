import java.util.*;
import java.util.Scanner;

public class Main{

    public static void main(String[] args) {
        TreeMap<String, Integer> m = new TreeMap<String, Integer>();
        Scanner in = new Scanner(System.in);
        int count = 0;
        while(in.hasNext()){
            String x = in.nextLine();
            count++;
            Integer v = m.get(x);
            if(v == null) {
                m.put(x, 1);
            } else {
                m.put(x, v + 1);
            }
        }

        for(String k : m.keySet()) {
            System.out.format("%s %.4f\n", k, 100.0 * m.get(k)/count);
        }
    }
}

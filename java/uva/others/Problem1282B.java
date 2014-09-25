import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
 
class Problem1282B {
    static String[] prefix = new String[102];
    static String[] sufix = new String[102];
    static long[] ans = new long[102];
    static char[] pattern;
    static char[] text;
    static int[] f = new int[100005];
    static int n, m;
 
    static void kmpProcess() {
        int i = 0, j;
        j = f[0] = -1;
 
        while (i < m) {
            while (j >= 0 && pattern[i] != pattern[j])
                j = f[j];
            i++;
            j++;
            f[i] = j;
        }
    }
 
    static int kmpSerach() {
        int res = 0;
        int i = 0, j = 0;
        n = text.length;
 
        while (i < n) {
            while (j >= 0 && text[i] != pattern[j])
                j = f[j];
            i++;
            j++;
            if (j == m) {
                res++;
                j = f[j];
            }
        }
        return res;
    }
 
    static void makePrefix(int i) {
        prefix[i] = prefix[i - 1];
        int remaining = m - 1 - prefix[i].length();
        if (remaining > 0) {
            int last = remaining > prefix[i - 2].length() ? prefix[i - 2]
                    .length() : remaining;
            prefix[i] += prefix[i - 2].substring(0, last);
        }
    }
 
    static void makeSufix(int i) {
        sufix[i] = sufix[i - 2];
        int remaining = m - 1 - sufix[i].length();
 
        if (remaining > 0) {
            int first = remaining > prefix[i - 1].length() ? 0 : prefix[i - 1]
                    .length() - remaining;
            sufix[i] = sufix[i - 1].substring(first) + sufix[i];
        }
    }
 
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder out = new StringBuilder();
        String l;
        prefix[0] = sufix[0] = "0";
        prefix[1] = sufix[1] = "1";
        int c = 1;
        while ((l = br.readLine()) != null) {
            Arrays.fill(ans, 0);
            int N = Integer.parseInt(l);
            pattern = br.readLine().toCharArray();
            m = pattern.length;
            kmpProcess();
            if (pattern.length == 1)
                ans[pattern[0] - '0']++;
            int i = 2;
            while (i <= N) {
                ans[i] = ans[i - 1] + ans[i - 2];
                if (m > 1) {
                    makePrefix(i);
                    makeSufix(i);
                    text = (sufix[i - 1] + prefix[i - 2]).toCharArray();
                    ans[i] += kmpSerach();
                }
                i++;
            }
            out.append("Case " + c++ + ": " + ans[N] + "\n");
        }
        System.out.print(out);
    }
 
}

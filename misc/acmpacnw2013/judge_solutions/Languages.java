import java.util.* ;
import java.io.* ;
public class Languages {

    static Hashtable<String, String> lexicon = new Hashtable<String, String>() ;

    public static void addLanguage(String line) {

        String[] words = line.split(" ");

        String language = words[0];

        for( int i = 1; i < words.length; i++)

            lexicon.put(words[i].toLowerCase(), language);

    }


    public static String getLanguageFromText(String text) {

        String[] words = text.toLowerCase().split("[^a-z\\-\\']+");

        for( int i = 0; i < words.length; i++ )

            if( lexicon.containsKey(words[i]))

                return lexicon.get(words[i]);

        return null;

    }

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)) ;
        int langs = Integer.parseInt(br.readLine()) ;
        for (int i=0; i<langs; i++)
           addLanguage(br.readLine()) ;
        br.readLine() ;
        while (true) {
           String s = br.readLine() ;
           if (s == null)
              break ;
           System.out.println(getLanguageFromText(s)) ;
        }
    }

}

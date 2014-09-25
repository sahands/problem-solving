import java.util.Scanner;

public class Generations
{
   public static void main(String [] args) throws Exception
   {
            
      int cases, n;
      
      Scanner in = new Scanner(System.in);
      cases = in.nextInt();
      
      while (cases > 0)
      {
         long tribn_4 = 1, tribn_3 = 1, tribn_2 = 2, tribn_1 = 4;
         long tribn = 0;

         n = in.nextInt();
         
         if (n < 2)
            System.out.println(1);
         else if (n == 2)
            System.out.println(2);
         else if (n == 3)
            System.out.println(4);
         else
         {
            for (int i = 4; i <= n; i++)
            {
               tribn = tribn_1 + tribn_2 + tribn_3 + tribn_4;
               tribn_4 = tribn_3;
               tribn_3 = tribn_2;
               tribn_2 = tribn_1;
               tribn_1 = tribn;
            
            
            }//end for
            System.out.println(tribn);
               
         }//end else
         cases--;
      
      }//end while
        
      
      
   
   
   }//end main


}//end class tribbles

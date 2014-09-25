/*
   PacNW 2013 Regional
   Easy/Gimme problem
   
   Determine whether or not a positive integer 2 < p < 100,000
   is a perfect number.  A number is perfect if the sum of its
   divisors add up to the value of the number itself. Example:
   
   6 = 1 + 2 + 3

*/
import java.util.Scanner;

public class Federation
{
   public static void main(String [] args)
   {
      Scanner in = new Scanner(System.in);
      int num;
      int sum = 1;
      int nFacs = 1;
      int [] fac = new int[1000];
      fac[0] = 1;
      
      num = in.nextInt();
      while (num != -1)
      {
         sum = 1;
         nFacs = 1;
         
         for (int i = 2; i <= num/2; i++)
         {
            if (num % i == 0)
            {
               sum += i;
               fac[nFacs++] = i;
            }
         
         }//end for
         
         if (sum == num)
         {
            System.out.print(num + " = " + fac[0]);
            for (int i = 1; i < nFacs; i++)
               System.out.print(" + " + fac[i]);
            System.out.println();
         }
         else
            System.out.println(num + " is NOT perfect.");
         
         num = in.nextInt();
      
      }//end while
   
   
   }//end main



}//end class Perfect

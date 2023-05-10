import java.util.Scanner;
import java.util.InputMismatchException;

public class Main {
   public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in);
      double distMiles = 0.0;
      double lightTravelTime = 0.0;
      boolean needInput = true;

      while (needInput) {
         System.out.print("Enter a distance in miles: ");
         
         try {
            distMiles = scnr.nextDouble();
            if (distMiles >= 0.0) {
                lightTravelTime = distMiles / 186282.0;
                needInput = false;
            }
            else {
                System.out.println("Values must be >= 0.0");
            }
         }
         catch (InputMismatchException e) {
            scnr.nextLine(); // Throw away incorrect input
         }
      }

      System.out.println("Light travels " + distMiles + 
                         " miles in " + lightTravelTime +
                         " seconds");
   }
}
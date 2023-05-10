import java.util.Scanner;
import java.util.InputMismatchException;
import java.lang.IllegalStateException;

public class Main {
  public static void main(String[] args) {
     Scanner scnr = new Scanner(System.in);
     double distMiles = 0.0;
     double lightTravelTimeSec = 0.0;
  
     System.out.print("Enter distance in miles: ");
     try {
        distMiles = scnr.nextDouble();
        lightTravelTimeSec = distMiles / 186282.0;
        System.out.println(lightTravelTimeSec);
     }
     catch (InputMismatchException e) {
        System.out.println("Must enter a number!");
     }
     catch (IllegalStateException e) {
        System.out.println("Scanner is closed for some reason!");
     }

  }
}
import java.util.Scanner;

public class DensityCalculator {
   public static double getPositiveValue(Scanner scnr, String valName)
                        throws InvalidNegativeInputException,MyCustomException {

      System.out.print("Enter " + valName + ": ");

      double inputVal = scnr.nextDouble();

      if(inputVal < 0.0) {
         throw new MyCustomException(valName,new Throwable("User input error."));
      }
      // if (inputVal < 0.0) {
      //     throw new InvalidNegativeInputException(valName);
      // }

      return inputVal;
   }

   public static double getDensity(Scanner scnr)
                        throws InvalidNegativeInputException, 
                               NaNException,
                               ZeroDivideException,
                               MyCustomException
                                {

      double massVal = getPositiveValue(scnr, "massVal");
      double volumeVal = getPositiveValue(scnr, "volumeVal");
      if(volumeVal == 0.0) {
         throw new ZeroDivideException();
      }
      double densityCalc = massVal / volumeVal;

      if (Double.isNaN(densityCalc)) {
         throw new NaNException("densityCalc");
      }

      return densityCalc;
   }

   public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in);

      try {
         System.out.println("Density: " + getDensity(scnr));
      }
      catch (MyCustomException excpt) {
         System.out.println(excpt.getMessage());
         excpt.printStackTrace();
      }
      catch (NaNException excpt) {
         System.out.println(excpt.getMessage());
         // Handle ...
      }
      catch (ZeroDivideException excpt) {
         System.out.println(excpt.getMessage());
         // Handle ...
      }
      catch (InvalidNegativeInputException excpt) {
         System.out.println(excpt.getMessage());
         // Handle ...
      }
   }
}

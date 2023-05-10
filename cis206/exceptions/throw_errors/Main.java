import java.util.Scanner;

public class Main {
    public static double getRatio(double gasVolume,double oilVolume) throws Exception {
         double mixRatio = gasVolume / oilVolume;
         if (Double.isNaN(mixRatio)) {
            throw new Exception("mixRatio is NaN!");
         }
         else{
            return mixRatio;
         }
    }
    
   public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in);
      double gasVolume;
      double oilVolume;
      double mixRatio = 0.0;

      try {
         gasVolume = scnr.nextDouble();
         oilVolume = scnr.nextDouble();
         mixRatio = getRatio(gasVolume,oilVolume);
         System.out.println("mixRatio: " + mixRatio);
      }
      catch (Exception excpt) {
        System.out.println(excpt.getMessage());
      }
   }
}

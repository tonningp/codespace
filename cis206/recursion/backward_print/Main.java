import java.util.Scanner;

public class Main {
   public static void backwardsAlphabet(char currLetter) {
      try {
        if (currLetter == 'a') {
            System.out.println(currLetter);
        }
        else {
            System.out.print(currLetter + " ");
            backwardsAlphabet((char)(currLetter - 1));
        }
      }
      catch(StackOverflowError e) {
        System.out.println("You got a stack overflow");

      }
   }

   public static void main (String [] args) {
      Scanner scnr = new Scanner(System.in);
      char startingLetter;

      startingLetter = scnr.next().charAt(0);

      backwardsAlphabet(startingLetter);

   }
}
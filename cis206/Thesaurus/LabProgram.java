import java.util.Scanner;
import java.io.FileInputStream;
import java.io.IOException;

public class LabProgram {
   public static void main(String[] args) throws IOException {
      Scanner scnr = new Scanner(System.in);
      int NUM_CHARACTERS = 26;      // Maximum number of letters
      int MAX_WORDS = 10;           // Maximum number of synonyms per starting letter

      String[][] synonyms = new String[NUM_CHARACTERS][MAX_WORDS];  // Declare 2D array for all synonyms
      String[] words = new String[MAX_WORDS]; // The words of each input line
      String filename;
      String lookupChar;
      filename = scnr.next();
      lookupChar = scnr.next();
      FileInputStream fileString = new FileInputStream(filename + ".txt");
      Scanner fsInput = new Scanner(fileString);
      while(fsInput.hasNext()) {
        String line = fsInput.nextLine();
        char letter = line.charAt(0);
        Scanner stringScan = new Scanner(line); 
        int wordCount = 0;
        while (stringScan.hasNext() && wordCount <= MAX_WORDS) {
            String word = stringScan.next();
            synonyms[(int)letter-97][wordCount] = word;
            wordCount++;
        }

      }
      int loopIndex = (int)lookupChar.charAt(0)-97;
      if (synonyms[loopIndex][0] == null) {
        System.out.println("No synonyms for "+ filename + " begin with " + lookupChar + ".");
      }
      words = synonyms[loopIndex];
      for(int i=0;i<MAX_WORDS;i++)
      {
          if(words[i] != null) {
            System.out.println(words[i]);
          }
          else {
            break;
          }

      }
   }
}

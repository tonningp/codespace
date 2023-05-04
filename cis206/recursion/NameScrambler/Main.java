import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void printAllPermutations(ArrayList<String> permList, 
                                   ArrayList<String> nameList) {
      ArrayList<String> tmpRemainNames;
      String tmpRemovedName;
      int i;

      if (permList.size() == 0) {
         int j;
         for(j=0;j < nameList.size()-1;++j)
         {
            System.out.print(nameList.get(j)+",");
         }
         System.out.println(nameList.get(j));
      }
      else {
         for (i = 0; i < permList.size(); ++i) {
            tmpRemainNames = new ArrayList<String>(permList); // Make a copy.
            tmpRemovedName = tmpRemainNames.remove(i);
            nameList.add(tmpRemovedName);
            printAllPermutations(tmpRemainNames, nameList);
            nameList.remove(nameList.size() - 1);
         }
      }
   }

   public static void main(String[] args) {
    Scanner scnr = new Scanner(System.in);
    ArrayList<String> nameList = new ArrayList<String>();
    ArrayList<String> permList = new ArrayList<String>();
    String name;
    
    // TODO: Read in a list of names; stop when -1 is read. Then call recursive method.
    name = scnr.next();
    while(!name.equals("-1")) {
        permList.add(name);
        name = scnr.next();
    }
    printAllPermutations(permList,nameList);

   }
}
//import java.util.ArrayList;
import java.util.LinkedList;
import java.util.ListIterator;
import java.util.Collections;

public class Main {
    public static void main(String []args) {
        LinkedList<String> teamRoster = new LinkedList<String>();
        ListIterator<String> lit;
        // Adding player names
        teamRoster.add("Toni");
        teamRoster.add("Scottie");
        teamRoster.add("Mike");
        teamRoster.add("Joe");
        teamRoster.add("Jane");
        teamRoster.add("Herbert");
        teamRoster.add(1,"Alice");
        teamRoster.set(5,"Janice");
        boolean found = teamRoster.remove("Herbert");
        lit = teamRoster.listIterator();

        //Collections.sort(teamRoster);

        System.out.println("Removed correct element?: "+found);
        System.out.println("Current roster:");

        // for (String playerName : teamRoster) {
        //   System.out.println(playerName);
        // }
         while(lit.hasNext()) {
            lit.set(lit.next().toUpperCase());
         }
        lit = teamRoster.listIterator();
        while(lit.hasNext()) {
            System.out.println(lit.next());
        }

    }
}
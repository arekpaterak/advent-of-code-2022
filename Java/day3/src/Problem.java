import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Problem {
    int sumOfPriorities = 0;

    public void solve() {
        processFile("./src/input.txt");

        System.out.println(sumOfPriorities);
    }
    
    private void processFile(String filename) {
        try {
            File file = new File(filename);
            Scanner reader = new Scanner(file);
            while (reader.hasNextLine()) {
                Group group = new Group();
                for (int i = 0; i < 3; ++i) {
                    String line = reader.nextLine();
                    Rucksack rucksack = new Rucksack(line);
                    group.rucksacks.add(rucksack);
                }

                sumOfPriorities += group.getPriorityOfBadge();

                // processLine(line);
            }
            reader.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    private void processLine(String line) {
        Rucksack rucksack = new Rucksack(line);
        sumOfPriorities += rucksack.getPriorityOfSharedItem();
    }
}
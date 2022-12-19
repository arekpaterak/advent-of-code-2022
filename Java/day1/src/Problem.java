import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Problem {
    List<Elf> elves = new ArrayList<Elf>();

    public int solve() {
        processFile("./src/input.txt");

        Collections.sort(elves, Collections.reverseOrder(new Comparator<Elf>() {
            @Override
            public int compare(Elf elf1, Elf elf2) {
                if (elf1.getTotalCalories() < elf2.getTotalCalories()) {
                    return -1;
                } else if (elf1.getTotalCalories() == elf2.getTotalCalories()) {
                    return 0;
                } else {
                    return 1;
                }
            }
        }));

        int topThreeElvesTotalCalories = 0;
        for (int i = 0; i < 3; ++i) {
            topThreeElvesTotalCalories += elves.get(i).getTotalCalories();
        }
        return topThreeElvesTotalCalories;
    }
    
    private void processFile(String filename) {
        try {
            File myObj = new File(filename);
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String line = myReader.nextLine();
                processLine(line);
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }

    private void processLine(String line) {
        Elf elf;
        if ((elves.isEmpty()) || (line.isEmpty())) {
            elf = new Elf(elves.size() + 1);
            elves.add(elf);
        } else {
            elf = elves.get(elves.size() - 1);
        }

        if (!line.isEmpty()) {
            int calories = Integer.parseInt(line);
            elf.food.add(new Food(calories));
        }
    }
}
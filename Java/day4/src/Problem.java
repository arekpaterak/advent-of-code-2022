import java.io.File;
import java.io.FileNotFoundException;
import java.util.List;
import java.util.Scanner;

public class Problem {
    int count = 0;

    public void solve() {
        processFile("./src/input.txt");

        System.out.println(count);
    }
    
    private void processFile(String filename) {
        try {
            File file = new File(filename);
            Scanner reader = new Scanner(file);
            while (reader.hasNextLine()) {
                String line = reader.nextLine();
                processLine(line);
            }
            reader.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    private void processLine(String line) {
        String[] pair = line.split(",");

        Range range1 = new Range(pair[0].split("-"));
        Range range2 = new Range(pair[1].split("-"));

//        if (range1.contains(range2) || range2.contains(range1))
//            ++count;

        if (range1.overlaps(range2))
            ++count;
    }
}
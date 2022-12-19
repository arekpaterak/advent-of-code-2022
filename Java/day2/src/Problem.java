import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Problem {
    int totalScore = 0;

    public void solve() {
        processFile("./src/input.txt");

        System.out.println(totalScore);
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
        String[] choices = line.strip().split(" ");
        Round round = new Round(choices[0], choices[1]);
        totalScore += round.getScore();
    }
}
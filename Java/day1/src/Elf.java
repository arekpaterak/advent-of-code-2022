import java.util.List;
import java.util.ArrayList;

public class Elf {
    int number;
    List<Food> food = new ArrayList<Food>();

    Elf(int number) {
        this.number = number;
    }

    int getTotalCalories() {
        int sum = 0;
        for (Food item : food) {
            sum += item.calories;
        }
        return sum;
    }
}

import java.util.ArrayList;
import java.util.List;

public class Group {
    List<Rucksack> rucksacks = new ArrayList<Rucksack>();
    char badge;

    void findBadge() {
        String items1 = rucksacks.get(0).items;
        String items2 = rucksacks.get(1).items;
        String items3 = rucksacks.get(2).items;
        for (int i = 0; i < items1.length(); ++i) {
            char item = items1.charAt(i);
            if (items2.contains(Character.toString(item)) && items3.contains(Character.toString(item))) {
                badge = item;
                return;
            }
        }
    }

    int getPriorityOfBadge() {
        findBadge();
        if (Character.isUpperCase(badge)) {
            return badge - 38;
        } else {
            return badge - 96;
        }
    }
}

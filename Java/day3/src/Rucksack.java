public class Rucksack {
    String items;
    String compartment1;
    String compartment2;
    char sharedItem;

    public Rucksack(String items) {
        this.items = items;
        int half = items.length() / 2;
        this.compartment1 = items.substring(0, half);;
        this.compartment2 = items.substring(half);
    }

    void findSharedItem() {
        for (int i = 0; i < compartment1.length(); ++i) {
            char item = compartment1.charAt(i);
            if (compartment2.contains(Character.toString(item))) {
                sharedItem = item;
                return;
            }
        }
    }

    int getPriorityOfSharedItem() {
        findSharedItem();
        if (Character.isUpperCase(sharedItem)) {
            return sharedItem - 38;
        } else {
            return sharedItem - 96;
        }
    }
}

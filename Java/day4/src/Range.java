public class Range {
    int start;
    int end;

    Range(String[] range) {
        start = Integer.parseInt(range[0]);
        end = Integer.parseInt(range[1]);
    }

    boolean contains(Range other) {
        if (start <= other.start && other.end <= end)
            return true;
        else
            return false;
    }

    boolean overlaps(Range other) {
        if (start <= other.end && other.start <= end)
            return true;
        else
            return false;
    }
}

import java.util.HashMap;
import java.util.Map;

public class Round {
    String opponentShape;
    String selectedShape;
    String outcome;

    public Round(String opponentShape, String selectedShape) {
        this.opponentShape = shapesForSymbols.get(opponentShape);
        this.selectedShape = shapesForSymbols.get(selectedShape);
        determineOutcome();
    }

    private static final Map<String, String> shapesForSymbols;
    static {
        shapesForSymbols = new HashMap<String, String>();
        shapesForSymbols.put("A", "rock");
        shapesForSymbols.put("B", "paper");
        shapesForSymbols.put("C", "scissors");

        shapesForSymbols.put("X", "rock");
        shapesForSymbols.put("Y", "paper");
        shapesForSymbols.put("Z", "scissors");
    }

    private static final Map<String, Integer> scoresForShape;
    static {
        scoresForShape = new HashMap<String, Integer>();
        scoresForShape.put("rock", 1);
        scoresForShape.put("paper", 2);
        scoresForShape.put("scissors", 3);
    }

    private static final Map<String, Integer> scoresForOutcome;
    static {
        scoresForOutcome = new HashMap<String, Integer>();
        scoresForOutcome.put("lost", 0);
        scoresForOutcome.put("draw", 3);
        scoresForOutcome.put("win", 6);
    }

    private void determineOutcome() {
        if (opponentShape.equals(selectedShape)) {
            outcome = "draw";
        } else if (opponentShape.equals("rock") && selectedShape.equals("scissors")) {
            outcome = "lost";
        } else if (opponentShape.equals("scissors") && selectedShape.equals("paper")) {
            outcome = "lost";
        } else if (opponentShape.equals("paper") && selectedShape.equals("rock")) {
            outcome = "lost";
        } else {
            outcome = "win";
        }
    }

    int getScore() {
        return scoresForShape.get(selectedShape) + scoresForOutcome.get(outcome);
    }
}

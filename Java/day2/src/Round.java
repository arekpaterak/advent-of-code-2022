import java.util.HashMap;
import java.util.Map;

public class Round {
    String opponentShape;
    String selectedShape;
    String outcome;

    public Round(String opponentShape, String outcome) {
        this.opponentShape = shapesForSymbols.get(opponentShape);
//        this.selectedShape = shapesForSymbols.get(selectedShape);
//        determineOutcome();

        this.outcome = outcomeForSymbols.get(outcome);
        determineChoice();
    }

    private static final Map<String, String> shapesForSymbols;
    static {
        shapesForSymbols = new HashMap<String, String>();
        shapesForSymbols.put("A", "rock");
        shapesForSymbols.put("B", "paper");
        shapesForSymbols.put("C", "scissors");

//        shapesForSymbols.put("X", "rock");
//        shapesForSymbols.put("Y", "paper");
//        shapesForSymbols.put("Z", "scissors");
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
        scoresForOutcome.put("lose", 0);
        scoresForOutcome.put("draw", 3);
        scoresForOutcome.put("win", 6);
    }

    private static final Map<String, String> outcomeForSymbols;
    static {
        outcomeForSymbols = new HashMap<String, String>();
        outcomeForSymbols.put("X", "lose");
        outcomeForSymbols.put("Y", "draw");
        outcomeForSymbols.put("Z", "win");
    }

//    private void determineOutcome() {
//        if (opponentShape.equals(selectedShape)) {
//            outcome = "draw";
//        } else if (opponentShape.equals("rock") && selectedShape.equals("scissors")) {
//            outcome = "lose";
//        } else if (opponentShape.equals("scissors") && selectedShape.equals("paper")) {
//            outcome = "lose";
//        } else if (opponentShape.equals("paper") && selectedShape.equals("rock")) {
//            outcome = "lose";
//        } else {
//            outcome = "win";
//        }
//    }

    private void determineChoice() {
        if (opponentShape.equals("rock")) {
            if (outcome.equals("lose")) {
                selectedShape = "scissors";
            } else if (outcome.equals("draw")) {
                selectedShape = "rock";
            } else if (outcome.equals("win")) {
                selectedShape = "paper";
            }
        } else if (opponentShape.equals("paper")) {
            if (outcome.equals("lose")) {
                selectedShape = "rock";
            } else if (outcome.equals("draw")) {
                selectedShape = "paper";
            } else if (outcome.equals("win")) {
                selectedShape = "scissors";
            }
        } else if (opponentShape.equals("scissors")) {
            if (outcome.equals("lose")) {
                selectedShape = "paper";
            } else if (outcome.equals("draw")) {
                selectedShape = "scissors";
            } else if (outcome.equals("win")) {
                selectedShape = "rock";
            }
        }
    }

    int getScore() {
        return scoresForShape.get(selectedShape) + scoresForOutcome.get(outcome);
    }
}

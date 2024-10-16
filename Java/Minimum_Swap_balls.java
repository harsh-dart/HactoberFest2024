
class Minimum_Swap_balls {

    public int minimumSteps(String s) {
        int swaps = 0;       // Count of swaps
        int whiteCount = 0;  // Count of white balls ('0's) seen so far

        // Iterate through the string
        for (char ch : s.toCharArray()) {
            if (ch == '0') {
                whiteCount += 1;  // Increment count of white balls
            } else {
                swaps += whiteCount;  // Each '1' needs to swap with each '0' to its left
            }
        }

        return swaps; // Return the total swaps needed
    }

    public static void main(String[] args) {
        Minimum_Swap_balls solution = new Minimum_Swap_balls(); // Create instance of Minimum_Swap_balls
        System.out.println(solution.minimumSteps("101"));   // Output: 1
        System.out.println(solution.minimumSteps("100"));   // Output: 2
        System.out.println(solution.minimumSteps("0111"));  // Output: 0
    }
}

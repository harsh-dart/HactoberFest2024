public class PowerUsingLoop {
    public static void main(String[] args) {
        int base = 2;
        int exponent = 3;
        long result = 1;

        // Calculate power using a loop
        for (int i = 1; i <= exponent; i++) {
            result *= base;
        }

        // Print the result
        System.out.println("Result: " + result);
    }
}

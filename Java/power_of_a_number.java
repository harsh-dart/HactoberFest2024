public class PowerUsingLoop {
    public static void main(String[] args) {
        int base = 2;
        int exponent = 3;
        long result = 1;

        for (int i = 1; i <= exponent; i++) {
            result *= base;
        }

        System.out.println("Result: " + result);
    }
}

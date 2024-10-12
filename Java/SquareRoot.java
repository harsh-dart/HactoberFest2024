// An algorithm to find the square root of a num using the Newton Raphson Algo

public class SquareRoot {
    public static void main(String[] args) {
        System.out.println(sqrt(40));
    }
    static double sqrt(int n) {
        double x = n;
        double root;
        while (true) {
            root = 0.5 * (x + (n/x));
            //this is the newton raphson method
            if (Math.abs(root-x)<0.01) {
                break;
            }
            x = root;
        }
        return root;


    }
}

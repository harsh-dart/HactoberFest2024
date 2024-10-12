//a program to find prime numbers in a range using the sieve of eratosthenes algorithm

public class SieveOfEratosthenes {
    //print all primes between 2 and n
    public static void main(String[] args) {
        int n = 43;
        boolean[] primes = new boolean[n+1];
        sieve(n,primes);
    }

    static void sieve(int n, boolean[] primes) {
        //initially all values in a boolean array are false. Say that false values means the number is prime,
        // then change the non-primes to true, and print the false values ie primes
        for (int i = 2; i*i <= n; i++) {
            if (!primes[i]) {
                for (int j = i*2; j <= n; j+=i) {
                    primes[j] = true;
                }
            }
        }
        for (int i = 2; i <= n; i++) {
            if (!primes[i]) {
                System.out.print(i +" ");
            }
        }
    }
}

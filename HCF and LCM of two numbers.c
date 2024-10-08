//HCF and LCM of two numbers
#include <stdio.h>

int calculateHCF(int a, int b) {
    if (b == 0)
        return a;
    return calculateHCF(b, a % b);
}


int calculateLCM(int a, int b, int hcf) {
    return (a * b) / hcf;
}

int main() {
    int num1, num2, hcf, lcm;

    printf("Enter two numbers: ");
    scanf("%d %d", &num1, &num2);

   
    hcf = calculateHCF(num1, num2);

    
    lcm = calculateLCM(num1, num2, hcf);

    
    printf("HCF of %d and %d is: %d\n", num1, num2, hcf);
    printf("LCM of %d and %d is: %d\n", num1, num2, lcm);

    return 0;
}

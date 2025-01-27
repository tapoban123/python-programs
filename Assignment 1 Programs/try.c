#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    double xInput, term, sum;
    int nInput;

    printf("Enter value of x: ");
    scanf("%lf", &xInput);

    printf("Enter value of n: ");
    scanf("%d", &nInput);

    term = xInput;
    sum = 0;

    for (int i = 1; i <= nInput; i++)
    {
        sum += term;
        term = (-term * xInput * 2 * 2) / ((2 * i) * (2 * i + 1));
    }

    printf("The value of term: %lf\n", sum);
    printf("The value of sin: %lf", sin(xInput));
}
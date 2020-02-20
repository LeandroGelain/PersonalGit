//Somas

#include <stdio.h>

int main()
{
    int soma, num1, num2;
    printf("Primeiro numero: ");
    scanf("%i", &num1);

    printf("Segundo numero: ");
    scanf("%i", &num2);

    soma = num1 + num2;

    printf("A soma de %i com %i resulta em %i", num1, num2, soma);

    return 0;
}


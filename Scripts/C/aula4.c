#include <stdio.h>
int main (void)
{
  int num1, num2, op, soma, sub, mult, divi, e;
    
    while (e!=0)
    printf("Quer continuar sim 0, não 1: ");
    scanf("%i", &e);
    
  {  
    printf("Escolha uma operação: Soma 1, subtração 2, multiplicação 3, divisão 4: \n");
    scanf("%i", &op);
    printf("%i", &op);
    
      printf("Primeiro numero: ");
      scanf("%i", &num1);
      
      printf("Segundo numero: ");
      scanf("%i", &num2);
      soma = num1 + num2;
      printf("%i + %i = %i", num1, num2, soma);
     
    
     if (op == 2)
     {
      printf("Primeiro numero: ");
      scanf("%i", &num1);
      
      printf("Segundo numero: ");
      scanf("%i", &num2);
      sub = num1 - num2;
      printf("%i - %i = %i", num1, num2, sub);
     }
    
     if (op == 3)
     {
      printf("Primeiro numero: ");
      scanf("%i", &num1);
      
      printf("Segundo numero: ");
      scanf("%i", &num2);
      mult = num1 * num2;
      printf("%i * %i = %i", num1, num2, mult);
     }
      
     if (op == 4)
     {
      printf("Primeiro numero: ");
      scanf("%i", &num1);
      
      printf("Segundo numero: ");
      scanf("%i", &num2);
      divi = num1 / num2;
      printf("%i / %i = %f", num1, num2, divi);
     }
  }
    
}
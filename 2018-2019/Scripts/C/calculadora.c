#include "stdio.h"

int main()
{
  int num1, num2, op, resultado;
  
  printf("-=-=-=-=-=-=-=-=-=-=-=-=-=\n");
  printf("'1' = soma.\n");
  printf("'2' = subtração.\n");
  printf("'3' = multiplicação.\n");
  printf("'4' = divisão.\n");
  printf("-=-=-=-=-=-=-=-=-=-=-=-=-=\n");
  printf("Para sair digite 000.\n");
  
  printf("Primeiro numero: \n");
  scanf("%d",num1);
  
  printf("Operação: \n");
  scanf("%d", op);
  
  printf("Segundo numero: \n");
  scanf("%d", num2);
  
  if (op == 1)
  {
    resultado = num1 + num2;
    printf(" ",resultado);
  }
  return 0;
}
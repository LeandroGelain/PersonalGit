#include "stdio.h"

int main()
{
  int n1;
  int n2, resultado;
  int op;
  
  printf("-=-=-=-=-=-=-=-=-=-=-=-=-=\n");
  printf("'1' = soma.\n");
  printf("'2' = subtração.\n");
  printf("'3' = multiplicação.\n");
  printf("'4' = divisão.\n");
  printf("-=-=-=-=-=-=-=-=-=-=-=-=-=\n");
  printf("Para sair digite 000.\n");
  
  printf("Primeiro numero: \n");
  scanf("%i", &n1);
  
  printf("Operação: \n");
  scanf("%i", &op);
  
  printf("Segundo numero: \n");
  scanf("%i", &n2);
  
  if (op == 1)
  {
    resultado = n1 + n2;
    printf(" ",resultado);
  }
  return 0;
}


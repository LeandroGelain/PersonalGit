#include "stdio.h"

int main()
{
  int n1;
  int n2, resultado;
  int op;
  
  printf("-=-=-=-=-=-=-=-=-=-=-=-=-=\n");
  printf("'1' = soma.\n");
  printf("'2' = subtra��o.\n");
  printf("'3' = multiplica��o.\n");
  printf("'4' = divis�o.\n");
  printf("-=-=-=-=-=-=-=-=-=-=-=-=-=\n");
  printf("Para sair digite 000.\n");
  
  printf("Primeiro numero: \n");
  scanf("%i", &n1);
  
  printf("Opera��o: \n");
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


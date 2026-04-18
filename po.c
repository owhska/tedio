#include <stdio.h>
#include <stdlib.h>


int main(int argc, char *argv[]){ //*argv[] == **argv
    if (argc != 4){
        printf("Uso: %s num1 operador num2\n", argv[0]);
        return 1;
    }

    int a = atoi(argv[1]);
    int b = atoi(argv[3]);
    char op = argv[2][0];

    int resultado;

    if (op == '+') resultado = a + b;
    else if (op == '-') resultado = a - b;
    else if (op == '*') resultado = a * b;
    else if (op == '/') resultado = a / b;
    else {
        printf("Operador invalido\n");
        return 1;
    }

    printf("Resultado = %d\n",resultado);
    return 0;
}

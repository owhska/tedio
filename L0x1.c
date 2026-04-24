#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int reconhecedor_0x1(char * s){

    int i = 0;
    int n0 = 0; //qualtidade de zeros no inicio de s
    int n1 = 0; //qualtidade de zeros no final de s


    if(s == NULL) return 0;

    while (s[i] == '0'){
        n0++;
        i++;
    } // Para contar a quantidade de zeros no inicio da palavra

    while(s[i] == '1'){
        n1++;
        i++;
    } // Para contar a quantidade de uns no final da palavra
      

    if(s[i] != '\0') return 0;
    return n0 == n1;

}

int main(int argc, char ** argv){

    printf("%s\n",reconhecedor_0x1(argv[1]) ? "ACERTA" : "REJEITA");
    return 0;

}



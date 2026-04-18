#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char nome[20];
    int idade;
} Pessoa;

int main(){

    Pessoa pessoas[3] = {
        {"Funalo", 20},
        {"Ciclano", 21},
        {"Beltrano",22}
    };

    //printf("%d\n", pessoas[1].idade);
    //printf("%s\n", pessoas[2].nome);
    
    for (int i = 0; i < 3; i++){
        printf("Pessoa [%d] Nome: %s Idade: %d\n", i, pessoas[i].nome, pessoas[i].idade);
    }

    return 0;
}

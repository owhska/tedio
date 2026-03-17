#include <stdio.h>

int main(){
    
    int lista[5] = {4,4,22,1,6};
    int i,j,temp;
    int n = sizeof(lista) / sizeof(lista[0]);

    for (i=0;i<n;i++){
        for(j=0;j< n - 1;j++){
            if(lista[j] > lista[j+1]){
                temp = lista[j];
                lista[j] = lista[j+1];
                lista[j+1] = temp;
            }
       }
    }

    for (i=0;i<5;i++){
        printf("%d ",lista[i]);
    }

    printf("\n");
    return 0;
}

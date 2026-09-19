#include <stdio.h>

void main() {

    int l, c;
    int m[3][3] = {1, 2, 3, 4, 5, 6, 7, 8, 9};

    for (l = 0; l < 3; l++){
        for (c = 0; c < 3; c++ ){
            printf("%d ", m[l][c]);
        }
        printf("\n");
    }
}

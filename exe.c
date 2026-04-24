#include <stdio.h>
#include <ctype.h>

typedef enum{S, Q1, Q2, Q3, DEAD} State;

State step (State s, char x){

    switch(s){
        case S:
            if(x == 'a') return S;
            if(x == 'b') return Q1;
            break;
        case Q1:
            if(x == 'a') return Q1;
            if(x == 'c') return Q2;
            break;
        case Q2:
            break;
        case Q3:
            if(x == 'b') return Q1;
            break;
        default:
            break;
    }
        return DEAD;

}

int main(){

    char buf[1024];

    while(fgets(buf, sizeof(buf), stdin)) {
    
        State s = S;
        int ok = 1;

        for (int i = 0; buf[i] != '\0'; i++){
            unsigned char ch = (unsigned char) buf[i];

            if (ch == '\n') continue;
            if (ch == '\r') continue;
            if (isspace(ch)) continue;

            if (ch != 'a' && ch != 'b' && ch != 'c'){ok = 0; break;}

            s = step(s, ch);

            if (s == DEAD) {ok = 0; break;}
        }
        
        if (ok == 1 && s == Q2) printf("ACEITA\n");
        else printf("REJEITA\n");
    }

    return 0;
}

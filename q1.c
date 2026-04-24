#include <stdio.h>
#include <ctype.h>

typedef enum{E0, E1, E2, E3, E4, E5, E6, E7, DEAD} State;

State step (State s, char x){

    switch(s){
        case E0:
            if(x == '+' || x == '-') return E1;
            if(x == '.') return E2;
            if(isdigit(x)) return E3;
            break;
        case E1:
            if(isdigit(x)) return E3;
            if(x == '.') return E2;
            break;
        case E2:
            if(isdigit(x)) return E4;
            break;
        case E3:
            if(isdigit(x)) return E3;
            if(x == '.') return E4;
            if(x == 'E') return E5;
            break;
        case E4:
            if(isdigit(x)) return E4;
            if(x == 'E') return E5;
            break;
        case E5:
            if(isdigit(x)) return E7;
            if(x == '+' || x == '-') return E6;
            break;
        case E6:
            if(isdigit(x)) return E7;
            break;
        case E7:
            if(isdigit(x)) return E7;
            break;
        default:
            break;
    }
    return DEAD;

}

int main(){

    char buf[1024];

    while(fgets(buf, sizeof(buf), stdin)) {

        State s = E0;
        int ok = 1;

        for (int i = 0; buf[i] != '\0'; i++){
            unsigned char ch = (unsigned char) buf[i];

            if (ch == '\n') continue;
            if (ch == '\r') continue;
            if (isspace(ch)) continue;

            if (!isdigit(ch) && ch != '+' && ch != '-' && ch != 'E' && ch != '.'){ok = 0; break;}

            s = step(s, ch);

            if (s == DEAD) {ok = 0; break;}
        }

        if (ok && (s == E3 || s == E4 || s == E7)) printf("ACEITA\n");
        else printf("REJEITA\n");
    }

    return 0;
}


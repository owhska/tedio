#include <stdio.h>
#include <math.h>

int main(){
	
	int x1,x2,a,b,c,delta;
	
	printf("Digite o valor pra a: ");
	scanf("%d",&a);
	
	printf("Digite o valor pra b: ");
	scanf("%d",&b);
	
	printf("Digite o valor pra c: ");
	scanf("%d",&c);
	
	delta = (b*b) - (4*a*c);
	int raizDelta = sqrt(delta);
	
	if( delta < 0){
		printf("Nao valido");
	}else if(delta == 0){
		printf("somente um valor de x\n");
		
		x1 = (-b + raizDelta) / (2*a);
	}else{
		x1 = (-b + raizDelta) / (2*a);
		x2 = (-b - raizDelta) / (2*a);
		
		printf("X1 = %d X2 = %d",x1,x2);
	}
		
	
}

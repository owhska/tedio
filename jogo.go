package main

import(
	"fmt"
	"math/rand"

)

func main(){

	numero := rand.Intn(10);
	var valor int;
	var tentativas int;

	for valor != numero{

		fmt.Println("Digite um valor: ");
		fmt.Scan(&valor);

		tentativas = tentativas + 1;

		if valor == numero {
			fmt.Println("Voce acertou!");
			fmt.Printf("Voce precisou de %d tentativa(s)", tentativas);
			break;
		} else if valor < numero {
			fmt.Println("O numero e maior");

		} else if valor > numero{
			fmt.Println("O numero e menor");

		}

	}

}

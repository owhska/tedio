package main

import "fmt"

type Pessoa struct { 
	nome string
	idade int
}

func main(){

	p := Pessoa{
		nome: "Fulano",
		idade: 20,
	}

	fmt.Println(p.nome,p.idade)

	pessoas := []Pessoa{
		{"Fulano", 20},
		{"Ciclano", 22},
		{"Beltrano", 21},
	}

	for  i := 0; i < len(pessoas); i++ {
		fmt.Printf("Pessoa [%d]: %s, %d\n",
		i,
		pessoas[i].nome,
		pessoas[i].idade,
		)
	}
}

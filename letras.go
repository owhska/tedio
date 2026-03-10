package main

import (
	"fmt"
	"unicode/utf8"
)

func contarLetras(s string) int {
	return utf8.RuneCountInString(s)
}

func main() {
	texto := "Ação" // 'ç' e 'ã' ocupam mais de um byte(ocupam dois cada)
	
	fmt.Printf("len() (numero de letras bytes): %d\n", len(texto))
	
	fmt.Printf("RuneCountInString (numero de letras): %d\n", contarLetras(texto))
}


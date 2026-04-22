package main

import (
	"fmt"
	"net/http"
)

func main(){
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request){
		fmt.Fprintf(w, `<h1 style="font-size: 40px;text-align: center;">Titulo</h1>`)
	})

	http.ListenAndServe(":8080", nil)
}

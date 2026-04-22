package main

import(
	"fmt"
	"net/http"
)

func main(){
		http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, `
			<html>
				<body>
					<form method="POST" action="/enviar">
						<input type="text" name="nome" placeholder="Seu nome">
						<input type="submit" value="Enviar">
					</form>
				</body>
			</html>
		`)
	})

	http.HandleFunc("/enviar", func(w http.ResponseWriter, r *http.Request){
		nome := r.FormValue("nome")
		fmt.Fprintf(w, "<h1>Ola, %s!</h1>", nome)
	})

	http.ListenAndServe(":8080", nil)
}

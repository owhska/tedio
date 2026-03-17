const botao = document.getElementById("botao");
    let som = new Audio("sound.mp3");    
    let contador = 0    
    let mensagem = 'sua pontuacao e ${contador}';

    botao.addEventListener('click', function(){
        //alert('botao clicado!');
    
        som.play();
        contador = contador + 1;
        
        console.log("Voce apertou o botao " + contador + " vez(es)");
    });

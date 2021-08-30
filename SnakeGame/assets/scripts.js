let canvas;
let ctx;
let score;
let pontos;
let cor;
var xFPS = 9;

function xFPSy(){
    if(pontos.value > 9){xFPS++;if(xFPS.value > 15){xFPS=15};};
    if(pontos.value < 9){xFPS=9};
}

window.onload = function(){
    canvas = document.getElementById("canvas");
    ctx = canvas.getContext("2d");

    document.addEventListener("keydown", keyDownEvent);

    //  Renderiza 9 vezes por segundo
    // O FPS aumenta de acordo com os pontos
    setInterval(desenharJogo, 1000 / xFPS);
};
    
//Criação da tela de jogo
let tamanhoTela = 27;
let tamanhoCaminho = 22;
let nextX = nextY = 0;

//Criação da cobra
let defaultTamanhoCauda = 3;
let tamanhoCauda = defaultTamanhoCauda;
let caminhoCobra = [];
let cobraEixoX = cobraEixoY = 13;

//Criação da comida
let appleX = (appleY = Math.floor(Math.random() * tamanhoTela));

//Declaração do Score
pontos = 0;
score = document.querySelector(`.score`);
score.innerHTML = `Score = ${pontos}`;

function desenharJogo(){
    cobraEixoX += nextX;
    cobraEixoY += nextY;

    if (cobraEixoX < 0){
        cobraEixoX = tamanhoTela -1;
    }
    if (cobraEixoX > tamanhoTela - 1){
        cobraEixoX = 0;
    }
    if (cobraEixoY < 0){
        cobraEixoY = tamanhoTela -1;
    }
    if (cobraEixoY > tamanhoTela - 1){
        cobraEixoY = 0;
    }
    
    //Se a cobra comer a maçã:
    if (cobraEixoX == appleX && cobraEixoY == appleY){
        tamanhoCauda++;
        appleX = Math.floor(Math.random() * tamanhoTela);
        appleY = Math.floor(Math.random() * tamanhoTela);
        pontos++;
        score.innerHTML = `Score = ${pontos}`;
        xFPSy();
    }

    ctx.fillStyle = "#1C1C1C";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    cor = document.querySelector(".cor");
    ctx.fillStyle = cor.value;
    for (let i = 0; i < caminhoCobra.length; i++){
        ctx.fillRect(
            caminhoCobra[i].x * tamanhoCaminho,
            caminhoCobra[i].y * tamanhoCaminho,
            tamanhoCaminho,
            tamanhoCaminho
        );
        if (caminhoCobra[i].x == cobraEixoX && caminhoCobra[i].y == cobraEixoY){
            //caso a cobra encostar no próprio corpo, ela volta para o default
            tamanhoCauda = defaultTamanhoCauda;
            //os pontos zeram 
            pontos = 0;
            score.innerHTML = `Score = ${pontos}`;
            //e o FPS volta ao normal
            xFPSy();
        }
    }

    ctx.fillStyle = "#FF0000";
    ctx.fillRect(appleX * tamanhoCaminho, appleY * tamanhoCaminho, tamanhoCaminho, tamanhoCaminho);

    caminhoCobra.push({
        x:cobraEixoX,
        y:cobraEixoY
    });
    while (caminhoCobra.length > tamanhoCauda){
        caminhoCobra.shift();
    }
}

function keyDownEvent(event){
//  nextX e nextY 
// Representam as direções que a cobra irá percorrer nos eixos X e Y, respectivamente.

    switch(event.keyCode){
        case 37:
            nextX = -1;
            nextY = 0;
            break;
        case 38:
            nextX = 0;
            nextY = -1;
            break;
        case 39:
            nextX = 1;
            nextY = 0;
            break;
        case 40:
            nextX = 0;
            nextY = 1;
            break;
    }
}

let a = prompt('Digite um número inteiro para ser o dividendo'); 
let b = prompt('Digite um segundo número inteiro para ser o divisor');
let Q = 0; 
let r = a-b*Q;

while(r>=b){
    r = r - b;
    Q = Q + 1;
}

console.log(`O quociente é ${Q} e o resto é ${r}`);

// Testando o programa para, por exemplo, a = 25 e b = 3, temos que quando for Q = 7 e r = 4, como 4 > 3,
// o programa realizará suas últimas operações: r = 4 - 3 e Q = 7 + 1. 
// Obtemos então o resultado esperado, Q = 8 e r = 1.






let b = prompt('Digite um número inteiro para ser o dividendo'); 
let a = prompt('Digite um segundo número inteiro para ser o divisor'); 
let c = b/a;
let d = b%a;
console.log(d);
if(d > 0) {
    console.log(`Não existe um inteiro n tal que n multiplicado por ${a} seja igual a ${b}`);
} else {
    console.log(`Temos que ${c} satisfaz a relação ${a} divide ${b}.`);
}


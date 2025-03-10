let a = prompt('Digite um número inteiro para ser o dividendo'); 
let b = prompt('Digite um segundo número inteiro diferente de 0 para ser o divisor');
let Q = 0; 
let r = a-b*Q;
while(r>=b){
    r = r - b;
    Q = Q + 1;
}
console.log(`O quociente é ${Q} e o resto é ${r}`);
if(r == 1){
    console.log(`Temos que ${a} e ${b} são primos entre si`);
} else{
    let q = 0;
    let s = b-r*q
    while(s>=r){
        s = s - r;
        q = q + 1;
    }
    console.log(`O quociente é ${q} e o resto é ${s}`);
    if(s == 1){
        console.log(`Temos que ${a} e ${b} são primos entre si`);
    } else if(s == 0){
        console.log(`Temos que o máximo divisor comum de ${a} e ${b} é igual a ${r}`);
    } else{
        let p = 0;
        let t = r-s*p
        while(t>=s){
            t = t - s;
            p = p + 1;
        }
        console.log(`O quociente é ${p} e o resto é ${t}`);
        if(t == 1){
            console.log(`Temos que ${a} e ${b} são primos entre si`);
        } else if(t == 0){
            console.log(`Temos que o máximo divisor comum de ${a} e ${b} é igual a ${s}`);
        }
    }
}




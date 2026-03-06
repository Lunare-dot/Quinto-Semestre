console.log("Testando impressão");

//variáveis
var animal = "gato";
var nomeCompleto = "Matheus Ferreira Souza";
const valor1 = 1;

console.log(animal);
console.log(nomeCompleto);
console.log(valor1);

let nome = "Cicrano";
nome = "Beltrano"
animal = 'peixe';

//verificar os tipos
console.log(typeof nome);

//algoritmo: entrada + processamento + saída
var nome2 = window.prompt("Digite seu nome: ");
console.log("Nome digitado: " + nome2 + " Aproveite.");

//template literal
console.log(`Nome: ${nome2}. Aproveite!`);

//operadores aritméticos: + - * / ** Funcionam da mesma maneira que em outras linguagens

//operadores de comparação: < > >= <= == != Funcionam da mesma maneira que em outras linguagens
// === !== Respectivamente: Estritamente igual e Estritamente diferente

console.log(5 == '5'); //Resultado esperado: True. O operador de igualdade diz respeito apenas aos valores.
console.log(5 !== '5'); //Resultado esperado: True. O operador está olhando apenas o tipo.
console.log(5 === '5'); //Resultado esperado: False. Number e String são tipos diferentes.

//Criar um algoritmo que realize a soma de dois números
//O usuário deve informar os números
//O programa deve apresentar o resultado da operação.

let n1 = window.prompt("Digite o primeiro número: ");
console.log(typeof n1);
let n2 = window.prompt("Digite o segundo número: ");
let result = Number(n1) + Number(n2);

console.log(`Resultado da operação: ${result}`);

//estruturas condicionais
//if-else, switch-case

var idade = 10;
if (idade >= 18) {
    console.log("maior de idade");
} else {
    console.log("menor de idade");
}
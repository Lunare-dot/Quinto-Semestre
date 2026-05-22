//Objetos
//formas de você criar o objeto
const pessoa = {
    nome: "Fulano",
    idade: 10
};
console.log(pessoa);

pessoa.idade = 20;
console.log(pessoa);

const pessoa2 = new Object(); //objeto pessoa2
pessoa2.cpf = 232432423;
pessoa2.nome = "Ciclano";
console.log(pessoa2.cpf);

//criar várias instancias de um objeto: Pessoa (p1, p2, p3 ...pn)
//construtor
class Pessoa {
    constructor(nome, idade) {
        this.nome = nome;
        this.idade = idade;
    }
};

//criar as instâncias
const p1 = new Pessoa("João", 12);
const p2 = new Pessoa("Maria", 40);
console.log(p1);
console.log(p2);

//modificadores de acesso: JavaScript (public e private)
//modificadores de acesso: Protected e Default (TypeScript)
class ContaBancaria{
    #saldo = 0; //propriedade

    //para transformar uma propriedade publica em privada, basta utilizar o símbolo "#"

    constructor(saldoInicial){ //método construtor
        this.#saldo = saldoInicial;
    }

    //métodos (getters e setters)
    getSaldo(){
        return this.#saldo;
    }
};

const conta = new ContaBancaria(100);
console.log(conta.getSaldo()); //estou acessando o método
//console.log(conta.#saldo); //estou acesso a propriedade do objeto
//conta.#saldo = 1; //não vai funcionar pois é uma propriedade privada
console.log(conta);


//Arrays
let itens = []; //carrinho de compras
itens[0] = "Arroz"; //adicionar na posição
itens[1] = "Tapete";
console.log(itens);

//métodos
//adicionar
itens.unshift("Pêra"); //inicio
console.log(itens);

itens.push("Livro"); //final
console.log(itens);

itens.splice(1,0,"Feijão"); //posição específica (adicionar na posição 1)
console.log(itens);

//remover
itens.shift(); //remover o primeiro elemento
console.log(itens);

itens.pop(); //remover o último elemento
console.log(itens);

itens.splice(1,1); //remover o elemento de uma determinada posição específica
console.log(itens);

console.log(itens.toString());
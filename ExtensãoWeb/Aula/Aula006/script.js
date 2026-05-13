const pessoa = {
    nome: "Fulano",
    idade: 20
};
console.log(pessoa);

pessoa.idade = 10;
console.log(pessoa);

const pessoa2 = new Object();
pessoa2.cpf = 2324252627;
pessoa2.nome = "Ciclano";
console.log(pessoa2);

//criar várias instancias de um objeto: Pessoa (p1, p2, p3... pn)
//construtor
class Pessoa {
    constructor(nome, idade) {
        this.nome = nome;
        this.idade = idade;
    }
}

//criar as instâncias
const p1 = new Pessoa("João", 12);
const p2 = new Pessoa("Lúcia", 40);
console.log(p1);
console.log(p2);

//modificadores de acesso: JavaScript (public e private)
//modificadores de acesso: Protected e Default (TypeScript)
class ContaBancaria {
    #saldo = 0; //propriedade

    constructor(saldoInicial) {
        this.#saldo = saldoInicial;
    }

    //métodos (getters e setters)
    getSaldo() {
        return this.#saldo;
    }
};

const conta = new ContaBancaria(100);
console.log(conta.getSaldo()); //estou acessando o método
//console.log(conta.#saldo); estou acessando a propriedade do objeto
//conta.#saldo = 1; vai dar erro por ser uma propriedade privada
console.log(conta);

//arrays
let itens = []; //carrinho de compras
itens[0] = "Arroz"; //adicionar no índice
itens[1] = "Feijão";
console.log(itens);

//métodos
//adicionar
itens.unshift("Pêra"); //inicio
console.log(itens);

itens.push("Livro"); //final
console.log(itens);

itens.splice(1, 0, "Piru"); //posilão específica (adicionar na posição 1)
console.log(itens)

//remover
itens.shift(); //remover o primeiro elemento
console.log(itens);

itens.pop(); //remover o último elemento
console.log(itens);

itens.splice(1, 1); //posição específica (remove o item no índice 1)
console.log(itens);

console.log(itens.toString());
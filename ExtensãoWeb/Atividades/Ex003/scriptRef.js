const main = () => {
    let combustivel = document.getElementById('combustivel');
    let litros = document.getElementById('litros');

    keydown(combustivel);
}
document.addEventListener("DOMContentLoaded", main);

const atualizarValor = (tipo) => {
    const precoGasolina = 6.79;
    const precoEtanol = 5.40;
    const precoDiesel = 6.20;

    const precos = {
        gasolina: precoGasolina,
        etanol: precoEtanol,
        diesel: precoDiesel 
    }

    let precoPorLitro = precos[tipo] ?? null;

    if(precoPorLitro === null) {
        document.getElementById('resultado').textContent = "Escolha uma opção";
        return;
    }

    calcularAbastecimento(precoPorLitro);
}

const calcularAbastecimento = (precoCombustivel) => {
    const resultado = document.getElementById('resultado');
    const inputLitros = document.getElementById('litros');
    const litros = parseFloat(inputLitros.value);

    const validacao = [
        { condicao: inputLitros.value.trim() === "", mensagem: "O campo não pode estar vazio."},
        { condicao: isNaN(litros), mensagem: "Digite apenas números válidos."},
        { condicao: litros <= 0, mensagem: "A quantidade de litros não pode ser negativa."}
    ];

    const erro = validacao.find(v => v.condicao);
    if(erro) {
        resultado.textContent =  erro.mensagem;
        return;
    } else {
        resultado.textContent = formatarMoeda(precoCombustivel * litros);
    }
}

const formatarMoeda = valor => {
    return "R$" + valor.toLocaleString('pt-BR', {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    });
}

const keydown = (change) => {
    document.addEventListener("keydown", event => {
        if(event.key === "Enter") {
            event.preventDefault();
            atualizarValor(change.value);
        }
    });
}
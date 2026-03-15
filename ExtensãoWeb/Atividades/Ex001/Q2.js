function getRandomInt(min, max) {
    const minCeiled = Math.ceil(min);
    const maxFloored = Math.floor(max);
    return Math.floor(Math.random() * (maxFloored - minCeiled + 1) + minCeiled);
}

function getAttribute(sequence) {
    if(sequence == 1) sequence = "Pedra";
    if(sequence == 2) sequence = "Papel";
    if(sequence == 3) sequence = "Tesoura";
    return sequence;
}

(function() {
    console.log("Pedra, Papel, Tesoura!\n1 - Pedra\n2 - Papel\n3 - Tesoura");

    while(true) {
        const w = window.prompt("Leia o log e escolha Pedra, Papel ou Tesoura.");
        if(w === null) {
            console.log("Jogo encerrado!");
            break;
        }

        const uEntry = Number(w);
        if(![1, 2, 3].includes(uEntry)) {
            console.log("Escolha 1, 2 ou 3!");
            continue;
        }

        const rNum = getRandomInt(1, 3);
        const botNum = getAttribute(rNum);
        const playerNum = getAttribute(uEntry);

        console.log(`Jogador: ${playerNum}\nComputador: ${botNum}`);

        const playerWins = 
            (uEntry === 1 && rNum === 3) ||
            (uEntry === 2 && rNum === 1) ||
            (uEntry === 3 && rNum === 2);

        if(uEntry === rNum) {
            console.log(`${playerNum} === ${botNum}. Empate! Joguem novamente.`);
            continue;
        }

        if(playerWins) {
            console.log(`${playerNum} vence ${botNum}. Vitória do jogador!\nReinicie a página para jogar novamente.`);
            break;
        } else {
            console.log(`${botNum} vence ${playerNum}. Vitória do computador!\nJoguem novamente.`);
            continue;
        }
    }
})();
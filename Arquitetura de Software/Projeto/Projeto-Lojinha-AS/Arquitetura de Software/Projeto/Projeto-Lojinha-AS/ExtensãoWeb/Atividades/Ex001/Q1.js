function getRandomInt(min, max) {
    const minCeiled = Math.ceil(min);
    const maxFloored = Math.floor(max);
    return Math.floor(Math.random() * (maxFloored - minCeiled + 1) + minCeiled);
}

(function() {
    var rNum = (getRandomInt(1, 20));

    const form = document.getElementById('contactForm');
    const messageArea = document.getElementById('message');
    const messageArea2 = document.getElementById('message2');
    const input = document.getElementById('uNum');

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        const userNumber = Number(input.value);
        input.value = "";
        console.log("User entry: ", userNumber);

        if(userNumber == rNum) {
            messageArea.textContent = "Número aleatório encontrado!";
            messageArea2.textContent = "Jogo finalizado! Reincie a página para jogar novamente.";
            messageArea.style.color = messageArea2.style.color = "green";

            input.disabled = true;
            form.querySelector('input[type="submit"]').disabled = true;
            return 0;
        } else {
            const dica = userNumber > rNum ? "menor" : "maior";
            messageArea.textContent = "Número incorreto! Tente novamente...";
            messageArea2.textContent = `Dica: O número a ser encontrado é ${dica} que ${userNumber}.`;
            messageArea.style.color = messageArea2.style.color = "red";
        }
    });
})();
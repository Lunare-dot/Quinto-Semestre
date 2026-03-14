(function() {
    const form = document.getElementById('contactForm');
    const input = document.getElementById('uNum');
    const messageArea = document.getElementById('message');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const uEntry = Number(input.value);
        input.value = "";
        console.log(`User entry: ${uEntry}`);

        triangle = "";
        for(let i = 0; i < uEntry; i++) {
            triangle+=("\n");
            for(let j = 0; j <= i; j++) {
                triangle+=("*");
            }
        }
        //messageArea apenas para visualização melhor do problema.
        messageArea.style.whiteSpace = "pre-wrap";
        messageArea.textContent = triangle;
        messageArea.style.color = "black";
        //O .log() é a visualização correta da resposta da questão quatro.
        console.log(triangle);
    });
})();
(function() {
    const form = document.getElementById('contactForm');
    const input = document.getElementById('uNum');
    const messageArea = document.getElementById('message');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const uEntry = Number(input.value);
        input.value = "";
        console.log(`User entry: ${uEntry}`);

        let triangle = "";
        for(let i = 0; i < uEntry; i++) {
            triangle+=("\n");
            for(let j = 0; j <= i; j++) {
                triangle+=("*");
            }
        }
        messageArea.textContent = "Verifique o log para obter o resultado!";
        messageArea.style.color = "green";
        console.log(triangle);
    });
})();
(function() {
    const form = document.getElementById('contactForm');
    const input = document.getElementById('uNum');
    const messageArea = document.getElementById('message');
    const messageArea2 = document.getElementById('message2');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const uEntry = Number(input.value);
        input.value = "";
        console.log(`User entry: ${uEntry}`);

        if(uEntry == 0) {
            messageArea.textContent= "Todo número multiplicado por zero resultará em zero.";
            messageArea.style.color = "black";
        }

        messageArea.textContent = `A tabuada de ${uEntry} é:`;
        messageArea.style.color = "black";
        console.log(messageArea.textContent);

        let tTable = "";
        for(let i = 1; i <= 10; i++) {
            const calc = (uEntry * i)
            tTable += `${uEntry} * ${i} = ${calc}\n`;
        }
        messageArea2.style.whiteSpace = "pre-wrap";
        messageArea2.textContent = tTable;
        messageArea2.style.color = "black";
        console.log(tTable);
    });
})();
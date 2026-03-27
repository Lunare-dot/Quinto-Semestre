function seriesArraySum(quantifiers) {
    const series = [];
    let cVa = "";
    var num = quantifiers;

    for(let i = 1; i <= num; i++) {
        cVa += 1;
        series.push(cVa);
    }
    const numberArray = series.map(Number);
    const sum = numberArray.reduce((acc, cValue) => acc + cValue, 0);
    return {series, sum};
}

(function() {
    const form = document.getElementById('contactForm');
    const input = document.getElementById('uNum');
    const messageArea = document.getElementById('message');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const uEntry = Number(input.value);
        input.value = "";
        console.log(`User entry: ${uEntry}`);

        if(uEntry === 0) {
            messageArea.textContent = "O resultado da soma de uma série infinita de zeros sempre será zero.";
            messageArea.style.color = "green";
        } else {
            const resultado = seriesArraySum(uEntry);

            messageArea.textContent = "Verifique o log para obter o resultado da série!";
            messageArea.style.color = "green";

            console.log(`Série: ${resultado.series.join(" + ")}`);
            console.log(`Soma da série: ${resultado.sum}`);
        }
    });
})();
document.addEventListener("DOMContentLoaded", main);

function main() {
    const inputText = document.getElementById('uEntry');
    const b1 =  document.getElementById('botao1');
    const b2 = document.getElementById('botao2');
    const b3 = document.getElementById('botao3');
    const b4 =  document.getElementById('resetB')
    
    minMaxButton(b1, b2);
    inputList(inputText);
    stringCount(inputText);
    addItems(b3);
    resetButton(b4);
}

function minMaxButton(b1, b2) {
    const messageArea1 = document.getElementById('m1');
    messageArea1.style.color = "black";
    let num = 0;

    b1.onclick = function(event) {
        event.preventDefault();
        num += 1;
        messageArea1.textContent = `Cliques: ${num}`;
    }

    b2.onclick = function(event) {
        event.preventDefault();
        num -= 1;
        if(num >= 0) {
            messageArea1.textContent = `Cliques: ${num}`;
        }
        if(num < 0) {
            alert("O contador já chegou ao limite mínimo.")
        }
    }
}

function inputList(input) {
    const messageArea2 = document.getElementById('m2');

    messageArea2.style.color = "black";
    messageArea2.style.whiteSpace = "pre-wrap";

    let list = "";
    input.addEventListener("keydown", function(event) {
        if(event.key == "Enter") {
            list += input.value + "\n";
            messageArea2.textContent = list;
            input.value = "";
        }
    });
}

function stringCount(input) {
    const count = document.getElementById('count');

    count.style.color = "black";
    
    input.addEventListener("keydown", function(event) {
        if(event.key === "Enter") {
            count.textContent = 0;
        }
    });

    input.addEventListener("input", function() {
        count.textContent = input.value.replace(/\s/g, '').length;
    });
}

function addItems(b3) {
    const options = document.getElementById('opts');
    const messageArea3 = document.getElementById('m3');

    messageArea3.style.color = "black";

    b3.onclick = function(event) {
        event.preventDefault();

        const list = options.value == "opt1" 
            ? document.createElement('ul') 
            : document.createElement('ol');

        ["Item 1", "Item 2", "Item 3"].forEach(text => {
            const li = document.createElement('li');
            li.textContent = text;
            list.appendChild(li);
        });

        messageArea3.appendChild(list);
    }
}

function resetButton(b4) {
    b4.onclick = function() {
        location.reload();
    }
}
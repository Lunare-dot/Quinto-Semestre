function getRandomInt(min, max) {
    const minCeiled = Math.ceil(min);
    const maxFloored = Math.floor(max);
    return Math.floor(Math.random() * (maxFloored - minCeiled + 1) + minCeiled);
}

(function() {
let rNum = getRandomInt(1, 3);
console.log("Random Number: ", rNum);


})();
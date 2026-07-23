const form = document.getElementById("compatibilityForm");
const name = document.getElementById("name");
const time = document.getElementById("time");
const materialPrice = document.getElementById("materialPrice");
const patternPrice = document.getElementById("patternPrice");
const result = document.getElementById("result");

function hoursToMinutes(time) {
    let hours = Number(time.value).toFixed(1);
    return (hours * 60).toFixed(1);
}

form.addEventListener('submit', (event) => {
    event.preventDefault();

    let minutes = hoursToMinutes(time).toFixed(1);
    let timePrice =  ((minutes * 9,8) /60).toFixed(1);

    let totalPrice = (timePrice + materialPrice + patternPrice).toFixed(1); // FAIRE QUE PATTERN PUISSE ETRE IGNORE

    result.textContent = `Ta peluche ${name} devrait coûter environ ${totalPrice} !`
});

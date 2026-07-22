const form=document.getElementById("tempForm");
const entree=document.getElementById("inputTemperature");
const unit=document.getElementById("unit");
const result=document.getElementById("result");

form.addEventListener('submit', (event) => {
    event.preventDefault();

    const temperature = Number(entree.value);
    const unitChoice = unit.value;
    if(unitChoice === "F-to-C") {
        const celsius = (temperature - 32) * 5/9;
        result.textContent = `${temperature}°F = ${celsius.toFixed(2)}°C`;
    }
    else if(unitChoice === "C-to-F") {
        const fahrenheit = (temperature * 9/5) + 32;
        result.textContent = `${temperature}°C = ${fahrenheit.toFixed(2)}°F`;
    }
})
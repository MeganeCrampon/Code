(function () {
    const converterForm=document.getElementById("converterForm");
    const inputTemperature=document.getElementById("inputTemperature");
    const unit=document.getElementById("unit");
    const converterResult=document.getElementById("converterResult");

    converterForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const temperature = Number(inputTemperature.value);
        const unitChoice = unit.value;
        if(unitChoice === "F-to-C") {
            const celsius = (temperature - 32) * 5/9;
            converterResult.textContent = `${temperature}°F = ${celsius.toFixed(2)}°C`;
        }
        else if(unitChoice === "C-to-F") {
            const fahrenheit = (temperature * 9/5) + 32;
            converterResult.textContent = `${temperature}°C = ${fahrenheit.toFixed(2)}°F`;
        }
    })
})();
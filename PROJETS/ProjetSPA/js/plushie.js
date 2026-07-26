(function () {
    const plushieForm = document.getElementById("plushieForm");
    const currency = document.getElementById("currency");
    const plushieName = document.getElementById("name");
    const hours = document.getElementById("hours");
    const minutes = document.getElementById("minutes");
    const materialPrice = document.getElementById("materialPrice");
    const patternPrice = document.getElementById("patternPrice");
    const priceResult = document.getElementById("priceResult");

    const convertionRate = {
    EUR: 1,
    USD: 1.08,
    GBP: 0.85
    };

    const currencySymbol = {
    EUR: '€',
    USD: '$',
    GBP: '£'
    };

    plushieForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const totalHours = Number(hours.value) + (Number(minutes.value) / 60);
        const timePrice = totalHours * 10;
        const materialPriceValue = Number(materialPrice.value) || 0;
        const patternPriceValue = Number(patternPrice.value) || 0;

        const totalPriceEUR = Math.ceil(timePrice + materialPriceValue + patternPriceValue);

        const currencyChoice = currency.value;
        const convertedTotalPrice = Math.ceil(totalPriceEUR * convertionRate[currencyChoice]);
        const currencySymbolChoice = currencySymbol[currencyChoice];

        priceResult.textContent = `Ta peluche ${plushieName.value} devrait coûter environ ${convertedTotalPrice}${currencySymbolChoice} ! ✨`
    });

    currency.addEventListener('change', () => {
        plushieForm.requestSubmit();
    });
})();

const languageSelector = document.getElementById("languageSelector");

applyTranslations("fr"); // Applique les traductions par défaut (français) au chargement de la page

languageSelector.addEventListener("change", (event) => {
    const selectedLanguage = event.target.value;
    applyTranslations(selectedLanguage);
});
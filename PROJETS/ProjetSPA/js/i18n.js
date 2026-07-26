function applyTranslations(language) {
    const elements = document.querySelectorAll("[data-i18n]");

    elements.forEach((element) => {
        const key = element.dataset.i18n;
        const pieces = key.split(".");
        const section = pieces[0];
        const field = pieces[1];

        const translation = translations[language][section][field];

        if (translation) {
            element.textContent = translation;
        }
    });

    const placeholderElements = document.querySelectorAll("[data-i18n-placeholder]");

    placeholderElements.forEach((element) => {
        const key = element.dataset.i18nPlaceholder;
        const pieces = key.split(".");
        const section = pieces[0];
        const field = pieces[1];

        const translation = translations[language][section][field];

        if (translation) {
            element.placeholder = translation;
        }
    });

    const emptyTextElements = document.querySelectorAll("[data-i18n-empty]");

    emptyTextElements.forEach((element) => {
        const key = element.dataset.i18nEmpty;
        const pieces = key.split(".");
        const section = pieces[0];
        const field = pieces[1];

        const translation = translations[language][section][field];

        if (translation) {
            element.setAttribute("data-empty-text", translation);
        }
    });

    document.documentElement.lang = language; // met à jour l'attribut lang="fr"/"en" sur <html>
}
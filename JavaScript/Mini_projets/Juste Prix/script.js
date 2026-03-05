const entree=document.getElementById("entree");
const bouton=document.getElementById("monBouton");
const resultat=document.getElementById("resultat");

let nombreSecret = Math.floor(Math.random() * 100) + 1;
let essais = 0;

bouton.addEventListener('click', () => {
    essais ++;
    let proposition = Number(entree.value);

    if (proposition === nombreSecret) {
        confetti({
            particleCount: 160,
            spread: 100,
            origin: { y: 0.7 }
        })
        resultat.textContent = `BRAVO ! Tu as trouvé le juste prix en ${essais} essais !`;
        resultat.className = "gagne";
        nombreSecret = Math.floor(Math.random() * 100) + 1;
        essais = 0;
    }
    else if (proposition < nombreSecret) {
        resultat.textContent = "C'est PLUS !"
        resultat.className = "plus";
    }
    else {
        resultat.textContent = "C'est MOINS !"
        resultat.className = "moins";
    }

    entree.value = "";
    entree.focus();
})

entree.addEventListener('keydown', (event) => {
    if (event.key === "Enter") {
        bouton.click(); // Cela simule un clic !
    }
});
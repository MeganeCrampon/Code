const personnes = [
    { nom: "Thomas", metier: "Développeur" },
    { nom: "Mégane", metier: "Designer" },
    { nom: "Luc", metier: "Astronaute" }
];
const leTexte = document.getElementById('texte');
const btnGen = document.getElementById('boutonGenerer');
const btnAjouter = document.getElementById('boutonAjouter');
const inputNom = document.getElementById('inputNom');
const inputMetier = document.getElementById('inputMetier');

function afficherMetiers() {
    for (let individu of personnes) {
        console.log(individu.metier)
    }
}

function changerCouleurFond() {
    // On génère 3 nombres au hasard entre 0 et 255
    let r = Math.floor(Math.random() * 256);
    let g = Math.floor(Math.random() * 256);
    let b = Math.floor(Math.random() * 256);

    document.body.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;
}

btnGen.addEventListener('click', () => {
    let index = Math.floor(Math.random() * personnes.length);
    let choix = personnes[index];
    leTexte.textContent = `${choix.nom} est ${choix.metier}`;
    leTexte.style.color = "white";
    changerCouleurFond();
 });

btnAjouter.addEventListener('click', () => {
    let nomTape = inputNom.value;
    let metierTape = inputMetier.value;
    // 2. Sécurité : on vérifie que les cases ne sont pas vides
    if (nomTape !== "" && metierTape !== "") {
        personnes.push({ 
            nom: nomTape, 
            metier: metierTape 
        });
        alert(`${nomTape} a été ajouté avec succès !`);
        // 5. On vide les cases pour la prochaine saisie
        inputNom.value = "";
        inputMetier.value = "";
    } else {
        alert("Oups ! Il faut remplir les deux cases.");
    }
});
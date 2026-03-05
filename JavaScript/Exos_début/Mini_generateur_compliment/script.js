let compliments = [
    "Tu es superbe aujourd'hui !",
    "Mais quel beau plumage !",
    "Tu sens la rose, au moins.",
    "T'as déjà pensé à postuler pour Miss/Mister Univers ?",
    "On dirait un caillou, un BEAU caillou."
];
 const leTexte = document.getElementById('texte')
 const bouton = document.getElementById('boutonGenerer')

 function donnerCompliment() {
    let indexHasard = Math.floor(Math.random() * compliments.length);
    leTexte.textContent = compliments[indexHasard];
 }

 bouton.addEventListener('click', donnerCompliment);
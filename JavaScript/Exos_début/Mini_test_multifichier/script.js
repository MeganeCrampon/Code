const leBouton = document.getElementById('monBouton');

leBouton.addEventListener('click', () => {
    // LA MAGIE : On demande au body de "basculer" (toggle) la classe CSS
    // Si 'dark-mode' est présent, il le supprime. S'il est absent, il l'ajoute.
    document.body.classList.toggle('dark-mode');
    
    if (document.body.classList.contains('dark-mode')) {
        leBouton.textContent = "Passer en mode clair";
    } else {
        leBouton.textContent = "Passer en mode sombre";
    }
});
const wordDisplay = document.getElementById("word")
const input = document.getElementById("input")
const timeDisplay = document.getElementById("time")
const scoreDisplay = document.getElementById("score")

const soundSuccess = document.getElementById('sound-success');
const soundError = document.getElementById('sound-error');

document.getElementById('record-display').textContent = localStorage.getItem('highscore') || 0;

const words = {
    facile : ["patate", "dindon", "chat", "chien", "jambon", "camion"],
    moyen : ["python", "clavier", "crochet", "fabriquer", "collection", "supprimer"],
    difficile : ["javascript", "gestionnaire", "amigurumi", "hippopotame", "mutualisation", "commercialisation"]
};

let score = 0;
let time = 10; // 10 secondes
let niveauActuel = "facile";
let dernierMot = '';

function updateWord() {
    if (score > 10) {niveauActuel = "difficile";
    } else if (score > 5) {
        niveauActuel = "moyen";
    } else {
        niveauActuel = "facile";
    }    

    const liste = words[niveauActuel]
    let nouveauMot;

    // BOUCLE ANTI-RÉPÉTITION
    do {
        nouveauMot = liste[Math.floor(Math.random() * liste.length)];
    } while (nouveauMot === dernierMot && liste.length > 1);

    dernierMot = nouveauMot; // On enregistre ce mot pour le prochain tour
    wordDisplay.textContent = nouveauMot;

    if (nouveauMot.length > 12) {
        wordDisplay.className = "text-2xl font-mono font-black tracking-tight uppercase";
    } else if (nouveauMot.length > 8) {
        wordDisplay.className = "text-3xl font-mono font-black tracking-normal uppercase";
    } else {
        wordDisplay.className = "text-5xl font-mono font-black tracking-widest uppercase";
    }
    
    // Debug optionnel : affiche le niveau dans la console pour vérifier
    console.log("Niveau actuel : " + niveauActuel);

    document.getElementById('level-display').textContent = niveauActuel;
}

function playSuccess() {
    soundSuccess.currentTime = 0; // Remet le son au début pour pouvoir le rejouer vite
    soundSuccess.play();
}

const timer = setInterval(() => {
    time--; // secondes
    timeDisplay.textContent = time;

    if (time === 0) {
        clearInterval(timer);
        alert(`Perdu ! Le temps est écoulé. Score final : ${score}`);
        finDePartie(); // Recommencer
    }
}, 1000);


// HIGHSCORE STORAGE
let highscore = localStorage.getItem('highscore') || 0;

function finDePartie() {
    if (score > highscore) {
        localStorage.setItem('highscore', score);
        document.getElementById('record-display').textContent = score;
        alert(`BRAVO ! NOUVEAU RECORD : ${score} !`);
    } else {
        alert(`GAME OVER ! Le record à battre est de ${highscore} !`)
    }
    location.reload();
}

function playError() {
    soundError.currentTime = 0;
    soundError.play().catch(e => console.log("Son bloqué par le navigateur"));
}

input.addEventListener('input', () => {
    const valeurSaisie = input.value.toLowerCase();
    const motATaper = wordDisplay.textContent.toLowerCase();

    // On vérifie si ce qui est tapé correspond au DEBUT du mot
    if (valeurSaisie.length > 0) {
        if (!motATaper.startsWith(valeurSaisie)) {
            playError();
            // Utilise les classes Tailwind pour le rouge "Cupcake"
            input.classList.add('text-error'); 
            return; 
        } else {
            input.classList.remove('text-error');
        }
    }

    // LOGIQUE DE VICTOIRE
    if (valeurSaisie === motATaper) {
        score++;
        scoreDisplay.textContent = score;
        input.value = '';
        input.classList.remove('text-error'); // On nettoie la couleur

        // L'animation de "Game Feel" que tu as ajoutée
        wordDisplay.classList.add('scale-110', 'text-success');
        setTimeout(() => {
            wordDisplay.classList.remove('scale-110', 'text-success');
        }, 100);

        playSuccess();
        updateWord();
        
        // Bonus de temps selon le niveau
        time += (niveauActuel === "facile") ? 4 : (niveauActuel === "moyen") ? 3 : 2;
    }
});

updateWord() // lance premier mot